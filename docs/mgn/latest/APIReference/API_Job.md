---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_Job.html
---

# Job
<a name="API_Job"></a>

Job.

## Contents
<a name="API_Job_Contents"></a>

 ** jobID **   <a name="mgn-Type-Job-jobID"></a>
Job ID.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `mgnjob-[0-9a-zA-Z]{17}`
Required: Yes

 ** arn **   <a name="mgn-Type-Job-arn"></a>
the ARN of the specific Job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** creationDateTime **   <a name="mgn-Type-Job-creationDateTime"></a>
Job creation time.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** endDateTime **   <a name="mgn-Type-Job-endDateTime"></a>
Job end time.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** initiatedBy **   <a name="mgn-Type-Job-initiatedBy"></a>
Job initiated by field.
Type: String
Valid Values: `START_TEST | START_CUTOVER | DIAGNOSTIC | TERMINATE`
Required: No

 ** participatingServers **   <a name="mgn-Type-Job-participatingServers"></a>
Servers participating in a specific Job.
Type: Array of [ParticipatingServer](API_ParticipatingServer.md) objects
Required: No

 ** status **   <a name="mgn-Type-Job-status"></a>
Job status.
Type: String
Valid Values: `PENDING | STARTED | COMPLETED`
Required: No

 ** tags **   <a name="mgn-Type-Job-tags"></a>
Tags associated with specific Job.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** type **   <a name="mgn-Type-Job-type"></a>
Job type.
Type: String
Valid Values: `LAUNCH | TERMINATE`
Required: No

## See Also
<a name="API_Job_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/Job)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/Job)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/Job)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
