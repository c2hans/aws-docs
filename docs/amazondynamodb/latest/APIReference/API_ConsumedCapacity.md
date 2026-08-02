---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ConsumedCapacity.html
---

# ConsumedCapacity
<a name="API_ConsumedCapacity"></a>

The capacity units consumed by an operation. The data returned includes the total provisioned throughput consumed, along with statistics for the table and any indexes involved in the operation. `ConsumedCapacity` is only returned if the request asked for it. For more information, see [Provisioned capacity mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/provisioned-capacity-mode.html) in the *Amazon DynamoDB Developer Guide*.

## Contents
<a name="API_ConsumedCapacity_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CapacityUnits **   <a name="DDB-Type-ConsumedCapacity-CapacityUnits"></a>
The total number of capacity units consumed by the operation.
Type: Double
Required: No

 ** GlobalSecondaryIndexes **   <a name="DDB-Type-ConsumedCapacity-GlobalSecondaryIndexes"></a>
The amount of throughput consumed on each global index affected by the operation.
Type: String to [Capacity](API_Capacity.md) object map
Key Length Constraints: Minimum length of 3. Maximum length of 255.
Key Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** LocalSecondaryIndexes **   <a name="DDB-Type-ConsumedCapacity-LocalSecondaryIndexes"></a>
The amount of throughput consumed on each local index affected by the operation.
Type: String to [Capacity](API_Capacity.md) object map
Key Length Constraints: Minimum length of 3. Maximum length of 255.
Key Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** ReadCapacityUnits **   <a name="DDB-Type-ConsumedCapacity-ReadCapacityUnits"></a>
The total number of read capacity units consumed by the operation.
Type: Double
Required: No

 ** Table **   <a name="DDB-Type-ConsumedCapacity-Table"></a>
The amount of throughput consumed on the table affected by the operation.
Type: [Capacity](API_Capacity.md) object
Required: No

 ** TableName **   <a name="DDB-Type-ConsumedCapacity-TableName"></a>
The name of the table that was affected by the operation. If you had specified the Amazon Resource Name (ARN) of a table in the input, you'll see the table ARN in the response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** WriteCapacityUnits **   <a name="DDB-Type-ConsumedCapacity-WriteCapacityUnits"></a>
The total number of write capacity units consumed by the operation.
Type: Double
Required: No

## See Also
<a name="API_ConsumedCapacity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ConsumedCapacity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ConsumedCapacity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ConsumedCapacity)
