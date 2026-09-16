---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-voice-id_CreateDomain.html
---

# CreateDomain
<a name="API_connect-voice-id_CreateDomain"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

Creates a domain that contains all Connect Customer Voice ID data, such as speakers, fraudsters, customer audio, and voiceprints. Every domain is created with a default watchlist that fraudsters can be a part of.

## Request Syntax
<a name="API_connect-voice-id_CreateDomain_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "Name": "{{string}}",
   "ServerSideEncryptionConfiguration": {
      "KmsKeyId": "{{string}}"
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_connect-voice-id_CreateDomain_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_connect-voice-id_CreateDomain_RequestSyntax) **   <a name="connect-connect-voice-id_CreateDomain-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]+`
Required: No

 ** [Description](#API_connect-voice-id_CreateDomain_RequestSyntax) **   <a name="connect-connect-voice-id_CreateDomain-request-Description"></a>
A brief description of this domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`
Required: No

 ** [Name](#API_connect-voice-id_CreateDomain_RequestSyntax) **   <a name="connect-connect-voice-id_CreateDomain-request-Name"></a>
The name of the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: Yes

 ** [ServerSideEncryptionConfiguration](#API_connect-voice-id_CreateDomain_RequestSyntax) **   <a name="connect-connect-voice-id_CreateDomain-request-ServerSideEncryptionConfiguration"></a>
The configuration, containing the KMS key identifier, to be used by Voice ID for the server-side encryption of your data. Refer to [ Connect Customer Voice ID encryption at rest](https://docs.aws.amazon.com/connect/latest/adminguide/encryption-at-rest.html#encryption-at-rest-voiceid) for more details on how the KMS key is used.
Type: [ServerSideEncryptionConfiguration](API_connect-voice-id_ServerSideEncryptionConfiguration.md) object
Required: Yes

 ** [Tags](#API_connect-voice-id_CreateDomain_RequestSyntax) **   <a name="connect-connect-voice-id_CreateDomain-request-Tags"></a>
A list of tags you want added to the domain.
Type: Array of [Tag](API_connect-voice-id_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_connect-voice-id_CreateDomain_ResponseSyntax"></a>

```
{
   "Domain": {
      "Arn": "string",
      "CreatedAt": number,
      "Description": "string",
      "DomainId": "string",
      "DomainStatus": "string",
      "Name": "string",
      "ServerSideEncryptionConfiguration": {
         "KmsKeyId": "string"
      },
      "ServerSideEncryptionUpdateDetails": {
         "Message": "string",
         "OldKmsKeyId": "string",
         "UpdateStatus": "string"
      },
      "UpdatedAt": number,
      "WatchlistDetails": {
         "DefaultWatchlistId": "string"
      }
   }
}
```

## Response Elements
<a name="API_connect-voice-id_CreateDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Domain](#API_connect-voice-id_CreateDomain_ResponseSyntax) **   <a name="connect-connect-voice-id_CreateDomain-response-Domain"></a>
Information about the newly created domain.
Type: [Domain](API_connect-voice-id_Domain.md) object

## Errors
<a name="API_connect-voice-id_CreateDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action. Check the error message and try again.
HTTP Status Code: 400

 ** ConflictException **
The request failed due to a conflict. Check the `ConflictType` and error message for more details.
 ** ConflictType **
The type of conflict which caused a ConflictException. Possible types and the corresponding error messages are as follows:
+  `DOMAIN_NOT_ACTIVE`: The domain is not active.
+  `CANNOT_CHANGE_SPEAKER_AFTER_ENROLLMENT`: You cannot change the speaker ID after an enrollment has been requested.
+  `ENROLLMENT_ALREADY_EXISTS`: There is already an enrollment for this session.
+  `SPEAKER_NOT_SET`: You must set the speaker ID before requesting an enrollment.
+  `SPEAKER_OPTED_OUT`: You cannot request an enrollment for an opted out speaker.
+  `CONCURRENT_CHANGES`: The request could not be processed as the resource was modified by another request during execution.
HTTP Status Code: 400

 ** InternalServerException **
The request failed due to an unknown error on the server side.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found. Check the `ResourceType` and error message for more details.
 ** ResourceType **
The type of resource which cannot not be found. Possible types are `BATCH_JOB`, `COMPLIANCE_CONSENT`, `DOMAIN`, `FRAUDSTER`, `SESSION` and `SPEAKER`.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
The request exceeded the service quota. Refer to [Voice ID Service Quotas](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#voiceid-quotas) and try your request again.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling. Please slow down your request rate. Refer to [ Connect Customer Voice ID Service API throttling quotas ](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas) and try your request again.
HTTP Status Code: 400

 ** ValidationException **
The request failed one or more validations; check the error message for more details.
HTTP Status Code: 400

## See Also
<a name="API_connect-voice-id_CreateDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/voice-id-2021-09-27/CreateDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/voice-id-2021-09-27/CreateDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/CreateDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/voice-id-2021-09-27/CreateDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/CreateDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/voice-id-2021-09-27/CreateDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/voice-id-2021-09-27/CreateDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/voice-id-2021-09-27/CreateDomain)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/voice-id-2021-09-27/CreateDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/CreateDomain)
