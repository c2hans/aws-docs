---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BKS_S3ExportSpecification.html
---

# S3ExportSpecification
<a name="API_BKS_S3ExportSpecification"></a>

This specification contains a required string of the destination bucket; optionally, you can include the destination prefix.

## Contents
<a name="API_BKS_S3ExportSpecification_Contents"></a>

 ** DestinationBucket **   <a name="Backup-Type-BKS_S3ExportSpecification-DestinationBucket"></a>
This specifies the destination Amazon S3 bucket for the export job.
Type: String
Required: Yes

 ** DestinationPrefix **   <a name="Backup-Type-BKS_S3ExportSpecification-DestinationPrefix"></a>
This specifies the prefix for the destination Amazon S3 bucket for the export job.
Type: String
Required: No

## See Also
<a name="API_BKS_S3ExportSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backupsearch-2018-05-10/S3ExportSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backupsearch-2018-05-10/S3ExportSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backupsearch-2018-05-10/S3ExportSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
