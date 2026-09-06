---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-voice-id_StartSpeakerEnrollmentJob.html
---

# StartSpeakerEnrollmentJob
<a name="API_connect-voice-id_StartSpeakerEnrollmentJob"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

Starts a new batch speaker enrollment job using specified details.

## Request Syntax
<a name="API_connect-voice-id_StartSpeakerEnrollmentJob_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "DataAccessRoleArn": "{{string}}",
   "DomainId": "{{string}}",
   "EnrollmentConfig": {
      "ExistingEnrollmentAction": "{{string}}",
      "FraudDetectionConfig": {
         "FraudDetectionAction": "{{string}}",
         "RiskThreshold": {{number}},
         "WatchlistIds": [ "{{string}}" ]
      }
   },
   "InputDataConfig": {
      "S3Uri": "{{string}}"
   },
   "JobName": "{{string}}",
   "OutputDataConfig": {
      "KmsKeyId": "{{string}}",
      "S3Uri": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_connect-voice-id_StartSpeakerEnrollmentJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_connect-voice-id_StartSpeakerEnrollmentJob_RequestSyntax) **   <a name="connect-connect-voice-id_StartSpeakerEnrollmentJob-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]+`
Required: No

 ** [DataAccessRoleArn](#API_connect-voice-id_StartSpeakerEnrollmentJob_RequestSyntax) **   <a name="connect-connect-voice-id_StartSpeakerEnrollmentJob-request-DataAccessRoleArn"></a>
The IAM role Amazon Resource Name (ARN) that grants Voice ID permissions to access customer's buckets to read the input manifest file and write the job output file. Refer to [Batch enrollment using audio data from prior calls](https://docs.aws.amazon.com/connect/latest/adminguide/voiceid-batch-enrollment.html) for the permissions needed in this role.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
Required: Yes

 ** [DomainId](#API_connect-voice-id_StartSpeakerEnrollmentJob_RequestSyntax) **   <a name="connect-connect-voice-id_StartSpeakerEnrollmentJob-request-DomainId"></a>
The identifier of the domain that contains the speaker enrollment job and in which the speakers are enrolled.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: Yes

 ** [EnrollmentConfig](#API_connect-voice-id_StartSpeakerEnrollmentJob_RequestSyntax) **   <a name="connect-connect-voice-id_StartSpeakerEnrollmentJob-request-EnrollmentConfig"></a>
The enrollment config that contains details such as the action to take when a speaker is already enrolled in Voice ID or when a speaker is identified as a fraudster.
Type: [EnrollmentConfig](API_connect-voice-id_EnrollmentConfig.md) object
Required: No

 ** [InputDataConfig](#API_connect-voice-id_StartSpeakerEnrollmentJob_RequestSyntax) **   <a name="connect-connect-voice-id_StartSpeakerEnrollmentJob-request-InputDataConfig"></a>
The input data config containing the S3 location for the input manifest file that contains the list of speaker enrollment requests.
Type: [InputDataConfig](API_connect-voice-id_InputDataConfig.md) object
Required: Yes

 ** [JobName](#API_connect-voice-id_StartSpeakerEnrollmentJob_RequestSyntax) **   <a name="connect-connect-voice-id_StartSpeakerEnrollmentJob-request-JobName"></a>
A name for your speaker enrollment job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: No

 ** [OutputDataConfig](#API_connect-voice-id_StartSpeakerEnrollmentJob_RequestSyntax) **   <a name="connect-connect-voice-id_StartSpeakerEnrollmentJob-request-OutputDataConfig"></a>
The output data config containing the S3 location where Voice ID writes the job output file; you must also include a KMS key ID to encrypt the file.
Type: [OutputDataConfig](API_connect-voice-id_OutputDataConfig.md) object
Required: Yes

## Response Syntax
<a name="API_connect-voice-id_StartSpeakerEnrollmentJob_ResponseSyntax"></a>

```
{
   "Job": {
      "CreatedAt": number,
      "DataAccessRoleArn": "string",
      "DomainId": "string",
      "EndedAt": number,
      "EnrollmentConfig": {
         "ExistingEnrollmentAction": "string",
         "FraudDetectionConfig": {
            "FraudDetectionAction": "string",
            "RiskThreshold": number,
            "WatchlistIds": [ "string" ]
         }
      },
      "FailureDetails": {
         "Message": "string",
         "StatusCode": number
      },
      "InputDataConfig": {
         "S3Uri": "string"
      },
      "JobId": "string",
      "JobName": "string",
      "JobProgress": {
         "PercentComplete": number
      },
      "JobStatus": "string",
      "OutputDataConfig": {
         "KmsKeyId": "string",
         "S3Uri": "string"
      }
   }
}
```

## Response Elements
<a name="API_connect-voice-id_StartSpeakerEnrollmentJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Job](#API_connect-voice-id_StartSpeakerEnrollmentJob_ResponseSyntax) **   <a name="connect-connect-voice-id_StartSpeakerEnrollmentJob-response-Job"></a>
Details about the started speaker enrollment job.
Type: [SpeakerEnrollmentJob](API_connect-voice-id_SpeakerEnrollmentJob.md) object

## Errors
<a name="API_connect-voice-id_StartSpeakerEnrollmentJob_Errors"></a>

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
<a name="API_connect-voice-id_StartSpeakerEnrollmentJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/voice-id-2021-09-27/StartSpeakerEnrollmentJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/voice-id-2021-09-27/StartSpeakerEnrollmentJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/StartSpeakerEnrollmentJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/voice-id-2021-09-27/StartSpeakerEnrollmentJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/StartSpeakerEnrollmentJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/voice-id-2021-09-27/StartSpeakerEnrollmentJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/voice-id-2021-09-27/StartSpeakerEnrollmentJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/voice-id-2021-09-27/StartSpeakerEnrollmentJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/voice-id-2021-09-27/StartSpeakerEnrollmentJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/StartSpeakerEnrollmentJob)
