---
source_url: https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/cloudwatch-events.html
---

# Amazon CloudWatch Events
<a name="cloudwatch-events"></a>

[Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) delivers a near real-time stream of system events that describe changes in AWS resources. Using simple rules that you can quickly set up, you can match events and route them to one or more target functions or streams.

CloudWatch Events becomes aware of operational changes as they occur. CloudWatch Events responds to these operational changes and takes corrective action as necessary, by sending messages to respond to the environment, activating functions, making changes, and capturing state information.

You can configure rules in Amazon CloudWatch Events to alert you to changes in AWS services and integrate these events with other third-party systems using Amazon EventBridge. The following are the AWS DevOps related services that have integration with CloudWatch Events.
+ [Application Auto Scaling Events](https://docs.aws.amazon.com/autoscaling/ec2/userguide/cloud-watch-events.html)
+ [CodeBuild Events](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-build-notifications.html)
+ [CodeCommit Events](https://docs.aws.amazon.com/codecommit/latest/userguide/monitoring-events.html)
+ [CodeDeploy Events](https://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-cloudwatch-events.html)
+ [CodePipeline Events](https://docs.aws.amazon.com/codepipeline/latest/userguide/detect-state-changes-cloudwatch-events.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
