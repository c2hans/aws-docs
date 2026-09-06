---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_IcebergTableUpdate.html
---

# IcebergTableUpdate
<a name="API_IcebergTableUpdate"></a>

Defines a complete set of updates to be applied to an Iceberg table, including schema changes, partitioning modifications, sort order adjustments, location updates, and property changes.

## Contents
<a name="API_IcebergTableUpdate_Contents"></a>

 ** Location **   <a name="Glue-Type-IcebergTableUpdate-Location"></a>
The updated S3 location where the Iceberg table data will be stored.
Type: String
Length Constraints: Maximum length of 2056.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** Schema **   <a name="Glue-Type-IcebergTableUpdate-Schema"></a>
The updated schema definition for the Iceberg table, specifying any changes to field structure, data types, or schema metadata.
Type: [IcebergSchema](API_IcebergSchema.md) object
Required: Yes

 ** Action **   <a name="Glue-Type-IcebergTableUpdate-Action"></a>
The type of update action to be performed on the Iceberg table. Defines the specific operation such as adding schema, setting current schema, adding partition spec, or managing encryption keys.
Type: String
Valid Values: `add-schema | set-current-schema | add-spec | set-default-spec | add-sort-order | set-default-sort-order | set-location | set-properties | remove-properties | add-encryption-key | remove-encryption-key`
Required: No

 ** EncryptionKey **   <a name="Glue-Type-IcebergTableUpdate-EncryptionKey"></a>
Encryption key information associated with an Iceberg table update operation. Used when adding or removing encryption keys from the table metadata during table evolution.
Type: [IcebergEncryptedKey](API_IcebergEncryptedKey.md) object
Required: No

 ** KeyId **   <a name="Glue-Type-IcebergTableUpdate-KeyId"></a>
Identifier of the encryption key involved in an Iceberg table update operation. References the specific key being added to or removed from the table's encryption configuration.
Type: String
Length Constraints: Maximum length of 2056.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** PartitionSpec **   <a name="Glue-Type-IcebergTableUpdate-PartitionSpec"></a>
The updated partitioning specification that defines how the table data should be reorganized and partitioned.
Type: [IcebergPartitionSpec](API_IcebergPartitionSpec.md) object
Required: No

 ** Properties **   <a name="Glue-Type-IcebergTableUpdate-Properties"></a>
Updated key-value pairs of table properties and configuration settings for the Iceberg table.
Type: String to string map
Required: No

 ** SortOrder **   <a name="Glue-Type-IcebergTableUpdate-SortOrder"></a>
The updated sort order specification that defines how data should be ordered within partitions for optimal query performance.
Type: [IcebergSortOrder](API_IcebergSortOrder.md) object
Required: No

## See Also
<a name="API_IcebergTableUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/IcebergTableUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/IcebergTableUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/IcebergTableUpdate)
