---
source_url: https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_ListStreams.html
---

# ListStreams
<a name="API_ListStreams"></a>

Returns a list of all data capture streams associated with your Amazon Keyspaces account or for a specific keyspace or table. The response includes information such as stream ARNs, table associations, creation timestamps, and current status. This operation helps you discover and manage all active data streams in your Amazon Keyspaces environment.

## Request Syntax
<a name="API_ListStreams_RequestSyntax"></a>

```
{
   "keyspaceName": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "tableName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListStreams_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [keyspaceName](#API_ListStreams_RequestSyntax) **   <a name="keyspaces-ListStreams-request-keyspaceName"></a>
 The name of the keyspace for which to list streams. If specified, only streams associated with tables in this keyspace are returned. If omitted, streams from all keyspaces are included in the results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`
Required: No

 ** [maxResults](#API_ListStreams_RequestSyntax) **   <a name="keyspaces-ListStreams-request-maxResults"></a>
 The maximum number of streams to return in a single `ListStreams` request. The default value is 100. The minimum value is 1 and the maximum value is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListStreams_RequestSyntax) **   <a name="keyspaces-ListStreams-request-nextToken"></a>
 An optional pagination token provided by a previous `ListStreams` operation. If this parameter is specified, the response includes only records beyond the token, up to the value specified by `maxResults`.
Type: String
Length Constraints: Minimum length of 80. Maximum length of 3000.
Required: No

 ** [tableName](#API_ListStreams_RequestSyntax) **   <a name="keyspaces-ListStreams-request-tableName"></a>
 The name of the table for which to list streams. Must be used together with `keyspaceName`. If specified, only streams associated with this specific table are returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`
Required: No

## Response Syntax
<a name="API_ListStreams_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "streams": [
      {
         "keyspaceName": "string",
         "streamArn": "string",
         "streamLabel": "string",
         "tableName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListStreams_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListStreams_ResponseSyntax) **   <a name="keyspaces-ListStreams-response-nextToken"></a>
 A pagination token that can be used in a subsequent `ListStreams` request. This token is returned if the response contains more streams than can be returned in a single response based on the `maxResults` parameter.
Type: String
Length Constraints: Minimum length of 80. Maximum length of 3000.

 ** [streams](#API_ListStreams_ResponseSyntax) **   <a name="keyspaces-ListStreams-response-streams"></a>
 An array of stream objects, each containing summary information about a stream including its ARN, status, and associated table information. This list includes all streams that match the request criteria.
Type: Array of [Stream](API_Stream.md) objects

## Errors
<a name="API_ListStreams_Errors"></a>

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
<a name="API_ListStreams_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/keyspacesstreams-2024-09-09/ListStreams)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/keyspacesstreams-2024-09-09/ListStreams)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspacesstreams-2024-09-09/ListStreams)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/keyspacesstreams-2024-09-09/ListStreams)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspacesstreams-2024-09-09/ListStreams)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/keyspacesstreams-2024-09-09/ListStreams)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/keyspacesstreams-2024-09-09/ListStreams)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/keyspacesstreams-2024-09-09/ListStreams)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/keyspacesstreams-2024-09-09/ListStreams)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspacesstreams-2024-09-09/ListStreams)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
