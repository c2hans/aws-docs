---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_Schema.html
---

# Schema
<a name="API_Schema"></a>

 A Schema specifies the expected data model of the table.

## Contents
<a name="API_Schema_Contents"></a>

 ** CompositePartitionKey **   <a name="timestream-Type-Schema-CompositePartitionKey"></a>
A non-empty list of partition keys defining the attributes used to partition the table data. The order of the list determines the partition hierarchy. The name and type of each partition key as well as the partition key order cannot be changed after the table is created. However, the enforcement level of each partition key can be changed.
Type: Array of [PartitionKey](API_PartitionKey.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_Schema_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-write-2018-11-01/Schema)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-write-2018-11-01/Schema)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-write-2018-11-01/Schema)
