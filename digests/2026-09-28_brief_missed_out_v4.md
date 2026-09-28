# Missed Out - AI Research Digest (Gap: 118 days)
*Catch-up brief for 118 days of articles*

Here's a high-signal technical digest from your raw feeds:

## OpenAI

*   **Model Introductions & Capabilities**:
    *   **GPT-6 Astra**: Launched as OpenAI’s most intelligent and aligned model, exhibiting state-of-the-art capabilities across computer use, coding, cybersecurity, and science. It's the first model to reach "Critical" cybersecurity capability under their Preparedness Framework, with stronger safeguards. This model notably completed a 50-tab tax workbook twice as fast as GPT-5.6 Sol and improved color grading threefold for invideo. It also powers legal document generation for Harvey and helps Cognition's Devin test its own software.
        [https://openai.com/index/gpt-6-astra-next-generation-work](https://openai.com/index/gpt-6-astra-next-generation-work)
        [https://openai.com/index/gpt-6-astra](https://openai.com/index/gpt-6-astra)
        [https://openai.com/index/safety-overview-gpt-6-astra](https://openai.com/index/safety-overview-gpt-6-astra)
        [https://openai.com/index/path-to-astra](https://openai.com/index/path-to-astra)
        [https://openai.com/index/basis-tax-workbook-with-astra](https://openai.com/index/basis-tax-workbook-with-astra)
        [https://openai.com/index/invideo-builds-with-gpt-6-astra](https://openai.com/index/invideo-builds-with-gpt-6-astra)
        [https://openai.com/index/harvey-from-context-to-confidence-with-astra](https://openai.com/index/harvey-from-context-to-confidence-with-astra)
        [https://openai.com/index/cognition-devin-testing-with-astra](https://openai.com/index/cognition-devin-testing-with-astra)
    *   **GPT-6 Sol and Luna**: Two new models offering a balance of capability and cost for everyday work.
        [https://openai.com/index/introducing-gpt-6-sol-and-luna](https://openai.com/index/introducing-gpt-6-sol-and-luna)
    *   **GPT-Live-1**: Brings natural, full-duplex voice conversations to the API, featuring stronger instruction following, custom voices, and telephony support.
        [https://openai.com/index/introducing-gpt-live-1-in-the-api](https://openai.com/index/introducing-gpt-live-1-in-the-api)
    *   **GPT-5.6**: Focuses on frontier intelligence and efficiency, improving AI efficiency across models, inference, and agentic workflows. Available in variants like Sol, Luna, and Terra with advanced price-performance. GPT-5.6 Sol is previewed with stronger capabilities in coding, science, and cybersecurity and an advanced safety stack. Ultrafast mode for GPT-5.6 Sol, powered by Cerebras, delivers up to 14X speed (750 output tokens/sec). GPT-5.6 is also the preferred model in Microsoft 365 Copilot.
        [https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6](https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6)
        [https://openai.com/index/gpt-5-6-frontier-intelligence-efficiency](https://openai.com/index/gpt-5-6-frontier-intelligence-efficiency)
        [https://openai.com/index/previewing-ultrafast](https://openai.com/index/previewing-ultrafast)
        [https://openai.com/index/previewing-gpt-5-6-sol](https://openai.com/index/previewing-gpt-5-6-sol)
        [https://openai.com/index/gpt-5-6-preferred-model-microsoft-365-copilot](https://openai.com/index/gpt-5-6-preferred-model-microsoft-365-copilot)
    *   **GPT-5.6-Cyber**: A cybersecurity-specific model available through Daybreak Red for authorized vulnerability research, exploit validation, and security testing.
        [https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows](https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows)
    *   **GPT-Rosalind**: Enhanced for life sciences research, with biological reasoning, medicinal chemistry expertise, genomics analysis, and experimental workflow capabilities.
        [https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind)
    *   **GPT-Realtime**: Powers 24/7 multilingual retail agents, demonstrating high positive survey responses.
        [https://openai.com/index/avatarin](https://openai.com/index/avatarin)
    *   **GPT-5.5 Instant**: Improves ChatGPT’s health and wellness responses with stronger reasoning, better context, and clearer communication.
        [https://openai.com/index/improving-health-intelligence-in-chatgpt](https://openai.com/index/improving-health-intelligence-in-chatgpt)
    *   **GPT-5 Pro / GPT-5.4**: Applied in immunology to solve a 3-year-old mystery, and for a near-autonomous AI chemist to improve drug-making reactions.
        [https://openai.com/index/gpt-5-immunology-mystery](https://openai.com/index/gpt-5-immunology-mystery)
        [https://openai.com/index/ai-chemist-improves-reaction](https://openai.com/index/ai-chemist-improves-reaction)

*   **Core Infrastructure & Architecture**:
    *   **Habitat**: Evolved from a Python library into a globally distributed storage platform, serving 1 billion ChatGPT users and 22 million requests per second.
        [https://openai.com/index/scaling-storage-one-billion-users-part-one](https://openai.com/index/scaling-storage-one-billion-users-part-one)
    *   **Jalapeño**: A custom inference chip, developed with Broadcom, designed for LLM inference to deliver faster, more power-efficient AI with higher throughput and lower latency.
        [https://openai.com/index/jalapeno-first-results](https://openai.com/index/jalapeno-first-results)
        [https://openai.com/index/openai-broadcom-jalapeno-inference-chip](https://openai.com/index/openai-broadcom-jalapeno-inference-chip)
    *   **Deployment Simulation**: A new method to predict AI model behavior before deployment using real conversation data to improve safety and evaluation accuracy.
        [https://openai.com/index/deployment-simulation](https://openai.com/index/deployment-simulation)
    *   **Better prompt caching for GPT-6**: Introduces higher cache hit rates, new diagnostics, explicit breakpoints, and controls to reduce latency and costs.
        [https://openai.com/index/better-prompt-caching-for-gpt-6](https://openai.com/index/better-prompt-caching-for-gpt-6)
    *   **Core dump epidemiology**: Engineers used large-scale core dump analysis to debug rare infrastructure crashes, identifying both hardware and long-standing software bugs.
        [https://openai.com/index/core-dump-epidemiology-data-infrastructure-bug](https://openai.com/index/core-dump-epidemiology-data-infrastructure-bug)
    *   **Ona Acquisition**: OpenAI plans to acquire Ona to expand Codex with secure, persistent cloud environments, enabling long-running AI agents across enterprise workflows.
        [https://openai.com/index/openai-to-acquire-ona](https://openai.com/index/openai-to-acquire-ona)

*   **API & Developer Tools**:
    *   **Agents API**: A managed service powered by the Codex harness, enabling developers to build and launch cloud agents for orchestration, long-running sessions, and tool use.
        [https://openai.com/index/introducing-the-agents-api](https://openai.com/index/introducing-the-agents-api)
    *   **Codex**: Positioned as a key productivity tool for various roles beyond coding, including analysts, marketers, and designers. Case studies show significant productivity boosts (e.g., 1Password 21% increase, Asana code migration in 2 weeks, NTT DATA incident analysis cut to 30 mins). It also helps researchers search for antimicrobial molecules and astrophysicists simulate black holes.
        [https://openai.com/index/codex-for-every-role-tool-workflow](https://openai.com/index/codex-for-knowledge-work)
        [https://openai.com/index/1password](https://openai.com/index/1password)
        [https://openai.com/index/asana](https://openai.com/index/asana)
        [https://openai.com/index/ntt-data](https://openai.com/index/ntt-data)
        [https://openai.com/index/using-codex-chatgpt-to-search-for-new-antimicrobials](https://openai.com/index/using-codex-chatgpt-to-search-for-new-antimicrobials)
        [https://openai.com/index/using-codex-to-simulate-black-holes](https://openai.com/index/using-codex-to-simulate-black-holes)
        [https://openai.com/index/codex-maxxing-long-running-work](https://openai.com/index/codex-maxxing-long-running-work)
    *   **ChatGPT Work**: An agent platform that can take action across apps and files, persist on projects, and transform goals into finished work. Features include a Data agent for insights and interactive dashboards, education plugins, and an Admin plugin for usage analytics and spend controls.
        [https://openai.com/index/chatgpt-for-your-most-ambitious-work](https://openai.com/index/chatgpt-for-your-most-ambitious-work)
        [https://openai.com/index/put-data-to-work](https://openai.com/index/put-data-to-work)
        [https://openai.com/index/learn-teach-chatgpt-work-codex](https://openai.com/index/learn-teach-chatgpt-work-codex)
        [https://openai.com/index/introducing-admin-plugin](https://openai.com/index/introducing-admin-plugin)
        [https://openai.com/index/chatgpt-enterprise-spend-controls](https://openai.com/index/chatgpt-enterprise-spend-controls)
    *   **Zero Data Retention**: Reaffirmed for eligible API customers, with a preview of Private Safety Processing for advanced AI safety without data privacy compromise.
        [https://openai.com/index/offering-zero-data-retention-for-frontier-models](https://openai.com/index/offering-zero-data-retention-for-frontier-models)
    *   **Daybreak Program**: Expands access to frontier cyber AI, training, and support for essential services and government entities, including the Government of Ukraine. Daybreak models are now available on AWS through Amazon Bedrock.
        [https://openai.com/index/daybreak-for-frontline-defenders](https://openai.com/index/daybreak-for-frontline-defenders)
        [https://openai.com/index/openai-extends-cyber-access-to-ukraine-for-civilian-defense](https://openai.com/index/openai-extends-cyber-access-to-ukraine-for-civilian-defense)
        [https://openai.com/index/daybreak-models-are-now-available-on-aws](https://openai.com/index/daybreak-models-are-now-available-on-aws)
    *   **OpenAI Presence**: A proven enterprise AI agent platform for deploying trusted voice and chat agents for customer and internal workflows.
        [https://openai.com/index/introducing-openai-presence](https://openai.com/index/introducing-openai-presence)

*   **Benchmarks & Research**:
    *   **MentalHealthBench**: An expert-informed benchmark for evaluating helpful and safe AI responses in mental health conversations.
        [https://openai.com/index/introducing-mentalhealthbench](https://openai.com/index/introducing-mentalhealthbench)
    *   **GeneBench-Pro / LifeSciBench**: New benchmarks for testing AI performance in genomics, biology, scientific research, and real-world life science tasks.
        [https://openai.com/index/introducing-genebench-pro](https://openai.com/index/introducing-genebench-pro)
        [https://openai.com/index/introducing-life-sci-bench](https://openai.com/index/introducing-life-sci-bench)
    *   **Navier–Stokes Millennium Prize Problem**: OpenAI shared an AI-generated solution, including a formal proof in Lean.
        [https://openai.com/index/navier-stokes-solution](https://openai.com/index/navier-stokes-solution)
    *   **GPT-Red**: An automated red teaming system utilizing self-play to improve AI safety, alignment, and prompt injection robustness.
        [https://openai.com/index/unlocking-self-improvement-gpt-red](https://openai.com/index/unlocking-self-improvement-gpt-red)
    *   **ARC-AGI-3 benchmark improvement**: Two API settings significantly boosted GPT-5.6 performance and efficiency on ARC-AGI-3 by retaining reasoning and enabling compaction.
        [https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores](https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores)
    *   **AI coding agents**: Reshaping AI research by accelerating experiment velocity and task complexity.
        [https://openai.com/index/research-acceleration-view-inside-openai](https://openai.com/index/research-acceleration-view-inside-openai)

*   **Security & Safety Initiatives**:
    *   **Hugging Face incident**: Shared findings from a security incident during AI model evaluation, highlighting advanced cyber capabilities and steps to strengthen model security, monitoring, and alignment.
        [https://openai.com/index/hugging-face-model-evaluation-security-incident](https://openai.com/index/hugging-face-model-evaluation-security-incident)
        [https://openai.com/index/hugging-face-incident-and-the-road-ahead](https://openai.com/index/hugging-face-incident-and-the-road-ahead)
    *   **Model Misalignment Reporting Framework**: Shared framework for tracking, investigating, and disclosing model misalignment, alongside reports of unexpected or concerning model behavior.
        [https://openai.com/index/model-misalignment-reporting-framework](https://openai.com/index/model-misalignment-reporting-framework)
    *   **Pacing Model Development**: Strengthening monitoring, alignment, and security for frontier AI models, with new safeguards guiding development pace, especially for cyber-critical capabilities.
        [https://openai.com/index/pacing-model-development-cyber-capabilities](https://openai.com/index/pacing-model-development-cyber-capabilities)
    *   **Third-party Cyber Evaluations**: Outlined new safeguards for strengthening AI model testing and evaluation following incidents.
        [https://openai.com/index/third-party-cyber-evaluations-involving-openai-models](https://openai.com/index/third-party-cyber-evaluations-involving-openai-models)
    *   **Biodefense in the Intelligence Age**: An action plan for AI-powered biological resilience.
        [https://openai.com/index/biodefense-in-the-intelligence-age](https://openai.com/index/biodefense-in-the-intelligence-age)

*   **Enterprise Adoption & Partnerships**:
    *   Major enterprise deployments and partnerships announced, including Samsung Electronics, NVIDIA, Airbnb, Perplexity, Cognition, invideo, Harvey, Basis, Proaction, Parallel, Higgsfield AI, Hex, Fyxer, Legora, Playco, V7, Cooley, Ringg, Replit, Model ML, Omio, Circles, avatarin, Wasmer, 1Password, Asana, Nextdoor, Notion, NTT DATA, loveholidays, Travelers, Zapier, Virgin Atlantic, HSP GRUPPE, Deutsche Telekom, MUFG, Australian Payments Plus, LSEG, Endava, BBVA. These highlight use cases in accelerating product development, automating workflows, improving customer service, and enabling data analysis.
        [https://openai.com/index/samsung-electronics-chatgpt-codex-deployment](https://openai.com/index/samsung-electronics-chatgpt-codex-deployment)
        [https://openai.com/index/nvidia/chatgpt-work](https://openai.com/index/nvidia/chatgpt-work)
        (and many other specific links from the original dataset for each company)
    *   **OpenAI Partner Network**: Launched with a $150M investment to accelerate enterprise AI adoption.
        [https://openai.com/index/introducing-openai-partner-network](https://openai.com/index/introducing-openai-partner-network)
    *   **Oracle Cloud Integration**: OpenAI models and Codex are accessible through Oracle Cloud, leveraging existing commitments for enterprise security and governance.
        [https://openai.com/index/openai-on-oracle-cloud](https://openai.com/index/openai-on-oracle-cloud)

*   **Product Enhancements & Market Expansion**:
    *   **ChatGPT Images 2.5**: Helps turn ideas, sketches, and reference photos into personalized, polished images.
        [https://openai.com/index/introducing-chatgpt-images-2-5](https://openai.com/index/introducing-chatgpt-images-2-5)
    *   **ChatGPT Ads**: Expanding globally (Southeast Asia, Taiwan, Europe), reaching $1 billion in annualized revenue run rate. Testing ads in ChatGPT to support free access, with privacy protections and user control. Also reimagining advertising with AI-powered experiences like Sponsored Agents.
        [https://openai.com/index/chatgpt-ads-expands-southeast-asia-taiwan](https://openai.com/index/chatgpt-ads-expands-southeast-asia-taiwan)
        [https://openai.com/index/chatgpt-ads-expands-across-europe](https://openai.com/index/chatgpt-ads-expands-across-europe)
        [https://openai.com/index/a-milestone-in-expanding-access-to-ai](https://openai.com/index/a-milestone-in-expanding-access-to-ai)
        [https://openai.com/index/testing-ads-in-chatgpt](https://openai.com/index/testing-ads-in-chatgpt)
        [https://openai.com/index/reimagining-advertising-with-ai](https://openai.com/index/reimagining-advertising-with-ai)
    *   **ChatGPT for Financial Services**: Combining built-in financial data and GPT-6 Astra for research, modeling, and client-ready materials.
        [https://openai.com/index/introducing-chatgpt-financial-services](https://openai.com/index/introducing-chatgpt-financial-services)
    *   **Health in ChatGPT**: Eligible U.S. users can securely connect medical records and Apple Health for personalized insights. Healthcare organizations can connect EHR and industry data.
        [https://openai.com/index/health-in-chatgpt](https://openai.com/index/health-in-chatgpt)
        [https://openai.com/index/chatgpt-connects-health-records-and-healthcare-sources](https://openai.com/index/chatgpt-connects-health-records-and-healthcare-sources)
    *   **ChatGPT for Academic Researchers**: Offering 100,000 academic researchers free access to advanced AI models.
        [https://openai.com/index/chatgpt-for-academic-researchers](https://openai.com/index/chatgpt-for-academic-researchers)

## Google AI

*   **Product Enhancements & Features**:
    *   **AI Mode in Search**: Introduced new capabilities for travel planning and booking, home decor inspiration, learning tools, and football features, leveraging Gemini spark for enhanced search experiences.
        [https://blog.google/products-and-platforms/products/search/book-travel-ai-mode/](https://blog.google/products-and-platforms/products/search/book-travel-ai-mode/)
        [https://blog.google/products-and-platforms/products/search/home-decor-tips/](https://blog.google/products-and-platforms/products/search/home-decor-tips/)
        [https://blog.google/products-and-platforms/products/search/back-to-school-study-tools/](https://blog.google/products-and-platforms/products/search/back-to-school-study-tools/)
        [https://blog.google/products-and-platforms/products/search/running-race-training-tips/](https://blog.google/products-and-platforms/products/search/running-race-training-tips/)
        [https://blog.google/products-and-platforms/products/search/football-features-google-search/](https://blog.google/products-and-platforms/products/search/football-features-google-search/)
    *   **Google Pics**: New tool for easy image creation and editing integrated into Google Workspace.
        [https://blog.google/products-and-platforms/products/workspace/google-pics/](https://blog.google/products-and-platforms/products/workspace/google-pics/)
    *   **Gemini 3.7 Flash**: Mentioned as a recent AI model update, suggesting focus on speed and efficiency.
        [https://blog.google/innovation-and-ai/technology/google-ai-updates-august-2026/](https://blog.google/innovation-and-ai/technology/google-ai-updates-august-2026/)
    *   **Google Beam**: Expands with new regions, partners, and customers, indicating growth in its AI infrastructure or service offering.
        [https://blog.google/innovation-and-ai/technology/research/google-beam-expansion/](https://blog.google/innovation-and-ai/technology/research/google-beam-expansion/)

*   **Security Initiatives**:
    *   **Fairwind Program**: Introduced for proactive cyber defense tailored for governments and enterprises.
        [https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/](https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/)

*   **Data & Research**:
    *   **UN System Data Commons Platform**: Initiative to make global data easier to explore, likely leveraging AI for synthesis and accessibility.
        [https://blog.google/innovation-and-ai/technology/ai/google-un-data-commons-platform/](https://blog.google/innovation-and-ai/technology/ai/google-un-data-commons-platform/)
    *   **AI & Economy ATLAS**: Provided new insights from Google's research program on AI's economic impact.
        [https://blog.google/innovation-and-ai/technology/ai/ai-economy-atlas-september-2026/](https://blog.google/innovation-and-ai/technology/ai/ai-economy-atlas-september-2026/)

## Hugging Face

*   **Agent Development & Frameworks**:
    *   **Holo4 / Holo3.1**: Powering generalist and fast/local computer-use agents, respectively, indicating advancements in autonomous AI interaction with systems.
        [https://huggingface.co/blog/Hcompany/holo4](https://huggingface.co/blog/Hcompany/holo4)
        [https://huggingface.co/blog/Hcompany/holo31](https://huggingface.co/blog/Hcompany/holo31)
    *   **Strands Agents & LeRobot**: Integrated with Hugging Face Storage Buckets for recording robot-manipulation data, streaming data loops, and deploying models from the Hub to robot hardware. NVIDIA Warp and MjWarp also accelerate robotics simulation.
        [https://huggingface.co/blog/amazon/strands-lerobot-streaming-data-loop](https://huggingface.co/blog/amazon/strands-lerobot-streaming-data-loop)
        [https://huggingface.co/blog/amazon/strands-lerobot-hub-to-hardware](https://huggingface.co/blog/amazon/strands-lerobot-hub-to-hardware)
        [https://huggingface.co/blog/nvidia/how-to-use-nvidia-warp-and-mjwarp](https://huggingface.co/blog/nvidia/how-to-use-nvidia-warp-and-mjwarp)
    *   **Funes**: Introduces a memory system for coding agents, allowing ownership of agent memory.
        [https://huggingface.co/blog/funes](https://huggingface.co/blog/funes)
    *   **OpenEnv**: The open-source community is backing OpenEnv for Agentic Reinforcement Learning.
        [https://huggingface.co/blog/openenv-agentic-rl](https://huggingface.co/blog/openenv-agentic-rl)
    *   **Agentic Resource Discovery**: Enables agents to autonomously search for resources.
        [https://huggingface.co/blog/agentic-resource-discovery-launch](https://huggingface.co/blog/agentic-resource-discovery-launch)

*   **Model Efficiency & Optimization**:
    *   **LFM2.5-VL-DSpark & LFM2.5-DSpark**: Accelerating vision-language models and inference by up to 3.2x faster.
        [https://huggingface.co/blog/LiquidAI/lfm2-5-vl-dspark](https://huggingface.co/blog/LiquidAI/lfm2-5-vl-dspark)
        [https://huggingface.co/blog/LiquidAI/lfm25-dspark](https://huggingface.co/blog/LiquidAI/lfm25-dspark)
    *   **Transformers `llama.cpp` quants**: Transformers now natively runs `llama.cpp` quantized models.
        [https://huggingface.co/blog/transformers-llama-cpp-quants](https://huggingface.co/blog/transformers-llama-cpp-quants)
    *   **Quantization-Aware Healing**: A technique to create compressed, 4-bit models that outperform their full-precision originals.
        [https://huggingface.co/blog/MultiverseComputingCAI/quantization-aware-healing](https://huggingface.co/blog/MultiverseComputingCAI/quantization-aware-healing)
    *   **Efficient Knowledge Distillation**: Making knowledge distillation cheap enough to run at scale.
        [https://huggingface.co/blog/MultiverseComputingCAI/efficient-knowledge-distillation](https://huggingface.co/blog/MultiverseComputingCAI/efficient-knowledge-distillation)
    *   **Native-speed vLLM transformers modeling backend**: Improves inference speed for vLLM transformers.
        [https://huggingface.co/blog/native-speed-vllm-transformers-backend](https://huggingface.co/blog/native-speed-vllm-transformers-backend)
    *   **Pruning LLMs Like a Physicist**: Explores block removal as an Ising Optimization Problem for LLM pruning.
        [https://huggingface.co/blog/MultiverseComputingCAI/pruning-llms-like-a-physicist-block-removal-as-an](https://huggingface.co/blog/MultiverseComputingCAI/pruning-llms-like-a-physicist-block-removal-as-an)
    *   **GLM-5.2**: Introduced as a model built for long-horizon tasks.
        [https://huggingface.co/blog/zai-org/glm-52-blog](https://huggingface.co/blog/zai-org/glm-52-blog)
    *   **NeoMME**: An efficient Multimodal-native and Multilingual Encoder model.
        [https://huggingface.co/blog/Hcompany/neomme](https://huggingface.co/blog/Hcompany/neomme)

*   **Developer Tools & Platform Integration**:
    *   **@huggingface/kernels**: Launched with over 200 WebGPU Kernels for local AI, enabling faster in-browser machine learning. Major updates to Kernels were also announced.
        [https://huggingface.co/blog/webgpu-kernels](https://huggingface.co/blog/webgpu-kernels)
        [https://huggingface.co/blog/revamped-kernels](https://huggingface.co/blog/revamped-kernels)
    *   **Gradio Workflow**: Rebuilding AUTOMATIC1111 with Gradio Workflow, providing a guide for AI workflow development.
        [https://huggingface.co/blog/gradio-workflow-1111](https://huggingface.co/blog/gradio-workflow-guide)
    *   **HF CLI**: Designed as an agent-optimized way to work with the Hugging Face Hub.
        [https://huggingface.co/blog/hf-cli-for-agents](https://huggingface.co/blog/hf-cli-for-agents)
    *   **`huggingface_hub`**: Shipping weekly releases with AI, open tools, and a human-in-the-loop CI process.
        [https://huggingface.co/blog/huggingface-hub-release-ci](https://huggingface.co/blog/huggingface-hub-release-ci)
    *   **SkyPilot Integration**: Enables running AI workloads on any cloud with zero-egress storage on Hugging Face.
        [https://huggingface.co/blog/skypilot-hf-storage](https://huggingface.co/blog/skypilot-hf-storage)
    *   **Cloud Integrations**: One-click deployment from Hugging Face Hub to Amazon SageMaker Studio and Hugging Face Models on Microsoft Foundry Managed Compute.
        [https://huggingface.co/blog/amazon/one-click-to-sagemaker-studio](https://huggingface.co/blog/amazon/one-click-to-sagemaker-studio)
        [https://huggingface.co/blog/microsoft/foundry-managed-compute](https://huggingface.co/blog/microsoft/foundry-managed-compute)
    *   **Cross-Origin Storage API**: Experimentation in Transformers.js with the proposed API.
        [https://huggingface.co/blog/cross-origin-storage](https://huggingface.co/blog/cross-origin-storage)

*   **Benchmarking & Evaluation**:
    *   **BenchMIRT**: Addresses the question of what LLM benchmarks are actually measuring.
        [https://huggingface.co/blog/allenai/benchmirt](https://huggingface.co/blog/allenai/benchmirt)
    *   **FFASR Leaderboard**: Introduced for benchmarking Automatic Speech Recognition (ASR) in real-world scenarios.
        [https://huggingface.co/blog/ffasr-leaderboard](https://huggingface.co/blog/ffasr-leaderboard)
    *   **Open ASR Leaderboard**: Expanded to include its first Global South language.
        [https://huggingface.co/blog/open-asr-leaderboard-global-south](https://huggingface.co/blog/open-asr-leaderboard-global-south)
    *   **EvalEval & UK AISI**: Collaborating to make benchmark results reproducible.
        [https://huggingface.co/blog/evaleval-aisi](https://huggingface.co/blog/evaleval-aisi)
    *   **ScarfBench**: A benchmark for AI agents in enterprise Java framework migration.
        [https://huggingface.co/blog/ibm-research/scarfbench](https://huggingface.co/blog/ibm-research/scarfbench)
    *   **MosaicLeaks**: Benchmarks research agents' ability to keep secrets.
        [https://huggingface.co/blog/ServiceNow/mosaicleaks](https://huggingface.co/blog/ServiceNow/mosaicleaks)
    *   **"Is it agentic enough?"**: A method for benchmarking open models on custom tooling.
        [https://huggingface.co/blog/is-it-agentic-enough](https://huggingface.co/blog/is-it-agentic-enough)

*   **Security**:
    *   **Security incident disclosure (July 2026)**: Published a technical timeline of a frontier lab agent intrusion, providing insights into advanced cyber capabilities and lessons for defenders.
        [https://huggingface.co/blog/security-incident-july-2026](https://huggingface.co/blog/security-incident-july-2026)
        [https://huggingface.co/blog/agent-intrusion-technical-timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline)

*   **Advanced AI Research**:
    *   **DiScoFormer**: A single transformer for density and score across different distributions.
        [https://huggingface.co/blog/allenai/discoformer](https://huggingface.co/blog/allenai/discoformer)
    *   **Profiling in PyTorch (Part 3)**: Deep dives into attention profiling, following previous parts on MLP fusion.
        [https://huggingface.co/blog/torch-attention-profile](https://huggingface.co/blog/torch-attention-profile)
        [https://huggingface.co/blog/torch-mlp-fusion](https://huggingface.co/blog/torch-mlp-fusion)
    *   **Direct Preference Optimization Beyond Chatbots**: Exploring DPO for broader applications.
        [https://huggingface.co/blog/Dharma-AI/direct-preference-optimization-beyond-chatbots](https://huggingface.co/blog/Dharma-AI/direct-preference-optimization-beyond-chatbots)
    *   **Muse Glimmer**: Meta's new local, agentic, multimodal, and open-source model.
        [https://huggingface.co/blog/muse-glimmer](https://huggingface.co/blog/muse-glimmer)