---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ExpressPrivateOfferConfigurationFilters.html
---

# ExpressPrivateOfferConfigurationFilters

The filter fields for the express private offer configuration entity.

## Contents
<a name="API_ExpressPrivateOfferConfigurationFilters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** EntityId **   <a name="AWSMarketplaceService-Type-ExpressPrivateOfferConfigurationFilters-EntityId"></a>
You can filter on the `EntityId` of an express private offer configuration.
Type: [ExpressPrivateOfferConfigurationEntityIdFilter](API_ExpressPrivateOfferConfigurationEntityIdFilter.md) object
Required: No

 ** ProductId **   <a name="AWSMarketplaceService-Type-ExpressPrivateOfferConfigurationFilters-ProductId"></a>
You can filter on the `ProductId` of an express private offer configuration.
Type: [ExpressPrivateOfferConfigurationProductIdFilter](API_ExpressPrivateOfferConfigurationProductIdFilter.md) object
Required: No

 ** State **   <a name="AWSMarketplaceService-Type-ExpressPrivateOfferConfigurationFilters-State"></a>
The state of the express private offer configuration to filter on. Valid values are the following:
+  `ACTIVE` – The configuration is active and you can use it to generate offers.
+  `INACTIVE` – The configuration is deprecated or deleted.
Type: [ExpressPrivateOfferConfigurationStateFilter](API_ExpressPrivateOfferConfigurationStateFilter.md) object
Required: No

## See Also
<a name="API_ExpressPrivateOfferConfigurationFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ExpressPrivateOfferConfigurationFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ExpressPrivateOfferConfigurationFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ExpressPrivateOfferConfigurationFilters)
