---
source_url: https://docs.aws.amazon.com/voiceid/latest/APIReference/API_SpeakerEnrollmentJobSummary.html
---

# SpeakerEnrollmentJobSummary
<a name="API_connect-voice-id_SpeakerEnrollmentJobSummary"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

Contains a summary of information about a speaker enrollment job.

## Contents
<a name="API_connect-voice-id_SpeakerEnrollmentJobSummary_Contents"></a>

 ** CreatedAt **   <a name="connect-Type-connect-voice-id_SpeakerEnrollmentJobSummary-CreatedAt"></a>
A timestamp of when of the speaker enrollment job was created.
Type: Timestamp
Required: No

 ** DomainId **   <a name="connect-Type-connect-voice-id_SpeakerEnrollmentJobSummary-DomainId"></a>
The identifier of the domain that contains the speaker enrollment job.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: No

 ** EndedAt **   <a name="connect-Type-connect-voice-id_SpeakerEnrollmentJobSummary-EndedAt"></a>
A timestamp of when the speaker enrollment job ended.
Type: Timestamp
Required: No

 ** FailureDetails **   <a name="connect-Type-connect-voice-id_SpeakerEnrollmentJobSummary-FailureDetails"></a>
Contains details that are populated when an entire batch job fails. In cases of individual registration job failures, the batch job as a whole doesn't fail; it is completed with a `JobStatus` of `COMPLETED_WITH_ERRORS`. You can use the job output file to identify the individual registration requests that failed.
Type: [FailureDetails](API_connect-voice-id_FailureDetails.md) object
Required: No

 ** JobId **   <a name="connect-Type-connect-voice-id_SpeakerEnrollmentJobSummary-JobId"></a>
The service-generated identifier for the speaker enrollment job.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: No

 ** JobName **   <a name="connect-Type-connect-voice-id_SpeakerEnrollmentJobSummary-JobName"></a>
The client-provided name for the speaker enrollment job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: No

 ** JobProgress **   <a name="connect-Type-connect-voice-id_SpeakerEnrollmentJobSummary-JobProgress"></a>
Provides details regarding job progress. This field shows the completed percentage of enrollment requests listed in the input file.
Type: [JobProgress](API_connect-voice-id_JobProgress.md) object
Required: No

 ** JobStatus **   <a name="connect-Type-connect-voice-id_SpeakerEnrollmentJobSummary-JobStatus"></a>
The current status of the speaker enrollment job.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | FAILED`
Required: No

## See Also
<a name="API_connect-voice-id_SpeakerEnrollmentJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/SpeakerEnrollmentJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/SpeakerEnrollmentJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/SpeakerEnrollmentJobSummary)
