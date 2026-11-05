---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CancelBulkOperation.html
---

# CancelBulkOperation
<a name="API_CancelBulkOperation"></a>

Cancels an in-progress bulk operation asynchronously. Cancellation doesn't remove items that the operation has already written. Use `DescribeBulkOperation` to monitor the operation until it reaches a terminal status.

## Request Syntax
<a name="API_CancelBulkOperation_RequestSyntax"></a>

```
{
   "BulkOperationArn": "{{string}}"
}
```

## Request Parameters
<a name="API_CancelBulkOperation_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [BulkOperationArn](#API_CancelBulkOperation_RequestSyntax) **   <a name="DDB-CancelBulkOperation-request-BulkOperationArn"></a>
The Amazon Resource Name (ARN) of the bulk operation to cancel.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.
Required: Yes

## Response Syntax
<a name="API_CancelBulkOperation_ResponseSyntax"></a>

```
{
   "BulkOperationArn": "string",
   "BulkOperationStatus": "string"
}
```

## Response Elements
<a name="API_CancelBulkOperation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BulkOperationArn](#API_CancelBulkOperation_ResponseSyntax) **   <a name="DDB-CancelBulkOperation-response-BulkOperationArn"></a>
The Amazon Resource Name (ARN) of the bulk operation for which DynamoDB accepted the cancellation request.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.

 ** [BulkOperationStatus](#API_CancelBulkOperation_ResponseSyntax) **   <a name="DDB-CancelBulkOperation-response-BulkOperationStatus"></a>
The status returned after DynamoDB accepts the cancellation request. This value is `CANCELLING`. Use `DescribeBulkOperation` to determine when the operation reaches `CANCELLED`.
Type: String
Valid Values: `IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | CANCELLING | CANCELLED | FAILED`

## Errors
<a name="API_CancelBulkOperation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be `ACTIVE`.
 ** message **
The resource which is being requested does not exist.
HTTP Status Code: 400

## See Also
<a name="API_CancelBulkOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/CancelBulkOperation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/CancelBulkOperation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/CancelBulkOperation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/CancelBulkOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/CancelBulkOperation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/CancelBulkOperation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/CancelBulkOperation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/CancelBulkOperation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/CancelBulkOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/CancelBulkOperation)
