---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_PricingModel.html
---

# PricingModel
<a name="API_marketplace-discovery_PricingModel"></a>

A pricing model that determines how buyers are charged for a listing, such as usage-based, contract, BYOL, or free.

## Contents
<a name="API_marketplace-discovery_PricingModel_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** displayName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PricingModel-displayName"></a>
The human-readable name of the pricing model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

 ** pricingModelType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PricingModel-pricingModelType"></a>
The machine-readable type of the pricing model.
Type: String
Valid Values: `USAGE | CONTRACT | BYOL | FREE`
Required: Yes

## See Also
<a name="API_marketplace-discovery_PricingModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/PricingModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/PricingModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/PricingModel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
