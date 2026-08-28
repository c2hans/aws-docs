---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListStreamUrls.html
---

# ListStreamUrls
<a name="API_ListStreamUrls"></a>

Retrieves a list of the stream URLs in the current AWS Region for your AWS account. You can filter the results by status or by stream group. Use the pagination parameters to retrieve results as a set of sequential pages. If you delete the stream group or application that backs a stream URL, this operation updates that stream URL's status to `REVOKED`.

## Request Syntax
<a name="API_ListStreamUrls_RequestSyntax"></a>

```
GET /streamurls?MaxResults={{MaxResults}}&NextToken={{NextToken}}&Status={{Status}}&StreamGroupIdentifier={{StreamGroupIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListStreamUrls_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListStreamUrls_RequestSyntax) **   <a name="gameliftstreams-ListStreamUrls-request-uri-MaxResults"></a>
The maximum number of results to return per page. Valid values are 1-100. The default is 25.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListStreamUrls_RequestSyntax) **   <a name="gameliftstreams-ListStreamUrls-request-uri-NextToken"></a>
The token that marks the start of the next set of results. Use this token when you retrieve results as sequential pages. To get the first page of results, omit a token value. To get the remaining pages, provide the token returned with the previous result set.

 ** [Status](#API_ListStreamUrls_RequestSyntax) **   <a name="gameliftstreams-ListStreamUrls-request-uri-Status"></a>
Filters the list to stream URLs with the specified status.
+  `ACTIVE`: The stream URL is valid and can start stream sessions.
+  `EXPIRED`: The stream URL has passed its expiration time and can no longer start stream sessions.
+  `REVOKED`: The stream URL was revoked and can no longer start stream sessions.
+  `LIMIT_REACHED`: The stream URL has been used the maximum number of times and can no longer start stream sessions.
Valid Values: `ACTIVE | EXPIRED | REVOKED | LIMIT_REACHED`

 ** [StreamGroupIdentifier](#API_ListStreamUrls_RequestSyntax) **   <a name="gameliftstreams-ListStreamUrls-request-uri-StreamGroupIdentifier"></a>
Filters the list to stream URLs that belong to the specified stream group.
This value is an [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the stream group resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`. Example ID: `sg-1AB2C3De4`.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`

## Request Body
<a name="API_ListStreamUrls_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListStreamUrls_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "ApplicationArn": "string",
         "Arn": "string",
         "CreatedAt": number,
         "Description": "string",
         "ExpiresAt": number,
         "RemainingUses": number,
         "SessionLengthSeconds": number,
         "Status": "string",
         "StatusReason": "string",
         "StreamGroupArn": "string",
         "StreamUrl": "string",
         "StreamUrlId": "string",
         "UsageLimit": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListStreamUrls_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListStreamUrls_ResponseSyntax) **   <a name="gameliftstreams-ListStreamUrls-response-Items"></a>
A collection of stream URL summaries. Each summary includes the identity, status, and usage of the stream URL, but not its full configuration.
Type: Array of [StreamUrlSummary](API_StreamUrlSummary.md) objects

 ** [NextToken](#API_ListStreamUrls_ResponseSyntax) **   <a name="gameliftstreams-ListStreamUrls-response-NextToken"></a>
A token that marks the start of the next sequential page of results. If an operation doesn't return a token, you've reached the end of the list.
Type: String

## Errors
<a name="API_ListStreamUrls_Errors"></a>

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

## Examples
<a name="API_ListStreamUrls_Examples"></a>

### List Stream URLs (AWS CLI)
<a name="API_ListStreamUrls_Example_1"></a>

The following AWS CLI command lists the stream URLs in the current AWS Region.

#### Sample Request
<a name="API_ListStreamUrls_Example_1_Request"></a>

```
aws gameliftstreams list-stream-urls
```

## See Also
<a name="API_ListStreamUrls_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gameliftstreams-2018-05-10/ListStreamUrls)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gameliftstreams-2018-05-10/ListStreamUrls)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/ListStreamUrls)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gameliftstreams-2018-05-10/ListStreamUrls)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/ListStreamUrls)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gameliftstreams-2018-05-10/ListStreamUrls)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gameliftstreams-2018-05-10/ListStreamUrls)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gameliftstreams-2018-05-10/ListStreamUrls)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gameliftstreams-2018-05-10/ListStreamUrls)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/ListStreamUrls)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftstreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
