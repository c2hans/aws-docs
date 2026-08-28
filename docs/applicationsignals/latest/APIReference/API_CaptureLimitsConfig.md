---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_CaptureLimitsConfig.html
---

# CaptureLimitsConfig
<a name="API_CaptureLimitsConfig"></a>

Guardrails that prevent instrumentation from impacting application performance by limiting how much data is captured.

## Contents
<a name="API_CaptureLimitsConfig_Contents"></a>

 ** MaxCollectionDepth **   <a name="applicationsignals-Type-CaptureLimitsConfig-MaxCollectionDepth"></a>
The maximum nesting depth to traverse inside collections. Defaults to 3.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5.
Required: No

 ** MaxCollectionWidth **   <a name="applicationsignals-Type-CaptureLimitsConfig-MaxCollectionWidth"></a>
The maximum number of items to capture from any collection to prevent large payloads. Defaults to 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: No

 ** MaxFieldsPerObject **   <a name="applicationsignals-Type-CaptureLimitsConfig-MaxFieldsPerObject"></a>
The maximum number of fields to capture for any object. Defaults to 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: No

 ** MaxHits **   <a name="applicationsignals-Type-CaptureLimitsConfig-MaxHits"></a>
The maximum number of times the instrumentation point can be hit before it is automatically disabled. Defaults to 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** MaxObjectDepth **   <a name="applicationsignals-Type-CaptureLimitsConfig-MaxObjectDepth"></a>
The maximum depth for nested object traversal when capturing structured data. Defaults to 3.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5.
Required: No

 ** MaxStackFrames **   <a name="applicationsignals-Type-CaptureLimitsConfig-MaxStackFrames"></a>
The maximum number of stack frames to capture in stack traces. Defaults to 2.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: No

 ** MaxStackTraceSize **   <a name="applicationsignals-Type-CaptureLimitsConfig-MaxStackTraceSize"></a>
The maximum total size, in bytes, of a captured stack trace. Defaults to 1000.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** MaxStringLength **   <a name="applicationsignals-Type-CaptureLimitsConfig-MaxStringLength"></a>
The maximum length of captured string values in characters. Strings longer than this are truncated. Defaults to 128.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 255.
Required: No

## See Also
<a name="API_CaptureLimitsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/CaptureLimitsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/CaptureLimitsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/CaptureLimitsConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
