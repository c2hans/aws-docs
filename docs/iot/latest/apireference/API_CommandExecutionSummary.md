---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CommandExecutionSummary.html
---

# CommandExecutionSummary
<a name="API_CommandExecutionSummary"></a>

Summary information about a particular command execution.

## Contents
<a name="API_CommandExecutionSummary_Contents"></a>

 ** commandArn **   <a name="iot-Type-CommandExecutionSummary-commandArn"></a>
The Amazon Resource Name (ARN) of the command execution.
Type: String
Required: No

 ** completedAt **   <a name="iot-Type-CommandExecutionSummary-completedAt"></a>
The date and time at which the command completed executing on the target device.
Type: Timestamp
Required: No

 ** createdAt **   <a name="iot-Type-CommandExecutionSummary-createdAt"></a>
The date and time at which the command execution was created for the target device.
Type: Timestamp
Required: No

 ** executionId **   <a name="iot-Type-CommandExecutionSummary-executionId"></a>
The unique identifier of the command execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** startedAt **   <a name="iot-Type-CommandExecutionSummary-startedAt"></a>
The date and time at which the command started executing on the target device.
Type: Timestamp
Required: No

 ** status **   <a name="iot-Type-CommandExecutionSummary-status"></a>
The status of the command executions.
Type: String
Valid Values: `CREATED | IN_PROGRESS | SUCCEEDED | FAILED | REJECTED | TIMED_OUT`
Required: No

 ** targetArn **   <a name="iot-Type-CommandExecutionSummary-targetArn"></a>
The Amazon Resource Name (ARN) of the target device for which the command is being executed.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

## See Also
<a name="API_CommandExecutionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CommandExecutionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CommandExecutionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CommandExecutionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
