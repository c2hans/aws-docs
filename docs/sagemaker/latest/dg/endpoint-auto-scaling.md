---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling.html
---

# Automatic scaling of Amazon SageMaker AI models
<a name="endpoint-auto-scaling"></a>

Amazon SageMaker AI supports automatic scaling (auto scaling) for your hosted models. *Auto scaling* dynamically adjusts the number of instances provisioned for a model in response to changes in your workload. When the workload increases, auto scaling brings more instances online. When the workload decreases, auto scaling removes unnecessary instances so that you don't pay for provisioned instances that you aren't using. For more information about using per-instance metrics for scaling decisions, see [Amazon SageMaker AI enhanced metrics for inference endpoints](monitoring-cloudwatch-enhanced-metrics.md) and [Enhanced metrics for Amazon SageMaker AI endpoints](https://aws.amazon.com/blogs/machine-learning/enhanced-metrics-for-amazon-sagemaker-ai-endpoints-deeper-visibility-for-better-performance/).

**Topics**
+ [Auto scaling policy overview](endpoint-auto-scaling-policy.md)
+ [Auto scaling prerequisites](endpoint-auto-scaling-prerequisites.md)
+ [Configure model auto scaling with the console](endpoint-auto-scaling-add-console.md)
+ [Register a model](endpoint-auto-scaling-add-policy.md)
+ [Define a scaling policy](endpoint-auto-scaling-add-code-define.md)
+ [Apply a scaling policy](endpoint-auto-scaling-add-code-apply.md)
+ [Instructions for editing a scaling policy](endpoint-auto-scaling-edit.md)
+ [Temporarily turn off scaling policies](endpoint-auto-scaling-suspend-scaling-activities.md)
+ [Delete a scaling policy](endpoint-auto-scaling-delete.md)
+ [Check the status of a scaling activity by describing scaling activities](endpoint-scaling-query-history.md)
+ [Scale an endpoint to zero instances](endpoint-auto-scaling-zero-instances.md)
+ [Load testing your auto scaling configuration](endpoint-scaling-loadtest.md)
+ [Use CloudFormation to create a scaling policy](endpoint-scaling-cloudformation.md)
+ [Update endpoints that use auto scaling](endpoint-scaling-update.md)
+ [Delete endpoints configured for auto scaling](endpoint-delete-with-scaling.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
