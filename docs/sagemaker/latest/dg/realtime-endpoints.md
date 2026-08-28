---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html
---

# Real-time inference
<a name="realtime-endpoints"></a>

 Real-time inference is ideal for inference workloads where you have real-time, interactive, low latency requirements. You can deploy your model to SageMaker AI hosting services and get an endpoint that can be used for inference. These endpoints are fully managed and support autoscaling (see [Automatic scaling of Amazon SageMaker AI models](endpoint-auto-scaling.md)). You can monitor individual instances and containers on your endpoints with enhanced metrics (see [Amazon SageMaker AI enhanced metrics for inference endpoints](monitoring-cloudwatch-enhanced-metrics.md)).

**Topics**
+ [Deploy models for real-time inference](realtime-endpoints-deploy-models.md)
+ [Invoke models for real-time inference](realtime-endpoints-test-endpoints.md)
+ [Invoke endpoints with OpenAI-compatible APIs](realtime-endpoints-openai-compatible.md)
+ [Endpoints](realtime-endpoints-manage.md)
+ [Hosting options](realtime-endpoints-options.md)
+ [Automatic scaling of Amazon SageMaker AI models](endpoint-auto-scaling.md)
+ [Instance storage volumes](host-instance-storage.md)
+ [Validation of models in production](model-validation.md)
+ [Online explainability with SageMaker Clarify](clarify-online-explainability.md)
+ [Deploy to multiple instance types with instance pools](realtime-endpoints-heterogeneous.md)
+ [Fine-tune models with adapter inference components](realtime-endpoints-adapt.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
