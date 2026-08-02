---
source_url: https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_ParentSavingsPlanOffering.html
---

# ParentSavingsPlanOffering
<a name="API_ParentSavingsPlanOffering"></a>

Information about a Savings Plan offering.

## Contents
<a name="API_ParentSavingsPlanOffering_Contents"></a>

 ** currency **   <a name="savingsplans-Type-ParentSavingsPlanOffering-currency"></a>
The currency.
Type: String
Valid Values: `CNY | USD | EUR`
Required: No

 ** durationSeconds **   <a name="savingsplans-Type-ParentSavingsPlanOffering-durationSeconds"></a>
The duration, in seconds.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** offeringId **   <a name="savingsplans-Type-ParentSavingsPlanOffering-offeringId"></a>
The ID of the offering.
Type: String
Pattern: `[a-f0-9]+(-[a-f0-9]+)*`
Required: No

 ** paymentOption **   <a name="savingsplans-Type-ParentSavingsPlanOffering-paymentOption"></a>
The payment option.
Type: String
Valid Values: `All Upfront | Partial Upfront | No Upfront`
Required: No

 ** planDescription **   <a name="savingsplans-Type-ParentSavingsPlanOffering-planDescription"></a>
The description.
Type: String
Pattern: `^[a-zA-Z0-9_\- ]+$`
Required: No

 ** planType **   <a name="savingsplans-Type-ParentSavingsPlanOffering-planType"></a>
The plan type.
Type: String
Valid Values: `Compute | EC2Instance | SageMaker | Database`
Required: No

## See Also
<a name="API_ParentSavingsPlanOffering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/savingsplans-2019-06-28/ParentSavingsPlanOffering)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/savingsplans-2019-06-28/ParentSavingsPlanOffering)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/savingsplans-2019-06-28/ParentSavingsPlanOffering)
