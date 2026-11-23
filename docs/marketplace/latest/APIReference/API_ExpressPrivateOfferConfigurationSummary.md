---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ExpressPrivateOfferConfigurationSummary.html
---

# ExpressPrivateOfferConfigurationSummary

Summarized information about an express private offer configuration.

## Contents
<a name="API_ExpressPrivateOfferConfigurationSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ProductId **   <a name="AWSMarketplaceService-Type-ExpressPrivateOfferConfigurationSummary-ProductId"></a>
The product ID associated with the express private offer configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9][.a-zA-Z0-9/-]+[a-zA-Z0-9]$`
Required: No

 ** State **   <a name="AWSMarketplaceService-Type-ExpressPrivateOfferConfigurationSummary-State"></a>
The state of the express private offer configuration. Valid values are the following:
+  `ACTIVE` – The configuration is active and you can use it to generate offers.
+  `INACTIVE` – The configuration is deprecated or deleted.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

## See Also
<a name="API_ExpressPrivateOfferConfigurationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ExpressPrivateOfferConfigurationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ExpressPrivateOfferConfigurationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ExpressPrivateOfferConfigurationSummary)
