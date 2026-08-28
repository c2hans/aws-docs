---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_TaskScheduledEventDetails.html
---

# TaskScheduledEventDetails
<a name="API_TaskScheduledEventDetails"></a>

Contains details about a task scheduled during an execution.

## Contents
<a name="API_TaskScheduledEventDetails_Contents"></a>

 ** parameters **   <a name="StepFunctions-Type-TaskScheduledEventDetails-parameters"></a>
The JSON data passed to the resource referenced in a task state. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 262144.
Required: Yes

 ** region **   <a name="StepFunctions-Type-TaskScheduledEventDetails-region"></a>
The region of the scheduled task
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Required: Yes

 ** resource **   <a name="StepFunctions-Type-TaskScheduledEventDetails-resource"></a>
The action of the resource called by a task state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Required: Yes

 ** resourceType **   <a name="StepFunctions-Type-TaskScheduledEventDetails-resourceType"></a>
The service name of the resource in a task state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Required: Yes

 ** heartbeatInSeconds **   <a name="StepFunctions-Type-TaskScheduledEventDetails-heartbeatInSeconds"></a>
The maximum allowed duration between two heartbeats for the task.
Type: Long
Required: No

 ** taskCredentials **   <a name="StepFunctions-Type-TaskScheduledEventDetails-taskCredentials"></a>
The credentials that Step Functions uses for the task.
Type: [TaskCredentials](API_TaskCredentials.md) object
Required: No

 ** timeoutInSeconds **   <a name="StepFunctions-Type-TaskScheduledEventDetails-timeoutInSeconds"></a>
The maximum allowed duration of the task.
Type: Long
Required: No

## See Also
<a name="API_TaskScheduledEventDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/TaskScheduledEventDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/TaskScheduledEventDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/TaskScheduledEventDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Step Functions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query step-functions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
