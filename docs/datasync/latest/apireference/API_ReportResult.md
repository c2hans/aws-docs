---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_ReportResult.html
---

# ReportResult
<a name="API_ReportResult"></a>

Indicates whether DataSync created a complete [task report](https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html) for your transfer.

## Contents
<a name="API_ReportResult_Contents"></a>

 ** ErrorCode **   <a name="DataSync-Type-ReportResult-ErrorCode"></a>
Indicates the code associated with the error if DataSync can't create a complete report.
Type: String
Required: No

 ** ErrorDetail **   <a name="DataSync-Type-ReportResult-ErrorDetail"></a>
Provides details about issues creating a report.
Type: String
Required: No

 ** Status **   <a name="DataSync-Type-ReportResult-Status"></a>
Indicates whether DataSync is still working on your report, created a report, or can't create a complete report.
Type: String
Valid Values: `PENDING | SUCCESS | ERROR`
Required: No

## See Also
<a name="API_ReportResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/ReportResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/ReportResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/ReportResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
