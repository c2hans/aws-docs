---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ReportOutput.html
---

# ReportOutput
<a name="API_ReportOutput"></a>

The output location or cause of a failure in report generation.

## Contents
<a name="API_ReportOutput_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** failedReportOutput **   <a name="regionswitch-Type-ReportOutput-failedReportOutput"></a>
The details about a failed report generation.
Type: [FailedReportOutput](API_FailedReportOutput.md) object
Required: No

 ** s3ReportOutput **   <a name="regionswitch-Type-ReportOutput-s3ReportOutput"></a>
Information about a report delivered to Amazon S3.
Type: [S3ReportOutput](API_S3ReportOutput.md) object
Required: No

## See Also
<a name="API_ReportOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/ReportOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/ReportOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/ReportOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-region-switch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
