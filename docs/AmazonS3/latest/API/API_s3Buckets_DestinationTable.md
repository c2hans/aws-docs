---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_DestinationTable.html
---

# DestinationTable
<a name="API_s3Buckets_DestinationTable"></a>

The table that a migration creates in a table bucket and migrates the source into.

## Contents
<a name="API_s3Buckets_DestinationTable_Contents"></a>

 ** name **   <a name="AmazonS3-Type-s3Buckets_DestinationTable-name"></a>
The name of the table to create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[0-9a-z_]*`
Required: Yes

 ** namespace **   <a name="AmazonS3-Type-s3Buckets_DestinationTable-namespace"></a>
The namespace to create the table in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[0-9a-z_]*`
Required: Yes

 ** tableBucketARN **   <a name="AmazonS3-Type-s3Buckets_DestinationTable-tableBucketARN"></a>
The Amazon Resource Name (ARN) of the table bucket to create the table in.
Type: String
Pattern: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`
Required: Yes

 ** encryptionConfiguration **   <a name="AmazonS3-Type-s3Buckets_DestinationTable-encryptionConfiguration"></a>
The encryption configuration for the table. If you don't specify one, the table uses the default encryption configuration of its table bucket. If you specify an encryption configuration, the migration role must have the `s3tables:PutTableEncryption` permission. If you choose SSE-KMS, the migration role must have the `kms:DescribeKey`, `kms:GenerateDataKey` and `kms:Decrypt` permissions on the KMS key, and the S3 Tables maintenance principal must have access to it. For more information, see [Permissions requirements for S3 Tables SSE-KMS encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html).
Type: [EncryptionConfiguration](API_s3Buckets_EncryptionConfiguration.md) object
Required: No

 ** icebergSortOrder **   <a name="AmazonS3-Type-s3Buckets_DestinationTable-icebergSortOrder"></a>
The sort order of the rows within each data file that the migration writes. A sort order can have up to five fields, each naming a column of the schema that you specify by its field ID, so to use a sort order you must specify a schema. `StartTableMigration` rejects a field that names no column of the schema, or whose transform doesn't fit the column's type.
Type: [IcebergSortOrder](API_s3Buckets_IcebergSortOrder.md) object
Required: No

 ** properties **   <a name="AmazonS3-Type-s3Buckets_DestinationTable-properties"></a>
The properties of the destination table, such as its Iceberg format version and the format of its data files.
Type: [MigrationTableProperties](API_s3Buckets_MigrationTableProperties.md) object
Required: No

 ** schema **   <a name="AmazonS3-Type-s3Buckets_DestinationTable-schema"></a>
The schema of the table to create. If you don't specify a schema, the migration infers it from the source table, with every column optional. A schema that you specify must include every partition column of the source table. It can leave out other columns only if `unmatchedSourceFieldsPolicy` is `drop`. A struct column must have the same fields as the source column. Column default values aren't supported. If you mark a column as required, every source object must have a value for it: an object with a null value in a required column fails to migrate. The destination table is partitioned in the same way as the source table. To specify fields in `icebergSortOrder`, you must specify a schema.
Type: [IcebergSchemaV2](API_s3Buckets_IcebergSchemaV2.md) object
Required: No

 ** storageClassConfiguration **   <a name="AmazonS3-Type-s3Buckets_DestinationTable-storageClassConfiguration"></a>
The storage class configuration for the table. If you don't specify one, the table inherits the storage class configuration of its table bucket. If you specify a storage class configuration, the migration role must have the `s3tables:PutTableStorageClass` permission.
Type: [StorageClassConfiguration](API_s3Buckets_StorageClassConfiguration.md) object
Required: No

 ** tags **   <a name="AmazonS3-Type-s3Buckets_DestinationTable-tags"></a>
The tags to add to the table. A tag is a key-value pair that you apply to your resources. For more information, see [Tagging for cost allocation or attribute-based access control (ABAC)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html). If you specify tags, the migration role must have the `s3tables:TagResource` permission.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_s3Buckets_DestinationTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/DestinationTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/DestinationTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/DestinationTable)
