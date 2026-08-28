---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CloudWatchLogsDestination.html
---

# CloudWatchLogsDestination
<a name="API_CloudWatchLogsDestination"></a>

Contains the destination configuration to use when publishing message sending events.

## Contents
<a name="API_CloudWatchLogsDestination_Contents"></a>

 ** IamRoleArn **   <a name="pinpoint-Type-CloudWatchLogsDestination-IamRoleArn"></a>
The Amazon Resource Name (ARN) of an AWS Identity and Access Management role that is able to write event data to an Amazon CloudWatch destination.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:\S+`
Required: Yes

 ** LogGroupArn **   <a name="pinpoint-Type-CloudWatchLogsDestination-LogGroupArn"></a>
The name of the Amazon CloudWatch log group that you want to record events in.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:\S+`
Required: Yes

## See Also
<a name="API_CloudWatchLogsDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/CloudWatchLogsDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/CloudWatchLogsDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/CloudWatchLogsDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
