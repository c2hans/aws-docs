---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_DeletePlaybackKeyPair.html
---

# DeletePlaybackKeyPair
<a name="API_DeletePlaybackKeyPair"></a>

Deletes a specified authorization key pair. This invalidates future viewer tokens generated using the key pair’s `privateKey`. For more information, see [Setting Up Private Channels](https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html) in the *Amazon IVS User Guide*.

## Request Syntax
<a name="API_DeletePlaybackKeyPair_RequestSyntax"></a>

```
POST /DeletePlaybackKeyPair HTTP/1.1
Content-type: application/json

{
   "arn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeletePlaybackKeyPair_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeletePlaybackKeyPair_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arn](#API_DeletePlaybackKeyPair_RequestSyntax) **   <a name="ivs-DeletePlaybackKeyPair-request-arn"></a>
ARN of the key pair to be deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:playback-key/[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_DeletePlaybackKeyPair_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeletePlaybackKeyPair_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeletePlaybackKeyPair_Errors"></a>

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

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_DeletePlaybackKeyPair_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/DeletePlaybackKeyPair)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/DeletePlaybackKeyPair)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/DeletePlaybackKeyPair)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/DeletePlaybackKeyPair)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/DeletePlaybackKeyPair)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/DeletePlaybackKeyPair)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/DeletePlaybackKeyPair)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/DeletePlaybackKeyPair)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/DeletePlaybackKeyPair)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/DeletePlaybackKeyPair)
