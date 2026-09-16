---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListStreamSessionsByAccount.html
---

# ListStreamSessionsByAccount
<a name="API_ListStreamSessionsByAccount"></a>

Retrieves a list of Amazon GameLift Streams stream sessions that this user account has access to.

In the returned list of stream sessions, the `ExportFilesMetadata` property only shows the `Status` value. To get the `OutpurUri` and `StatusReason` values, use [GetStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html).

We don't recommend using this operation to regularly check stream session statuses because it's costly. Instead, to check status updates for a specific stream session, use [GetStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html).

## Request Syntax
<a name="API_ListStreamSessionsByAccount_RequestSyntax"></a>

```
GET /streamsessions?ExportFilesStatus={{ExportFilesStatus}}&MaxResults={{MaxResults}}&NextToken={{NextToken}}&Status={{Status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListStreamSessionsByAccount_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ExportFilesStatus](#API_ListStreamSessionsByAccount_RequestSyntax) **   <a name="gameliftstreams-ListStreamSessionsByAccount-request-uri-ExportFilesStatus"></a>
Filter by the exported files status. You can specify one status in each request to retrieve only sessions that currently have that exported files status.
Valid Values: `SUCCEEDED | FAILED | PENDING`

 ** [MaxResults](#API_ListStreamSessionsByAccount_RequestSyntax) **   <a name="gameliftstreams-ListStreamSessionsByAccount-request-uri-MaxResults"></a>
The number of results to return. Use this parameter with `NextToken` to return results in sequential pages. Default value is `25`.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListStreamSessionsByAccount_RequestSyntax) **   <a name="gameliftstreams-ListStreamSessionsByAccount-request-uri-NextToken"></a>
The token that marks the start of the next set of results. Use this token when you retrieve results as sequential pages. To get the first page of results, omit a token value. To get the remaining pages, provide the token returned with the previous result set.

 ** [Status](#API_ListStreamSessionsByAccount_RequestSyntax) **   <a name="gameliftstreams-ListStreamSessionsByAccount-request-uri-Status"></a>
Filter by the stream session status. You can specify one status in each request to retrieve only sessions that are currently in that status.
Valid Values: `ACTIVATING | ACTIVE | CONNECTED | PENDING_CLIENT_RECONNECTION | RECONNECTING | TERMINATING | TERMINATED | ERROR`

## Request Body
<a name="API_ListStreamSessionsByAccount_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListStreamSessionsByAccount_ResponseSyntax"></a>

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
<a name="API_ListStreamSessionsByAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListStreamSessionsByAccount_ResponseSyntax) **   <a name="gameliftstreams-ListStreamSessionsByAccount-response-Items"></a>
A collection of Amazon GameLift Streams stream sessions that are associated with a stream group and returned in response to a list request. Each item includes stream session metadata and status.
Type: Array of [StreamSessionSummary](API_StreamSessionSummary.md) objects

 ** [NextToken](#API_ListStreamSessionsByAccount_ResponseSyntax) **   <a name="gameliftstreams-ListStreamSessionsByAccount-response-NextToken"></a>
A token that marks the start of the next sequential page of results. If an operation doesn't return a token, you've reached the end of the list.
Type: String

## Errors
<a name="API_ListStreamSessionsByAccount_Errors"></a>

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

## See Also
<a name="API_ListStreamSessionsByAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gameliftstreams-2018-05-10/ListStreamSessionsByAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gameliftstreams-2018-05-10/ListStreamSessionsByAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/ListStreamSessionsByAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gameliftstreams-2018-05-10/ListStreamSessionsByAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/ListStreamSessionsByAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gameliftstreams-2018-05-10/ListStreamSessionsByAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gameliftstreams-2018-05-10/ListStreamSessionsByAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gameliftstreams-2018-05-10/ListStreamSessionsByAccount)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gameliftstreams-2018-05-10/ListStreamSessionsByAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/ListStreamSessionsByAccount)
