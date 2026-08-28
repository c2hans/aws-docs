---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/dev-architecting.html
---

# Architecting a successful generative AI proof of concept
<a name="dev-architecting"></a>

The journey to a production-grade generative AI application begins long before the first line of code is written. It starts with a strategically sound proof of concept (PoC). Too often, PoCs are treated as technical demos that are designed to impress rather than as rigorous experiments that are designed to promote learning. A successful PoC is a strategic tool that derisks investment by validating the following: business value, data readiness, technical feasibility, and risk mitigation. This framework transforms the PoC from a technical exercise into a comprehensive business validation process. This helps you make sure that any "go" decision is backed by evidence, not just enthusiasm.

**This section contains the following topics:**
+ [Demonstrating business value](#dev-architecting-value)
+ [Validating data readiness](#dev-architecting-readiness)
+ [Assessing technical feasibility](#dev-architecting-feasibility)
+ [Choosing an AI approach](#dev-architecting-approach)
+ [Mitigating project delivery risks](#dev-architecting-risk)

## Demonstrating business value
<a name="dev-architecting-value"></a>

In this phase, you connect business goals with technical metrics. A PoC must first and foremost answer the question: "If we build this, will it matter?" This requires translating a high-level business objective to specific, measurable success criteria. The following actions can help you validate business value:

1. **Start with strategic business objectives** – A generative AI initiative must be anchored in the organization's overarching goals. Primary drivers might be to increase operational efficiency, enhance customer experience, accelerate innovation, or create new revenue streams. Top-down alignment with business objectives helps you make sure that the project is strategically relevant.

1. **Translate value with the OGSM framework** – Tracking technical metrics that are disconnected from tangible business impact is a common failure point in generative AI projects. A robust evaluation strategy requires a clear, structured framework that links high-level business goals to specific, actionable metrics that engineers can use to optimize the system. The [Objectives, Goals, Strategies, and Measures (OGSM) framework](https://www.ogsm.com/en/ogsm-model) can provide this structure. It helps you make sure that every technical measurement is traceable back to a meaningful business outcome. It consists of the following levels

   1. **Objectives (the *why*)** – Objectives are the overarching business intent or strategic intent. An example is improving customer support efficiency.

   1. **Goals (the *what*)** – Goals are the quantifiable business targets that track progress toward the objective. An example is reducing the average handle time by 20%.

   1. **Strategies (the *how*)** – Strategies are broad approaches or initiatives to achieve the goals. An example is implementing AI-driven email summarization to accelerate support workflows.

   1. **Measures (the *how we track*)** – Measures are the specific metrics, at both the system level (user experience) and the model level (developer-facing), that track performance against the goals. Examples include: first-contact resolution rates, user satisfaction scores, a hallucination rate, answer relevancy, or latency.

The following table provides a practical template for applying the OGSM framework. The examples in the template demonstrate how to connect objectives to metrics across different use cases. This translation exercise is a critical communication tool because it creates a shared language between business and technical teams.

|
|
| **Objective** | **Goal** | **Strategies** | **Measures** |
| --- |--- |--- |--- |
| Improve customer support efficiency | Reduce average handle time by 30% | + Task completion rate+ First-contact resolution+ User satisfaction | + **Answer relevancy** – Is the answer pertinent to the query? + **Hallucination rate** – Is the answer grounded in the provided context?+ **Latency** – How quickly does the user get a response?   |
| Increase sales team productivity | Increase number of qualified leads generated per week by 15% | + Lead quality score, as rated by Sales team+ Time to generate outreach draft+ User adoption rate | + **Coherence or fluency** – Is the generated email well written and persuasive? + **Context relevance** – For Retrieval Augmented Generation (RAG), was the correct customer information retrieved and used? + **Toxicity or safety** – Is the tone appropriate and professional?  |
| Reduce content creation costs | Decrease cost per marketing article by 40% | + First draft usability rate (percentage of drafts used with only minor edits)+ Subject matter expert (SME) quality rating | + [**ROUGE**](https://en.wikipedia.org/wiki/ROUGE_(metric))** or **[**BERTScore**](https://arxiv.org/abs/1904.09675) – How similar is the generated text to a set of human-written samples? + **Token usage** – What is the API cost per draft? + **Diversity** – Is the model producing varied, non-repetitive content? |

** **For more information about validating business value, see following resources:
+ [KPIs for Generative AI: Measuring Business Impact & Strategic Value](https://www.debutinfotech.com/blog/a-comprehensive-guide-for-generative-ai-kpis) (Debut Infotech blog post)
+ [OGSM framework](https://www.ogsm.com/en/ogsm-model) (OGSM)
+ [AI Proof of Concept (PoC): What It Is & How to Build One?](https://www.quinnox.com/blogs/ai-proof-of-concept-guide/) (Quinnox blog post)

## Validating data readiness
<a name="dev-architecting-readiness"></a>

Generative AI outcomes are only as good as the data they are built on. A PoC must rigorously assess whether the required data is available, accessible, and of sufficient quality to support the use case. The following checklist can help you validate data readiness for a generative AI PoC:
+ **Data privacy and security** – These are the highest priority. The default approach should be to use synthetic or fully anonymized data. If real data containing any potentially sensitive or personally identifiable information (PII) is necessary for the PoC, explicit approval from your information security and legal teams must be obtained before ingesting the data into any system. Ignoring this step is one of the most common pitfalls. For more information and privacy and the how to anonymize data on AWS, see the [Personal Data OU – PD Application](https://docs.aws.amazon.com/prescriptive-guidance/latest/privacy-reference-architecture/personal-data-account.html) account in the *AWS Privacy Reference Architecture*.
+ **Data inventory and access** – Catalog all data sources that are relevant to your PoC and assess their accessibility, reliability, and integration complexity. Document data lineage to understand the origin and transformation history of your datasets. Establish clear data lineage tracking to enable auditing and troubleshooting throughout the PoC lifecycle.
+ **Ground truth data curation** – For generative AI PoC projects, preparation of an evaluation dataset replaces traditional curation of training data curation. You need high-quality test datasets so that you can assess AI outputs against validated benchmarks and ground truth references.
+ **Reference answer validation** – Ground truth must achieve high factual accuracy through SME validation. Validation should incorporate historical workflow data, expert-annotated examples, and verified documentation.
+ **Business context alignment** – Datasets must comprehensively represent target business scenarios with contextual richness that aligns to PoC objectives. Customer service applications require conversational context and multi-turn dialogue patterns, while document processing needs structured content hierarchies and domain-specific terminology.
+ **Data currency and relevance** – Establish data freshness requirements based on application sensitivity. Verify temporal relevance to prevent outdated information from generating misleading AI content. Document refresh cycles and establish version control.
+ **Multi-modal completeness** – For text, image, or code generation applications, ground truth must encompass all relevant output modalities with cross-modal consistency validation. Define format-specific quality standards and confirm comprehensive coverage across different content types to identify model limitations and enable accurate cross-format evaluation.

For more information about validating data readiness, see the following resources:
+ [How to build a successful AI PoC: A step-by-step guide](https://www.azilen.com/blog/ai-poc/) (Azilen blog post)
+ [A comprehensive guide to generative AI implementation for enterprises](https://xtm.cloud/blog/generative-ai-implementation/) (XTM blog post)
+ [Data quality for successful generative AI program implementation](https://www.wipro.com/analytics/articles/generative-ai-success-begins-and-ends-with-data-quality-readiness/) (Wipro article)
+ [Data security, lifecycle, and strategy for generative AI applications](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-considerations-gen-ai/introduction.html) (AWS Prescriptive Guidance)

## Assessing technical feasibility
<a name="dev-architecting-feasibility"></a>

After you have defined the business value and confirmed data readiness, the PoC must prove that the solution is technically buildable within the organization's specific environment and that it can meet the goals outlined in the initial business case. This includes evaluating the integration landscape, making pragmatic technology choices, and confirming that the team has the right skills.

The PoC should test technical feasibility against these goals, and at its completion, the learnings and metrics across different technical dimensions should inform updates to the business case and potentially refine the functional requirements.

The following are the key dimensions of technical feasibility:
+ **Focus on rapid iteration and model-task fit** – Start with a solid, general-purpose base model and prioritize prompt or context engineering over chasing the perfect model. Choose a few models, and then test them for suitability. Consider modality, size, cost, context window, tool use, output speed, and multilingual support. For feasibility, consider starting with higher-cost, higher-performance models, then evaluate lower-cost options to balance cost, accuracy, and latency.
+ **Evaluate integration** – Assess the integration landscape and non-functional requirements (NFRs), such as privacy, security, scalability, and maintainability. Include performance metrics, such as end-to-end latency, requests or tokens per second, and concurrency to align system design with application needs, such as real-time or batch operations. For Retrieval Augmented Generation (RAG), evaluate managed and self-hosted vector database options for latency and scalability. For agentic AI use cases, validate the reliability, latency, and security of external APIs or tools that the agent will use.
+ **API compared to self-hosted** – Choose between commercial, self-hosted, or open source APIs based on NFRs, such as privacy, compliance, cost, and customization. Factor in cost-per-unit economics, such as the costs for one thousand tokens, GPU hours, storage, and egress. Consider how they scale after deployment. Validate compliance with data regulations, content policies, and intellectual property rights.
+ **Team capabilities** – Confirm the team has the technical skills to deliver the vision, including model evaluation, optimization, integration, performance tuning, safety measures, and adversarial input handling.

## Choosing an AI approach
<a name="dev-architecting-approach"></a>

Before development begins, it's essential to select the primary generative AI approach for the PoC. Options include prompt engineering, RAG, agentic AI, and fine-tuning. This decision shapes the architecture, data requirements, and complexity of the project.

We recommend that you choose an approach as follows:

1. **Start with prompt engineering** – This approach is ideal for tasks that rely on the model's general knowledge and reasoning abilities without needing external, real-time, or proprietary information. Examples include summarization, content generation, and simple classification.

   For PoCs that use this approach, focus on rapidly iterating on prompt design and context engineering. This is the simplest and fastest starting point for most PoCs.

1. **Add Retrieval-Augmented Generation (RAG)** – Choose this approach if the application must provide factually grounded answers that are based on specific, proprietary, or up-to-date documents, such as internal knowledge bases or product manuals. RAG can help mitigate hallucinations by providing the model with relevant context. For more information about RAG, see [What is RAG (Retrieval-Augmented Generation)](https://aws.amazon.com/what-is/retrieval-augmented-generation/) and [Retrieval-Augmented Generation for Large Language Models: A Survey](https://arxiv.org/abs/2312.10997) (Arxiv).

   For PoCs that use this approach, in addition to prompting, the PoC must validate the retrieval pipeline. You must select an embedding model, choose a vector store, and optimize document chunking and retrieval strategies.

1. **Evolve to agentic AI** – Consider agentic AI for complex, multi-step tasks that require the model to do more than just answer a question. Agents can interact with external tools, APIs, and data sources to accomplish a goal. For example, they can diagnose a technical issue by running commands. For more information, see [Agentic AI](https://aws.amazon.com/prescriptive-guidance/agentic-ai/) (AWS Prescriptive Guidance).

   For PoCs that use this approach, define the agent's goals and the available tools. The PoC must test the agent's ability to reason, plan, and reliably use its tools. This involves selecting an agentic framework, such as [Strands Agents](https://strandsagents.com/), and managing the security and reliability of the tool integrations.

1. **Consider fine-tuning** – Consider this approach if you need to teach the model a specific style, format, or niche terminology that is difficult to replicate through prompting or RAG alone. It can also be used to improve performance on a very narrow, repetitive task. Before you choose this approach, evaluate the significant costs (time and money) of the fine-tuning process compared to the expected performance improvements. For most knowledge-injection use cases, RAG is a better starting point than fine-tuning.

   For PoCs that use this approach, the PoC must focus on curating a high-quality training dataset of prompt-completion pairs.

Your choice of approaches does not have to be mutually exclusive. A sophisticated system might combine all these techniques. However, for a PoC, it's crucial to start with the simplest method that can validate the core business value.

## Mitigating project delivery risks
<a name="dev-architecting-risk"></a>

Generative AI PoC projects face unique risks that differ from traditional software development projects. Unlike deterministic systems, generative AI applications produce variable outputs that can be difficult to predict or control, making early risk identification and mitigation critical for project success. Additionally, the experimental nature of generative AI technology means that teams often work with rapidly evolving tools, uncertain performance benchmarks, and unclear cost structures.

This section outlines a pragmatic governance approach specifically designed for the PoC phase. It focuses on the most critical risk factors that can derail generative AI projects before they reach production. Rather than implementing heavy-weight processes that slow innovation, it emphasizes lightweight but essential practices that help teams:
+ Catch quality and performance issues early before significant resources are invested
+ Maintain stakeholder alignment through structured feedback mechanisms
+ Make data-driven decisions about whether to continue, pivot, or terminate the PoC
+ Establish realistic expectations for costs, timelines, and technical feasibility
+ Build confidence in the approach before scaling to production

The goal of governance during a PoC is to pragmatically address critical showstoppers early in the process. This lightweight approach focuses on a few non-negotiable areas:
+ **Feedback loops** – From the beginning, you must establish a simple, structured process for collecting feedback from the business leads, domain SMEs, and other key stakeholders. This could be as simple as a shared spreadsheet for reviewing outputs, a dedicated Slack or Microsoft Teams channel, or a minimal UI with positive and negative feedback ratings. The key is to make the feedback process consistent, timely, and actionable for the engineering team.
+ **Iterative development with clear outcomes** – Use short, outcome-focused iterations to manage risk and enable quick adjustments. This helps teams learn and adapt without committing excessive resources too early.
+ **Exit criteria** – Set clear thresholds for quality, latency, and cost, If results fail to meet these, pivot or end the PoC so that poor performance does not lead to wasted effort or sunk costs.
+ **Scoped testing** – Validate only the core components before you invest in full end-to-end integration. This reduces complexity and isolates potential failure points early.
+ **Operational readiness** – Address data quality and retrieval issues before prompt tuning, and track unit economics early. *Unit economics* are the per-request costs, which includes token usage, compute resources, and storage. Unit economics determine your application's financial viability at scale.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
