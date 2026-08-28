---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus06-bp01.html
---

# ADVSUS06-BP01 Shut down resources when not in use, and implement energy-efficient machine learning models
<a name="advsus06-bp01"></a>

 Resources for machine learning may have real-time demands that fluctuate or not be needed at certain times, such as when data can be processed as a batch. Set machine learning workloads to respond to demand in real-time, including turning off or shutting down resources when not needed. Use available tools to optimize the compute resources and models used for machine learning workloads.

## Implementation guidance
<a name="implementation-guidance-73"></a>
+  Organizations can use machine learning to draw insights on correlation and causation from data sets in order to optimize advertising activities. However, resources for data preparation, identity resolution, data collaboration, and creation of machine learning models do not need to run 24/7. Optimize and shut down these resources when not in use to reduce carbon emissions.
+  When using [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/), customers can take multiple steps to optimize their compute usage:
  +  Use Graviton-based instances when possible.
  +  [Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html) can specify the most performant instance type.
  +  [Inference optimization techniques](https://docs.aws.amazon.com/sagemaker/latest/dg/model-optimize.html) can be applied to SageMaker AI models.
  +  SageMaker AI can dynamically adjust the number of instances provisioned for a model in response to changes in your workload by using [scaling policies](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling.html).
+  Use AI chips that provide the highest performance for training and inference, such as [AWS Tranium](https://aws.amazon.com/ai/machine-learning/trainium/) and [AWS Inferentia](https://aws.amazon.com/ai/machine-learning/inferentia/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
