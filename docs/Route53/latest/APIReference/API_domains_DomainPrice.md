---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DomainPrice.html
---

# DomainPrice
<a name="API_domains_DomainPrice"></a>

Information about the domain price associated with a TLD.

## Contents
<a name="API_domains_DomainPrice_Contents"></a>

 ** ChangeOwnershipPrice **   <a name="Route53Domains-Type-domains_DomainPrice-ChangeOwnershipPrice"></a>
The price for changing domain ownership.
Type: [PriceWithCurrency](API_domains_PriceWithCurrency.md) object
Required: No

 ** Name **   <a name="Route53Domains-Type-domains_DomainPrice-Name"></a>
The name of the TLD for which the prices apply.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** RegistrationPrice **   <a name="Route53Domains-Type-domains_DomainPrice-RegistrationPrice"></a>
The price for domain registration with Route 53.
Type: [PriceWithCurrency](API_domains_PriceWithCurrency.md) object
Required: No

 ** RenewalPrice **   <a name="Route53Domains-Type-domains_DomainPrice-RenewalPrice"></a>
The price for renewing domain registration with Route 53.
Type: [PriceWithCurrency](API_domains_PriceWithCurrency.md) object
Required: No

 ** RestorationPrice **   <a name="Route53Domains-Type-domains_DomainPrice-RestorationPrice"></a>
The price for restoring the domain with Route 53.
Type: [PriceWithCurrency](API_domains_PriceWithCurrency.md) object
Required: No

 ** TransferPrice **   <a name="Route53Domains-Type-domains_DomainPrice-TransferPrice"></a>
The price for transferring the domain registration to Route 53.
Type: [PriceWithCurrency](API_domains_PriceWithCurrency.md) object
Required: No

## See Also
<a name="API_domains_DomainPrice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/DomainPrice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/DomainPrice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/DomainPrice)
