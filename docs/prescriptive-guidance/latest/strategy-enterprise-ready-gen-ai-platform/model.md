---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-enterprise-ready-gen-ai-platform/model.html
---

# Layer 2: Approved set of foundation models and tools
<a name="model"></a>

As organizations navigate the early stages of generative AI adoption, they quickly realize that no single model can address all use cases effectively. Different models excel in various domains and tasks, and enterprises need to balance capability, cost, and performance for each specific application. This reality drives the need for a flexible, yet controlled, approach to foundation model access.

**This section contains the following topics:**
+ [Model experimentation and customization](#model-experimentation-customization)
+ [Model evaluation](#model-evaluation)
+ [Implementation recommendations](#model-implementation-recs)

## Model experimentation and customization
<a name="model-experimentation-customization"></a>

[Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) is designed to help you experiment with various foundation models, and it supports scalable production deployments. With Amazon Bedrock [Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html), you have a fully managed solution to build end-to-end Retrieval Augmented Generation (RAG) workflows. Amazon Bedrock also supports managed agents that can run complex tasks without code, from booking travel to managing inventory. Because it's serverless, Amazon Bedrock reduces infrastructure management concerns and integrates securely with other AWS services.

Additionally, you can use Amazon Bedrock to [privately customize the foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html) with your own proprietary data and make them securely available to the users within your organization. For more information, see [Customize your model to improve its performance for your use case](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html) in the Amazon Bedrock documentation. For access management, AWS Identity and Access Management (IAM) integrates with Amazon Bedrock so that you can configure fine-grained access control. The controls determine which users can enable and access specific models. For more information, see [Layer 3: Security and governance](security.md) in this guide.

## Model evaluation
<a name="model-evaluation"></a>

As your organization progresses from generative AI prototypes to production, it's essential to establish rigorous evaluation processes for foundation models. Although open benchmarks offer general insights into model performance, they often fall short when determining a model's suitability for specific enterprise needs. Tailored evaluation strategies help users select the most appropriate model that aligns with the unique requirements of your organization.

### Objectives of custom model evaluation
<a name="objectives-of-custom-model-evaluation.cf6c6e06-7c6d-5670-9017-c45e4a156191"></a>

A custom evaluation approach helps organizations do the following:
+ **Assess performance on business-relevant tasks** – Evaluate how well models handle tasks directly related to your enterprise use cases.
+ **Identify potential biases and limitations** – Detect areas where models might exhibit biases or fail so that you can make sure the model is suitable for real-world deployment.
+ **Compare models with relevant metrics** – Compare different models by using metrics that align you're your organizational priorities and objectives.
+ **Make informed model selection** – Make data-driven decisions about model selection, fine-tuning, and deployment to production environments.

### Choosing model evaluation metrics
<a name="choosing-model-evaluation-metrics.66ee6e17-2ab1-5a76-b64d-601ce4a12bd1"></a>

Effective model evaluation draws on a mix of techniques that provide a holistic view of model performance. With these techniques, organizations can assess not only the technical accuracy of a model but also its alignment with enterprise-specific needs. To evaluate a model, you combine quantitative and qualitative metrics to determine performance, identify biases, and choose a model. Organizations should use both ground truth-based metrics (with reference data) and flexible metrics (without reference data) to gain a comprehensive view of model suitability. In AI, *ground truth* refers to data that is factual and is withheld during model training so that you can use it for model evaluation.

Use ground truth-based metrics if reference data exists. These metrics provide concrete, quantitative assessments. Meanwhile, techniques without ground truth can offer flexibility. These techniques help you evaluate models on dimensions such as readability and completeness, even when predefined correct answers aren't available.

#### Metrics based on ground truth data
<a name="metrics-based-on-ground-truth-data.265d4b19-08dd-5906-9780-d276083eca43"></a>

If reference data is available, ground truth-based metrics can provide quantitative assessments. The following metrics provide quantitative performance assessments:
+ **ROUGE-L score** – Recall-oriented understudy for gisting evaluation (ROUGE) for longest common subsequence (LCS), also known as *ROUGE-L*, measures the longest common subsequence between generated and reference texts. The metric assesses the coherence and content overlap.
+ **Cosine similarity** – This metric evaluates semantic similarity between texts. It provides insights into the model's contextual understanding.
+ **METEOR score** – Metric for evaluation of translation with explicit ordering (METEOR) scoring combines word alignment and semantic matching to provide a balanced assessment of content accuracy and meaning.
+ **Binary similarity** – This metric checks for exact matches, making it particularly useful for tasks that require precise outputs, such as command generation.
+ **LLM-as-a-judge score** – This metric uses another large language model (LLM) to rate similarity on a defined scale. It offers a nuanced evaluation of quality.

Amazon SageMaker Clarify and Amazon Bedrock include features to help you evaluate models. They can automate model evaluation jobs so that you can quantify model risks and response quality. For more information, see [Evaluate, explain, and detect bias in models](https://docs.aws.amazon.com/sagemaker/latest/dg/model-explainability.html) and [Evaluate the performance of Amazon Bedrock resources](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html).

#### Metrics without ground truth data
<a name="metrics-without-ground-truth-data.7369b473-f728-50da-82d2-c342ec853841"></a>

When reference data is unavailable, or as a complementary approach, you can use the *LLM-as-a-judge technique*. It uses a separate model to evaluate the outputs of a generative AI solution based on dimensions that are important to the business. This technique provides flexibility for assessing various model qualities. For more information, see [Evaluate model performance using another LLM as a judge](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html) in the Amazon Bedrock documentation.

You can use computed metrics to evaluate how effectively a Retrieval Augmented Generation (RAG) system retrieves relevant information from your data sources, and how effective the generated responses are in answering questions. The results of a RAG evaluation allow you to compare different Amazon Bedrock Knowledge Bases and other RAG sources, and then to choose the best Knowledge Base or RAG system for your application. For more information, see [Evaluate the performance of RAG sources](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html) in the Amazon Bedrock documentation.

### Model evaluation techniques in practice
<a name="model-evaluation-techniques-in-practice.cb0aa493-2098-58f0-9ad3-df3e558d15f7"></a>

To effectively match enterprise needs with model capabilities, use a robust set of evaluation criteria to direct the model evaluation process. These criteria cover a spectrum of priorities, from correctness and completeness to factuality and sensitive data handling. Each criterion aligns with specific techniques to deliver actionable insights. For instance, when factual accuracy is critical, metrics like ROUGE-L score or cosine similarity provide concrete, quantifiable benchmarks. Conversely, use techniques such as LLM-as-a-judge to evaluate readability and freshness. These techniques offer flexible, qualitative insights tailored to organizational standards. Key dimensions for evaluating models include:
+ **Correctness** – Validates the accuracy of information provided
+ **Completeness** – Verifies the depth and coverage of responses
+ **Readability** – Assesses clarity and ease of understanding
+ **Freshness of information** – Checks that content is relevant and current
+ **Sensitive data suppression** – Checks for proper handling of confidential information
+ **Accuracy** – Measures alignment with factual information
+ **Coherence** – Examines logical flow and consistency
+ **Factuality** – Verifies the truthfulness of the content
+ **Comprehensiveness** – Assesses the scope and thoroughness of coverage

By anchoring model evaluation techniques in these clear criteria, you can thoroughly vet models for their specific purposes. This structured approach aligns models with enterprise goals, compliance requirements, and user expectations. It also lays a strong foundation for deploying generative AI applications at scale in production environments.

## Implementation recommendations
<a name="model-implementation-recs"></a>

To establish an effective foundation model strategy, consider the following recommendations:
+ Form a model governance committee that has clear roles, responsibilities, and decision-making processes.
+ Develop evaluation criteria and scoring mechanisms for the assessment of foundation models before they are available for use across the organization.
+ Remember that the largest foundation model is not necessarily always the best model for your use case. Begin proof-of-concept development with top-tier models to validate business value, and then systematically evaluate smaller models for cost optimization.
+ Develop dashboards to track key metrics, such as inference latency, throughput, error rates, and cost per inference.
+ Provide clear guidance to teams about how to select the right model for their use case, including experimentation processes and evaluation criteria.
