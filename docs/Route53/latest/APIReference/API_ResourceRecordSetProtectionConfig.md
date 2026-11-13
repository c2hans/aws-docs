---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ResourceRecordSetProtectionConfig.html
---

# ResourceRecordSetProtectionConfig
<a name="API_ResourceRecordSetProtectionConfig"></a>

A protection to create for the resource record sets in a hosted zone that have the specified name and type.

## Contents
<a name="API_ResourceRecordSetProtectionConfig_Contents"></a>

 ** RecordName **   <a name="Route53-Type-ResourceRecordSetProtectionConfig-RecordName"></a>
The name of the resource record sets to protect, for example, `www.example.com`. The name must be the name of the hosted zone or a subdomain of it.
Type: String
Length Constraints: Maximum length of 1024.
Required: Yes

 ** RecordType **   <a name="Route53-Type-ResourceRecordSetProtectionConfig-RecordType"></a>
The DNS record type of the resource record sets to protect. You can't protect records of type `DNAME` or of the DNSSEC record types that Route 53 manages.
Type: String
Valid Values: `SOA | A | TXT | NS | CNAME | MX | NAPTR | PTR | SRV | SPF | AAAA | CAA | DS | TLSA | SSHFP | SVCB | HTTPS`
Required: Yes

 ** Comment **   <a name="Route53-Type-ResourceRecordSetProtectionConfig-Comment"></a>
An optional comment about the protection, for example, the reason that the resource record sets are protected. The comment can be up to 256 characters long. If you don't specify a comment, the protection doesn't have a comment. When Route 53 rejects a `ChangeResourceRecordSets` request because of this protection, the error message includes the comment, so don't include sensitive information.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_ResourceRecordSetProtectionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ResourceRecordSetProtectionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ResourceRecordSetProtectionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ResourceRecordSetProtectionConfig)
