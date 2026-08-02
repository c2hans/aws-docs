---
source_url: https://docs.aws.amazon.com/voiceid/latest/APIReference/API_FraudsterRegistrationJob.html
---

# FraudsterRegistrationJob
<a name="API_connect-voice-id_FraudsterRegistrationJob"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

Contains all the information about a fraudster registration job.

## Contents
<a name="API_connect-voice-id_FraudsterRegistrationJob_Contents"></a>

 ** CreatedAt **   <a name="connect-Type-connect-voice-id_FraudsterRegistrationJob-CreatedAt"></a>
A timestamp of when the fraudster registration job was created.
Type: Timestamp
Required: No

 ** DataAccessRoleArn **   <a name="connect-Type-connect-voice-id_FraudsterRegistrationJob-DataAccessRoleArn"></a>
The IAM role Amazon Resource Name (ARN) that grants Voice ID permissions to access customer's buckets to read the input manifest file and write the job output file.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
Required: No

 ** DomainId **   <a name="connect-Type-connect-voice-id_FraudsterRegistrationJob-DomainId"></a>
The identifier of the domain that contains the fraudster registration job.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: No

 ** EndedAt **   <a name="connect-Type-connect-voice-id_FraudsterRegistrationJob-EndedAt"></a>
A timestamp of when the fraudster registration job ended.
Type: Timestamp
Required: No

 ** FailureDetails **   <a name="connect-Type-connect-voice-id_FraudsterRegistrationJob-FailureDetails"></a>
Contains details that are populated when an entire batch job fails. In cases of individual registration job failures, the batch job as a whole doesn't fail; it is completed with a `JobStatus` of `COMPLETED_WITH_ERRORS`. You can use the job output file to identify the individual registration requests that failed.
Type: [FailureDetails](API_connect-voice-id_FailureDetails.md) object
Required: No

 ** InputDataConfig **   <a name="connect-Type-connect-voice-id_FraudsterRegistrationJob-InputDataConfig"></a>
The input data config containing an S3 URI for the input manifest file that contains the list of fraudster registration job requests.
Type: [InputDataConfig](API_connect-voice-id_InputDataConfig.md) object
Required: No

 ** JobId **   <a name="connect-Type-connect-voice-id_FraudsterRegistrationJob-JobId"></a>
The service-generated identifier for the fraudster registration job.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: No

 ** JobName **   <a name="connect-Type-connect-voice-id_FraudsterRegistrationJob-JobName"></a>
The client-provided name for the fraudster registration job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: No

 ** JobProgress **   <a name="connect-Type-connect-voice-id_FraudsterRegistrationJob-JobProgress"></a>
Shows the completed percentage of registration requests listed in the input file.
Type: [JobProgress](API_connect-voice-id_JobProgress.md) object
Required: No

 ** JobStatus **   <a name="connect-Type-connect-voice-id_FraudsterRegistrationJob-JobStatus"></a>
The current status of the fraudster registration job.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | FAILED`
Required: No

 ** OutputDataConfig **   <a name="connect-Type-connect-voice-id_FraudsterRegistrationJob-OutputDataConfig"></a>
The output data config containing the S3 location where you want Voice ID to write your job output file; you must also include a KMS key ID in order to encrypt the file.
Type: [OutputDataConfig](API_connect-voice-id_OutputDataConfig.md) object
Required: No

 ** RegistrationConfig **   <a name="connect-Type-connect-voice-id_FraudsterRegistrationJob-RegistrationConfig"></a>
The registration config containing details such as the action to take when a duplicate fraudster is detected, and the similarity threshold to use for detecting a duplicate fraudster.
Type: [RegistrationConfig](API_connect-voice-id_RegistrationConfig.md) object
Required: No

## See Also
<a name="API_connect-voice-id_FraudsterRegistrationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/FraudsterRegistrationJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/FraudsterRegistrationJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/FraudsterRegistrationJob)
