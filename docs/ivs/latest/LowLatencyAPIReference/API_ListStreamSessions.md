---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ListStreamSessions.html
---

# ListStreamSessions
<a name="API_ListStreamSessions"></a>

Gets a summary of current and previous streams for a specified channel in your account, in the AWS region where the API request is processed.

## Request Syntax
<a name="API_ListStreamSessions_RequestSyntax"></a>

```
POST /ListStreamSessions HTTP/1.1
Content-type: application/json

{
   "channelArn": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListStreamSessions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListStreamSessions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [channelArn](#API_ListStreamSessions_RequestSyntax) **   <a name="ivs-ListStreamSessions-request-channelArn"></a>
Channel ARN used to filter the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+`
Required: Yes

 ** [maxResults](#API_ListStreamSessions_RequestSyntax) **   <a name="ivs-ListStreamSessions-request-maxResults"></a>
Maximum number of streams to return. Default: 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListStreamSessions_RequestSyntax) **   <a name="ivs-ListStreamSessions-request-nextToken"></a>
The first stream to retrieve. This is used for pagination; see the `nextToken` response field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=_-]*`
Required: No

## Response Syntax
<a name="API_ListStreamSessions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "streamSessions": [
      {
         "endTime": "string",
         "hasErrorEvent": boolean,
         "startTime": "string",
         "streamId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListStreamSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListStreamSessions_ResponseSyntax) **   <a name="ivs-ListStreamSessions-response-nextToken"></a>
If there are more streams than `maxResults`, use `nextToken` in the request to get the next set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=_-]*`

 ** [streamSessions](#API_ListStreamSessions_ResponseSyntax) **   <a name="ivs-ListStreamSessions-response-streamSessions"></a>
List of stream sessions.
Type: Array of [StreamSessionSummary](API_StreamSessionSummary.md) objects

## Errors
<a name="API_ListStreamSessions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ResourceNotFoundException **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListStreamSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/ListStreamSessions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/ListStreamSessions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/ListStreamSessions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/ListStreamSessions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/ListStreamSessions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/ListStreamSessions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/ListStreamSessions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/ListStreamSessions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/ListStreamSessions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/ListStreamSessions)
