import os
import time
import json
from agno.agent import Agent
from agno.models.google import Gemini
from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()


class AIEditorialEngine:
    def __init__(self):
        if not os.environ.get("GOOGLE_API_KEY"):
            raise PermissionError("Execution halted: GOOGLE_API_KEY environment variable is missing.")

        self.instructions = [
            "You are an expert financial market intelligence editor.",
            "Extract breakthroughs, architectural updates, and macro sentiment from the raw feed text.",
            "Strictly group findings by source channel and keep descriptions dense and developer-centric.",
            "Always preserve and append the original source hyperlinks to the end of every technical insight."
        ]

        # Primary agent: Gemini
        self.primary_agent = Agent(
            name="Macro Sentiment Research Editor - Gemini",
            role="Filter raw scraped engineering/macro feeds and compile a high-signal technical digest.",
            model=Gemini(id="gemini-2.5-flash"),
            instructions=self.instructions
        )

        # Fallback agent: Groq
        self.fallback_agent = Agent(
            name="Macro Sentiment Research Editor - Groq",
            role="Filter raw scraped engineering/macro feeds and compile a high-signal technical digest.",
            model=Groq(id="mixtral-8x7b-32768"),
            instructions=self.instructions
        )

    def _try_agent(self, agent, agent_name: str, raw_data_payload: str, max_retries: int = 3) -> tuple:
        """Try to generate digest with a specific agent.

        Returns: (success: bool, content: str, error: str)
        """
        initial_delay = 4  # seconds

        for attempt in range(max_retries):
            try:
                response = agent.run(raw_data_payload)

                # Extract content robustly (handle different agno versions)
                content = None
                if hasattr(response, 'content'):
                    content = response.content
                elif hasattr(response, 'message'):
                    content = response.message
                elif isinstance(response, str):
                    content = response
                else:
                    content = str(response)

                # Structural check: If the API returned a successful text block containing a 503 error string
                if "503" in content or "experiencing high demand" in content:
                    raise IOError(f"{agent_name} API overloaded (503 Service Unavailable).")

                print(f"✅ {agent_name} successfully generated digest")
                return True, content, None

            except Exception as e:
                # If we have remaining attempts, calculate the backoff delay
                if attempt < max_retries - 1:
                    sleep_time = initial_delay * (2 ** attempt)  # Delays: 4s, then 8s
                    print(f"⚠️ {agent_name} Warning: {e}. Retrying in {sleep_time} seconds...")
                    time.sleep(sleep_time)
                else:
                    error_msg = f"{agent_name} failed after {max_retries} retries: {str(e)}"
                    return False, None, error_msg

        return False, None, "Unknown error"

    def generate_digest(self, raw_data_payload: str) -> str:
        """Dispatches data payloads with multi-provider fallback strategy.

        Priority order:
        1. Gemini (primary)
        2. Groq (fallback)
        3. Fail if both exhausted
        """
        print("🚀 Attempting Gemini (primary model)...")
        success, content, error = self._try_agent(self.primary_agent, "Gemini", raw_data_payload)

        if success:
            return content

        print(f"⚠️ Gemini failed: {error}")
        print("🔄 Falling back to Groq (fallback model)...")
        success, content, error = self._try_agent(self.fallback_agent, "Groq", raw_data_payload)

        if success:
            return content

        # Both models failed: Raise error and fail pipeline
        error_msg = f"❌ Both Gemini and Groq exhausted. Last error: {error}"
        print(error_msg)
        raise RuntimeError(error_msg)