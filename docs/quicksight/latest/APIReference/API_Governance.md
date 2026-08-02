---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Governance.html
---

# Governance
<a name="API_Governance"></a>

Contains the governance configuration for a custom permissions profile. When governance controls are defined for a category, any capabilities in that category not explicitly set to `ALLOW` in `Capabilities` are denied. Even newly added capabilities in the category are implicitly disabled when Amazon Quick releases them.

## Contents
<a name="API_Governance_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DefaultCategoryEffects **   <a name="QS-Type-Governance-DefaultCategoryEffects"></a>
A map of `DefaultCategoryEffects`.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Valid Values: `DENY_BY_DEFAULT`
Required: No

## See Also
<a name="API_Governance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/Governance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/Governance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/Governance)
