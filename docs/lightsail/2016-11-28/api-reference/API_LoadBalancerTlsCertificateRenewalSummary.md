---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_LoadBalancerTlsCertificateRenewalSummary.html
---

# LoadBalancerTlsCertificateRenewalSummary
<a name="API_LoadBalancerTlsCertificateRenewalSummary"></a>

Contains information about the status of Lightsail's managed renewal for the certificate.

The renewal status of the certificate.

The following renewal status are possible:
+  ** `PendingAutoRenewal` ** - Lightsail is attempting to automatically validate the domain names in the certificate. No further action is required.
+  ** `PendingValidation` ** - Lightsail couldn't automatically validate one or more domain names in the certificate. You must take action to validate these domain names or the certificate won't be renewed. If you used DNS validation, check to make sure your certificate's domain validation records exist in your domain's DNS, and that your certificate remains in use.
+  ** `Success` ** - All domain names in the certificate are validated, and Lightsail renewed the certificate. No further action is required.
+  ** `Failed` ** - One or more domain names were not validated before the certificate expired, and Lightsail did not renew the certificate. You can request a new certificate using the `CreateCertificate` action.

## Contents
<a name="API_LoadBalancerTlsCertificateRenewalSummary_Contents"></a>

 ** domainValidationOptions **   <a name="Lightsail-Type-LoadBalancerTlsCertificateRenewalSummary-domainValidationOptions"></a>
Contains information about the validation of each domain name in the certificate, as it pertains to Lightsail's managed renewal. This is different from the initial validation that occurs as a result of the RequestCertificate request.
Type: Array of [LoadBalancerTlsCertificateDomainValidationOption](API_LoadBalancerTlsCertificateDomainValidationOption.md) objects
Required: No

 ** renewalStatus **   <a name="Lightsail-Type-LoadBalancerTlsCertificateRenewalSummary-renewalStatus"></a>
The renewal status of the certificate.
The following renewal status are possible:
+  ** `PendingAutoRenewal` ** - Lightsail is attempting to automatically validate the domain names of the certificate. No further action is required.
+  ** `PendingValidation` ** - Lightsail couldn't automatically validate one or more domain names of the certificate. You must take action to validate these domain names or the certificate won't be renewed. Check to make sure your certificate's domain validation records exist in your domain's DNS, and that your certificate remains in use.
+  ** `Success` ** - All domain names in the certificate are validated, and Lightsail renewed the certificate. No further action is required.
+  ** `Failed` ** - One or more domain names were not validated before the certificate expired, and Lightsail did not renew the certificate. You can request a new certificate using the `CreateCertificate` action.
Type: String
Valid Values: `PENDING_AUTO_RENEWAL | PENDING_VALIDATION | SUCCESS | FAILED`
Required: No

## See Also
<a name="API_LoadBalancerTlsCertificateRenewalSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/LoadBalancerTlsCertificateRenewalSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/LoadBalancerTlsCertificateRenewalSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/LoadBalancerTlsCertificateRenewalSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
