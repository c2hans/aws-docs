---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ListStreams.html
---

# ListStreams
<a name="API_ListStreams"></a>

Gets summary information about live streams in your account, in the AWS region where the API request is processed.

## Request Syntax
<a name="API_ListStreams_RequestSyntax"></a>

```
POST /ListStreams HTTP/1.1
Content-type: application/json

{
   "filterBy": {
      "health": "{{string}}"
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListStreams_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListStreams_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filterBy](#API_ListStreams_RequestSyntax) **   <a name="ivs-ListStreams-request-filterBy"></a>
Filters the stream list to match the specified criterion.
Type: [StreamFilters](API_StreamFilters.md) object
Required: No

 ** [maxResults](#API_ListStreams_RequestSyntax) **   <a name="ivs-ListStreams-request-maxResults"></a>
Maximum number of streams to return. Default: 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListStreams_RequestSyntax) **   <a name="ivs-ListStreams-request-nextToken"></a>
The first stream to retrieve. This is used for pagination; see the `nextToken` response field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=_-]*`
Required: No

## Response Syntax
<a name="API_ListStreams_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "streams": [
      {
         "channelArn": "string",
         "health": "string",
         "startTime": "string",
         "state": "string",
         "streamId": "string",
         "viewerCount": number
      }
   ]
}
```

## Response Elements
<a name="API_ListStreams_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListStreams_ResponseSyntax) **   <a name="ivs-ListStreams-response-nextToken"></a>
If there are more streams than `maxResults`, use `nextToken` in the request to get the next set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=_-]*`

 ** [streams](#API_ListStreams_ResponseSyntax) **   <a name="ivs-ListStreams-response-streams"></a>
List of streams.
Type: Array of [StreamSummary](API_StreamSummary.md) objects

## Errors
<a name="API_ListStreams_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListStreams_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/ListStreams)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/ListStreams)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/ListStreams)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/ListStreams)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/ListStreams)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/ListStreams)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/ListStreams)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/ListStreams)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/ListStreams)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/ListStreams)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
