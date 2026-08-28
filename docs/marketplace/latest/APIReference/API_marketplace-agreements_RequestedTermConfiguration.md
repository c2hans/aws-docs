---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_RequestedTermConfiguration.html
---

# RequestedTermConfiguration
<a name="API_marketplace-agreements_RequestedTermConfiguration"></a>

A tagged union that represents the term configuration provided by the acceptor. Only one configuration is accepted per term.

## Contents
<a name="API_marketplace-agreements_RequestedTermConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** configurableUpfrontPricingTermConfiguration **   <a name="AWSMarketplaceService-Type-marketplace-agreements_RequestedTermConfiguration-configurableUpfrontPricingTermConfiguration"></a>
Defines a prepaid payment model that allows buyers to configure the entitlements they want to purchase and the duration.
Type: [ConfigurableUpfrontPricingTermConfiguration](API_marketplace-agreements_ConfigurableUpfrontPricingTermConfiguration.md) object
Required: No

 ** renewalTermConfiguration **   <a name="AWSMarketplaceService-Type-marketplace-agreements_RequestedTermConfiguration-renewalTermConfiguration"></a>
Additional parameters specified by the acceptor while accepting the term.
Type: [RenewalTermConfiguration](API_marketplace-agreements_RenewalTermConfiguration.md) object
Required: No

 ** variablePaymentTermConfiguration **   <a name="AWSMarketplaceService-Type-marketplace-agreements_RequestedTermConfiguration-variablePaymentTermConfiguration"></a>
Additional parameters specified by the acceptor while accepting the variable payment term.
Type: [VariablePaymentTermConfiguration](API_marketplace-agreements_VariablePaymentTermConfiguration.md) object
Required: No

## See Also
<a name="API_marketplace-agreements_RequestedTermConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/RequestedTermConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/RequestedTermConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/RequestedTermConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
