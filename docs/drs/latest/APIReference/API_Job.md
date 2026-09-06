---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_Job.html
---

# Job
<a name="API_Job"></a>

A job is an asynchronous workflow.

## Contents
<a name="API_Job_Contents"></a>

 ** jobID **   <a name="drs-Type-Job-jobID"></a>
The ID of the Job.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `drsjob-[0-9a-zA-Z]{17}`
Required: Yes

 ** arn **   <a name="drs-Type-Job-arn"></a>
The ARN of a Job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.{16,2044}`
Required: No

 ** creationDateTime **   <a name="drs-Type-Job-creationDateTime"></a>
The date and time of when the Job was created.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** endDateTime **   <a name="drs-Type-Job-endDateTime"></a>
The date and time of when the Job ended.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** initiatedBy **   <a name="drs-Type-Job-initiatedBy"></a>
A string representing who initiated the Job.
Type: String
Valid Values: `START_RECOVERY | START_DRILL | FAILBACK | DIAGNOSTIC | TERMINATE_RECOVERY_INSTANCES | TARGET_ACCOUNT | CREATE_NETWORK_RECOVERY | UPDATE_NETWORK_RECOVERY | ASSOCIATE_NETWORK_RECOVERY`
Required: No

 ** participatingResources **   <a name="drs-Type-Job-participatingResources"></a>
A list of resources that the Job is acting upon.
Type: Array of [ParticipatingResource](API_ParticipatingResource.md) objects
Required: No

 ** participatingServers **   <a name="drs-Type-Job-participatingServers"></a>
A list of servers that the Job is acting upon.
Type: Array of [ParticipatingServer](API_ParticipatingServer.md) objects
Required: No

 ** status **   <a name="drs-Type-Job-status"></a>
The status of the Job.
Type: String
Valid Values: `PENDING | STARTED | COMPLETED`
Required: No

 ** tags **   <a name="drs-Type-Job-tags"></a>
A list of tags associated with the Job.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** type **   <a name="drs-Type-Job-type"></a>
The type of the Job.
Type: String
Valid Values: `LAUNCH | TERMINATE | CREATE_CONVERTED_SNAPSHOT`
Required: No

## See Also
<a name="API_Job_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/Job)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/Job)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/Job)
