---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BKS_ExportSpecification.html
---

# ExportSpecification
<a name="API_BKS_ExportSpecification"></a>

This contains the export specification object.

## Contents
<a name="API_BKS_ExportSpecification_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** s3ExportSpecification **   <a name="Backup-Type-BKS_ExportSpecification-s3ExportSpecification"></a>
This specifies the destination Amazon S3 bucket for the export job. And, if included, it also specifies the destination prefix.
Type: [S3ExportSpecification](API_BKS_S3ExportSpecification.md) object
Required: No

## See Also
<a name="API_BKS_ExportSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backupsearch-2018-05-10/ExportSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backupsearch-2018-05-10/ExportSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backupsearch-2018-05-10/ExportSpecification)
