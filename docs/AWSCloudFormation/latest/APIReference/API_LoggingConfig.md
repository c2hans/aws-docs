---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_LoggingConfig.html
---

# LoggingConfig
<a name="API_LoggingConfig"></a>

Contains logging configuration information for an extension.

## Contents
<a name="API_LoggingConfig_Contents"></a>

 ** LogGroupName **
The Amazon CloudWatch Logs group to which CloudFormation sends error logging information when invoking the extension's handlers.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: Yes

 ** LogRoleArn **
The Amazon Resource Name (ARN) of the role that CloudFormation should assume when sending log entries to CloudWatch Logs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:.+:iam::[0-9]{12}:role/.+`
Required: Yes

## See Also
<a name="API_LoggingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/LoggingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/LoggingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/LoggingConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
