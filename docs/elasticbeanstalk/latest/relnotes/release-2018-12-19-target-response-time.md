---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2018-12-19-target-response-time.html
---

# Release: AWS Elastic Beanstalk adds TargetResponseTime Auto Scaling trigger metric on December 19, 2018
<a name="release-2018-12-19-target-response-time"></a>

Elastic Beanstalk added the option to trigger Auto Scaling events based on response time for environments with Application Load Balancers.

**Release date:** December 19, 2018

## Changes
<a name="release-2018-12-19-target-response-time.changes"></a>

Today's release adds `TargetResponseTime` as a metric to trigger Auto Scaling activity for Elastic Beanstalk environments.

Previously, Elastic Beanstalk required custom `.ebextensions` to configure scaling based on response time for environments with Application Load Balancers. With today's release, you can configure scaling activity directly with the `TargetResponseTime` option in the [`aws:autoscaling:trigger`](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options-general.html#command-options-general-autoscalingtrigger) namespace. For details, see [Auto Scaling Triggers](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-autoscaling-triggers.html) in the *AWS Elastic Beanstalk Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
