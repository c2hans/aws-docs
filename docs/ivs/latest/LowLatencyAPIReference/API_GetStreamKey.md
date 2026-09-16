---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_GetStreamKey.html
---

# GetStreamKey
<a name="API_GetStreamKey"></a>

Gets stream-key information for a specified ARN.

## Request Syntax
<a name="API_GetStreamKey_RequestSyntax"></a>

```
POST /GetStreamKey HTTP/1.1
Content-type: application/json

{
   "arn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetStreamKey_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetStreamKey_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arn](#API_GetStreamKey_RequestSyntax) **   <a name="ivs-GetStreamKey-request-arn"></a>
ARN for the stream key to be retrieved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:stream-key/[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_GetStreamKey_ResponseSyntax"></a>

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
<a name="API_GetStreamKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [streamKey](#API_GetStreamKey_ResponseSyntax) **   <a name="ivs-GetStreamKey-response-streamKey"></a>
Object specifying a stream key.
Type: [StreamKey](API_StreamKey.md) object

## Errors
<a name="API_GetStreamKey_Errors"></a>

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
<a name="API_GetStreamKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/GetStreamKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/GetStreamKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/GetStreamKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/GetStreamKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/GetStreamKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/GetStreamKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/GetStreamKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/GetStreamKey)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/GetStreamKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/GetStreamKey)
