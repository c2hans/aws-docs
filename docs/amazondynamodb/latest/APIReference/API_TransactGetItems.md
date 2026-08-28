---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactGetItems.html
---

# TransactGetItems
<a name="API_TransactGetItems"></a>

 `TransactGetItems` is a synchronous operation that atomically retrieves multiple items from one or more tables (but not from indexes) in a single account and Region. A `TransactGetItems` call can contain up to 100 `TransactGetItem` objects, each of which contains a `Get` structure that specifies an item to retrieve from a table in the account and Region. A call to `TransactGetItems` cannot retrieve items from tables in more than one AWS account or Region. The aggregate size of the items in the transaction cannot exceed 4 MB.

DynamoDB rejects the entire `TransactGetItems` request if any of the following is true:
+ A conflicting operation is in the process of updating an item to be read.
+ There is insufficient provisioned capacity for the transaction to be completed.
+ There is a user error, such as an invalid data format.
+ The aggregate size of the items in the transaction exceeded 4 MB.

## Request Syntax
<a name="API_TransactGetItems_RequestSyntax"></a>

```
{
   "ReturnConsumedCapacity": "{{string}}",
   "TransactItems": [
      {
         "Get": {
            "ExpressionAttributeNames": {
               "{{string}}" : "{{string}}"
            },
            "Key": {
               "{{string}}" : {
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
            },
            "ProjectionExpression": "{{string}}",
            "TableName": "{{string}}"
         }
      }
   ]
}
```

## Request Parameters
<a name="API_TransactGetItems_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [TransactItems](#API_TransactGetItems_RequestSyntax) **   <a name="DDB-TransactGetItems-request-TransactItems"></a>
An ordered array of up to 100 `TransactGetItem` objects, each of which contains a `Get` structure.
Type: Array of [TransactGetItem](API_TransactGetItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

 ** [ReturnConsumedCapacity](#API_TransactGetItems_RequestSyntax) **   <a name="DDB-TransactGetItems-request-ReturnConsumedCapacity"></a>
A value of `TOTAL` causes consumed capacity information to be returned, and a value of `NONE` prevents that information from being returned. No other value is valid.
Type: String
Valid Values: `INDEXES | TOTAL | NONE`
Required: No

## Response Syntax
<a name="API_TransactGetItems_ResponseSyntax"></a>

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
<a name="API_TransactGetItems_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConsumedCapacity](#API_TransactGetItems_ResponseSyntax) **   <a name="DDB-TransactGetItems-response-ConsumedCapacity"></a>
If the *ReturnConsumedCapacity* value was `TOTAL`, this is an array of `ConsumedCapacity` objects, one for each table addressed by `TransactGetItem` objects in the *TransactItems* parameter. These `ConsumedCapacity` objects report the read-capacity units consumed by the `TransactGetItems` call in that table.
Type: Array of [ConsumedCapacity](API_ConsumedCapacity.md) objects

 ** [Responses](#API_TransactGetItems_ResponseSyntax) **   <a name="DDB-TransactGetItems-response-Responses"></a>
An ordered array of up to 100 `ItemResponse` objects, each of which corresponds to the `TransactGetItem` object in the same position in the *TransactItems* array. Each `ItemResponse` object contains a Map of the name-value pairs that are the projected attributes of the requested item.
If a requested item could not be retrieved, the corresponding `ItemResponse` object is Null, or if the requested item has no projected attributes, the corresponding `ItemResponse` object is an empty Map.
Type: Array of [ItemResponse](API_ItemResponse.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

## Errors
<a name="API_TransactGetItems_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

## See Also
<a name="API_TransactGetItems_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/TransactGetItems)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/TransactGetItems)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/TransactGetItems)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/TransactGetItems)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/TransactGetItems)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/TransactGetItems)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/TransactGetItems)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/TransactGetItems)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/TransactGetItems)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/TransactGetItems)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
