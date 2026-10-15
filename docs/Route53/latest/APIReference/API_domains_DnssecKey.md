---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_DnssecKey.html
---

# DnssecKey
<a name="API_domains_DnssecKey"></a>

Information about the DNSSEC key.

You get this from your DNS provider and then give it to Route 53 (by using [AssociateDelegationSignerToDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_AssociateDelegationSignerToDomain.html)) to pass it to the registry to establish the chain of trust.

## Contents
<a name="API_domains_DnssecKey_Contents"></a>

 ** Algorithm **   <a name="Route53Domains-Type-domains_DnssecKey-Algorithm"></a>
The number of the public key’s cryptographic algorithm according to an [IANA](https://www.iana.org/assignments/dns-sec-alg-numbers/dns-sec-alg-numbers.xml) assignment.
If Route 53 is your DNS service, set this to 13.
For more information about enabling DNSSEC signing, see [Enabling DNSSEC signing and establishing a chain of trust](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec-enable-signing.html).
Type: Integer
Required: No

 ** Digest **   <a name="Route53Domains-Type-domains_DnssecKey-Digest"></a>
 The delegation signer digest.
Digest is calculated from the public key provided using specified digest algorithm and this digest is the actual value returned from the registry nameservers as the value of DS records.
Type: String
Required: No

 ** DigestType **   <a name="Route53Domains-Type-domains_DnssecKey-DigestType"></a>
 The number of the DS digest algorithm according to an IANA assignment.
For more information, see [IANA](https://www.iana.org/assignments/ds-rr-types/ds-rr-types.xhtml) for DNSSEC Delegation Signer (DS) Resource Record (RR) Type Digest Algorithms.
Type: Integer
Required: No

 ** Flags **   <a name="Route53Domains-Type-domains_DnssecKey-Flags"></a>
The DNSKEY flags that indicate the key type. This field is deprecated; the `DnssecKey` response no longer returns the flags.
Type: Integer
Required: No

 ** Id **   <a name="Route53Domains-Type-domains_DnssecKey-Id"></a>
 An ID assigned to each DS record created by [AssociateDelegationSignerToDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_AssociateDelegationSignerToDomain.html).
Type: String
Required: No

 ** KeyTag **   <a name="Route53Domains-Type-domains_DnssecKey-KeyTag"></a>
 A numeric identification of the DNSKEY record referred to by this DS record.
Type: Integer
Required: No

 ** PublicKey **   <a name="Route53Domains-Type-domains_DnssecKey-PublicKey"></a>
The base64-encoded public key of the key pair. This field is deprecated; the `DnssecKey` response no longer returns the public key.
Type: String
Length Constraints: Maximum length of 32768.
Required: No

## See Also
<a name="API_domains_DnssecKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/DnssecKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/DnssecKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/DnssecKey)
