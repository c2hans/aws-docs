---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/prod-monitoring-drift.html
---

# Detecting drift in production applications
<a name="prod-monitoring-drift"></a>

In the context of LLMs, *drift* refers to the gradual degradation of its performance over time. This is typically caused by changes in data distributions or user behavior that the model was not originally trained on. Like ML models, the output of generative AI models is dictated by their input. When the input changes, the output from these models can drift from the original intent. This can lead to a degradation of the generative AI application. In extreme cases, it can produce detrimental outcomes in terms of safety, legal, or monetary losses.  A proactive drift-monitoring framework is essential for maintaining quality and reliability.

## Types of drift in LLMs
<a name="prod-monitoring-drift-types"></a>

Drift can be categorized into two main types, both of which can affect performance: data drift and concept drift.

*Data drift *refers to a statistical change in the input data the model receives. In LLMs, this is most effectively measured as a shift in the distribution of input prompt embeddings. Data drift occurs when the topics, questions, or language style of user prompts in production begin to differ significantly from the data the model was trained or last evaluated on. For example, a customer service bot for a mobile phone company might experience data drift after the launch of a new flagship phone because the distribution of user queries shifts to this new topic.

*Concept drift* refers to a more subtle change in the underlying relationship between inputs and the desired outputs. It occurs when user expectations change or when the meaning of concepts evolves over time. For example, in a financial analysis application, the factors that define a "good investment" might change due to new market conditions. The user prompts might look statistically similar (which means that the data drift is low), but the desired answer has changed (which means the concept drift is high). Detecting concept drift is significantly more challenging. It often involves monitoring downstream business metrics and user feedback rather than direct statistical tests on inputs.

## Data drift detection
<a name="prod-monitoring-drift-detection"></a>

A robust framework for detecting data drift in LLM embeddings should be multi-layered. It should combine efficient statistical methods for initial detection with more sophisticated semantic analysis for interpretation.

### Layer 1: Statistical drift on embeddings
<a name="layer-1--statistical-drift-on-embeddings.bafa8e0f-247b-57b7-9195-1c719f04a65d"></a>

This layer serves as the automated, first line of defense. It follows this process:

1. **Establish a baseline** – Capture a representative sample of prompt embeddings from a stable period, such as the first month of production, to serve as the reference distribution.

1. **Monitor production data** – In real-time or in batches, capture the embeddings of incoming production prompts to create the current distribution.

1. **Compare distributions** – Use statistical tests to quantify the distance between the reference and the current distributions. Commonly used drift metrics, such as the [Kolmogorov–Smirnov (KS) test](https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test) are less effective for generative AI use cases because of the multi-dimensional nature of the LLM embeddings. It's therefore important to use statistics that perform better at measuring drift changes in embedding spaces, such as [Wasserstein distance](https://en.wikipedia.org/wiki/Wasserstein_metric).

1. **Alert if a threshold is breached** – If the calculated distance exceeds a predefined threshold, an alert is triggered. This alert indicates that significant data drift has occurred.

For more information about statistical detection of drift, see the following resources:
+ [Feature attribution drift for models in production](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-monitor-feature-attribution-drift.html) (Amazon SageMaker AI documentation)
+ [Monitor embedding drift for LLMs deployed from Amazon SageMaker JumpStart](https://aws.amazon.com/blogs/machine-learning/monitor-embedding-drift-for-llms-deployed-from-amazon-sagemaker-jumpstart/) (AWS blog post)
+ [How A&E Engineering Uses Serverless Technology to Host Online Machine Learning Models](https://aws.amazon.com/blogs/opensource/how-ae-engineering-uses-serverless-technology-to-host-online-machine-learning-models/) (AWS blog post)
+ [Detecting data drift using Amazon SageMaker AI](https://aws.amazon.com/blogs/architecture/detecting-data-drift-using-amazon-sagemaker/) (AWS blog post)
+ [Learning High-Density Regions for a Generalized Kolmogorov-Smirnov Test in High-Dimensional Data](https://proceedings.neurips.cc/paper/2012/hash/6855456e2fe46a9d49d3d3af4f57443d-Abstract.html) (NeurIPS Proceedings)
+ [Kolmogorov-Smirnov (KS)](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-data-bias-metric-kolmogorov-smirnov.html) (Amazon SageMaker AI documentation)

### Layer 2: Semantic drift using an LLM
<a name="layer-2--semantic-drift-using-an-llm.2e083eeb-deb5-59e5-8a9f-4d64b7e72d59"></a>

A statistical alert indicates that a drift has happened, but it doesn't indicate why. To gain actionable insights, you can use the LLM-as-a-judge approach to analyze and classify the nature of the drift:

1. **Sample the drifted data** – When a statistical drift alert is triggered, collect a sample of the prompts from the period that caused the alert.

1. **Perform a semantic analysis and classify the drift** – Use a judge LLM with a carefully engineered prompt to compare the drifted prompts to a sample from the reference baseline. The judge's task is to categorize the nature of the change. For example, it might be prompted to classify the primary reason for the drift as "Emergence of a new topic," "Shift in user intent," "Increase in query complexity," or "Change in language style."

1. **Review the results** – The results of this classification provide the human team with a clear understanding of the drift's root cause. This classification guides the subsequent improvement actions.

For more information about using an LLM to gain a semantic understanding of detected drift, see the following resources:
+ [Joint Detection of Fraud and Concept Drift inOnline Conversations with LLM-Assisted Judgment](https://arxiv.org/abs/2505.07852v1) (Arxiv)
+ [LLM-as-a-judge: a complete guide to using LLMs for evaluations](https://www.evidentlyai.com/llm-guide/llm-as-a-judge) (Evidently AI)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
