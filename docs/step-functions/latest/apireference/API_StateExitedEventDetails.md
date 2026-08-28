---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_StateExitedEventDetails.html
---

# StateExitedEventDetails
<a name="API_StateExitedEventDetails"></a>

Contains details about an exit from a state during an execution.

## Contents
<a name="API_StateExitedEventDetails_Contents"></a>

 ** name **   <a name="StepFunctions-Type-StateExitedEventDetails-name"></a>
The name of the state.
A name must *not* contain:
+ white space
+ brackets `< > { } [ ]`
+ wildcard characters `? *`
+ special characters `" # % \ ^ | ~ ` $ & , ; : /`
+ control characters (`U+0000-001F`, `U+007F-009F`, `U+FFFE-FFFF`)
+ surrogates (`U+D800-DFFF`)
+ invalid characters (` U+10FFFF`)
To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and \_.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Required: Yes

 ** assignedVariables **   <a name="StepFunctions-Type-StateExitedEventDetails-assignedVariables"></a>
Map of variable name and value as a serialized JSON representation.
Type: String to string map
Required: No

 ** assignedVariablesDetails **   <a name="StepFunctions-Type-StateExitedEventDetails-assignedVariablesDetails"></a>
Provides details about input or output in an execution history event.
Type: [AssignedVariablesDetails](API_AssignedVariablesDetails.md) object
Required: No

 ** output **   <a name="StepFunctions-Type-StateExitedEventDetails-output"></a>
The JSON output data of the state. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.
Type: String
Length Constraints: Maximum length of 262144.
Required: No

 ** outputDetails **   <a name="StepFunctions-Type-StateExitedEventDetails-outputDetails"></a>
Contains details about the output of an execution history event.
Type: [HistoryEventExecutionDataDetails](API_HistoryEventExecutionDataDetails.md) object
Required: No

## See Also
<a name="API_StateExitedEventDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/StateExitedEventDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/StateExitedEventDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/StateExitedEventDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Step Functions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query step-functions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
