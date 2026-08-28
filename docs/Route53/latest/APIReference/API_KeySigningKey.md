---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_KeySigningKey.html
---

# KeySigningKey
<a name="API_KeySigningKey"></a>

A key-signing key (KSK) is a complex type that represents a public/private key pair. The private key is used to generate a digital signature for the zone signing key (ZSK). The public key is stored in the DNS and is used to authenticate the ZSK. A KSK is always associated with a hosted zone; it cannot exist by itself.

## Contents
<a name="API_KeySigningKey_Contents"></a>

 ** CreatedDate **   <a name="Route53-Type-KeySigningKey-CreatedDate"></a>
The date when the key-signing key (KSK) was created.
Type: Timestamp
Required: No

 ** DigestAlgorithmMnemonic **   <a name="Route53-Type-KeySigningKey-DigestAlgorithmMnemonic"></a>
A string used to represent the delegation signer digest algorithm. This value must follow the guidelines provided by [RFC-8624 Section 3.3](https://tools.ietf.org/html/rfc8624#section-3.3).
Type: String
Required: No

 ** DigestAlgorithmType **   <a name="Route53-Type-KeySigningKey-DigestAlgorithmType"></a>
An integer used to represent the delegation signer digest algorithm. This value must follow the guidelines provided by [RFC-8624 Section 3.3](https://tools.ietf.org/html/rfc8624#section-3.3).
Type: Integer
Required: No

 ** DigestValue **   <a name="Route53-Type-KeySigningKey-DigestValue"></a>
A cryptographic digest of a DNSKEY resource record (RR). DNSKEY records are used to publish the public key that resolvers can use to verify DNSSEC signatures that are used to secure certain kinds of information provided by the DNS system.
Type: String
Required: No

 ** DNSKEYRecord **   <a name="Route53-Type-KeySigningKey-DNSKEYRecord"></a>
A string that represents a DNSKEY record.
Type: String
Required: No

 ** DSRecord **   <a name="Route53-Type-KeySigningKey-DSRecord"></a>
A string that represents a delegation signer (DS) record.
Type: String
Required: No

 ** Flag **   <a name="Route53-Type-KeySigningKey-Flag"></a>
An integer that specifies how the key is used. For key-signing key (KSK), this value is always 257.
Type: Integer
Required: No

 ** KeyTag **   <a name="Route53-Type-KeySigningKey-KeyTag"></a>
An integer used to identify the DNSSEC record for the domain name. The process used to calculate the value is described in [RFC-4034 Appendix B](https://tools.ietf.org/rfc/rfc4034.txt).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65536.
Required: No

 ** KmsArn **   <a name="Route53-Type-KeySigningKey-KmsArn"></a>
The Amazon resource name (ARN) used to identify the customer managed key in AWS Key Management Service (AWS KMS). The `KmsArn` must be unique for each key-signing key (KSK) in a single hosted zone.
You must configure the customer managed key as follows:
Status
Enabled
Key spec
ECC\_NIST\_P256
Key usage
Sign and verify
Key policy
The key policy must give permission for the following actions:
+ DescribeKey
+ GetPublicKey
+ Sign
The key policy must also include the Amazon Route 53 service in the principal for your account. Specify the following:
+  `"Service": "dnssec-route53.amazonaws.com"`
For more information about working with the customer managed key in AWS KMS, see [AWS Key Management Service concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html).
Type: String
Required: No

 ** LastModifiedDate **   <a name="Route53-Type-KeySigningKey-LastModifiedDate"></a>
The last time that the key-signing key (KSK) was changed.
Type: Timestamp
Required: No

 ** Name **   <a name="Route53-Type-KeySigningKey-Name"></a>
A string used to identify a key-signing key (KSK). `Name` can include numbers, letters, and underscores (\_). `Name` must be unique for each key-signing key in the same hosted zone.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Required: No

 ** PublicKey **   <a name="Route53-Type-KeySigningKey-PublicKey"></a>
The public key, represented as a Base64 encoding, as required by [ RFC-4034 Page 5](https://tools.ietf.org/rfc/rfc4034.txt).
Type: String
Required: No

 ** SigningAlgorithmMnemonic **   <a name="Route53-Type-KeySigningKey-SigningAlgorithmMnemonic"></a>
A string used to represent the signing algorithm. This value must follow the guidelines provided by [RFC-8624 Section 3.1](https://tools.ietf.org/html/rfc8624#section-3.1).
Type: String
Required: No

 ** SigningAlgorithmType **   <a name="Route53-Type-KeySigningKey-SigningAlgorithmType"></a>
An integer used to represent the signing algorithm. This value must follow the guidelines provided by [RFC-8624 Section 3.1](https://tools.ietf.org/html/rfc8624#section-3.1).
Type: Integer
Required: No

 ** Status **   <a name="Route53-Type-KeySigningKey-Status"></a>
A string that represents the current key-signing key (KSK) status.
Status can have one of the following values:
ACTIVE
The KSK is being used for signing.
INACTIVE
The KSK is not being used for signing.
DELETING
The KSK is in the process of being deleted.
ACTION\_NEEDED
There is a problem with the KSK that requires you to take action to resolve. For example, the customer managed key might have been deleted, or the permissions for the customer managed key might have been changed.
INTERNAL\_FAILURE
There was an error during a request. Before you can continue to work with DNSSEC signing, including actions that involve this KSK, you must correct the problem. For example, you may need to activate or deactivate the KSK.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 150.
Required: No

 ** StatusMessage **   <a name="Route53-Type-KeySigningKey-StatusMessage"></a>
The status message provided for the following key-signing key (KSK) statuses: `ACTION_NEEDED` or `INTERNAL_FAILURE`. The status message includes information about what the problem might be and steps that you can take to correct the issue.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: No

## See Also
<a name="API_KeySigningKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/KeySigningKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/KeySigningKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/KeySigningKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
