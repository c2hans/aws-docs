---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ProtectionError.html
---

# ProtectionError
<a name="API_ProtectionError"></a>

Describes one entry in a `CreateResourceRecordSetProtections` or `DeleteResourceRecordSetProtections` request that Route 53 couldn't process.

## Contents
<a name="API_ProtectionError_Contents"></a>

 ** Code **   <a name="Route53-Type-ProtectionError-Code"></a>
The reason that the entry failed. Valid values include the following:
+  `InvalidInput` means that the entry isn't valid. For example, the name isn't a valid DNS name, the name isn't in the hosted zone, the record type can't be protected, or the same name and type appear more than once in the request.
+  `ProtectionAlreadyExists` means that a protection already exists for the name and type.
+  `ProtectionNotFound` means that no protection exists for the name and type.
Type: String
Required: Yes

 ** Message **   <a name="Route53-Type-ProtectionError-Message"></a>
A message that explains why Route 53 couldn't process the entry.
Type: String
Required: Yes

 ** RecordName **   <a name="Route53-Type-ProtectionError-RecordName"></a>
The name in the failing entry.
Type: String
Length Constraints: Maximum length of 1024.
Required: Yes

 ** RecordType **   <a name="Route53-Type-ProtectionError-RecordType"></a>
The record type in the failing entry.
Type: String
Valid Values: `SOA | A | TXT | NS | CNAME | MX | NAPTR | PTR | SRV | SPF | AAAA | CAA | DS | TLSA | SSHFP | SVCB | HTTPS`
Required: Yes

## See Also
<a name="API_ProtectionError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ProtectionError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ProtectionError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ProtectionError)
