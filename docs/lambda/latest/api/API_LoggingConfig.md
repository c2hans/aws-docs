---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_LoggingConfig.html
---

# LoggingConfig
<a name="API_LoggingConfig"></a>

The function's Amazon CloudWatch Logs configuration settings.

## Contents
<a name="API_LoggingConfig_Contents"></a>

 ** ApplicationLogLevel **   <a name="lambda-Type-LoggingConfig-ApplicationLogLevel"></a>
Set this property to filter the application logs for your function that Lambda sends to CloudWatch. Lambda only sends application logs at the selected level of detail and lower, where `TRACE` is the highest level and `FATAL` is the lowest.
Type: String
Valid Values: `TRACE | DEBUG | INFO | WARN | ERROR | FATAL`
Required: No

 ** LogFormat **   <a name="lambda-Type-LoggingConfig-LogFormat"></a>
The format in which Lambda sends your function's application and system logs to CloudWatch. Select between plain text and structured JSON.
Type: String
Valid Values: `JSON | Text`
Required: No

 ** LogGroup **   <a name="lambda-Type-LoggingConfig-LogGroup"></a>
The name of the Amazon CloudWatch log group the function sends logs to. By default, Lambda functions send logs to a default log group named `/aws/lambda/<function name>`. To use a different log group, enter an existing log group or enter a new log group name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** SystemLogLevel **   <a name="lambda-Type-LoggingConfig-SystemLogLevel"></a>
Set this property to filter the system logs for your function that Lambda sends to CloudWatch. Lambda only sends system logs at the selected level of detail and lower, where `DEBUG` is the highest level and `WARN` is the lowest.
Type: String
Valid Values: `DEBUG | INFO | WARN`
Required: No

## See Also
<a name="API_LoggingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/LoggingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/LoggingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/LoggingConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
