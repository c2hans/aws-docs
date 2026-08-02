---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ReportOutput.html
---

# ReportOutput
<a name="API_ReportOutput"></a>

Union of possible report outputs.

## Contents
<a name="API_ReportOutput_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** failedReportOutput **   <a name="ngresiliencehub-Type-ReportOutput-failedReportOutput"></a>
Details when report generation failed.
Type: [FailedReportOutput](API_FailedReportOutput.md) object
Required: No

 ** s3ReportOutput **   <a name="ngresiliencehub-Type-ReportOutput-s3ReportOutput"></a>
The S3 location where the report was written.
Type: [S3ReportOutput](API_S3ReportOutput.md) object
Required: No

## See Also
<a name="API_ReportOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ReportOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ReportOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ReportOutput)
