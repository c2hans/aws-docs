---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactWriteItem.html
---

# TransactWriteItem
<a name="API_TransactWriteItem"></a>

A list of requests that can perform update, put, delete, or check operations on multiple items in one or more tables atomically.

## Contents
<a name="API_TransactWriteItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ConditionCheck **   <a name="DDB-Type-TransactWriteItem-ConditionCheck"></a>
A request to perform a check item operation.
Type: [ConditionCheck](API_ConditionCheck.md) object
Required: No

 ** Delete **   <a name="DDB-Type-TransactWriteItem-Delete"></a>
A request to perform a `DeleteItem` operation.
Type: [Delete](API_Delete.md) object
Required: No

 ** Put **   <a name="DDB-Type-TransactWriteItem-Put"></a>
A request to perform a `PutItem` operation.
Type: [Put](API_Put.md) object
Required: No

 ** Update **   <a name="DDB-Type-TransactWriteItem-Update"></a>
A request to perform an `UpdateItem` operation.
Type: [Update](API_Update.md) object
Required: No

## See Also
<a name="API_TransactWriteItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/TransactWriteItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/TransactWriteItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/TransactWriteItem)
