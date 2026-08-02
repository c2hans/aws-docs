---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-voice-id_SpeakerEnrollmentJob.html
---

# SpeakerEnrollmentJob
<a name="API_connect-voice-id_SpeakerEnrollmentJob"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

Contains all the information about a speaker enrollment job.

## Contents
<a name="API_connect-voice-id_SpeakerEnrollmentJob_Contents"></a>

 ** CreatedAt **   <a name="connect-Type-connect-voice-id_SpeakerEnrollmentJob-CreatedAt"></a>
A timestamp of when the speaker enrollment job was created.
Type: Timestamp
Required: No

 ** DataAccessRoleArn **   <a name="connect-Type-connect-voice-id_SpeakerEnrollmentJob-DataAccessRoleArn"></a>
The IAM role Amazon Resource Name (ARN) that grants Voice ID permissions to access customer's buckets to read the input manifest file and write the job output file.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
Required: No

 ** DomainId **   <a name="connect-Type-connect-voice-id_SpeakerEnrollmentJob-DomainId"></a>
The identifier of the domain that contains the speaker enrollment job.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: No

 ** EndedAt **   <a name="connect-Type-connect-voice-id_SpeakerEnrollmentJob-EndedAt"></a>
A timestamp of when the speaker enrollment job ended.
Type: Timestamp
Required: No

 ** EnrollmentConfig **   <a name="connect-Type-connect-voice-id_SpeakerEnrollmentJob-EnrollmentConfig"></a>
The configuration that defines the action to take when the speaker is already enrolled in Voice ID, and the `FraudDetectionConfig` to use.
Type: [EnrollmentConfig](API_connect-voice-id_EnrollmentConfig.md) object
Required: No

 ** FailureDetails **   <a name="connect-Type-connect-voice-id_SpeakerEnrollmentJob-FailureDetails"></a>
Contains details that are populated when an entire batch job fails. In cases of individual registration job failures, the batch job as a whole doesn't fail; it is completed with a `JobStatus` of `COMPLETED_WITH_ERRORS`. You can use the job output file to identify the individual registration requests that failed.
Type: [FailureDetails](API_connect-voice-id_FailureDetails.md) object
Required: No

 ** InputDataConfig **   <a name="connect-Type-connect-voice-id_SpeakerEnrollmentJob-InputDataConfig"></a>
The input data config containing an S3 URI for the input manifest file that contains the list of speaker enrollment job requests.
Type: [InputDataConfig](API_connect-voice-id_InputDataConfig.md) object
Required: No

 ** JobId **   <a name="connect-Type-connect-voice-id_SpeakerEnrollmentJob-JobId"></a>
The service-generated identifier for the speaker enrollment job.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: No

 ** JobName **   <a name="connect-Type-connect-voice-id_SpeakerEnrollmentJob-JobName"></a>
The client-provided name for the speaker enrollment job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: No

 ** JobProgress **   <a name="connect-Type-connect-voice-id_SpeakerEnrollmentJob-JobProgress"></a>
Provides details on job progress. This field shows the completed percentage of registration requests listed in the input file.
Type: [JobProgress](API_connect-voice-id_JobProgress.md) object
Required: No

 ** JobStatus **   <a name="connect-Type-connect-voice-id_SpeakerEnrollmentJob-JobStatus"></a>
The current status of the speaker enrollment job.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | FAILED`
Required: No

 ** OutputDataConfig **   <a name="connect-Type-connect-voice-id_SpeakerEnrollmentJob-OutputDataConfig"></a>
The output data config containing the S3 location where Voice ID writes the job output file; you must also include a KMS key ID to encrypt the file.
Type: [OutputDataConfig](API_connect-voice-id_OutputDataConfig.md) object
Required: No

## See Also
<a name="API_connect-voice-id_SpeakerEnrollmentJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/SpeakerEnrollmentJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/SpeakerEnrollmentJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/SpeakerEnrollmentJob)
