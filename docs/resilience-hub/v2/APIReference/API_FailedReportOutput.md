---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_FailedReportOutput.html
---

# FailedReportOutput
<a name="API_FailedReportOutput"></a>

Details when report generation failed.

## Contents
<a name="API_FailedReportOutput_Contents"></a>

 ** errorCode **   <a name="ngresiliencehub-Type-FailedReportOutput-errorCode"></a>
The error code describing why the report generation failed.
Type: String
Valid Values: `INSUFFICIENT_PERMISSIONS | CONFIGURATION_ERROR | INTERNAL_ERROR`
Required: Yes

 ** errorMessage **   <a name="ngresiliencehub-Type-FailedReportOutput-errorMessage"></a>
The error message describing why the report generation failed.
Type: String
Required: No

## See Also
<a name="API_FailedReportOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/FailedReportOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/FailedReportOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/FailedReportOutput)
