---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_Logging.html
---

# Logging
<a name="API_Logging"></a>

Configuration for MicroVM logging output. Specify exactly one: cloudWatch to enable CloudWatch logging, or disabled to turn off logging.

## Contents
<a name="API_Logging_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cloudWatch **   <a name="lambdamicrovm-Type-Logging-cloudWatch"></a>
Configuration for sending logs to Amazon CloudWatch Logs.
Type: [CloudWatchLogging](API_CloudWatchLogging.md) object
Required: No

 ** disabled **   <a name="lambdamicrovm-Type-Logging-disabled"></a>
Specifies that logging is disabled.
Type: [LoggingDisabled](API_LoggingDisabled.md) object
Required: No

## See Also
<a name="API_Logging_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/Logging)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/Logging)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/Logging)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda MicroVMs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
