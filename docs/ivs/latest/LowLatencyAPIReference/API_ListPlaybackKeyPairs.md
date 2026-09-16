---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ListPlaybackKeyPairs.html
---

# ListPlaybackKeyPairs
<a name="API_ListPlaybackKeyPairs"></a>

Gets summary information about playback key pairs. For more information, see [Setting Up Private Channels](https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html) in the *Amazon IVS User Guide*.

## Request Syntax
<a name="API_ListPlaybackKeyPairs_RequestSyntax"></a>

```
POST /ListPlaybackKeyPairs HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListPlaybackKeyPairs_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListPlaybackKeyPairs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListPlaybackKeyPairs_RequestSyntax) **   <a name="ivs-ListPlaybackKeyPairs-request-maxResults"></a>
Maximum number of key pairs to return. Default: your service quota or 100, whichever is smaller.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListPlaybackKeyPairs_RequestSyntax) **   <a name="ivs-ListPlaybackKeyPairs-request-nextToken"></a>
The first key pair to retrieve. This is used for pagination; see the `nextToken` response field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=_-]*`
Required: No

## Response Syntax
<a name="API_ListPlaybackKeyPairs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "keyPairs": [
      {
         "arn": "string",
         "name": "string",
         "tags": {
            "string" : "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListPlaybackKeyPairs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [keyPairs](#API_ListPlaybackKeyPairs_ResponseSyntax) **   <a name="ivs-ListPlaybackKeyPairs-response-keyPairs"></a>
List of key pairs.
Type: Array of [PlaybackKeyPairSummary](API_PlaybackKeyPairSummary.md) objects

 ** [nextToken](#API_ListPlaybackKeyPairs_ResponseSyntax) **   <a name="ivs-ListPlaybackKeyPairs-response-nextToken"></a>
If there are more key pairs than `maxResults`, use `nextToken` in the request to get the next set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=_-]*`

## Errors
<a name="API_ListPlaybackKeyPairs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListPlaybackKeyPairs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/ListPlaybackKeyPairs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/ListPlaybackKeyPairs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/ListPlaybackKeyPairs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/ListPlaybackKeyPairs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/ListPlaybackKeyPairs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/ListPlaybackKeyPairs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/ListPlaybackKeyPairs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/ListPlaybackKeyPairs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/ListPlaybackKeyPairs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/ListPlaybackKeyPairs)
