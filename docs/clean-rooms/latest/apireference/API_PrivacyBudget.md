---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_PrivacyBudget.html
---

# PrivacyBudget
<a name="API_PrivacyBudget"></a>

The epsilon parameter value and number of each aggregation function that you can perform.

## Contents
<a name="API_PrivacyBudget_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** accessBudget **   <a name="API-Type-PrivacyBudget-accessBudget"></a>
Access budget information associated with this privacy budget.
Type: [AccessBudget](API_AccessBudget.md) object
Required: No

 ** differentialPrivacy **   <a name="API-Type-PrivacyBudget-differentialPrivacy"></a>
An object that specifies the epsilon parameter and the utility in terms of total aggregations, as well as the remaining aggregations available.
Type: [DifferentialPrivacyPrivacyBudget](API_DifferentialPrivacyPrivacyBudget.md) object
Required: No

## See Also
<a name="API_PrivacyBudget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/PrivacyBudget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/PrivacyBudget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/PrivacyBudget)
