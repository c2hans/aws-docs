---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_AccessBudgetsPrivacyTemplateParametersInput.html
---

# AccessBudgetsPrivacyTemplateParametersInput
<a name="API_AccessBudgetsPrivacyTemplateParametersInput"></a>

Input parameters for privacy budget templates that support access budgets functionality, enabling enhanced budget management capabilities.

## Contents
<a name="API_AccessBudgetsPrivacyTemplateParametersInput_Contents"></a>

 ** budgetParameters **   <a name="API-Type-AccessBudgetsPrivacyTemplateParametersInput-budgetParameters"></a>
An array of budget parameters that define the access budget configuration for the privacy template.
Type: Array of [BudgetParameter](API_BudgetParameter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: Yes

 ** resourceArn **   <a name="API-Type-AccessBudgetsPrivacyTemplateParametersInput-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource associated with this privacy budget template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/(configuredtableassociation|intermediatetable)/[\d\w-]+`
Required: Yes

## See Also
<a name="API_AccessBudgetsPrivacyTemplateParametersInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/AccessBudgetsPrivacyTemplateParametersInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/AccessBudgetsPrivacyTemplateParametersInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/AccessBudgetsPrivacyTemplateParametersInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
