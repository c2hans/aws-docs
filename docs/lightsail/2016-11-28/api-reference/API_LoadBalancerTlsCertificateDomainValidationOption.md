---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_LoadBalancerTlsCertificateDomainValidationOption.html
---

# LoadBalancerTlsCertificateDomainValidationOption
<a name="API_LoadBalancerTlsCertificateDomainValidationOption"></a>

Contains information about the domain names on an SSL/TLS certificate that you will use to validate domain ownership.

## Contents
<a name="API_LoadBalancerTlsCertificateDomainValidationOption_Contents"></a>

 ** domainName **   <a name="Lightsail-Type-LoadBalancerTlsCertificateDomainValidationOption-domainName"></a>
The fully qualified domain name in the certificate request.
Type: String
Required: No

 ** validationStatus **   <a name="Lightsail-Type-LoadBalancerTlsCertificateDomainValidationOption-validationStatus"></a>
The status of the domain validation. Valid values are listed below.
Type: String
Valid Values: `PENDING_VALIDATION | FAILED | SUCCESS`
Required: No

## See Also
<a name="API_LoadBalancerTlsCertificateDomainValidationOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/LoadBalancerTlsCertificateDomainValidationOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/LoadBalancerTlsCertificateDomainValidationOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/LoadBalancerTlsCertificateDomainValidationOption)
