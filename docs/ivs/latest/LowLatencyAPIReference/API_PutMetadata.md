---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_PutMetadata.html
---

# PutMetadata
<a name="API_PutMetadata"></a>

Inserts metadata into the active stream of the specified channel. At most 5 requests per second per channel are allowed, each with a maximum 1 KB payload. (If 5 TPS is not sufficient for your needs, we recommend batching your data into a single PutMetadata call.) At most 155 requests per second per account are allowed. Also see [Embedding Metadata within a Video Stream](https://docs.aws.amazon.com/ivs/latest/userguide/metadata.html) in the *Amazon IVS User Guide*.

## Request Syntax
<a name="API_PutMetadata_RequestSyntax"></a>

```
POST /PutMetadata HTTP/1.1
Content-type: application/json

{
   "channelArn": "{{string}}",
   "metadata": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutMetadata_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutMetadata_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [channelArn](#API_PutMetadata_RequestSyntax) **   <a name="ivs-PutMetadata-request-channelArn"></a>
ARN of the channel into which metadata is inserted. This channel must have an active stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+`
Required: Yes

 ** [metadata](#API_PutMetadata_RequestSyntax) **   <a name="ivs-PutMetadata-request-metadata"></a>
Metadata to insert into the stream. Maximum: 1 KB per request.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

## Response Syntax
<a name="API_PutMetadata_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_PutMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_PutMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ChannelNotBroadcasting **
The stream is offline for the given channel ARN.
HTTP Status Code: 404

 ** ResourceNotFoundException **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_PutMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/PutMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/PutMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/PutMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/PutMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/PutMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/PutMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/PutMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/PutMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/PutMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/PutMetadata)
