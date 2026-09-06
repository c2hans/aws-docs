---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_PrivacyBudgetTemplateUpdateParameters.html
---

# PrivacyBudgetTemplateUpdateParameters
<a name="API_PrivacyBudgetTemplateUpdateParameters"></a>

The epsilon and noise parameters that you want to update in the privacy budget template.

## Contents
<a name="API_PrivacyBudgetTemplateUpdateParameters_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** accessBudget **   <a name="API-Type-PrivacyBudgetTemplateUpdateParameters-accessBudget"></a>
 The new access budget configuration that completely replaces the existing access budget settings in the privacy budget template.
Type: [AccessBudgetsPrivacyTemplateUpdateParameters](API_AccessBudgetsPrivacyTemplateUpdateParameters.md) object
Required: No

 ** differentialPrivacy **   <a name="API-Type-PrivacyBudgetTemplateUpdateParameters-differentialPrivacy"></a>
An object that specifies the new values for the epsilon and noise parameters.
Type: [DifferentialPrivacyTemplateUpdateParameters](API_DifferentialPrivacyTemplateUpdateParameters.md) object
Required: No

## See Also
<a name="API_PrivacyBudgetTemplateUpdateParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/PrivacyBudgetTemplateUpdateParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/PrivacyBudgetTemplateUpdateParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/PrivacyBudgetTemplateUpdateParameters)
