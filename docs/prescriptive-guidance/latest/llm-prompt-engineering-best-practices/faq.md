---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/llm-prompt-engineering-best-practices/faq.html
---

# FAQ
<a name="faq"></a>

**Q. What additional security layers should I consider to prevent prompt injection attacks?** **A. **The following diagram shows the three main security layers: LLM input, LLM built-in guardrails, and user-introduced guardrails.

![LLM security layers: input, built-in guardrails, and user-introduced guardrails](https://docs.aws.amazon.com/prescriptive-guidance/latest/llm-prompt-engineering-best-practices/images/guide-img/68090e47-53ec-4c59-81ce-88b96fe5e380/images/f0d7cc7a-a566-4c0c-bc7e-c024d41c0c78.png)

Your organization should consider implementing security protocols across all layers. For the first layer (*LLM input*), consider risk mitigation steps to help secure the application by implementing mechanisms such as personally identifiable information (PII) or sensitive information redaction, authentication, authorization, and encryption. The second layer (*LLM built-in guardrails*) are model or application securities provided by the LLM. Although most LLMs are trained with security protocols to prevent inappropriate use, your organization should still consider adding additional security controls by using [Guardrails for Amazon Bedrock](https://aws.amazon.com/bedrock/guardrails/) to bring a consistent level of AI safety across all generative AI applications. Lastly, *user-introduced guardrails* should introduce best prompt template designs and post-processing security measures on the generated output to prevent undesirable results.

**Q. How can organizations defend against prompt injection attacks in prompt engineering?**

**A. **Organizations can defend against prompt injection attacks by implementing best prompt engineering practices as discussed in the [Best practices](best-practices.md) section. Your organization can also consider adding guardrails such as input validation, prompt sanitization, and secure communication channels.

**Q. Are prompt security elements model-agnostic?**

**A. **Generally, prompt security elements are designed for specific LLMs. Each LLM is trained differently in terms of data quality, diversity, representation, bias, and fine-tuning approaches, so a prompt security element that was introduced for one LLM isn't directly transferrable to another LLM. However, the security elements discussed in this guide can provide a framework and direction for developing tailored prompt security elements for other LLMs.

**Q. How should I integrate these elements into an enterprise MLOps framework?**

**A. **Depending on your organization's constraints and data landscape, prompt security elements can be owned by the data scientist or developer who is working on a specific generative AI use case or by a central generative AI governance team. When you design the MLOps framework for a generative AI solution and release the solution to the production environment, we recommend that you review the AWS blog posts [FMOps/LLMOps: Operationalize generative AI and differences with MLOps](https://aws.amazon.com/blogs/machine-learning/fmops-llmops-operationalize-generative-ai-and-differences-with-mlops/) and [Operationalize LLM Evaluation at Scale using SageMaker AI Clarify and MLOps services](https://aws.amazon.com/blogs/machine-learning/operationalize-llm-evaluation-at-scale-using-amazon-sagemaker-clarify-and-mlops-services/) as a starting point. Consider introducing security gates to ensure that proper prompt-level security has been added.

**Q. What are some of the successful use cases?**

**A. **The guardrails that are discussed in this guide were used successfully in RAG-based solutions for HR, corporate policy, insurance document summarization, corporate investment, and medical record summarization.
