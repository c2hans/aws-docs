---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-quotas.html
---

# Quotas for Application Auto Scaling
<a name="application-auto-scaling-quotas"></a>

Your AWS account has default quotas, formerly referred to as limits, for each AWS service. Unless otherwise noted, each quota is Region-specific. You can request increases for some quotas, and other quotas cannot be increased.

To view the quotas for Application Auto Scaling, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home). In the navigation pane, choose **AWS services** and select **Application Auto Scaling**.

To request a quota increase, see [Requesting a Quota Increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.

Your AWS account has the following quotas related to Application Auto Scaling.

| Name | Default | Adjustable |
| --- | --- | --- |
| Scalable targets per resource type | Amazon DynamoDB: 5,000 \| Amazon ECS: 3,000 \| Amazon Keyspaces: 1,500 \| Other resource types: 500 | Yes |
| Scaling policies per scalable target (both step scaling and target tracking policies) | 50 | No |
| Scheduled actions per scalable target | 200 | No |
| Step adjustments per step scaling policy | 20 | Yes |

Keep service quotas in mind as you scale out your workloads. For example, when you reach the maximum number of capacity units allowed by a service, scaling out will stop. If demand drops and the current capacity decreases, Application Auto Scaling can scale out again. To avoid reaching this capacity limit again, you can request an increase. Each service has its own default quotas for the maximum capacity of the resource. For information about the default quotas for other Amazon Web Services, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) in the *Amazon Web Services General Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
