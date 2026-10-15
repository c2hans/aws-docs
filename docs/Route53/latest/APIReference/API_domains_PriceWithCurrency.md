---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_PriceWithCurrency.html
---

# PriceWithCurrency
<a name="API_domains_PriceWithCurrency"></a>

Currency-specific price information.

## Contents
<a name="API_domains_PriceWithCurrency_Contents"></a>

 ** Currency **   <a name="Route53Domains-Type-domains_PriceWithCurrency-Currency"></a>
The currency specifier.
Type: String
Length Constraints: Fixed length of 3.
Required: Yes

 ** Price **   <a name="Route53Domains-Type-domains_PriceWithCurrency-Price"></a>
The price of a domain, in a specific currency.
Type: Double
Valid Range: Minimum value of 0.0.
Required: Yes

 ** PriceType **   <a name="Route53Domains-Type-domains_PriceWithCurrency-PriceType"></a>
Indicates whether the domain has standard or premium pricing. A value of `STANDARD` means the domain is priced at the regular rate for its TLD. A value of `REGISTRY_PREMIUM` means the domain has registry premium pricing, which may be different than the standard rate.
Type: String
Valid Values: `STANDARD | REGISTRY_PREMIUM`
Required: No

## See Also
<a name="API_domains_PriceWithCurrency_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/PriceWithCurrency)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/PriceWithCurrency)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/PriceWithCurrency)
