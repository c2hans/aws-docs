---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_TelemetryMetadata.html
---

# TelemetryMetadata
<a name="API_TelemetryMetadata"></a>

The metadata about the Amazon Inspector Classic application data metrics collected by the agent. This data type is used as the response element in the [GetTelemetryMetadata](API_GetTelemetryMetadata.md) action.

## Contents
<a name="API_TelemetryMetadata_Contents"></a>

 ** count **   <a name="Inspector-Type-TelemetryMetadata-count"></a>
The count of messages that the agent sends to the Amazon Inspector Classic service.
Type: Long
Required: Yes

 ** messageType **   <a name="Inspector-Type-TelemetryMetadata-messageType"></a>
A specific type of behavioral data that is collected by the agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** dataSize **   <a name="Inspector-Type-TelemetryMetadata-dataSize"></a>
The data size of messages that the agent sends to the Amazon Inspector service.
Type: Long
Required: No

## See Also
<a name="API_TelemetryMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/TelemetryMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/TelemetryMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/TelemetryMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Inspector Classic. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
