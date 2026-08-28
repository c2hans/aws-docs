---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_LustreLogConfiguration.html
---

# LustreLogConfiguration
<a name="API_LustreLogConfiguration"></a>

The configuration for Lustre logging used to write the enabled logging events for your Amazon FSx for Lustre file system or Amazon File Cache resource to Amazon CloudWatch Logs.

## Contents
<a name="API_LustreLogConfiguration_Contents"></a>

 ** Level **   <a name="FSx-Type-LustreLogConfiguration-Level"></a>
The data repository events that are logged by Amazon FSx.
+  `WARN_ONLY` - only warning events are logged.
+  `ERROR_ONLY` - only error events are logged.
+  `WARN_ERROR` - both warning events and error events are logged.
+  `DISABLED` - logging of data repository events is turned off.
Note that Amazon File Cache uses a default setting of `WARN_ERROR`, which can't be changed.
Type: String
Valid Values: `DISABLED | WARN_ONLY | ERROR_ONLY | WARN_ERROR`
Required: Yes

 ** Destination **   <a name="FSx-Type-LustreLogConfiguration-Destination"></a>
The Amazon Resource Name (ARN) that specifies the destination of the logs. The destination can be any Amazon CloudWatch Logs log group ARN. The destination ARN must be in the same AWS partition, AWS Region, and AWS account as your Amazon FSx file system.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.
Pattern: `^arn:[^:]{1,63}:[^:]{0,63}:[^:]{0,63}:(?:|\d{12}):[^/].{0,1023}$`
Required: No

## See Also
<a name="API_LustreLogConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/LustreLogConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/LustreLogConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/LustreLogConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
