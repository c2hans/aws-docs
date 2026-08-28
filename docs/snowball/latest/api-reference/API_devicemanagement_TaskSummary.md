---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_devicemanagement_TaskSummary.html
---

# TaskSummary
<a name="API_devicemanagement_TaskSummary"></a>

Information about the task assigned to one or many devices.

## Contents
<a name="API_devicemanagement_TaskSummary_Contents"></a>

 ** taskId **   <a name="Snowball-Type-devicemanagement_TaskSummary-taskId"></a>
The task ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** state **   <a name="Snowball-Type-devicemanagement_TaskSummary-state"></a>
The state of the task assigned to one or many devices.
Type: String
Valid Values: `IN_PROGRESS | CANCELED | COMPLETED`
Required: No

 ** tags **   <a name="Snowball-Type-devicemanagement_TaskSummary-tags"></a>
Optional metadata that you assign to a resource. You can use tags to categorize a resource in different ways, such as by purpose, owner, or environment.
Type: String to string map
Required: No

 ** taskArn **   <a name="Snowball-Type-devicemanagement_TaskSummary-taskArn"></a>
The Amazon Resource Name (ARN) of the task.
Type: String
Required: No

## See Also
<a name="API_devicemanagement_TaskSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snow-device-management-2021-08-04/TaskSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snow-device-management-2021-08-04/TaskSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snow-device-management-2021-08-04/TaskSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
