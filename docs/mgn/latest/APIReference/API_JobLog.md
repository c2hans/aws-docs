---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_JobLog.html
---

# JobLog
<a name="API_JobLog"></a>

Job log.

## Contents
<a name="API_JobLog_Contents"></a>

 ** event **   <a name="mgn-Type-JobLog-event"></a>
Job log event.
Type: String
Valid Values: `JOB_START | SERVER_SKIPPED | CLEANUP_START | CLEANUP_END | CLEANUP_FAIL | SNAPSHOT_START | SNAPSHOT_END | SNAPSHOT_FAIL | USING_PREVIOUS_SNAPSHOT | CONVERSION_START | CONVERSION_END | CONVERSION_FAIL | LAUNCH_START | LAUNCH_FAILED | JOB_CANCEL | JOB_END`
Required: No

 ** eventData **   <a name="mgn-Type-JobLog-eventData"></a>
Job event data
Type: [JobLogEventData](API_JobLogEventData.md) object
Required: No

 ** logDateTime **   <a name="mgn-Type-JobLog-logDateTime"></a>
Job log event date and time.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

## See Also
<a name="API_JobLog_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/JobLog)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/JobLog)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/JobLog)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
