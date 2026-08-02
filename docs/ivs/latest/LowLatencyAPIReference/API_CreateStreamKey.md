---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_CreateStreamKey.html
---

# CreateStreamKey
<a name="API_CreateStreamKey"></a>

Creates a stream key, used to initiate a stream, for the specified channel ARN.

Note that [CreateChannel](API_CreateChannel.md) creates a stream key. If you subsequently use CreateStreamKey on the same channel, it will fail because a stream key already exists and there is a limit of 1 stream key per channel. To reset the stream key on a channel, use [DeleteStreamKey](API_DeleteStreamKey.md) and then CreateStreamKey.

## Request Syntax
<a name="API_CreateStreamKey_RequestSyntax"></a>

```
POST /CreateStreamKey HTTP/1.1
Content-type: application/json

{
   "channelArn": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateStreamKey_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateStreamKey_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [channelArn](#API_CreateStreamKey_RequestSyntax) **   <a name="ivs-CreateStreamKey-request-channelArn"></a>
ARN of the channel for which to create the stream key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+`
Required: Yes

 ** [tags](#API_CreateStreamKey_RequestSyntax) **   <a name="ivs-CreateStreamKey-request-tags"></a>
Array of 1-50 maps, each of the form `string:string (key:value)`. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]+)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

## Response Syntax
<a name="API_CreateStreamKey_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "streamKey": {
      "arn": "string",
      "channelArn": "string",
      "tags": {
         "string" : "string"
      },
      "value": "string"
   }
}
```

## Response Elements
<a name="API_CreateStreamKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [streamKey](#API_CreateStreamKey_ResponseSyntax) **   <a name="ivs-CreateStreamKey-response-streamKey"></a>
Stream key used to authenticate an RTMPS stream for ingestion.
Type: [StreamKey](API_StreamKey.md) object

## Errors
<a name="API_CreateStreamKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** PendingVerification **
Your account is pending verification.
HTTP Status Code: 403

 ** ResourceNotFoundException **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateStreamKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/CreateStreamKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/CreateStreamKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/CreateStreamKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/CreateStreamKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/CreateStreamKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/CreateStreamKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/CreateStreamKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/CreateStreamKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/CreateStreamKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/CreateStreamKey)
