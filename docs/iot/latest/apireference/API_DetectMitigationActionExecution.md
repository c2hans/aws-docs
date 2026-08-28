---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DetectMitigationActionExecution.html
---

# DetectMitigationActionExecution
<a name="API_DetectMitigationActionExecution"></a>

 Describes which mitigation actions should be executed.

## Contents
<a name="API_DetectMitigationActionExecution_Contents"></a>

 ** actionName **   <a name="iot-Type-DetectMitigationActionExecution-actionName"></a>
 The friendly name that uniquely identifies the mitigation action.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** errorCode **   <a name="iot-Type-DetectMitigationActionExecution-errorCode"></a>
 The error code of a mitigation action.
Type: String
Required: No

 ** executionEndDate **   <a name="iot-Type-DetectMitigationActionExecution-executionEndDate"></a>
 The date a mitigation action ended.
Type: Timestamp
Required: No

 ** executionStartDate **   <a name="iot-Type-DetectMitigationActionExecution-executionStartDate"></a>
 The date a mitigation action was started.
Type: Timestamp
Required: No

 ** message **   <a name="iot-Type-DetectMitigationActionExecution-message"></a>
 The message of a mitigation action.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** status **   <a name="iot-Type-DetectMitigationActionExecution-status"></a>
 The status of a mitigation action.
Type: String
Valid Values: `IN_PROGRESS | SUCCESSFUL | FAILED | SKIPPED`
Required: No

 ** taskId **   <a name="iot-Type-DetectMitigationActionExecution-taskId"></a>
 The unique identifier of the task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** thingName **   <a name="iot-Type-DetectMitigationActionExecution-thingName"></a>
 The name of the thing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** violationId **   <a name="iot-Type-DetectMitigationActionExecution-violationId"></a>
 The unique identifier of the violation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

## See Also
<a name="API_DetectMitigationActionExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DetectMitigationActionExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DetectMitigationActionExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DetectMitigationActionExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
