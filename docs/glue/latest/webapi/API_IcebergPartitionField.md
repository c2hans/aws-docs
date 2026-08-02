---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_IcebergPartitionField.html
---

# IcebergPartitionField
<a name="API_IcebergPartitionField"></a>

Defines a single partition field within an Iceberg partition specification, including the source field, transformation function, partition name, and unique identifier.

## Contents
<a name="API_IcebergPartitionField_Contents"></a>

 ** Name **   <a name="Glue-Type-IcebergPartitionField-Name"></a>
The name of the partition field as it will appear in the partitioned table structure.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** SourceId **   <a name="Glue-Type-IcebergPartitionField-SourceId"></a>
The identifier of the source field from the table schema that this partition field is based on.
Type: Integer
Required: Yes

 ** Transform **   <a name="Glue-Type-IcebergPartitionField-Transform"></a>
The transformation function applied to the source field to create the partition, such as identity, bucket, truncate, year, month, day, or hour.
Type: String
Required: Yes

 ** FieldId **   <a name="Glue-Type-IcebergPartitionField-FieldId"></a>
The unique identifier assigned to this partition field within the Iceberg table's partition specification.
Type: Integer
Required: No

## See Also
<a name="API_IcebergPartitionField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/IcebergPartitionField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/IcebergPartitionField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/IcebergPartitionField)
