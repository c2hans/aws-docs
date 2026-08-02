---
source_url: https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_GetShardIterator.html
---

# GetShardIterator
<a name="API_GetShardIterator"></a>

Returns a shard iterator that serves as a bookmark for reading data from a specific position in an Amazon Keyspaces data stream's shard. The shard iterator specifies the shard position from which to start reading data records sequentially. You can specify whether to begin reading at the latest record, the oldest record, or at a particular sequence number within the shard.

## Request Syntax
<a name="API_GetShardIterator_RequestSyntax"></a>

```
{
   "sequenceNumber": "{{string}}",
   "shardId": "{{string}}",
   "shardIteratorType": "{{string}}",
   "streamArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetShardIterator_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [sequenceNumber](#API_GetShardIterator_RequestSyntax) **   <a name="keyspaces-GetShardIterator-request-sequenceNumber"></a>
 The sequence number of the data record in the shard from which to start reading. Required if `ShardIteratorType` is `AT_SEQUENCE_NUMBER` or `AFTER_SEQUENCE_NUMBER`. This parameter is ignored for other iterator types.
Type: String
Length Constraints: Minimum length of 21. Maximum length of 48.
Required: No

 ** [shardId](#API_GetShardIterator_RequestSyntax) **   <a name="keyspaces-GetShardIterator-request-shardId"></a>
 The identifier of the shard within the stream. The shard ID uniquely identifies a subset of the stream's data records that you want to access.
Type: String
Length Constraints: Minimum length of 28. Maximum length of 65.
Required: Yes

 ** [shardIteratorType](#API_GetShardIterator_RequestSyntax) **   <a name="keyspaces-GetShardIterator-request-shardIteratorType"></a>
 Determines how the shard iterator is positioned. Must be one of the following:
+  `TRIM_HORIZON` - Start reading at the last untrimmed record in the shard, which is the oldest data record in the shard.
+  `AT_SEQUENCE_NUMBER` - Start reading exactly from the specified sequence number.
+  `AFTER_SEQUENCE_NUMBER` - Start reading right after the specified sequence number.
+  `LATEST` - Start reading just after the most recent record in the shard, so that you always read the most recent data.
Type: String
Valid Values: `TRIM_HORIZON | LATEST | AT_SEQUENCE_NUMBER | AFTER_SEQUENCE_NUMBER`
Required: Yes

 ** [streamArn](#API_GetShardIterator_RequestSyntax) **   <a name="keyspaces-GetShardIterator-request-streamArn"></a>
 The Amazon Resource Name (ARN) of the stream for which to get the shard iterator. The ARN uniquely identifies the stream within Amazon Keyspaces.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.
Required: Yes

## Response Syntax
<a name="API_GetShardIterator_ResponseSyntax"></a>

```
{
   "shardIterator": "string"
}
```

## Response Elements
<a name="API_GetShardIterator_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [shardIterator](#API_GetShardIterator_ResponseSyntax) **   <a name="keyspaces-GetShardIterator-response-shardIterator"></a>
 The unique identifier for the shard iterator. This value is used in the `GetRecords` operation to retrieve data records from the specified shard. Each shard iterator expires 15 minutes after it is returned to the requester.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

## Errors
<a name="API_GetShardIterator_Errors"></a>

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
<a name="API_GetShardIterator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/keyspacesstreams-2024-09-09/GetShardIterator)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/keyspacesstreams-2024-09-09/GetShardIterator)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspacesstreams-2024-09-09/GetShardIterator)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/keyspacesstreams-2024-09-09/GetShardIterator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspacesstreams-2024-09-09/GetShardIterator)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/keyspacesstreams-2024-09-09/GetShardIterator)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/keyspacesstreams-2024-09-09/GetShardIterator)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/keyspacesstreams-2024-09-09/GetShardIterator)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/keyspacesstreams-2024-09-09/GetShardIterator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspacesstreams-2024-09-09/GetShardIterator)
