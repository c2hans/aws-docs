---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/amazon-sns-topics.html
---

# Amazon SNS topics
<a name="amazon-sns-topics"></a>

Two Amazon SNS topics are created with the solution by default. One topic is to notify on all `AWSAccelerator-Pipeline` pipeline events. The second notifies only on `AWSAccelerator-Pipeline` pipeline failures. You can choose to subscribe to these topics to increase the observability of your pipeline operations. For more information, refer to [Subscribing to an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-subscribe-endpoint-to-topic.html) in the *Amazon SNS Developer Guide*.

An optional third Amazon SNS topic is created if the **EnableApprovalStage** parameter is set to `Yes` in the **AWSAccelerator-InstallerStack**. You can provide a comma-delimited list of email addresses in the **ApprovalStageNotifyEmailList** parameter to automatically subscribe to this Amazon SNS topic.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
