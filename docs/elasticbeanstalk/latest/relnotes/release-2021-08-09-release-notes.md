---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2021-08-09-release-notes.html
---

# Release: Elastic Beanstalk added support for Capacity Rebalancing for Amazon EC2 Spot Instances on August 9, 2021
<a name="release-2021-08-09-release-notes"></a>

AWS Elastic Beanstalk added support for Capacity Rebalancing for Amazon EC2 Spot Instances.

**Release date:** August 9, 2021

## Changes
<a name="release-2021-08-09-release-notes.changes"></a>

*Spot Instances* are an Amazon EC2 instance purchasing option that can lower your costs significantly. Although they are a cost-effective option, your requirements must be flexible regarding when your applications run and whether they can be interrupted.

Starting today, Elastic Beanstalk offers the Capacity Rebalancing feature for Amazon EC2 Auto Scaling groups. This feature reduces Spot Instance interruptions to your applications. With ASG Capacity Rebalancing enabled, Amazon EC2 automatically attempts to replace Spot Instances in an Auto Scaling group before they are interrupted.

You can enable Capacity Rebalancing on an existing EC2 Auto Scaling Group using the Elastic Beanstalk Console or the [aws:autoscaling:asg](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options-general.html#command-options-general-autoscalingasg) namespace configuration option. For more information, see [Auto Scaling group for your Elastic Beanstalk environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.as.html) in the *AWS Elastic Beanstalk Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
