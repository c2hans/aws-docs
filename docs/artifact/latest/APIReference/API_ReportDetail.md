---
source_url: https://docs.aws.amazon.com/artifact/latest/APIReference/API_ReportDetail.html
---

# ReportDetail
<a name="API_ReportDetail"></a>

Full detail for report resource metadata.

## Contents
<a name="API_ReportDetail_Contents"></a>

 ** acceptanceType **   <a name="artifact-Type-ReportDetail-acceptanceType"></a>
Acceptance type for report.
Type: String
Valid Values: `PASSTHROUGH | EXPLICIT`
Required: No

 ** arn **   <a name="artifact-Type-ReportDetail-arn"></a>
ARN for the report resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: No

 ** category **   <a name="artifact-Type-ReportDetail-category"></a>
Category for the report resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_\-\s]*`
Required: No

 ** companyName **   <a name="artifact-Type-ReportDetail-companyName"></a>
Associated company name for the report resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_\-\s]*`
Required: No

 ** createdAt **   <a name="artifact-Type-ReportDetail-createdAt"></a>
Timestamp indicating when the report resource was created.
Type: Timestamp
Required: No

 ** deletedAt **   <a name="artifact-Type-ReportDetail-deletedAt"></a>
Timestamp indicating when the report resource was deleted.
Type: Timestamp
Required: No

 ** description **   <a name="artifact-Type-ReportDetail-description"></a>
Description for the report resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: No

 ** id **   <a name="artifact-Type-ReportDetail-id"></a>
Unique resource ID for the report resource.
Type: String
Pattern: `report-[a-zA-Z0-9]{16}`
Required: No

 ** lastModifiedAt **   <a name="artifact-Type-ReportDetail-lastModifiedAt"></a>
Timestamp indicating when the report resource was last modified.
Type: Timestamp
Required: No

 ** name **   <a name="artifact-Type-ReportDetail-name"></a>
Name for the report resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_\-\s]*`
Required: No

 ** periodEnd **   <a name="artifact-Type-ReportDetail-periodEnd"></a>
Timestamp indicating the report resource effective end.
Type: Timestamp
Required: No

 ** periodStart **   <a name="artifact-Type-ReportDetail-periodStart"></a>
Timestamp indicating the report resource effective start.
Type: Timestamp
Required: No

 ** productName **   <a name="artifact-Type-ReportDetail-productName"></a>
Associated product name for the report resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_\-\s]*`
Required: No

 ** sequenceNumber **   <a name="artifact-Type-ReportDetail-sequenceNumber"></a>
Sequence number to enforce optimistic locking.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** series **   <a name="artifact-Type-ReportDetail-series"></a>
Series for the report resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_\-\s]*`
Required: No

 ** state **   <a name="artifact-Type-ReportDetail-state"></a>
Current state of the report resource
Type: String
Valid Values: `PUBLISHED | UNPUBLISHED`
Required: No

 ** statusMessage **   <a name="artifact-Type-ReportDetail-statusMessage"></a>
The message associated with the current upload state.
Type: String
Required: No

 ** termArn **   <a name="artifact-Type-ReportDetail-termArn"></a>
Unique resource ARN for term resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: No

 ** uploadState **   <a name="artifact-Type-ReportDetail-uploadState"></a>
The current state of the document upload.
Type: String
Valid Values: `PROCESSING | COMPLETE | FAILED | FAULT`
Required: No

 ** version **   <a name="artifact-Type-ReportDetail-version"></a>
Version for the report resource.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_ReportDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/artifact-2018-05-10/ReportDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/artifact-2018-05-10/ReportDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/artifact-2018-05-10/ReportDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Artifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query artifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
