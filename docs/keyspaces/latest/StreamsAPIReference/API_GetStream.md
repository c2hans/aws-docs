---
source_url: https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_GetStream.html
---

# GetStream
<a name="API_GetStream"></a>

Returns detailed information about a specific data capture stream for an Amazon Keyspaces table. The information includes the stream's Amazon Resource Name (ARN), creation time, current status, retention period, shard composition, and associated table details. This operation helps you monitor and manage the configuration of your Amazon Keyspaces data streams.

## Request Syntax
<a name="API_GetStream_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "shardFilter": {
      "shardId": "{{string}}",
      "type": "{{string}}"
   },
   "streamArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetStream_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_GetStream_RequestSyntax) **   <a name="keyspaces-GetStream-request-maxResults"></a>
 The maximum number of shard objects to return in a single `GetStream` request. The default value is 100. The minimum value is 1 and the maximum value is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_GetStream_RequestSyntax) **   <a name="keyspaces-GetStream-request-nextToken"></a>
 An optional pagination token provided by a previous `GetStream` operation. If this parameter is specified, the response includes only records beyond the token, up to the value specified by `MaxResults`.
Type: String
Length Constraints: Minimum length of 80. Maximum length of 3000.
Required: No

 ** [shardFilter](#API_GetStream_RequestSyntax) **   <a name="keyspaces-GetStream-request-shardFilter"></a>
 Optional filter criteria to apply when retrieving shards. You can filter shards based on their parent `shardID` to get a list of children shards to narrow down the results returned by the `GetStream` operation.
Type: [ShardFilter](API_ShardFilter.md) object
Required: No

 ** [streamArn](#API_GetStream_RequestSyntax) **   <a name="keyspaces-GetStream-request-streamArn"></a>
 The Amazon Resource Name (ARN) of the stream for which detailed information is requested. This uniquely identifies the specific stream you want to get information about.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.
Required: Yes

## Response Syntax
<a name="API_GetStream_ResponseSyntax"></a>

```
{
   "creationRequestDateTime": number,
   "keyspaceName": "string",
   "nextToken": "string",
   "shards": [
      {
         "parentShardIds": [ "string" ],
         "sequenceNumberRange": {
            "endingSequenceNumber": "string",
            "startingSequenceNumber": "string"
         },
         "shardId": "string"
      }
   ],
   "streamArn": "string",
   "streamLabel": "string",
   "streamStatus": "string",
   "streamViewType": "string",
   "tableName": "string"
}
```

## Response Elements
<a name="API_GetStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationRequestDateTime](#API_GetStream_ResponseSyntax) **   <a name="keyspaces-GetStream-response-creationRequestDateTime"></a>
 The date and time when the request to create this stream was issued. The value is represented in ISO 8601 format.
Type: Timestamp

 ** [keyspaceName](#API_GetStream_ResponseSyntax) **   <a name="keyspaces-GetStream-response-keyspaceName"></a>
 The name of the keyspace containing the table associated with this stream. The keyspace name is part of the table's hierarchical identifier in Amazon Keyspaces.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`

 ** [nextToken](#API_GetStream_ResponseSyntax) **   <a name="keyspaces-GetStream-response-nextToken"></a>
 A pagination token that can be used in a subsequent `GetStream` request. This token is returned if the response contains more shards than can be returned in a single response.
Type: String
Length Constraints: Minimum length of 80. Maximum length of 3000.

 ** [shards](#API_GetStream_ResponseSyntax) **   <a name="keyspaces-GetStream-response-shards"></a>
 An array of shard objects associated with this stream. Each shard contains a subset of the stream's data records and has its own unique identifier. The collection of shards represents the complete stream data.
Type: Array of [Shard](API_Shard.md) objects

 ** [streamArn](#API_GetStream_ResponseSyntax) **   <a name="keyspaces-GetStream-response-streamArn"></a>
 The Amazon Resource Name (ARN) that uniquely identifies the stream within Amazon Keyspaces. This ARN can be used in other API operations to reference this specific stream.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.

 ** [streamLabel](#API_GetStream_ResponseSyntax) **   <a name="keyspaces-GetStream-response-streamLabel"></a>
 A timestamp that serves as a unique identifier for this stream, used for debugging and monitoring purposes. The stream label represents the point in time when the stream was created.
Type: String

 ** [streamStatus](#API_GetStream_ResponseSyntax) **   <a name="keyspaces-GetStream-response-streamStatus"></a>
 The current status of the stream. Values can be `ENABLING`, `ENABLED`, `DISABLING`, or `DISABLED`. Operations on the stream depend on its current status.
Type: String
Valid Values: `ENABLING | ENABLED | DISABLING | DISABLED`

 ** [streamViewType](#API_GetStream_ResponseSyntax) **   <a name="keyspaces-GetStream-response-streamViewType"></a>
 The format of the data records in this stream. Currently, this can be one of the following options:
+  `NEW_AND_OLD_IMAGES` - both versions of the row, before and after the change. This is the default.
+  `NEW_IMAGE` - the version of the row after the change.
+  `OLD_IMAGE` - the version of the row before the change.
+  `KEYS_ONLY` - the partition and clustering keys of the row that was changed.
Type: String
Valid Values: `NEW_IMAGE | OLD_IMAGE | NEW_AND_OLD_IMAGES | KEYS_ONLY`

 ** [tableName](#API_GetStream_ResponseSyntax) **   <a name="keyspaces-GetStream-response-tableName"></a>
 The name of the table associated with this stream. The stream captures changes to rows in this Amazon Keyspaces table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`

## Errors
<a name="API_GetStream_Errors"></a>

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
<a name="API_GetStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/keyspacesstreams-2024-09-09/GetStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/keyspacesstreams-2024-09-09/GetStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspacesstreams-2024-09-09/GetStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/keyspacesstreams-2024-09-09/GetStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspacesstreams-2024-09-09/GetStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/keyspacesstreams-2024-09-09/GetStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/keyspacesstreams-2024-09-09/GetStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/keyspacesstreams-2024-09-09/GetStream)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/keyspacesstreams-2024-09-09/GetStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspacesstreams-2024-09-09/GetStream)
