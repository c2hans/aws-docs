---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/generative-ai-nlp-healthcare/choosing-approach.html
---

# Choosing an NLP approach for healthcare and life sciences
<a name="choosing-approach"></a>

The [Generative AI and NLP approaches for healthcare and life sciences](hcls-options.md) section describes the following approaches for addressing natural language processing (NLP) tasks for healthcare and life science applications:
+ Using Amazon Comprehend Medical
+ Combining Amazon Comprehend Medical with an LLM in a Retrieval Augment Generation (RAG) workflow
+ Using a fine-tuned LLM
+ Using a RAG workflow

By evaluating the known limitations of LLMs for medical domain tasks and your use case, you can choose which approach will work best for your task. The following decision tree can help you choose an LLM approach for your medical NLP task:

![Decision tree for choosing an approach to solve a medical domain NLP task.](http://docs.aws.amazon.com/prescriptive-guidance/latest/generative-ai-nlp-healthcare/images/guide-img/30175f3c-77fd-446d-b6ec-cdf244f32c6e/images/958d362f-e528-40b3-b2f5-7a7878ea1b2a.png)

The diagram shows the following workflow:

1. For healthcare and life science use cases, identify whether the NLP task requires specific domain knowledge. As needed, coordinate with subject matter experts (SMEs).

1. If you can use a general LLM or a model that has been trained on medical datasets, then use an available foundation model in Amazon Bedrock or the pretrained LLM. For more information, see [Choosing an LLM](llms.md#llm-selection) in this guide.

1. If the entity detection and ontology linking capabilities of Amazon Comprehend Medical address your use case, then use the Amazon Comprehend Medical APIs. For more information, see [Using Amazon Comprehend Medical](comprehend-medical.md) in this guide.

1. Sometimes, Amazon Comprehend Medical has the required context but doesn't support your use case. For example, you might need different entity definitions, receive an overwhelming number of results, need custom entities, or need a custom NLP task. If this is the case, use a RAG approach to query Amazon Comprehend Medical for context. For more information, see [Combining Amazon Comprehend Medical with large language models](comprehend-medical-rag.md) in this guide.

1. If you have a sufficient amount of ground truth data, fine-tune an existing LLM. For more information, see [Customization approaches](llms.md#llm-customization) in this guide.

1. If the other approaches do not satisfy medical your NLP task objectives, implement a RAG solution. For more information, see [Customization approaches](llms.md#llm-customization) in this guide.

1. After implementing the RAG solution, evaluate whether the generated responses are accurate. For more information, see [Evaluating LLMs for healthcare and life science applications](evaluation.md) in this guide. It's common to start with an Amazon Titan Text Embeddings model or a general sentence transformer model, such as [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). However, due to a lack of domain context, these models might not capture the medical terminology of the text. If necessary, consider the following adjustments:

   1. Evaluate other embedding models

   1. Fine-tune the embedding model with domain-specific datasets

## Business maturity considerations
<a name="business-maturity"></a>

Business maturity is critical when adapting LLM solutions for healthcare and life science applications. These organizations face varying levels of complexity when implementing LLMs, depending on their acceptance criteria. Frequently, organizations that lack AI/ML resources invest in contractor support to build LLM solutions. In these situations, it's important to understand the following trade-offs:
+ **High performance for high cost and maintenance** – You might require a complex solution that involves fine-tuned or custom LLMs to meet stringent performance standards. However, this comes with higher costs and maintenance requirements. You might need to hire specialized resources or partner with contractors to maintain these sophisticated solutions. This can potentially slow development.
+ **Good performance for low cost and maintenance** – Alternatively, you might find that services such as Amazon Bedrock or Amazon Comprehend Medical provide acceptable performance. Although these LLMs or approaches might provide perfect results, these solutions can often provide consistent, high-quality results. These solutions are lower cost and reduce the maintenance burden. This can accelerate development.

If a simpler, lower-cost approach consistently delivers high-quality results that meet your acceptance criteria, consider whether the increasing the performance is worth the cost, maintenance, and time tradeoffs. However, if the simpler solution falls significantly short of the target performance, and if your organization lacks the investment capacity for complex solutions and their maintenance requirements, consider postponing AI/ML development until more resources or alternative solutions are available.

In addition, for any medical NLP solution that relies on an LLM, we recommend that you perform continuous monitoring and evaluation. Assess feedback from users over time, and implement periodic assessments to make sure that the solution continues to meet your business objectives.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
