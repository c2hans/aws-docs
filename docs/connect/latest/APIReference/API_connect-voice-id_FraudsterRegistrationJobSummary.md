---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-voice-id_FraudsterRegistrationJobSummary.html
---

# FraudsterRegistrationJobSummary
<a name="API_connect-voice-id_FraudsterRegistrationJobSummary"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

Contains a summary of information about a fraudster registration job.

## Contents
<a name="API_connect-voice-id_FraudsterRegistrationJobSummary_Contents"></a>

 ** CreatedAt **   <a name="connect-Type-connect-voice-id_FraudsterRegistrationJobSummary-CreatedAt"></a>
A timestamp of when the fraudster registration job was created.
Type: Timestamp
Required: No

 ** DomainId **   <a name="connect-Type-connect-voice-id_FraudsterRegistrationJobSummary-DomainId"></a>
The identifier of the domain that contains the fraudster registration job.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: No

 ** EndedAt **   <a name="connect-Type-connect-voice-id_FraudsterRegistrationJobSummary-EndedAt"></a>
A timestamp of when the fraudster registration job ended.
Type: Timestamp
Required: No

 ** FailureDetails **   <a name="connect-Type-connect-voice-id_FraudsterRegistrationJobSummary-FailureDetails"></a>
Contains details that are populated when an entire batch job fails. In cases of individual registration job failures, the batch job as a whole doesn't fail; it is completed with a `JobStatus` of `COMPLETED_WITH_ERRORS`. You can use the job output file to identify the individual registration requests that failed.
Type: [FailureDetails](API_connect-voice-id_FailureDetails.md) object
Required: No

 ** JobId **   <a name="connect-Type-connect-voice-id_FraudsterRegistrationJobSummary-JobId"></a>
The service-generated identifier for the fraudster registration job.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: No

 ** JobName **   <a name="connect-Type-connect-voice-id_FraudsterRegistrationJobSummary-JobName"></a>
The client-provided name for the fraudster registration job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: No

 ** JobProgress **   <a name="connect-Type-connect-voice-id_FraudsterRegistrationJobSummary-JobProgress"></a>
Shows the completed percentage of registration requests listed in the input file.
Type: [JobProgress](API_connect-voice-id_JobProgress.md) object
Required: No

 ** JobStatus **   <a name="connect-Type-connect-voice-id_FraudsterRegistrationJobSummary-JobStatus"></a>
The current status of the fraudster registration job.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | FAILED`
Required: No

## See Also
<a name="API_connect-voice-id_FraudsterRegistrationJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/FraudsterRegistrationJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/FraudsterRegistrationJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/FraudsterRegistrationJobSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
