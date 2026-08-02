---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/dev-experimenting.html
---

# Developing and experimenting with generative AI
<a name="dev-experimenting"></a>

After you have established a strategic foundation per the [Architecting a successful generative AI proof of concept](dev-architecting.md) section, the project transitions to technical execution. The goal of the PoC is to validate the core AI value proposition as quickly and cheaply as possible.

At this stage, the platform should be minimal because you should prioritize speed of iteration over engineering purity**. **The architecture should be simple and use managed services to the greatest extent possible. For an example of a typical RAG PoC, this might be a single [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function that orchestrates API calls to an LLM through [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) and a managed knowledge base, such as through [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html). The focus is entirely on the application logic—the prompt, the retrieval strategy, the evaluation metrics, and the output parsing—not on building and managing infrastructure.

Development should occur in environments that facilitate rapid experimentation, such as simple Python scripts. There is no need for a formal CI/CD pipeline, extensive monitoring, or automated deployment at this stage. The objective is to enable a developer to change a prompt and re-run an evaluation in minutes. The lightweight, iterative development loop centers on rapidly improving the quality of the model's outputs through disciplined prompt and context engineering, which is guided by focused evaluation mechanisms.

The technical execution of a generative AI PoC follows a logical progression that mirrors the scientific method: hypothesis, experimentation, measurement, and iteration. This journey begins with selecting the right foundation model for initial experiments, progresses through increasingly sophisticated prompt and context engineering, and culminates in systematic optimization based on evaluation results. Each step builds upon the previous, creating a compound learning effect that transforms initial assumptions into validated solutions.

**This section contains the following topics:**
+ [Choosing models for generative AI applications](dev-experimenting-model-selection.md)
+ [Understanding context engineering for generative AI](dev-experimenting-context.md)
+ [Managing the generative AI prompt lifecycle](dev-experimenting-prompt-lifecycle.md)
+ [Creating evaluation loops for generative AI experimentation](dev-experimenting-experimentation-loops.md)
+ [Evaluating quality and reliability in generated outputs](dev-experimenting-quality.md)
+ [Optimizing generative AI prompts](dev-experimenting-prompt-optimization.md)
