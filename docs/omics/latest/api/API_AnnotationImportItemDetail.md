---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_AnnotationImportItemDetail.html
---

# AnnotationImportItemDetail
<a name="API_AnnotationImportItemDetail"></a>

Details about an imported annotation item.

## Contents
<a name="API_AnnotationImportItemDetail_Contents"></a>

 ** jobStatus **   <a name="omics-Type-AnnotationImportItemDetail-jobStatus"></a>
The item's job status.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | CANCELLED | COMPLETED | FAILED | COMPLETED_WITH_FAILURES`
Required: Yes

 ** source **   <a name="omics-Type-AnnotationImportItemDetail-source"></a>
The source file's location in Amazon S3.
Type: String
Pattern: `s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])/(.{1,1024})`
Required: Yes

## See Also
<a name="API_AnnotationImportItemDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/AnnotationImportItemDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/AnnotationImportItemDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/AnnotationImportItemDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
