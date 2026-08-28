---
source_url: https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_Channel.html
---

# Channel
<a name="API_Channel"></a>

Contains information about a returned CloudTrail channel.

## Contents
<a name="API_Channel_Contents"></a>

 ** ChannelArn **   <a name="awscloudtrail-Type-Channel-ChannelArn"></a>
The Amazon Resource Name (ARN) of a channel.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 256.
Pattern: `^[a-zA-Z0-9._/\-:]+$`
Required: No

 ** Name **   <a name="awscloudtrail-Type-Channel-Name"></a>
 The name of the CloudTrail channel. For service-linked channels, the name is `aws-service-channel/service-name/custom-suffix` where `service-name` represents the name of the AWS service that created the channel and `custom-suffix` represents the suffix created by the AWS service.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `^[a-zA-Z0-9._\-]+$`
Required: No

## See Also
<a name="API_Channel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/Channel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/Channel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/Channel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudTrail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awscloudtrail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
