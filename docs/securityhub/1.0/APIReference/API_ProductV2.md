---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ProductV2.html
---

# ProductV2
<a name="API_ProductV2"></a>

Defines the structure for the productV2.

## Contents
<a name="API_ProductV2_Contents"></a>

 ** ActivationUrl **   <a name="securityhub-Type-ProductV2-ActivationUrl"></a>
The URL to the serviceV@ or productV2 documentation about the integration, which includes how to activate the integration.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Categories **   <a name="securityhub-Type-ProductV2-Categories"></a>
The domains or functional areas the productV2 addresses.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** CompanyName **   <a name="securityhub-Type-ProductV2-CompanyName"></a>
The name of the organization or vendor that provides the productV2.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Description **   <a name="securityhub-Type-ProductV2-Description"></a>
Detailed information about the productV2.
Type: String
Pattern: `.*\S.*`
Required: No

 ** IntegrationV2Types **   <a name="securityhub-Type-ProductV2-IntegrationV2Types"></a>
The type of integration.
Type: Array of strings
Valid Values: `SEND_FINDINGS_TO_SECURITY_HUB | RECEIVE_FINDINGS_FROM_SECURITY_HUB | UPDATE_FINDINGS_IN_SECURITY_HUB | EXTENDED_PLAN`
Required: No

 ** MarketplaceProductId **   <a name="securityhub-Type-ProductV2-MarketplaceProductId"></a>
The identifier for the AWS Marketplace product associated with this integration.
Type: String
Pattern: `.*\S.*`
Required: No

 ** MarketplaceUrl **   <a name="securityhub-Type-ProductV2-MarketplaceUrl"></a>
The console URL where you can purchase or subscribe to products.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ProductV2Name **   <a name="securityhub-Type-ProductV2-ProductV2Name"></a>
The name of the productV2.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_ProductV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ProductV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ProductV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ProductV2)
