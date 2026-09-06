---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DnssecSigningAttributes.html
---

# DnssecSigningAttributes
<a name="API_domains_DnssecSigningAttributes"></a>

Information about a delegation signer (DS) record that was created in the registry by [AssociateDelegationSignerToDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_AssociateDelegationSignerToDomain.html).

## Contents
<a name="API_domains_DnssecSigningAttributes_Contents"></a>

 ** Algorithm **   <a name="Route53Domains-Type-domains_DnssecSigningAttributes-Algorithm"></a>
 Algorithm which was used to generate the digest from the public key.
Type: Integer
Required: No

 ** Flags **   <a name="Route53Domains-Type-domains_DnssecSigningAttributes-Flags"></a>
Defines the type of key. It can be either a KSK (key-signing-key, value 257) or ZSK (zone-signing-key, value 256). Using KSK is always encouraged. Only use ZSK if your DNS provider isn't Route 53 and you don’t have KSK available.
If you have KSK and ZSK keys, always use KSK to create a delegations signer (DS) record. If you have ZSK keys only – use ZSK to create a DS record.
Type: Integer
Required: No

 ** PublicKey **   <a name="Route53Domains-Type-domains_DnssecSigningAttributes-PublicKey"></a>
 The base64-encoded public key part of the key pair that is passed to the registry.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

## See Also
<a name="API_domains_DnssecSigningAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/DnssecSigningAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/DnssecSigningAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/DnssecSigningAttributes)
