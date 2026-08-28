---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_RemediationExecutionStep.html
---

# RemediationExecutionStep
<a name="API_RemediationExecutionStep"></a>

Name of the step from the SSM document.

## Contents
<a name="API_RemediationExecutionStep_Contents"></a>

 ** ErrorMessage **   <a name="config-Type-RemediationExecutionStep-ErrorMessage"></a>
An error message if the step was interrupted during execution.
Type: String
Required: No

 ** Name **   <a name="config-Type-RemediationExecutionStep-Name"></a>
The details of the step.
Type: String
Required: No

 ** StartTime **   <a name="config-Type-RemediationExecutionStep-StartTime"></a>
The time when the step started.
Type: Timestamp
Required: No

 ** State **   <a name="config-Type-RemediationExecutionStep-State"></a>
The valid status of the step.
Type: String
Valid Values: `SUCCEEDED | PENDING | FAILED | IN_PROGRESS | EXITED | UNKNOWN`
Required: No

 ** StopTime **   <a name="config-Type-RemediationExecutionStep-StopTime"></a>
The time when the step stopped.
Type: Timestamp
Required: No

## See Also
<a name="API_RemediationExecutionStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/RemediationExecutionStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/RemediationExecutionStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/RemediationExecutionStep)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
