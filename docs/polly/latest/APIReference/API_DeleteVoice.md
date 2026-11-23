---
source_url: https://docs.aws.amazon.com/polly/latest/APIReference/API_DeleteVoice.html
---

# DeleteVoice

Deletes a custom voice. `DescribeVoices` and `GetVoice` stop returning the voice immediately. You can't restore a deleted voice.

You can delete a voice in `active` or `failed` status. If the voice is in `pending` status, the request fails with `ConflictException`. If no custom voice with the specified ID exists in your account and Region, the request fails with `ResourceNotFoundException`. You can delete the voice even if you disabled its AWS KMS key or scheduled it for deletion.

This operation requires permissions to perform the `polly:DeleteVoice` action.

## Request Syntax
<a name="API_DeleteVoice_RequestSyntax"></a>

```
DELETE /v1/voices/{{VoiceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteVoice_RequestParameters"></a>

The request uses the following URI parameters.

 ** [VoiceId](#API_DeleteVoice_RequestSyntax) **   <a name="polly-DeleteVoice-request-uri-VoiceId"></a>
The ID of the custom voice to delete, for example, `vc-9a8fa85dd3`. You can't specify the ARN of the voice.
Length Constraints: Maximum length of 32.
Pattern: `^vc-[0-9a-f]+$`
Required: Yes

## Request Body
<a name="API_DeleteVoice_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteVoice_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteVoice_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteVoice_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request conflicts with the current state of the resource. For a custom voice, the voice isn't in the status that the operation requires. Check the status with `GetVoice`, and then try again.
 ** resourceId **
The ID of the resource that the request conflicts with.
 ** resourceType **
The type of the resource that the request conflicts with.
HTTP Status Code: 409

 ** ResourceNotFoundException **
Amazon Polly can't find the specified resource. Verify that the resource exists in the AWS account and Region of the request and that its ARN or ID is spelled correctly, and then try again.
 ** resourceId **
The identifier of the resource that wasn't found.
 ** resourceType **
The type of the resource that wasn't found.
HTTP Status Code: 404

 ** ServiceFailureException **
An unknown condition has caused a service failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied because of request throttling.
 ** throttlingReasons **
A list of reasons explaining why the request was throttled.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** fields **
The fields that caused the validation error.
 ** reason **
The reason the request failed validation. If Amazon Polly can't use the AWS KMS key that you specified in `CreateVoice`, `fields` names `CustomerManagedEncryption.KmsKeyArn` and the reason is one of the following:
kmsKeyNotFound
No key with the specified ARN exists.
kmsKeyUnusable
The key is disabled, scheduled for deletion, or missing its key material, or it isn't a symmetric encryption key.
HTTP Status Code: 400

## See Also
<a name="API_DeleteVoice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/polly-2016-06-10/DeleteVoice)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/polly-2016-06-10/DeleteVoice)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/polly-2016-06-10/DeleteVoice)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/polly-2016-06-10/DeleteVoice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/polly-2016-06-10/DeleteVoice)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/polly-2016-06-10/DeleteVoice)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/polly-2016-06-10/DeleteVoice)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/polly-2016-06-10/DeleteVoice)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/polly-2016-06-10/DeleteVoice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/polly-2016-06-10/DeleteVoice)
