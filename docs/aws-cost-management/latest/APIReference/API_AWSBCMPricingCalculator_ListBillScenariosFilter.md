---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_ListBillScenariosFilter.html
---

# ListBillScenariosFilter
<a name="API_AWSBCMPricingCalculator_ListBillScenariosFilter"></a>

 Represents a filter for listing bill scenarios.

## Contents
<a name="API_AWSBCMPricingCalculator_ListBillScenariosFilter_Contents"></a>

 ** name **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_ListBillScenariosFilter-name"></a>
 The name of the filter attribute.
Type: String
Valid Values: `STATUS | NAME | GROUP_SHARING_PREFERENCE | COST_CATEGORY_ARN`
Required: Yes

 ** values **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_ListBillScenariosFilter-values"></a>
 The values to filter by.
Type: Array of strings
Required: Yes

 ** matchOption **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_ListBillScenariosFilter-matchOption"></a>
 The match option for the filter (e.g., equals, contains).
Type: String
Valid Values: `EQUALS | STARTS_WITH | CONTAINS`
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_ListBillScenariosFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/ListBillScenariosFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/ListBillScenariosFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/ListBillScenariosFilter)
