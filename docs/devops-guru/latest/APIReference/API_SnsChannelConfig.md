---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_SnsChannelConfig.html
---

# SnsChannelConfig
<a name="API_SnsChannelConfig"></a>

 Contains the Amazon Resource Name (ARN) of an Amazon Simple Notification Service topic.

If you use an Amazon SNS topic in another account, you must attach a policy to it that grants DevOps Guru permission to send it notifications. DevOps Guru adds the required policy on your behalf to send notifications using Amazon SNS in your account. DevOps Guru only supports standard SNS topics. For more information, see [Permissions for Amazon SNS topics](https://docs.aws.amazon.com/devops-guru/latest/userguide/sns-required-permissions.html).

If you use an Amazon SNS topic that is encrypted by an AWS Key Management Service customer-managed key (CMK), then you must add permissions to the CMK. For more information, see [Permissions for AWS KMS–encrypted Amazon SNS topics](https://docs.aws.amazon.com/devops-guru/latest/userguide/sns-kms-permissions.html).

## Contents
<a name="API_SnsChannelConfig_Contents"></a>

 ** TopicArn **   <a name="DevOpsGuru-Type-SnsChannelConfig-TopicArn"></a>
 The Amazon Resource Name (ARN) of an Amazon Simple Notification Service topic.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 1024.
Pattern: `^arn:aws[a-z0-9-]*:sns:[a-z0-9-]+:\d{12}:[^:]+$`
Required: No

## See Also
<a name="API_SnsChannelConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/SnsChannelConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/SnsChannelConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/SnsChannelConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
