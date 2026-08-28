---
source_url: https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_GetRecords.html
---

# GetRecords
<a name="API_GetRecords"></a>

Retrieves data records from a specified shard in an Amazon Keyspaces data stream. This operation returns a collection of data records from the shard, including the primary key columns and information about modifications made to the captured table data. Each record represents a single data modification in the Amazon Keyspaces table and includes metadata about when the change occurred.

## Request Syntax
<a name="API_GetRecords_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "shardIterator": "{{string}}"
}
```

## Request Parameters
<a name="API_GetRecords_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_GetRecords_RequestSyntax) **   <a name="keyspaces-GetRecords-request-maxResults"></a>
 The maximum number of records to return in a single `GetRecords` request. The default value is 100. You can specify a limit between 1 and 1000, but the actual number returned might be less than the specified maximum if the size of the data for the returned records exceeds the internal size limit.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [shardIterator](#API_GetRecords_RequestSyntax) **   <a name="keyspaces-GetRecords-request-shardIterator"></a>
 The unique identifier of the shard iterator. A shard iterator specifies the position in the shard from which you want to start reading data records sequentially. You obtain this value by calling the `GetShardIterator ` operation. Each shard iterator is valid for 15 minutes after creation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

## Response Syntax
<a name="API_GetRecords_ResponseSyntax"></a>

```
{
   "changeRecords": [
      {
         "clusteringKeys": {
            "string" : { ... }
         },
         "createdAt": number,
         "eventVersion": "string",
         "newImage": {
            "rowMetadata": {
               "expirationTime": "string",
               "writeTime": "string"
            },
            "staticCells": {
               "string" : {
                  "metadata": {
                     "expirationTime": "string",
                     "writeTime": "string"
                  },
                  "value": { ... }
               }
            },
            "valueCells": {
               "string" : {
                  "metadata": {
                     "expirationTime": "string",
                     "writeTime": "string"
                  },
                  "value": { ... }
               }
            }
         },
         "oldImage": {
            "rowMetadata": {
               "expirationTime": "string",
               "writeTime": "string"
            },
            "staticCells": {
               "string" : {
                  "metadata": {
                     "expirationTime": "string",
                     "writeTime": "string"
                  },
                  "value": { ... }
               }
            },
            "valueCells": {
               "string" : {
                  "metadata": {
                     "expirationTime": "string",
                     "writeTime": "string"
                  },
                  "value": { ... }
               }
            }
         },
         "origin": "string",
         "partitionKeys": {
            "string" : { ... }
         },
         "sequenceNumber": "string"
      }
   ],
   "iteratorDescription": {
      "iteratorPosition": "string"
   },
   "nextShardIterator": "string"
}
```

## Response Elements
<a name="API_GetRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [changeRecords](#API_GetRecords_ResponseSyntax) **   <a name="keyspaces-GetRecords-response-changeRecords"></a>
 An array of change data records retrieved from the specified shard. Each record represents a single data modification (insert, update, or delete) to a row in the Amazon Keyspaces table. Records include the primary key columns and information about what data was modified.
Type: Array of [Record](API_Record.md) objects

 ** [iteratorDescription](#API_GetRecords_ResponseSyntax) **   <a name="keyspaces-GetRecords-response-iteratorDescription"></a>
 Provides information about the current iterator at the time GetRecords request was processed by Keyspaces.
Type: [IteratorDescription](API_IteratorDescription.md) object

 ** [nextShardIterator](#API_GetRecords_ResponseSyntax) **   <a name="keyspaces-GetRecords-response-nextShardIterator"></a>
 The next position in the shard from which to start sequentially reading data records. If null, the shard has been closed and the requested iterator will not return any more data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

## Errors
<a name="API_GetRecords_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You don't have sufficient access permissions to perform this operation.
This exception occurs when your IAM user or role lacks the required permissions to access the Amazon Keyspaces resource or perform the requested action. Check your IAM policies and ensure they grant the necessary permissions.
 ** message **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 400

 [InternalServerException](API_InternalServerException.md)
The Amazon Keyspaces service encountered an unexpected error while processing the request.
This internal server error is not related to your request parameters. Retry your request after a brief delay. If the issue persists, contact AWS Support with details of your request to help identify and resolve the problem.
 ** message **
The service encountered an internal error. Try your request again.
HTTP Status Code: 500

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
The requested resource doesn't exist or could not be found.
This exception occurs when you attempt to access a keyspace, table, stream, or other Amazon Keyspaces resource that doesn't exist or that has been deleted. Verify that the resource identifier is correct and that the resource exists in your account.
 ** message **
The requested resource wasn't found. Verify that the resource exists and try again.
HTTP Status Code: 400

 [ThrottlingException](API_ThrottlingException.md)
The request rate is too high and exceeds the service's throughput limits.
This exception occurs when you send too many requests in a short period of time. Implement exponential backoff in your retry strategy to handle this exception. Reducing your request frequency or distributing requests more evenly can help avoid throughput exceptions.
This exception can also occur when more than two processes are reading from the same stream shard at the same time. Ensure that only one process reads from a stream shard at the same time.
 ** message **
The request was denied due to request throttling. Reduce the frequency of requests and try again.
HTTP Status Code: 400

 [ValidationException](API_ValidationException.md)
The request validation failed because one or more input parameters failed validation.
This exception occurs when there are syntax errors in the request, field constraints are violated, or required parameters are missing. To help you fix the issue, the exception message provides details about which parameter failed and why.
 ** errorCode **
An error occurred validating your request. See the error message for details.
 ** message **
The input fails to satisfy the constraints specified by the service. Check the error details and modify your request.
HTTP Status Code: 400

## See Also
<a name="API_GetRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/keyspacesstreams-2024-09-09/GetRecords)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/keyspacesstreams-2024-09-09/GetRecords)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspacesstreams-2024-09-09/GetRecords)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/keyspacesstreams-2024-09-09/GetRecords)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspacesstreams-2024-09-09/GetRecords)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/keyspacesstreams-2024-09-09/GetRecords)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/keyspacesstreams-2024-09-09/GetRecords)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/keyspacesstreams-2024-09-09/GetRecords)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/keyspacesstreams-2024-09-09/GetRecords)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspacesstreams-2024-09-09/GetRecords)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
