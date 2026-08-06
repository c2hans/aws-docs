---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ExecuteStatement.html
---

# ExecuteStatement
<a name="API_ExecuteStatement"></a>

This operation allows you to perform reads and singleton writes on data stored in DynamoDB, using PartiQL.

For PartiQL reads (`SELECT` statement), if the total number of processed items exceeds the maximum dataset size limit of 1 MB, the read stops and results are returned to the user as a `LastEvaluatedKey` value to continue the read in a subsequent operation. If the filter criteria in `WHERE` clause does not match any data, the read will return an empty result set.

A single `SELECT` statement response can return up to the maximum number of items (if using the Limit parameter) or a maximum of 1 MB of data (and then apply any filtering to the results using `WHERE` clause). If `LastEvaluatedKey` is present in the response, you need to paginate the result set. If `NextToken` is present, you need to paginate the result set and include `NextToken`.

## Request Syntax
<a name="API_ExecuteStatement_RequestSyntax"></a>

```
{
   "ConsistentRead": {{boolean}},
   "Limit": {{number}},
   "NextToken": "{{string}}",
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
   "ReturnConsumedCapacity": "{{string}}",
   "ReturnValuesOnConditionCheckFailure": "{{string}}",
   "Statement": "{{string}}"
}
```

## Request Parameters
<a name="API_ExecuteStatement_RequestParameters"></a>

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Statement](#API_ExecuteStatement_RequestSyntax) **   <a name="DDB-ExecuteStatement-request-Statement"></a>
The PartiQL statement representing the operation to run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: Yes

 ** [ConsistentRead](#API_ExecuteStatement_RequestSyntax) **   <a name="DDB-ExecuteStatement-request-ConsistentRead"></a>
The consistency of a read operation. If set to `true`, then a strongly consistent read is used; otherwise, an eventually consistent read is used.
Type: Boolean
Required: No

 ** [Limit](#API_ExecuteStatement_RequestSyntax) **   <a name="DDB-ExecuteStatement-request-Limit"></a>
The maximum number of items to evaluate (not necessarily the number of matching items). If DynamoDB processes the number of items up to the limit while processing the results, it stops the operation and returns the matching values up to that point, along with a key in `LastEvaluatedKey` to apply in a subsequent operation so you can pick up where you left off. Also, if the processed dataset size exceeds 1 MB before DynamoDB reaches this limit, it stops the operation and returns the matching values up to the limit, and a key in `LastEvaluatedKey` to apply in a subsequent operation to continue the operation.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextToken](#API_ExecuteStatement_RequestSyntax) **   <a name="DDB-ExecuteStatement-request-NextToken"></a>
Set this value to get remaining results, if `NextToken` was returned in the statement response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.
Required: No

 ** [Parameters](#API_ExecuteStatement_RequestSyntax) **   <a name="DDB-ExecuteStatement-request-Parameters"></a>
The parameters for the PartiQL statement, if any.
Type: Array of [AttributeValue](API_AttributeValue.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [ReturnConsumedCapacity](#API_ExecuteStatement_RequestSyntax) **   <a name="DDB-ExecuteStatement-request-ReturnConsumedCapacity"></a>
Determines the level of detail about either provisioned or on-demand throughput consumption that is returned in the response:
+  `INDEXES` - The response includes the aggregate `ConsumedCapacity` for the operation, together with `ConsumedCapacity` for each table and secondary index that was accessed.

  Note that some operations, such as `GetItem` and `BatchGetItem`, do not access any indexes at all. In these cases, specifying `INDEXES` will only return `ConsumedCapacity` information for table(s).
+  `TOTAL` - The response includes only the aggregate `ConsumedCapacity` for the operation.
+  `NONE` - No `ConsumedCapacity` details are included in the response.
Type: String
Valid Values: `INDEXES | TOTAL | NONE`
Required: No

 ** [ReturnValuesOnConditionCheckFailure](#API_ExecuteStatement_RequestSyntax) **   <a name="DDB-ExecuteStatement-request-ReturnValuesOnConditionCheckFailure"></a>
An optional parameter that returns the item attributes for an `ExecuteStatement` operation that failed a condition check.
There is no additional cost associated with requesting a return value aside from the small network and processing overhead of receiving a larger response. No read capacity units are consumed.
Type: String
Valid Values: `ALL_OLD | NONE`
Required: No

## Response Syntax
<a name="API_ExecuteStatement_ResponseSyntax"></a>

```
{
   "ConsumedCapacity": {
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
   },
   "Items": [
      {
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
   ],
   "LastEvaluatedKey": {
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
   },
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ExecuteStatement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConsumedCapacity](#API_ExecuteStatement_ResponseSyntax) **   <a name="DDB-ExecuteStatement-response-ConsumedCapacity"></a>
The capacity units consumed by an operation. The data returned includes the total provisioned throughput consumed, along with statistics for the table and any indexes involved in the operation. `ConsumedCapacity` is only returned if the request asked for it. For more information, see [Provisioned capacity mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/provisioned-capacity-mode.html) in the *Amazon DynamoDB Developer Guide*.
Type: [ConsumedCapacity](API_ConsumedCapacity.md) object

 ** [Items](#API_ExecuteStatement_ResponseSyntax) **   <a name="DDB-ExecuteStatement-response-Items"></a>
If a read operation was used, this property will contain the result of the read operation; a map of attribute names and their values. For the write operations this value will be empty.
Type: Array of string to [AttributeValue](API_AttributeValue.md) object maps
Key Length Constraints: Maximum length of 65535.

 ** [LastEvaluatedKey](#API_ExecuteStatement_ResponseSyntax) **   <a name="DDB-ExecuteStatement-response-LastEvaluatedKey"></a>
The primary key of the item where the operation stopped, inclusive of the previous result set. Use this value to start a new operation, excluding this value in the new request. If `LastEvaluatedKey` is empty, then the "last page" of results has been processed and there is no more data to be retrieved. If `LastEvaluatedKey` is not empty, it does not necessarily mean that there is more data in the result set. The only way to know when you have reached the end of the result set is when `LastEvaluatedKey` is empty.
Type: String to [AttributeValue](API_AttributeValue.md) object map
Key Length Constraints: Maximum length of 65535.

 ** [NextToken](#API_ExecuteStatement_ResponseSyntax) **   <a name="DDB-ExecuteStatement-response-NextToken"></a>
If the response of a read request exceeds the response payload limit DynamoDB will set this value in the response. If set, you can use that this value in the subsequent request to get the remaining results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.

## Errors
<a name="API_ExecuteStatement_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConditionalCheckFailedException **
A condition specified in the operation failed to be evaluated.
 ** Item **
Item which caused the `ConditionalCheckFailedException`.
 ** message **
The conditional request failed.
HTTP Status Code: 400

 ** DuplicateItemException **
 There was an attempt to insert an item with the same primary key as an item that already exists in the DynamoDB table.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
 ** message **
The server encountered an internal error trying to fulfill the request.
HTTP Status Code: 500

 ** ItemCollectionSizeLimitExceededException **
An item collection is too large. This exception is only returned for tables that have one or more local secondary indexes.
 ** message **
The total size of an item collection has exceeded the maximum limit of 10 gigabytes.
HTTP Status Code: 400

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

 ** TransactionConflictException **
Operation was rejected because there is an ongoing transaction for the item.
HTTP Status Code: 400

## See Also
<a name="API_ExecuteStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dynamodb-2012-08-10/ExecuteStatement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dynamodb-2012-08-10/ExecuteStatement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ExecuteStatement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dynamodb-2012-08-10/ExecuteStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ExecuteStatement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dynamodb-2012-08-10/ExecuteStatement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dynamodb-2012-08-10/ExecuteStatement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dynamodb-2012-08-10/ExecuteStatement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/ExecuteStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ExecuteStatement)
