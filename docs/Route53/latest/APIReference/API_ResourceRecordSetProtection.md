---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ResourceRecordSetProtection.html
---

# ResourceRecordSetProtection
<a name="API_ResourceRecordSetProtection"></a>

A protection for the resource record sets in a hosted zone that have the specified name and type. While the protection exists, Route 53 rejects `ChangeResourceRecordSets` requests that create, update, or delete those resource record sets.

## Contents
<a name="API_ResourceRecordSetProtection_Contents"></a>

 ** RecordName **   <a name="Route53-Type-ResourceRecordSetProtection-RecordName"></a>
The name of the protected resource record sets.
Type: String
Length Constraints: Maximum length of 1024.
Required: Yes

 ** RecordType **   <a name="Route53-Type-ResourceRecordSetProtection-RecordType"></a>
The DNS record type of the protected resource record sets.
Type: String
Valid Values: `SOA | A | TXT | NS | CNAME | MX | NAPTR | PTR | SRV | SPF | AAAA | CAA | DS | TLSA | SSHFP | SVCB | HTTPS`
Required: Yes

 ** Comment **   <a name="Route53-Type-ResourceRecordSetProtection-Comment"></a>
The comment that was specified when the protection was created, if any.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_ResourceRecordSetProtection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ResourceRecordSetProtection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ResourceRecordSetProtection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ResourceRecordSetProtection)
