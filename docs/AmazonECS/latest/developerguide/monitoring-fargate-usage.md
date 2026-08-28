---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/monitoring-fargate-usage.html
---

# AWS Fargate usage metrics
<a name="monitoring-fargate-usage"></a>

You can use CloudWatch usage metrics to provide visibility into your accounts usage of resources. Use these metrics to visualize your current service usage on CloudWatch graphs and dashboards.

AWS Fargate usage metrics correspond to AWS service quotas. You can configure alarms that alert you when your usage approaches a service quota. For more information about Fargate service quotas, [Amazon ECS endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/ecs-service.html) in the *Amazon Web Services General Reference*..

AWS Fargate publishes the following metrics in the `AWS/Usage` namespace.

|  Metric  |  Description  |
| --- | --- |
| `ResourceCount` | The total number of the specified resource running on your account. The resource is defined by the dimensions associated with the metric. |

The following dimensions are used to refine the usage metrics that are published by AWS Fargate.

|  Dimension  |  Description  |
| --- | --- |
| `Service` | The name of the AWS service containing the resource. For AWS Fargate usage metrics, the value for this dimension is `Fargate`. |
| `Type` | The type of entity that is being reported. Currently, the only valid value for AWS Fargate usage metrics is `Resource`. |
| `Resource` | The type of resource that is running. The type of resource that is running. Currently, the only valid value for AWS Fargate usage metrics is `vCPU` which returns information about the running instances. |
| `Class` | The class of resource being tracked. The class of resource being tracked. For AWS Fargate usage metrics with vCPU as the value of the Resource dimension, the valid values are `Standard/OnDemand` and `Standard/Spot`. |

You can use the Service Quotas console to visualize your usage on a graph and configure alarms that alert you when your AWS Fargate usage approaches a service quota. For information about how to create a CloudWatch alarm to notify you when you're close to a quota value threshold, see [Service Quotas and Amazon CloudWatch ](https://docs.aws.amazon.com/servicequotas/latest/userguide/configure-cloudwatch.html)alarms in the *Service Quotas User Guide*

.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
