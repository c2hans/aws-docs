---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_IcebergSortField.html
---

# IcebergSortField
<a name="API_IcebergSortField"></a>

Defines a single field within an Iceberg sort order specification, including the source field, transformation, sort direction, and null value ordering.

## Contents
<a name="API_IcebergSortField_Contents"></a>

 ** Direction **   <a name="Glue-Type-IcebergSortField-Direction"></a>
The sort direction for this field, either ascending or descending.
Type: String
Valid Values: `asc | desc`
Required: Yes

 ** NullOrder **   <a name="Glue-Type-IcebergSortField-NullOrder"></a>
The ordering behavior for null values in this field, specifying whether nulls should appear first or last in the sort order.
Type: String
Valid Values: `nulls-first | nulls-last`
Required: Yes

 ** SourceId **   <a name="Glue-Type-IcebergSortField-SourceId"></a>
The identifier of the source field from the table schema that this sort field is based on.
Type: Integer
Required: Yes

 ** Transform **   <a name="Glue-Type-IcebergSortField-Transform"></a>
The transformation function applied to the source field before sorting, such as identity, bucket, or truncate.
Type: String
Required: Yes

## See Also
<a name="API_IcebergSortField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/IcebergSortField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/IcebergSortField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/IcebergSortField)
