---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_LoadBalancerTlsCertificateDomainValidationRecord.html
---

# LoadBalancerTlsCertificateDomainValidationRecord
<a name="API_LoadBalancerTlsCertificateDomainValidationRecord"></a>

Describes the validation record of each domain name in the SSL/TLS certificate.

## Contents
<a name="API_LoadBalancerTlsCertificateDomainValidationRecord_Contents"></a>

 ** dnsRecordCreationState **   <a name="Lightsail-Type-LoadBalancerTlsCertificateDomainValidationRecord-dnsRecordCreationState"></a>
An object that describes the state of the canonical name (CNAME) records that are automatically added by Lightsail to the DNS of a domain to validate domain ownership.
Type: [LoadBalancerTlsCertificateDnsRecordCreationState](API_LoadBalancerTlsCertificateDnsRecordCreationState.md) object
Required: No

 ** domainName **   <a name="Lightsail-Type-LoadBalancerTlsCertificateDomainValidationRecord-domainName"></a>
The domain name against which your SSL/TLS certificate was validated.
Type: String
Required: No

 ** name **   <a name="Lightsail-Type-LoadBalancerTlsCertificateDomainValidationRecord-name"></a>
A fully qualified domain name in the certificate. For example, `example.com`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** type **   <a name="Lightsail-Type-LoadBalancerTlsCertificateDomainValidationRecord-type"></a>
The type of validation record. For example, `CNAME` for domain validation.
Type: String
Pattern: `.*\S.*`
Required: No

 ** validationStatus **   <a name="Lightsail-Type-LoadBalancerTlsCertificateDomainValidationRecord-validationStatus"></a>
The validation status. Valid values are listed below.
Type: String
Valid Values: `PENDING_VALIDATION | FAILED | SUCCESS`
Required: No

 ** value **   <a name="Lightsail-Type-LoadBalancerTlsCertificateDomainValidationRecord-value"></a>
The value for that type.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_LoadBalancerTlsCertificateDomainValidationRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/LoadBalancerTlsCertificateDomainValidationRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/LoadBalancerTlsCertificateDomainValidationRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/LoadBalancerTlsCertificateDomainValidationRecord)
