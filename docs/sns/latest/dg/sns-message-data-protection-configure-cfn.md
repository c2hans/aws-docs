---
source_url: https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-configure-cfn.html
---

# Creating data protection policies in Amazon SNS using CloudFormation
<a name="sns-message-data-protection-configure-cfn"></a>

**Important**
Amazon SNS message data protection is no longer available to new customers. For more information and guidance on alternatives, see [Amazon SNS message data protection availability change](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-availability-change.html).

The number and size of Amazon SNS resources in an AWS account are limited. For more information, see [Amazon Simple Notification Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/sns.html).

## Creating data protection policies (CloudFormation)
<a name="create-policies-cfn"></a>

Create an Amazon SNS data protection policy using CloudFormation.

**To create a data protection policy together with an Amazon SNS topic (CloudFormation)**
Use this option to create a new data protection policy together with a standard Amazon SNS topic:
+ [AWS::SNS::Topic](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
