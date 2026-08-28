---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_EstimatedTaxes.html
---

# EstimatedTaxes
<a name="API_marketplace-agreements_EstimatedTaxes"></a>

Provides an aggregated view of estimated tax information.

## Contents
<a name="API_marketplace-agreements_EstimatedTaxes_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** breakdown **   <a name="AWSMarketplaceService-Type-marketplace-agreements_EstimatedTaxes-breakdown"></a>
A list of tax breakdown information.
Type: Array of [TaxBreakdownItem](API_marketplace-agreements_TaxBreakdownItem.md) objects
Required: No

 ** totalAmount **   <a name="AWSMarketplaceService-Type-marketplace-agreements_EstimatedTaxes-totalAmount"></a>
The total amount of tax aggregated from the tax breakdown.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

## See Also
<a name="API_marketplace-agreements_EstimatedTaxes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/EstimatedTaxes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/EstimatedTaxes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/EstimatedTaxes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
