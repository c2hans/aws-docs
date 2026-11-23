---
source_url: https://docs.aws.amazon.com/polly/latest/APIReference/API_CreateVoice.html
---

# CreateVoice

Creates a custom voice from recordings of a speaker and returns it in `pending` status. Use `GetVoice` to check the status. When the status is `active`, you can use the voice ID in `SynthesizeSpeech`, `StartSpeechSynthesisTask`, and `StartSpeechSynthesisStream`.

The `custom-voice-max-count` service quota limits the number of custom voices in your account in each Region. If you reach the quota, the request fails with `ServiceQuotaExceededException`.

This operation requires permissions to perform the `polly:CreateVoice` action. You also need `s3:GetObject` permission on each recording that you specify by `S3Url`. If you specify a customer managed key, you also need `kms:DescribeKey`, `kms:GenerateDataKey`, and `kms:Decrypt` permissions on the key. If you specify `Tags`, you also need the `polly:TagResource` permission.

## Request Syntax
<a name="API_CreateVoice_RequestSyntax"></a>

```
POST /v1/voices HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "CustomerManagedEncryption": {
      "EncryptionContext": {
         "{{string}}" : "{{string}}"
      },
      "KmsKeyArn": "{{string}}"
   },
   "LanguageCode": "{{string}}",
   "Name": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "TermsAccepted": {{boolean}},
   "VoiceCreationData": {
      "Recordings": [
         {
            "Data": {
               "Bytes": {{blob}},
               "S3Url": "{{string}}"
            },
            "Format": "{{string}}"
         }
      ]
   }
}
```

## URI Request Parameters
<a name="API_CreateVoice_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateVoice_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateVoice_RequestSyntax) **   <a name="polly-CreateVoice-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, the AWS SDKs generate one for you. If you retry a request that succeeded with the same client token and the same parameters, Amazon Polly returns the voice that the first request created and doesn't create a second voice.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[!-~]+$`
Required: No

 ** [CustomerManagedEncryption](#API_CreateVoice_RequestSyntax) **   <a name="polly-CreateVoice-request-CustomerManagedEncryption"></a>
The customer managed key that you want Amazon Polly to encrypt the voice with. If you omit this parameter, Amazon Polly encrypts the voice with an AWS owned key.
Type: [CustomerManagedEncryption](API_CustomerManagedEncryption.md) object
Required: No

 ** [LanguageCode](#API_CreateVoice_RequestSyntax) **   <a name="polly-CreateVoice-request-LanguageCode"></a>
The language of the recordings, for example, `en-US`. Amazon Polly doesn't detect the language from the recordings.
Type: String
Valid Values: `de-DE | en-US | es-US | fr-FR | hi-IN | it-IT | pt-BR`
Required: Yes

 ** [Name](#API_CreateVoice_RequestSyntax) **   <a name="polly-CreateVoice-request-Name"></a>
The name of the voice. Use the name to identify the voice in your application. The name can contain letters, digits, hyphens, and underscores, and can be up to 64 characters long. The name doesn't have to be unique. The name isn't the voice ID, which Amazon Polly assigns.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [Tags](#API_CreateVoice_RequestSyntax) **   <a name="polly-CreateVoice-request-Tags"></a>
The tags that you apply to the voice to help you categorize and organize it. Each tag consists of a key and an optional value, both of which you define.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [TermsAccepted](#API_CreateVoice_RequestSyntax) **   <a name="polly-CreateVoice-request-TermsAccepted"></a>
Confirms the following two statements:
+ "I confirm that I have obtained all necessary consents required under any applicable laws and regulations, including biometric privacy laws, from the owner of this voice to clone these voice samples."
+ "I confirm that I will not use the generated content for any illegal, fraudulent, or harmful purpose and reaffirm my obligation to abide by the AWS Service Terms, Biometric Notice and Consent Terms, AWS Responsible AI Policy, and AWS Acceptable Use Policy."
You can read the [AWS Service Terms](https://aws.amazon.com/service-terms/), the [Biometric Notice and Consent Terms](https://aws.amazon.com/legal/biometric-notice-and-consent-terms/), the [AWS Responsible AI Policy](https://aws.amazon.com/ai/responsible-ai/policy/), and the [AWS Acceptable Use Policy](https://aws.amazon.com/aup/) on the Amazon Web Services website.
You must set this parameter to `true` to create a voice. Otherwise, the request fails with `ValidationException`.
Type: Boolean
Required: Yes

 ** [VoiceCreationData](#API_CreateVoice_RequestSyntax) **   <a name="polly-CreateVoice-request-VoiceCreationData"></a>
The recordings that Amazon Polly uses to create the voice.
Type: [VoiceCreationData](API_VoiceCreationData.md) object
Required: Yes

## Response Syntax
<a name="API_CreateVoice_ResponseSyntax"></a>

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
<a name="API_CreateVoice_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Voice](#API_CreateVoice_ResponseSyntax) **   <a name="polly-CreateVoice-response-Voice"></a>
The new voice, in `pending` status.
Type: [Voice](API_Voice.md) object

## Errors
<a name="API_CreateVoice_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action. For a custom voice that uses a customer managed key, Amazon Polly also returns this exception if you don't have the required AWS KMS permissions on the key.
HTTP Status Code: 403

 ** InvalidTagParameterException **
The resource ARN or a tag in the request isn't valid. Specify the ARN of a supported resource in the AWS account and Region of the request. Tag keys can have a maximum length of 128 characters, and tag values can have a maximum length of 256 characters. Correct the ARN or the tags, and then try again.
HTTP Status Code: 400

 ** ServiceFailureException **
An unknown condition has caused a service failure.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
 ** quotaCode **
The quota code identifying the specific quota.
 ** serviceCode **
The service code identifying the originating service.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied because of request throttling.
 ** throttlingReasons **
A list of reasons explaining why the request was throttled.
HTTP Status Code: 400

 ** TooManyTagsException **
The list of tags on the resource is over the limit. The maximum number of tags that can be applied to a resource is 50. Remove unused tags or reduce the number of tags in the request, and then try again.
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
<a name="API_CreateVoice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/polly-2016-06-10/CreateVoice)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/polly-2016-06-10/CreateVoice)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/polly-2016-06-10/CreateVoice)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/polly-2016-06-10/CreateVoice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/polly-2016-06-10/CreateVoice)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/polly-2016-06-10/CreateVoice)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/polly-2016-06-10/CreateVoice)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/polly-2016-06-10/CreateVoice)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/polly-2016-06-10/CreateVoice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/polly-2016-06-10/CreateVoice)
