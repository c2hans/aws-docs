---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html
---

# Step scaling policies for Application Auto Scaling
<a name="application-auto-scaling-step-scaling-policies"></a>

A step scaling policy scales your application's capacity in predefined increments based on CloudWatch alarms. You can define separate scaling policies to handle scaling out (increasing capacity) and scaling in (decreasing capacity) when an alarm threshold is breached.

With step scaling policies, you create and manage the CloudWatch alarms that invoke the scaling process. When an alarm is breached, Application Auto Scaling initiates the scaling policy associated with that alarm.

The step scaling policy scales capacity using a set of adjustments, known as *step adjustments*. The size of the adjustment varies based on the magnitude of the alarm breach.
+ If the breach exceeds the first threshold, Application Auto Scaling will apply the first step adjustment.
+ If the breach exceeds the second threshold, Application Auto Scaling will apply the second step adjustment, and so on.

This allows the scaling policy to respond appropriately to both minor and major changes in the alarm metric.

The policy will continue to respond to additional alarm breaches, even while a scaling activity is in progress. This means Application Auto Scaling will evaluate all alarm breaches as they occur. A cooldown period is used to protect against over-scaling due to multiple alarm breaches occurring in rapid succession.

Like target tracking, step scaling can help automatically scale your application's capacity as traffic changes occur. However, target tracking policies tend to be easier to implement and manage for steady scaling needs.

**Supported scalable targets**

You can use step scaling policies with the following scalable targets:
+ WorkSpaces Applications fleets
+ Aurora DB clusters
+ ECS services
+ EMR clusters
+ SageMaker AI endpoint variants
+ SageMaker AI inference components
+ SageMaker AI Serverless provisioned concurrency
+ Spot Fleets
+ Custom resources

**Topics**
+ [How step scaling works](step-scaling-policy-overview.md)
+ [Create a step scaling policy](create-step-scaling-policy-cli.md)
+ [Describe step scaling policies](describe-step-scaling-policy.md)
+ [Delete a step scaling policy](delete-step-scaling-policy.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
