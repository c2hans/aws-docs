---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_ImportPlaybackKeyPair.html
---

# ImportPlaybackKeyPair
<a name="API_ImportPlaybackKeyPair"></a>

Imports the public portion of a new key pair and returns its `arn` and `fingerprint`. The `privateKey` can then be used to generate viewer authorization tokens, to grant viewers access to private channels. For more information, see [Setting Up Private Channels](https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html) in the *Amazon IVS User Guide*.

## Request Syntax
<a name="API_ImportPlaybackKeyPair_RequestSyntax"></a>

```
POST /ImportPlaybackKeyPair HTTP/1.1
Content-type: application/json

{
   "name": "{{string}}",
   "publicKeyMaterial": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ImportPlaybackKeyPair_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ImportPlaybackKeyPair_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [name](#API_ImportPlaybackKeyPair_RequestSyntax) **   <a name="ivs-ImportPlaybackKeyPair-request-name"></a>
Playback-key-pair name. The value does not need to be unique.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** [publicKeyMaterial](#API_ImportPlaybackKeyPair_RequestSyntax) **   <a name="ivs-ImportPlaybackKeyPair-request-publicKeyMaterial"></a>
The public portion of a customer-generated key pair.
Type: String
Required: Yes

 ** [tags](#API_ImportPlaybackKeyPair_RequestSyntax) **   <a name="ivs-ImportPlaybackKeyPair-request-tags"></a>
Any tags provided with the request are added to the playback key pair tags. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]+)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

## Response Syntax
<a name="API_ImportPlaybackKeyPair_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "keyPair": {
      "arn": "string",
      "fingerprint": "string",
      "name": "string",
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_ImportPlaybackKeyPair_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [keyPair](#API_ImportPlaybackKeyPair_ResponseSyntax) **   <a name="ivs-ImportPlaybackKeyPair-response-keyPair"></a>

Type: [PlaybackKeyPair](API_PlaybackKeyPair.md) object

## Errors
<a name="API_ImportPlaybackKeyPair_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** PendingVerification **
Your account is pending verification.
HTTP Status Code: 403

 ** ServiceQuotaExceededException **
Request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ImportPlaybackKeyPair_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/ImportPlaybackKeyPair)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/ImportPlaybackKeyPair)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/ImportPlaybackKeyPair)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/ImportPlaybackKeyPair)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/ImportPlaybackKeyPair)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/ImportPlaybackKeyPair)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/ImportPlaybackKeyPair)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/ImportPlaybackKeyPair)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/ImportPlaybackKeyPair)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/ImportPlaybackKeyPair)
