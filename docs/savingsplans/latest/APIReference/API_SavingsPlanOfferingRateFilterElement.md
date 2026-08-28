---
source_url: https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_SavingsPlanOfferingRateFilterElement.html
---

# SavingsPlanOfferingRateFilterElement
<a name="API_SavingsPlanOfferingRateFilterElement"></a>

Information about a Savings Plan offering rate filter.

## Contents
<a name="API_SavingsPlanOfferingRateFilterElement_Contents"></a>

 ** name **   <a name="savingsplans-Type-SavingsPlanOfferingRateFilterElement-name"></a>
The filter name.
Type: String
Valid Values: `region | instanceFamily | instanceType | productDescription | tenancy | productId`
Required: No

 ** values **   <a name="savingsplans-Type-SavingsPlanOfferingRateFilterElement-values"></a>
The filter values.
Type: Array of strings
Pattern: `^[a-zA-Z0-9_ \/.\:\-\(\)]+$`
Required: No

## See Also
<a name="API_SavingsPlanOfferingRateFilterElement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/savingsplans-2019-06-28/SavingsPlanOfferingRateFilterElement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/savingsplans-2019-06-28/SavingsPlanOfferingRateFilterElement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/savingsplans-2019-06-28/SavingsPlanOfferingRateFilterElement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Savings Plans. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query savingsplans` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
