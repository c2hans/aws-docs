---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_PrivacyBudgetTemplateParametersOutput.html
---

# PrivacyBudgetTemplateParametersOutput
<a name="API_PrivacyBudgetTemplateParametersOutput"></a>

The epsilon and noise parameters that were used in the privacy budget template.

## Contents
<a name="API_PrivacyBudgetTemplateParametersOutput_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** accessBudget **   <a name="API-Type-PrivacyBudgetTemplateParametersOutput-accessBudget"></a>
Access budget configuration returned from the privacy budget template, containing the configured access budget settings.
Type: [AccessBudgetsPrivacyTemplateParametersOutput](API_AccessBudgetsPrivacyTemplateParametersOutput.md) object
Required: No

 ** differentialPrivacy **   <a name="API-Type-PrivacyBudgetTemplateParametersOutput-differentialPrivacy"></a>
The epsilon and noise parameters.
Type: [DifferentialPrivacyTemplateParametersOutput](API_DifferentialPrivacyTemplateParametersOutput.md) object
Required: No

## See Also
<a name="API_PrivacyBudgetTemplateParametersOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/PrivacyBudgetTemplateParametersOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/PrivacyBudgetTemplateParametersOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/PrivacyBudgetTemplateParametersOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
