---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_CaptureConfiguration.html
---

# CaptureConfiguration
<a name="API_CaptureConfiguration"></a>

A union that defines what data to capture when the instrumentation point is hit. Specify `CodeCapture` for code-level capture settings.

## Contents
<a name="API_CaptureConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** CodeCapture **   <a name="applicationsignals-Type-CaptureConfiguration-CodeCapture"></a>
Capture settings for code-level instrumentation, including arguments, return values, stack traces, local variables, and safety limits.
Type: [CodeCaptureConfiguration](API_CodeCaptureConfiguration.md) object
Required: No

## See Also
<a name="API_CaptureConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/CaptureConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/CaptureConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/CaptureConfiguration)
