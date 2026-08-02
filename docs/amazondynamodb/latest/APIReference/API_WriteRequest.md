---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_WriteRequest.html
---

# WriteRequest
<a name="API_WriteRequest"></a>

Represents an operation to perform - either `DeleteItem` or `PutItem`. You can only request one of these operations, not both, in a single `WriteRequest`. If you do need to perform both of these operations, you need to provide two separate `WriteRequest` objects.

## Contents
<a name="API_WriteRequest_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DeleteRequest **   <a name="DDB-Type-WriteRequest-DeleteRequest"></a>
A request to perform a `DeleteItem` operation.
Type: [DeleteRequest](API_DeleteRequest.md) object
Required: No

 ** PutRequest **   <a name="DDB-Type-WriteRequest-PutRequest"></a>
A request to perform a `PutItem` operation.
Type: [PutRequest](API_PutRequest.md) object
Required: No

## See Also
<a name="API_WriteRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/WriteRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/WriteRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/WriteRequest)
