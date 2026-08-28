---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_StepInput.html
---

# StepInput
<a name="API_StepInput"></a>

A map of key value pairs that is generated when you create a migration workflow. The key value pairs will differ based on your selection of the template.

## Contents
<a name="API_StepInput_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** integerValue **   <a name="migrationhuborchestrator-Type-StepInput-integerValue"></a>
The value of the integer.
Type: Integer
Required: No

 ** listOfStringsValue **   <a name="migrationhuborchestrator-Type-StepInput-listOfStringsValue"></a>
List of string values.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** mapOfStringValue **   <a name="migrationhuborchestrator-Type-StepInput-mapOfStringValue"></a>
Map of string values.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `[a-zA-Z0-9-_ ()]+`
Value Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

 ** stringValue **   <a name="migrationhuborchestrator-Type-StepInput-stringValue"></a>
String value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

## See Also
<a name="API_StepInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/StepInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/StepInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/StepInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Orchestrator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-orchestrator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
