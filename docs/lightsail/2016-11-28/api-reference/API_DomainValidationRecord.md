---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DomainValidationRecord.html
---

# DomainValidationRecord
<a name="API_DomainValidationRecord"></a>

Describes the domain name system (DNS) records that you must add to the DNS of your registered domain to validate ownership for an Amazon Lightsail SSL/TLS certificate.

## Contents
<a name="API_DomainValidationRecord_Contents"></a>

 ** dnsRecordCreationState **   <a name="Lightsail-Type-DomainValidationRecord-dnsRecordCreationState"></a>
An object that describes the state of the canonical name (CNAME) records that are automatically added by Lightsail to the DNS of the domain to validate domain ownership.
Type: [DnsRecordCreationState](API_DnsRecordCreationState.md) object
Required: No

 ** domainName **   <a name="Lightsail-Type-DomainValidationRecord-domainName"></a>
The domain name of the certificate validation record. For example, `example.com` or `www.example.com`.
Type: String
Required: No

 ** resourceRecord **   <a name="Lightsail-Type-DomainValidationRecord-resourceRecord"></a>
An object that describes the DNS records to add to your domain's DNS to validate it for the certificate.
Type: [ResourceRecord](API_ResourceRecord.md) object
Required: No

 ** validationStatus **   <a name="Lightsail-Type-DomainValidationRecord-validationStatus"></a>
The validation status of the record.
Type: String
Valid Values: `PENDING_VALIDATION | FAILED | SUCCESS`
Required: No

## See Also
<a name="API_DomainValidationRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/DomainValidationRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/DomainValidationRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/DomainValidationRecord)
