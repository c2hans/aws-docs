---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_Consent.html
---

# Consent
<a name="API_domains_Consent"></a>

 The maximum amount that you agree to pay for an operation, and the currency for that amount.

## Contents
<a name="API_domains_Consent_Contents"></a>

 ** Currency **   <a name="Route53Domains-Type-domains_Consent-Currency"></a>
 The currency for the `MaxPrice`.
Type: String
Length Constraints: Fixed length of 3.
Required: Yes

 ** MaxPrice **   <a name="Route53Domains-Type-domains_Consent-MaxPrice"></a>
 The maximum amount that you agree to accept.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 2000000000.0.
Required: Yes

## See Also
<a name="API_domains_Consent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/Consent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/Consent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/Consent)
