---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/generative-ai-capabilities.html
---

# Generative AI capabilities
<a name="generative-ai-capabilities"></a>

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

This section discusses secure access, usage, and implementation recommendations for the following generative AI capabilities:
+ Capability 1. Providing developers and data scientists with secure access to generative AI FMs (model inference)
+ Capability 2. Providing secure access, usage, and implementation for generative AI model customization
+ Capability 3. Providing secure access to data and systems for generative AI
+ Capability 4. Providing secure access, usage, and implementation of tools
+ Capability 5. Providing secure access, usage, and implementation of generative AI agents
+ Capability 6. Providing secure access, usage, and implementation for AI applications

Most capability sections include the following information:
+ **Rationale **explains what the capability does and when to use it.
+ **Security considerations** describes risks that are specific to the capability.
+ **Remediations** reviews the AWS services and features that address the risks.
+ **Recommended AWS services** to build the capability securely.

All capabilities build on Capability 1 (foundation model inference) because they all invoke models. When you combine capabilities, apply security controls from each relevant section. For example, a customized model with Retrieval Augmented Generation (RAG) requires controls from Capabilities 1, 2, and 3.
