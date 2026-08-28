---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_TaskExecutionListEntry.html
---

# TaskExecutionListEntry
<a name="API_TaskExecutionListEntry"></a>

Represents a single entry in a list of AWS DataSync task executions that's returned with the [ListTaskExecutions](https://docs.aws.amazon.com/datasync/latest/userguide/API_ListTaskExecutions.html) operation.

## Contents
<a name="API_TaskExecutionListEntry_Contents"></a>

 ** Status **   <a name="DataSync-Type-TaskExecutionListEntry-Status"></a>
The status of a task execution. For more information, see [Task execution statuses](https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses).
Type: String
Valid Values: `QUEUED | CANCELLING | LAUNCHING | PREPARING | TRANSFERRING | VERIFYING | SUCCESS | ERROR`
Required: No

 ** TaskExecutionArn **   <a name="DataSync-Type-TaskExecutionListEntry-TaskExecutionArn"></a>
The Amazon Resource Name (ARN) of a task execution.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:task/task-[0-9a-f]{17}/execution/exec-[0-9a-f]{17}$`
Required: No

 ** TaskMode **   <a name="DataSync-Type-TaskExecutionListEntry-TaskMode"></a>
The task mode that you're using. For more information, see [Choosing a task mode for your data transfer](https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html).
Type: String
Valid Values: `BASIC | ENHANCED`
Required: No

## See Also
<a name="API_TaskExecutionListEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/TaskExecutionListEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/TaskExecutionListEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/TaskExecutionListEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
