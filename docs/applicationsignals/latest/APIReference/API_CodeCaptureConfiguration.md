---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_CodeCaptureConfiguration.html
---

# CodeCaptureConfiguration
<a name="API_CodeCaptureConfiguration"></a>

Defines what data to capture for code-level instrumentation, including arguments, return values, stack traces, local variables, and safety limits.

## Contents
<a name="API_CodeCaptureConfiguration_Contents"></a>

 ** CaptureLimits **   <a name="applicationsignals-Type-CodeCaptureConfiguration-CaptureLimits"></a>
Safety limits that bound what is captured, including hit counts, string length, collection depth, and stack trace size.
Type: [CaptureLimitsConfig](API_CaptureLimitsConfig.md) object
Required: Yes

 ** CaptureArguments **   <a name="applicationsignals-Type-CodeCaptureConfiguration-CaptureArguments"></a>
The function arguments to capture. Omit to capture defaults, use an empty list to capture none, use `["*"]` to capture all arguments, or specify argument names to capture selectively (up to 10 entries).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 80.
Required: No

 ** CaptureLocals **   <a name="applicationsignals-Type-CodeCaptureConfiguration-CaptureLocals"></a>
The local variables to capture by name. Omit or pass an empty list to capture none. You can specify up to 20 names.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 80.
Required: No

 ** CaptureReturn **   <a name="applicationsignals-Type-CodeCaptureConfiguration-CaptureReturn"></a>
Whether to capture the return value. Defaults to false.
Type: Boolean
Required: No

 ** CaptureStackTrace **   <a name="applicationsignals-Type-CodeCaptureConfiguration-CaptureStackTrace"></a>
Whether to capture a stack trace when the instrumentation point is hit. Defaults to true.
Type: Boolean
Required: No

## See Also
<a name="API_CodeCaptureConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/CodeCaptureConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/CodeCaptureConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/CodeCaptureConfiguration)
