---
source_url: https://docs.aws.amazon.com/autoscaling/plans/userguide/scaling-plan-quotas.html
---

# Quotas for your scaling plans
<a name="scaling-plan-quotas"></a>

Your AWS account has the default quotas (previously referred to as limits) related to scaling plans. Unless otherwise noted, each quota is Region-specific. You can request increases for some quotas, and other quotas cannot be increased.

To view the quotas for Application Auto Scaling, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home). In the navigation pane, choose **AWS services** and select **AWS Auto Scaling Plans**.

To request a quota increase, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.

Your AWS account has the following quotas related to scaling plans.

| Name | Default | Adjustable |
| --- | --- | --- |
| Scalable resources per resource type | Amazon DynamoDB: 3,000 \| Amazon EC2 Auto Scaling groups: 200 \| All other resource types: 500 | Yes |
| Scaling plans | 100 | Yes |
| Scaling instructions per scaling plan | 500 | No |
| Target tracking configurations per scaling instruction | 10 | No |

Keep service quotas in mind as you scale out your workloads. For example, when you reach the maximum number of capacity units allowed by a service, scaling out will stop. If demand drops and the current capacity decreases, AWS Auto Scaling can scale out again. To avoid reaching this service quota limit again, you can request an increase. Each service has its own default quotas for the maximum capacity of the resource. For information about the default quotas for other Amazon Web Services, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) in the *Amazon Web Services General Reference*.
