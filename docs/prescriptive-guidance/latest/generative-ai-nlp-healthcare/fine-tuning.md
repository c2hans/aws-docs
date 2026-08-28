---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/generative-ai-nlp-healthcare/fine-tuning.html
---

# Fine-tuning large language models in healthcare
<a name="fine-tuning"></a>

The fine-tuning approach described in this section supports compliance with ethical and regulatory guidelines and promotes the responsible use of AI systems in healthcare. It is designed to generate insights that are accurate and private. Generative AI is revolutionizing healthcare delivery, but off-the-shelf models often fall short in clinical environments where accuracy is critical and compliance is non-negotiable. Fine-tuning foundation models with domain-specific data bridges this gap. It helps you create AI systems that speak the language of medicine while adhering to strict regulatory standards. However, the path to successful fine-tuning requires careful navigation of healthcare's unique challenges: protecting sensitive data, justifying AI investments with measurable outcomes, and maintaining clinical relevance in fast-evolving medical landscapes.

When lighter-weight approaches reach their limits, fine-tuning becomes a strategic investment. The expectation is that the gains in accuracy, latency, or operational efficiency will offset the significant compute and engineering costs required. It's important to remember that the pace of progress in foundation models is rapid, so a fine-tuned model's advantage might last only until the next major model release.

This section anchors the discussion in the following two high-impact use cases from AWS healthcare customers:
+ **Clinical decision support systems** – Enhance diagnostic accuracy through models that understand complex patient histories and evolving guidelines. Fine-tuning can help models deeply understand complex patient histories and integrate specialized guidelines This can potentially reduce model prediction errors. However, you need to weigh these gains against the cost of training on large, sensitive datasets and the infrastructure required for high-stakes clinical applications. Will the improved accuracy and context-awareness justify the investment, especially when new models are released frequently?
+ **Medical document analysis** – Automate the processing of clinical notes, imaging reports, and insurance documents while maintaining Health Insurance Portability and Accountability Act (HIPAA) compliance. Here, fine-tuning may enable the model to handle unique formats, specialized abbreviations, and regulatory requirements more effectively. The payoff is often seen in reduced manual review time and improved compliance. Still, it's essential to assess whether these improvements are substantial enough to warrant the fine-tuning resources. Determine whether prompt engineering and workflow orchestration can meet your needs.

These real-world scenarios illustrate the fine-tuning journey, from initial experimentation to model deployment, while addressing healthcare's unique requirements at every stage.

## Estimating costs and return on investment
<a name="fine-tuning-costs"></a>

The following are cost factors that you must consider when fine-tuning an LLM:
+ **Model size** – Larger models cost more to fine-tune
+ **Dataset size** – The compute costs and time increase with the size of the dataset for fine-tuning
+ **Fine-tuning strategy** – Parameter-efficient methods can reduce costs compared to full parameter updates

When calculating the return on investment (ROI), consider the improvement in your chosen metrics (such as accuracy) multiplied by the volume of requests (how often the model will be used) and the expected duration before the model is surpassed by newer versions.

Also, consider the lifespan of your base LLM. New base models emerge every 6–12 months. If your rare disease detector takes 8 months to fine-tune and validate, you might only get 4 months of superior performance before newer models close the gap.

By calculating the costs, ROI, and potential lifespan for your use case, you can make a data-driven decision. For example, if fine-tuning your clinical decision support model leads to a measurable reduction in diagnostic errors across thousands of cases per year, the investment might quickly pay off. Conversely, if prompt engineering alone brings your document analysis workflow close to your target accuracy, it might be wise to hold off on fine-tuning until the next generation of models arrives.

Fine-tuning isn't one-size-fits-all. If you decide to fine-tune, the right approach depends on your use case, data, and resources.

## Choosing a fine-tuning strategy
<a name="fine-tuning-strategy"></a>

After you've determined that fine-tuning is the right approach for your healthcare use case, the next step is selecting the most appropriate fine-tuning strategy. There are several approaches available. Each has distinct advantages and trade-offs for healthcare applications. The choice between these methods depends on your specific objectives, available data, and resource constraints.

### Training objectives
<a name="training-objectives.a9b43906-96be-5047-8dad-97ae8ce083a4"></a>

[Domain-adaptive pre-training (DAPT)](https://arxiv.org/abs/2504.09687) is an unsupervised method that involves pre-training the model on a large body of domain-specific, unlabeled text (such as millions of medical documents). This approach is well suited for improving the models' ability to understand medical specialty abbreviations and the terminology used by radiologists, neurologists, and other specialized providers. However, DAPT requires vast amounts of data and doesn't address specific task outputs.

[Supervised fine-tuning (SFT)](https://arxiv.org/abs/2506.14681) teaches the model to follow explicit instructions by using structured input-output examples. This approach excels for medical document analysis workflows, such as document summarization or clinical coding. *Instruction tuning *is a common form of SFT where the model is trained on examples that include explicit instructions paired with desired outputs. This enhances the model's ability to understand and follow diverse user prompts. This technique is particularly valuable in healthcare settings because it trains the model with specific clinical examples. The main drawback is that it requires carefully labeled examples. In addition, the fine-tuned model might struggle with edge cases where there aren't examples. For a instructions about fine-tuning with Amazon SageMaker Jumpstart, see [Instruction fine-tuning for FLAN T5 XL with Amazon SageMaker Jumpstart](https://aws.amazon.com/blogs/machine-learning/instruction-fine-tuning-for-flan-t5-xl-with-amazon-sagemaker-jumpstart/) (AWS blog post).

[Reinforcement learning from human feedback (RLHF)](https://aws.amazon.com/what-is/reinforcement-learning-from-human-feedback/) optimizes model behavior based on expert feedback and preferences. Use a reward model trained on human preferences and methods, such as [proximal policy optimization (PPO)](https://docs.aws.amazon.com/nova/latest/userguide/customize-fine-tune-hyperpod-ppo.html) or [direct preference optimization (DPO)](https://docs.aws.amazon.com/nova/latest/userguide/customize-fine-tune-hyperpod-dpo.html), to optimize the model while preventing destructive updates. RLHF is ideal for aligning outputs with clinical guidelines and making sure that recommendations stay within approved protocols. This approach requires significant clinician time for feedback and involves a complex training pipeline. However, RLHF is particularly valuable in healthcare because it helps medical experts shape how AI systems communicate and make recommendations. For example, clinicians can provide feedback to make sure that the model maintains an appropriate bedside manner, knows when to express uncertainty, and stays within clinical guidelines. Techniques such as PPO iteratively optimize model behavior based on expert feedback while constraining parameter updates to preserve core medical knowledge. This allows models to convey complex diagnoses in patient-friendly language while still flagging serious conditions for immediate medical attention. This is crucial for healthcare where both accuracy and communication style matter. For more information about RLHF, see [Fine-tune large language models with reinforcement learning from human or AI feedback](https://aws.amazon.com/blogs/machine-learning/fine-tune-large-language-models-with-reinforcement-learning-from-human-or-ai-feedback/) (AWS blog post).

### Implementation methods
<a name="implementation-methods.e7b2de3f-5ed3-5148-9a73-c47ce838011c"></a>

A *full parameter update* involves updating all model parameters during training. This approach works best for clinical decision support systems that require deep integration of patient histories, lab results, and evolving guidelines. The drawbacks include high compute cost and risk of overfitting if your dataset isn't large and diverse.

[Parameter-efficient fine-tuning (PEFT)](https://arxiv.org/abs/2312.12148) methods update only a subset of parameters to prevent overfitting or a catastrophic loss of language capabilities. Types include [low-rank adaptation (LoRA)](https://arxiv.org/abs/2106.09685), adapters, and prefix-tuning. PEFT methods offer lower computational cost, faster training, and are great for experiments such as adapting a clinical decision support model to a new hospital's protocols or terminology. The main limitation is potentially reduced performance compared to full parameter updates.

For more information about fine-tuning methods, see [Advanced fine-tuning methods on Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/advanced-fine-tuning-methods-on-amazon-sagemaker-ai/) (AWS blog post).

## Building a fine-tuning dataset
<a name="fine-tuning-dataset"></a>

The quality and diversity of the fine-tuning dataset is critical to model performance, safety, and bias prevention. The following are three critical areas to consider when building this dataset:
+ Volume based on fine-tuning approach
+ Data annotation from a domain expert
+ Diversity of data set

As shown in the following table, the dataset size requirements for fine-tuning vary based on the type of fine-tuning being performed.

|
|
| **Fine-tuning strategy** | **Dataset size** |
| --- |--- |
| Domain adapted pre-training | 100,000\+ domain texts |
| Supervised fine-tuning | 10,000\+ labeled pairs |
| Reinforcement learning from human feedback | 1,000\+ expert preference pairs |

You can use [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html), [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html), and [Amazon SageMaker Data Wrangler](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler.html) to automate the data extraction and transformation process to curate a dataset that you own. If you are unable to curate a large enough dataset, you can discover and download datasets directly into your AWS account through [AWS Data Exchange](https://docs.aws.amazon.com/data-exchange/latest/userguide/what-is.html). Consult your legal counsel prior to utilizing any third-party datasets.

Expert annotators with domain knowledge, such as medical doctors, biologists, and chemists, should be a part of the data curation process in order to incorporate the nuances of medical and biological data into the model output. [Amazon SageMaker Ground Truth](https://docs.aws.amazon.com/sagemaker/latest/dg/sms.html) provides a low-code user interface for experts to annotate the dataset.

A dataset that represents the human population is essential for healthcare and life sciences fine-tuning use cases to prevent bias and reflect real world results. [AWS Glue interactive sessions](https://docs.aws.amazon.com/glue/latest/dg/interactive-sessions-chapter.html) or [Amazon SageMaker notebook instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html) offer a powerful way to iteratively explore datasets and fine-tune transformations by using Jupyter-compatible notebooks. Interactive sessions enable you to work with a choice of popular integrated development environments (IDEs) in your local environment. Alternatively, you can work with AWS Glue or [Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio.html) notebooks through the AWS Management Console.

## Fine-tuning the model
<a name="fine-tuning-implementation"></a>

AWS provides services such as [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) and [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) that are crucial for successful fine-tuning.

SageMaker AI is a fully managed machine learning service that helps developers and data scientists to build, train, and deploy ML models quickly. Three useful features of SageMaker AI for fine-tuning include:
+ [SageMaker Training](https://docs.aws.amazon.com/sagemaker/latest/dg/train-model.html) – A fully managed ML feature that helps you efficiently train a wide range of models at scale
+ [SageMaker JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html) – A capability that is built on top of SageMaker Training jobs to provide pre-trained models, built-in algorithms, and solution templates for ML tasks
+ [SageMaker HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html) – A purpose-built infrastructure solution for distributed training of foundation models and LLMs

Amazon Bedrock is a fully managed service that provides access to high-performing foundation models through an API, with built-in security, privacy, and scalability features. The service provides the capability to fine-tune several available foundational models. For more information, see [Supported models and Regions for fine-tuning and continued pre-training](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-supported.html) in the Amazon Bedrock documentation.

When approaching the fine-tuning process with either service, consider the base model, fine-tuning strategy, and infrastructure.

### Base model choice
<a name="base-model-choice.9ac49dfa-0d0f-5434-9ce4-383d4d601722"></a>

Closed-source models, such as Anthropic Claude, Meta Llama, and Amazon Nova, deliver strong out-of-the-box performance with managed compliance but limit fine-tuning flexibility to provider-supported options such as managed APIs like Amazon Bedrock. This constrains customizability, particularly for regulated healthcare use cases. In contrast, open-source models, such as Meta Llama, provide full control and flexibility across Amazon SageMaker AI services, making them ideal when you need to customize, audit, or deeply adapt a model to your specific data or workflow requirements.

### Fine-tuning strategy
<a name="fine-tuning-strategy.5c89c2cc-a11b-5bbd-9b85-f487aafd92ed"></a>

Simple instruction tuning can be handled by Amazon Bedrock [model customization](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html) or Amazon SageMaker JumpStart. Complex PEFT approaches, such as LoRA or adapters, require SageMaker Training jobs or custom fine-tuning feature in Amazon Bedrock. Distributed training for very large models is supported by SageMaker HyperPod.

### Infrastructure scale and control
<a name="infrastructure-scale-and-control.cdf2ff70-3099-570b-a6ed-d7ae06a019a0"></a>

Fully managed services, such as Amazon Bedrock, minimize infrastructure management and are ideal for organizations that prioritize ease of use and compliance. Semi-managed options, such as SageMaker JumpStart, offer some flexibility with less complexity. These options are suitable for rapid prototyping or when using pre-built workflows. Full control and customization come with SageMaker Training jobs and HyperPod, though these require more expertise and are best when you need to scale up for large datasets or require custom pipelines.

## Monitoring fine-tuned models
<a name="fine-tuning-monitoring"></a>

In healthcare and life sciences, monitoring LLM fine-tuning requires tracking multiple key performance indicators. Accuracy provides a baseline measurement, but this must be balanced against precision and recall, particularly in applications where misclassifications carry significant consequences. The F1-score helps address class imbalance issues that can be common in medical datasets. For more information, see [Evaluating LLMs for healthcare and life science applications](evaluation.md) in this guide.

Calibration metrics help you make sure that the model's confidence levels match real-world probabilities. [Fairness metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-measure-data-bias.html) can help you detect potential biases across different patient demographics.

[MLflow](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html) is an open source solution that can help you track fine-tuning experiments. MLflow is natively supported within Amazon SageMaker AI, which helps you to visually compare metrics from training runs. For fine-tuning jobs on Amazon Bedrock, metrics are streamed to Amazon CloudWatch so that you can visualize the metrics in the CloudWatch console.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
