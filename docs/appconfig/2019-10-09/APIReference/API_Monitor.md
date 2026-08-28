---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_Monitor.html
---

# Monitor
<a name="API_Monitor"></a>

Amazon CloudWatch alarms to monitor during the deployment process.

## Contents
<a name="API_Monitor_Contents"></a>

 ** AlarmArn **   <a name="appconfig-Type-Monitor-AlarmArn"></a>
Amazon Resource Name (ARN) of the Amazon CloudWatch alarm.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** AlarmRoleArn **   <a name="appconfig-Type-Monitor-AlarmRoleArn"></a>
ARN of an AWS Identity and Access Management (IAM) role for AWS AppConfig to monitor `AlarmArn`.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^((arn):(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov|aws-eusc):(iam)::\d{12}:role[/].*)$`
Required: No

## See Also
<a name="API_Monitor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/Monitor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/Monitor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/Monitor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
