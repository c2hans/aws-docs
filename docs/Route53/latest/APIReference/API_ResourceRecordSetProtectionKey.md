---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ResourceRecordSetProtectionKey.html
---

# ResourceRecordSetProtectionKey
<a name="API_ResourceRecordSetProtectionKey"></a>

The name and type that identify a resource record set protection.

## Contents
<a name="API_ResourceRecordSetProtectionKey_Contents"></a>

 ** RecordName **   <a name="Route53-Type-ResourceRecordSetProtectionKey-RecordName"></a>
The name of the protected resource record sets.
Type: String
Length Constraints: Maximum length of 1024.
Required: Yes

 ** RecordType **   <a name="Route53-Type-ResourceRecordSetProtectionKey-RecordType"></a>
The DNS record type of the protected resource record sets.
Type: String
Valid Values: `SOA | A | TXT | NS | CNAME | MX | NAPTR | PTR | SRV | SPF | AAAA | CAA | DS | TLSA | SSHFP | SVCB | HTTPS`
Required: Yes

## See Also
<a name="API_ResourceRecordSetProtectionKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ResourceRecordSetProtectionKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ResourceRecordSetProtectionKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ResourceRecordSetProtectionKey)
