---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ListStreamKeys.html
---

# ListStreamKeys
<a name="API_ListStreamKeys"></a>

Gets summary information about stream keys for the specified channel.

## Request Syntax
<a name="API_ListStreamKeys_RequestSyntax"></a>

```
POST /ListStreamKeys HTTP/1.1
Content-type: application/json

{
   "channelArn": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListStreamKeys_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListStreamKeys_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [channelArn](#API_ListStreamKeys_RequestSyntax) **   <a name="ivs-ListStreamKeys-request-channelArn"></a>
Channel ARN used to filter the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+`
Required: Yes

 ** [maxResults](#API_ListStreamKeys_RequestSyntax) **   <a name="ivs-ListStreamKeys-request-maxResults"></a>
Maximum number of streamKeys to return. Default: 1.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_ListStreamKeys_RequestSyntax) **   <a name="ivs-ListStreamKeys-request-nextToken"></a>
The first stream key to retrieve. This is used for pagination; see the `nextToken` response field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=_-]*`
Required: No

## Response Syntax
<a name="API_ListStreamKeys_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "streamKeys": [
      {
         "arn": "string",
         "channelArn": "string",
         "tags": {
            "string" : "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListStreamKeys_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListStreamKeys_ResponseSyntax) **   <a name="ivs-ListStreamKeys-response-nextToken"></a>
If there are more stream keys than `maxResults`, use `nextToken` in the request to get the next set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=_-]*`

 ** [streamKeys](#API_ListStreamKeys_ResponseSyntax) **   <a name="ivs-ListStreamKeys-response-streamKeys"></a>
List of stream keys.
Type: Array of [StreamKeySummary](API_StreamKeySummary.md) objects

## Errors
<a name="API_ListStreamKeys_Errors"></a>

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
<a name="API_ListStreamKeys_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/ListStreamKeys)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/ListStreamKeys)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/ListStreamKeys)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/ListStreamKeys)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/ListStreamKeys)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/ListStreamKeys)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/ListStreamKeys)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/ListStreamKeys)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/ListStreamKeys)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/ListStreamKeys)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
