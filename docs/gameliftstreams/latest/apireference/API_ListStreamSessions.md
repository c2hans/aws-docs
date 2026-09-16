---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListStreamSessions.html
---

# ListStreamSessions
<a name="API_ListStreamSessions"></a>

Retrieves a list of Amazon GameLift Streams stream sessions that a stream group is hosting.

To retrieve stream sessions, specify the stream group, and optionally filter by stream session status. You can paginate the results as needed.

This operation returns the requested stream sessions in no particular order.

## Request Syntax
<a name="API_ListStreamSessions_RequestSyntax"></a>

```
GET /streamgroups/{{Identifier}}/streamsessions?ExportFilesStatus={{ExportFilesStatus}}&MaxResults={{MaxResults}}&NextToken={{NextToken}}&Status={{Status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListStreamSessions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ExportFilesStatus](#API_ListStreamSessions_RequestSyntax) **   <a name="gameliftstreams-ListStreamSessions-request-uri-ExportFilesStatus"></a>
Filter by the exported files status. You can specify one status in each request to retrieve only sessions that currently have that exported files status.
 Exported files can be in one of the following states:
+  `SUCCEEDED`: The exported files are successfully stored in an S3 bucket.
+  `FAILED`: The session ended but Amazon GameLift Streams couldn't collect and upload the files to S3.
+  `PENDING`: Either the stream session is still in progress, or uploading the exported files to the S3 bucket is in progress.
Valid Values: `SUCCEEDED | FAILED | PENDING`

 ** [Identifier](#API_ListStreamSessions_RequestSyntax) **   <a name="gameliftstreams-ListStreamSessions-request-uri-Identifier"></a>
The unique identifier of a Amazon GameLift Streams stream group to retrieve the stream session for. You can use either the stream group ID or the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html).
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

 ** [MaxResults](#API_ListStreamSessions_RequestSyntax) **   <a name="gameliftstreams-ListStreamSessions-request-uri-MaxResults"></a>
The number of results to return. Use this parameter with `NextToken` to return results in sequential pages. Default value is `25`.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListStreamSessions_RequestSyntax) **   <a name="gameliftstreams-ListStreamSessions-request-uri-NextToken"></a>
The token that marks the start of the next set of results. Use this token when you retrieve results as sequential pages. To get the first page of results, omit a token value. To get the remaining pages, provide the token returned with the previous result set.

 ** [Status](#API_ListStreamSessions_RequestSyntax) **   <a name="gameliftstreams-ListStreamSessions-request-uri-Status"></a>
Filter by the stream session status. You can specify one status in each request to retrieve only sessions that are currently in that status.
Valid Values: `ACTIVATING | ACTIVE | CONNECTED | PENDING_CLIENT_RECONNECTION | RECONNECTING | TERMINATING | TERMINATED | ERROR`

## Request Body
<a name="API_ListStreamSessions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListStreamSessions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "ApplicationArn": "string",
         "Arn": "string",
         "CreatedAt": number,
         "ExportFilesMetadata": {
            "OutputUri": "string",
            "Status": "string",
            "StatusReason": "string"
         },
         "LastUpdatedAt": number,
         "Location": "string",
         "Protocol": "string",
         "RoleArn": "string",
         "Status": "string",
         "StatusReason": "string",
         "UserId": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListStreamSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListStreamSessions_ResponseSyntax) **   <a name="gameliftstreams-ListStreamSessions-response-Items"></a>
A collection of Amazon GameLift Streams stream sessions that are associated with a stream group and returned in response to a list request. Each item includes stream session metadata and status.
Type: Array of [StreamSessionSummary](API_StreamSessionSummary.md) objects

 ** [NextToken](#API_ListStreamSessions_ResponseSyntax) **   <a name="gameliftstreams-ListStreamSessions-response-NextToken"></a>
A token that marks the start of the next sequential page of results. If an operation doesn't return a token, you've reached the end of the list.
Type: String

## Errors
<a name="API_ListStreamSessions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.
 ** Message **
Description of the error.
HTTP Status Code: 403

 [InternalServerException](API_InternalServerException.md)
The service encountered an internal error and is unable to complete the request.
 ** Message **
Description of the error.
HTTP Status Code: 500

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
The resource specified in the request was not found. Correct the request before you try again.
 ** Message **
Description of the error.
HTTP Status Code: 404

 [ThrottlingException](API_ThrottlingException.md)
The request was denied due to request throttling. Retry the request after the suggested wait time.
 ** Message **
Description of the error.
HTTP Status Code: 429

 [ValidationException](API_ValidationException.md)
One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.
 ** Message **
Description of the error.
HTTP Status Code: 400

## Examples
<a name="API_ListStreamSessions_Examples"></a>

### CLI Example
<a name="API_ListStreamSessions_Example_1"></a>

The following example shows how to use the CLI to retrieve a list of stream sessions for a specified stream group and filter to return stream sessions in `ERROR` status. The request doesn't include a `MaxResults` or a `NextToken`, so the request returns the first 25 results in the set.

#### Sample Request
<a name="API_ListStreamSessions_Example_1_Request"></a>

```
aws gameliftstreams list-stream-sessions \
    --identifier arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4 \
    --status ERROR
```

## See Also
<a name="API_ListStreamSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gameliftstreams-2018-05-10/ListStreamSessions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gameliftstreams-2018-05-10/ListStreamSessions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/ListStreamSessions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gameliftstreams-2018-05-10/ListStreamSessions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/ListStreamSessions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gameliftstreams-2018-05-10/ListStreamSessions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gameliftstreams-2018-05-10/ListStreamSessions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gameliftstreams-2018-05-10/ListStreamSessions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gameliftstreams-2018-05-10/ListStreamSessions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/ListStreamSessions)
