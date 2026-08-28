---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableBucketMaintenanceSettings.html
---

# TableBucketMaintenanceSettings
<a name="API_s3Buckets_TableBucketMaintenanceSettings"></a>

Contains details about the maintenance settings for the table bucket.

## Contents
<a name="API_s3Buckets_TableBucketMaintenanceSettings_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** icebergUnreferencedFileRemoval **   <a name="AmazonS3-Type-s3Buckets_TableBucketMaintenanceSettings-icebergUnreferencedFileRemoval"></a>
The unreferenced file removal settings for the table bucket.
Type: [IcebergUnreferencedFileRemovalSettings](API_s3Buckets_IcebergUnreferencedFileRemovalSettings.md) object
Required: No

## See Also
<a name="API_s3Buckets_TableBucketMaintenanceSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/TableBucketMaintenanceSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/TableBucketMaintenanceSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/TableBucketMaintenanceSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
