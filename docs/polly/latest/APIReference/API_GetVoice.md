---
source_url: https://docs.aws.amazon.com/polly/latest/APIReference/API_GetVoice.html
---

# GetVoice

Returns the status and properties of a custom voice. Use this operation after `CreateVoice` to check whether the status of the voice is `active` or `failed`. Unlike `DescribeVoices`, `GetVoice` also returns `Arn`, `VoiceCreationData`, `CustomerManagedEncryption`, and `StatusReason`. If no custom voice with the specified ID exists in your account and Region, the request fails with `ResourceNotFoundException`.

This operation requires permissions to perform the `polly:GetVoice` action.

## Request Syntax
<a name="API_GetVoice_RequestSyntax"></a>

```
GET /v1/voices/{{VoiceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetVoice_RequestParameters"></a>

The request uses the following URI parameters.

 ** [VoiceId](#API_GetVoice_RequestSyntax) **   <a name="polly-GetVoice-request-uri-VoiceId"></a>
The ID of the custom voice that `CreateVoice` returned, for example, `vc-9a8fa85dd3`. You can't specify the ARN of the voice.
Length Constraints: Maximum length of 32.
Pattern: `^vc-[0-9a-f]+$`
Required: Yes

## Request Body
<a name="API_GetVoice_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetVoice_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Voice": {
      "AdditionalLanguageCodes": [ "string" ],
      "Arn": "string",
      "CreationTime": number,
      "CustomerManagedEncryption": {
         "EncryptionContext": {
            "string" : "string"
         },
         "KmsKeyArn": "string"
      },
      "Gender": "string",
      "Id": "string",
      "LanguageCode": "string",
      "LanguageName": "string",
      "Name": "string",
      "Origin": "string",
      "Status": "string",
      "StatusReason": "string",
      "SupportedEngines": [ "string" ],
      "VoiceCreationData": {
         "Recordings": [
            {
               "Data": {
                  "Bytes": blob,
                  "S3Url": "string"
               },
               "Format": "string"
            }
         ]
      }
   }
}
```

## Response Elements
<a name="API_GetVoice_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Voice](#API_GetVoice_ResponseSyntax) **   <a name="polly-GetVoice-response-Voice"></a>
The custom voice.
Type: [Voice](API_Voice.md) object

## Errors
<a name="API_GetVoice_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_GetVoice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/polly-2016-06-10/GetVoice)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/polly-2016-06-10/GetVoice)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/polly-2016-06-10/GetVoice)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/polly-2016-06-10/GetVoice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/polly-2016-06-10/GetVoice)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/polly-2016-06-10/GetVoice)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/polly-2016-06-10/GetVoice)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/polly-2016-06-10/GetVoice)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/polly-2016-06-10/GetVoice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/polly-2016-06-10/GetVoice)
