---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Projection.html
---

# Projection
<a name="API_Projection"></a>

Represents attributes that are copied (projected) from the table into an index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.

## Contents
<a name="API_Projection_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** NonKeyAttributes **   <a name="DDB-Type-Projection-NonKeyAttributes"></a>
Represents the non-key attribute names which will be projected into the index.
For global and local secondary indexes, the total count of `NonKeyAttributes` summed across all of the secondary indexes, must not exceed 100. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total. This limit only applies when you specify the ProjectionType of `INCLUDE`. You still can specify the ProjectionType of `ALL` to project all attributes from the source table, even if the table has more than 100 attributes.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** ProjectionType **   <a name="DDB-Type-Projection-ProjectionType"></a>
The set of attributes that are projected into the index:
+  `KEYS_ONLY` - Only the index and primary keys are projected into the index.
+  `INCLUDE` - In addition to the attributes described in `KEYS_ONLY`, the secondary index will include other non-key attributes that you specify.
+  `ALL` - All of the table attributes are projected into the index.
When using the DynamoDB console, `ALL` is selected by default.
Type: String
Valid Values: `ALL | KEYS_ONLY | INCLUDE`
Required: No

## See Also
<a name="API_Projection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/Projection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/Projection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/Projection)
