---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_WorkflowStepOutputUnion.html
---

# WorkflowStepOutputUnion
<a name="API_WorkflowStepOutputUnion"></a>

A structure to hold multiple values of an output.

## Contents
<a name="API_WorkflowStepOutputUnion_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** integerValue **   <a name="migrationhuborchestrator-Type-WorkflowStepOutputUnion-integerValue"></a>
The integer value.
Type: Integer
Required: No

 ** listOfStringValue **   <a name="migrationhuborchestrator-Type-WorkflowStepOutputUnion-listOfStringValue"></a>
The list of string value.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** stringValue **   <a name="migrationhuborchestrator-Type-WorkflowStepOutputUnion-stringValue"></a>
The string value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## See Also
<a name="API_WorkflowStepOutputUnion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/WorkflowStepOutputUnion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/WorkflowStepOutputUnion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/WorkflowStepOutputUnion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Orchestrator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-orchestrator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
