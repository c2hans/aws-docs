---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/bestpractice5.html
---

# Amazon EC2 On-Demand or Amazon EC2 Spot
<a name="bestpractice5"></a>

Most AWS Batch customers use Amazon EC2 Spot instances because of the savings over On-Demand instances. However, if your workload runs for multiple hours and can't be interrupted, On-Demand instances might be more suitable for you. You can always try Spot instances first and switch to On-Demand if necessary.

If you have the following requirements and expectations, use Amazon EC2 On-Demand instances:
+ The runtime of your jobs is more than an hour, and you can't tolerate interruptions to your workload.
+ You have a strict SLO (service-level objective) for your overall workload and can’t increase computational time.
+ The instances that you require are more likely to see interruptions.

If you have the following requirements and expectations, use Amazon EC2 Spot instances:
+ The runtime for your jobs is typically 30 minutes or less.
+ You can tolerate potential interruptions and job rescheduling as a part of your workload. For more information, see [Spot Instance advisor](https://aws.amazon.com/ec2/spot/instance-advisor/).
+ Long running jobs can be restarted from a checkpoint if interrupted.

You can mix both purchasing models by submitting on Spot instance first and then use On-Demand instance as a fallback option. For example, submit your jobs on a queue that's connected to compute environments that are running on Amazon EC2 Spot instances. If a job gets interrupted, catch the event from Amazon EventBridge and correlate it to a Spot instance reclamation. Then, resubmit the job to an On-Demand queue using an AWS Lambda function or AWS Step Functions. For more information, see [Tutorial: Sending Amazon Simple Notification Service alerts for failed job events](batch_sns_tutorial.md), [Best practices for handling Amazon EC2 Spot Instance interruptions](https://aws.amazon.com/blogs/compute/best-practices-for-handling-ec2-spot-instance-interruptions/) and [ Manage AWS Batch with Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/connect-batch.html).

**Important**
Use different instance types, sizes, and Availability Zones for your On-Demand compute environment to maintain Amazon EC2 Spot instance pool availability and decrease the interruption rate.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
