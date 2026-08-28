---
source_url: https://docs.aws.amazon.com/artifact/latest/APIReference/API_ReportSummary.html
---

# ReportSummary
<a name="API_ReportSummary"></a>

Summary for report resource.

## Contents
<a name="API_ReportSummary_Contents"></a>

 ** acceptanceType **   <a name="artifact-Type-ReportSummary-acceptanceType"></a>
Acceptance type for report.
Type: String
Valid Values: `PASSTHROUGH | EXPLICIT`
Required: No

 ** arn **   <a name="artifact-Type-ReportSummary-arn"></a>
ARN for the report resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: No

 ** category **   <a name="artifact-Type-ReportSummary-category"></a>
Category for the report resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_\-\s]*`
Required: No

 ** companyName **   <a name="artifact-Type-ReportSummary-companyName"></a>
Associated company name for the report resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_\-\s]*`
Required: No

 ** description **   <a name="artifact-Type-ReportSummary-description"></a>
Description for the report resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: No

 ** id **   <a name="artifact-Type-ReportSummary-id"></a>
Unique resource ID for the report resource.
Type: String
Pattern: `report-[a-zA-Z0-9]{16}`
Required: No

 ** name **   <a name="artifact-Type-ReportSummary-name"></a>
Name for the report resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_\-\s]*`
Required: No

 ** periodEnd **   <a name="artifact-Type-ReportSummary-periodEnd"></a>
Timestamp indicating the report resource effective end.
Type: Timestamp
Required: No

 ** periodStart **   <a name="artifact-Type-ReportSummary-periodStart"></a>
Timestamp indicating the report resource effective start.
Type: Timestamp
Required: No

 ** productName **   <a name="artifact-Type-ReportSummary-productName"></a>
Associated product name for the report resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_\-\s]*`
Required: No

 ** series **   <a name="artifact-Type-ReportSummary-series"></a>
Series for the report resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_\-\s]*`
Required: No

 ** state **   <a name="artifact-Type-ReportSummary-state"></a>
Current state of the report resource.
Type: String
Valid Values: `PUBLISHED | UNPUBLISHED`
Required: No

 ** statusMessage **   <a name="artifact-Type-ReportSummary-statusMessage"></a>
The message associated with the current upload state.
Type: String
Required: No

 ** uploadState **   <a name="artifact-Type-ReportSummary-uploadState"></a>
The current state of the document upload.
Type: String
Valid Values: `PROCESSING | COMPLETE | FAILED | FAULT`
Required: No

 ** version **   <a name="artifact-Type-ReportSummary-version"></a>
Version for the report resource.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_ReportSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/artifact-2018-05-10/ReportSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/artifact-2018-05-10/ReportSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/artifact-2018-05-10/ReportSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Artifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query artifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
