---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ExecuteTransaction.html
---

# ExecuteTransaction
<a name="API_ExecuteTransaction"></a>

This operation allows you to perform transactional reads or writes on data stored in DynamoDB, using PartiQL.

**Note**
The entire transaction must consist of either read statements or write statements, you cannot mix both in one transaction. The EXISTS function is an exception and can be used to check the condition of specific attributes of the item in a similar manner to `ConditionCheck` in the [TransactWriteItems](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/transaction-apis.html#transaction-apis-txwriteitems) API.

## Request Syntax
<a name="API_ExecuteTransaction_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "ReturnConsumedCapacity": "{{string}}",
   "TransactStatements": [
      {
         "Parameters": [
            {
               "B": {{blob}},
               "BOOL": {{boolean}},
               "BS": [ {{blob}} ],
               "L": [
                  "AttributeValue"
               ],
               "M": {
                  "{{string}}" : "AttributeValue"
               },
               "N": "{{string}}",
               "NS": [ "{{string}}" ],
               "NULL": {{boolean}},
               "S": "{{string}}",
               "SS": [ "{{string}}" ]
            }
         ],
         "ReturnValuesOnConditionCheckFailure": "{{string}}",
         "Statement": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_ExecuteTransaction_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [TransactStatements](#API_ExecuteTransaction_RequestSyntax) **   <a name="DDB-ExecuteTransaction-request-TransactStatements"></a>
The list of PartiQL statements representing the transaction to run.
Type: Array of [ParameterizedStatement](API_ParameterizedStatement.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

 ** [ClientRequestToken](#API_ExecuteTransaction_RequestSyntax) **   <a name="DDB-ExecuteTransaction-request-ClientRequestToken"></a>
Set this value to get remaining results, if `NextToken` was returned in the statement response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: No

 ** [ReturnConsumedCapacity](#API_ExecuteTransaction_RequestSyntax) **   <a name="DDB-ExecuteTransaction-request-ReturnConsumedCapacity"></a>
Determines the level of detail about either provisioned or on-demand throughput consumption that is returned in the response. For more information, see [TransactGetItems](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactGetItems.html) and [TransactWriteItems](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactWriteItems.html).
Type: String
Valid Values: `INDEXES | TOTAL | NONE`
Required: No

## Response Syntax
<a name="API_ExecuteTransaction_ResponseSyntax"></a>

```
{
   "ConsumedCapacity": [
      {
         "CapacityUnits": number,
         "GlobalSecondaryIndexes": {
            "string" : {
               "CapacityUnits": number,
               "ReadCapacityUnits": number,
               "WriteCapacityUnits": number
            }
         },
         "LocalSecondaryIndexes": {
            "string" : {
               "CapacityUnits": number,
               "ReadCapacityUnits": number,
               "WriteCapacityUnits": number
            }
         },
         "ReadCapacityUnits": number,
         "Table": {
            "CapacityUnits": number,
            "ReadCapacityUnits": number,
            "WriteCapacityUnits": number
         },
         "TableName": "string",
         "VectorIndexes": {
            "string" : {
               "VectorSearchRequestBytes": number,
               "VectorWriteRequestBytes": number
            }
         },
         "WriteCapacityUnits": number
      }
   ],
   "Responses": [
      {
         "Item": {
            "string" : {
               "B": blob,
               "BOOL": boolean,
               "BS": [ blob ],
               "L": [
                  "AttributeValue"
               ],
               "M": {
                  "string" : "AttributeValue"
               },
               "N": "string",
               "NS": [ "string" ],
               "NULL": boolean,
               "S": "string",
               "SS": [ "string" ]
            }
         }
      }
   ]
}
```

## Response Elements
<a name="API_ExecuteTransaction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConsumedCapacity](#API_ExecuteTransaction_ResponseSyntax) **   <a name="DDB-ExecuteTransaction-response-ConsumedCapacity"></a>
The capacity units consumed by the entire operation. The values of the list are ordered according to the ordering of the statements.
Type: Array of [ConsumedCapacity](API_ConsumedCapacity.md) objects

 ** [Responses](#API_ExecuteTransaction_ResponseSyntax) **   <a name="DDB-ExecuteTransaction-response-Responses"></a>
The response to a PartiQL transaction.
Type: Array of [ItemResponse](API_ItemResponse.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

## Errors
<a name="API_ExecuteTransaction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** IdempotentParameterMismatchException **
DynamoDB rejected the request because you retried a request with a different payload but with an idempotent token that was already used.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
 ** message **
The server encountered an internal error trying to fulfill the request.
HTTP Status Code: 500

 ** ProvisionedThroughputExceededException **
The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the [ThrottlingReason](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html) field in the returned exception. The AWS SDKs for DynamoDB automatically retry requests that receive this exception. Your request is eventually successful, unless your retry queue is too large to finish. Reduce the frequency of requests and use exponential backoff. For more information, go to [Error Retries and Exponential Backoff](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html#Programming.Errors.RetryAndBackoff) in the *Amazon DynamoDB Developer Guide*.
 ** message **
You exceeded your maximum allowed provisioned throughput.
 ** ThrottlingReasons **
A list of [ThrottlingReason](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html) that provide detailed diagnostic information about why the request was throttled.
HTTP Status Code: 400

 ** RequestLimitExceeded **
Throughput exceeds the current throughput quota for your account. For detailed information about why the request was throttled and the ARN of the impacted resource, find the [ThrottlingReason](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html) field in the returned exception. Contact [Support](https://aws.amazon.com/support) to request a quota increase.
 ** ThrottlingReasons **
A list of [ThrottlingReason](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html) that provide detailed diagnostic information about why the request was throttled.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be `ACTIVE`.
 ** message **
The resource which is being requested does not exist.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the [ThrottlingReason](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html) field in the returned exception.
 ** throttlingReasons **
A list of [ThrottlingReason](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html) that provide detailed diagnostic information about why the request was throttled.
HTTP Status Code: 400

 ** TransactionCanceledException **
The entire transaction request was canceled.
DynamoDB cancels a `TransactWriteItems` request under the following circumstances:
+ A condition in one of the condition expressions is not met.
+ A table in the `TransactWriteItems` request is in a different account or region.
+ More than one action in the `TransactWriteItems` operation targets the same item.
+ There is insufficient provisioned capacity for the transaction to be completed.
+ An item size becomes too large (larger than 400 KB), or a local secondary index (LSI) becomes too large, or a similar validation error occurs because of changes made by the transaction.
+ There is a user error, such as an invalid data format.
+  There is an ongoing `TransactWriteItems` operation that conflicts with a concurrent `TransactWriteItems` request. In this case the `TransactWriteItems` operation fails with a `TransactionCanceledException`.
DynamoDB cancels a `TransactGetItems` request under the following circumstances:
+ There is an ongoing `TransactGetItems` operation that conflicts with a concurrent `PutItem`, `UpdateItem`, `DeleteItem` or `TransactWriteItems` request. In this case the `TransactGetItems` operation fails with a `TransactionCanceledException`.
+ A table in the `TransactGetItems` request is in a different account or region.
+ There is insufficient provisioned capacity for the transaction to be completed.
+ There is a user error, such as an invalid data format.
DynamoDB lists the cancellation reasons on the `CancellationReasons` property. Transaction cancellation reasons are ordered in the order of requested items, if an item has no error it will have `None` code and `Null` message. The `None` code is returned as the literal string `"None"`, not a null or absent value; the message field is omitted entirely for an item that has no error. This is important to note when using an SDK that surfaces the code as an optional or nullable type.
Cancellation reason codes and possible error messages:
+ No Errors:
  + Code: `None`
  + Message: `null`
+ Conditional Check Failed:
  + Code: `ConditionalCheckFailed`
  + Message: The conditional request failed.
+ Item Collection Size Limit Exceeded:
  + Code: `ItemCollectionSizeLimitExceeded`
  + Message: Collection size exceeded.
+ Transaction Conflict:
  + Code: `TransactionConflict`
  + Message: Transaction is ongoing for the item.
+ Provisioned Throughput Exceeded:
  + Code: `ProvisionedThroughputExceeded`
  + Messages:
    + The level of configured provisioned throughput for the table was exceeded. Consider increasing your provisioning level with the UpdateTable API.
**Note**
This Message is received when provisioned throughput is exceeded is on a provisioned DynamoDB table.
    + The level of configured provisioned throughput for one or more global secondary indexes of the table was exceeded. Consider increasing your provisioning level for the under-provisioned global secondary indexes with the UpdateTable API.
**Note**
This message is returned when provisioned throughput is exceeded is on a provisioned GSI.
+ Throttling Error:
  + Code: `ThrottlingError`
  + Messages:
    + Throughput exceeds the current capacity of your table or index. DynamoDB is automatically scaling your table or index so please try again shortly. If exceptions persist, check if you have a hot key: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html.
**Note**
This message is returned when writes get throttled on an On-Demand table as DynamoDB is automatically scaling the table.
    + Throughput exceeds the current capacity for one or more global secondary indexes. DynamoDB is automatically scaling your index so please try again shortly.
**Note**
This message is returned when writes get throttled on an On-Demand GSI as DynamoDB is automatically scaling the GSI.
+ Validation Error:
  + Code: `ValidationError`
  + Messages:
    + One or more parameter values were invalid.
    + The update expression attempted to update the secondary index key beyond allowed size limits.
    + The update expression attempted to update the secondary index key to unsupported type.
    + An operand in the update expression has an incorrect data type.
    + Item size to update has exceeded the maximum allowed size.
    + Number overflow. Attempting to store a number with magnitude larger than supported range.
    + Type mismatch for attribute to update.
    + Nesting Levels have exceeded supported limits.
    + The document path provided in the update expression is invalid for update.
    + The provided expression refers to an attribute that does not exist in the item.
 ** CancellationReasons **
A list of cancellation reasons.
HTTP Status Code: 400

 ** TransactionInProgressException **
The transaction with the given request token is already in progress.
 Recommended Settings
 This is a general recommendation for handling the `TransactionInProgressException`. These settings help ensure that the client retries will trigger completion of the ongoing `TransactWriteItems` request.
+  Set `clientExecutionTimeout` to a value that allows at least one retry to be processed after 5 seconds have elapsed since the first attempt for the `TransactWriteItems` operation.
+  Set `socketTimeout` to a value a little lower than the `requestTimeout` setting.
+  `requestTimeout` should be set based on the time taken for the individual retries of a single HTTP request for your use case, but setting it to 1 second or higher should work well to reduce chances of retries and `TransactionInProgressException` errors.
+  Use exponential backoff when retrying and tune backoff if needed.
 Assuming [default retry policy](https://github.com/aws/aws-sdk-java/blob/fd409dee8ae23fb8953e0bb4dbde65536a7e0514/aws-java-sdk-core/src/main/java/com/amazonaws/retry/PredefinedRetryPolicies.java#L97), example timeout settings based on the guidelines above are as follows:
Example timeline:
+ 0-1000 first attempt
+ 1000-1500 first sleep/delay (default retry policy uses 500 ms as base delay for 4xx errors)
+ 1500-2500 second attempt
+ 2500-3500 second sleep/delay (500 \* 2, exponential backoff)
+ 3500-4500 third attempt
+ 4500-6500 third sleep/delay (500 \* 2^2)
+ 6500-7500 fourth attempt (this can trigger inline recovery since 5 seconds have elapsed since the first attempt reached TC)
HTTP Status Code: 400

## See Also
<a name="API_ExecuteTransaction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/ExecuteTransaction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/ExecuteTransaction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ExecuteTransaction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/ExecuteTransaction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ExecuteTransaction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/ExecuteTransaction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/ExecuteTransaction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/ExecuteTransaction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/ExecuteTransaction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ExecuteTransaction)
