---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_RenewalSummary.html
---

# RenewalSummary
<a name="API_RenewalSummary"></a>

Describes the status of a SSL/TLS certificate renewal managed by Amazon Lightsail.

## Contents
<a name="API_RenewalSummary_Contents"></a>

 ** domainValidationRecords **   <a name="Lightsail-Type-RenewalSummary-domainValidationRecords"></a>
An array of objects that describe the domain validation records of the certificate.
Type: Array of [DomainValidationRecord](API_DomainValidationRecord.md) objects
Required: No

 ** renewalStatus **   <a name="Lightsail-Type-RenewalSummary-renewalStatus"></a>
The renewal status of the certificate.
The following renewal status are possible:
+  ** `PendingAutoRenewal` ** - Lightsail is attempting to automatically validate the domain names of the certificate. No further action is required.
+  ** `PendingValidation` ** - Lightsail couldn't automatically validate one or more domain names of the certificate. You must take action to validate these domain names or the certificate won't be renewed. Check to make sure your certificate's domain validation records exist in your domain's DNS, and that your certificate remains in use.
+  ** `Success` ** - All domain names in the certificate are validated, and Lightsail renewed the certificate. No further action is required.
+  ** `Failed` ** - One or more domain names were not validated before the certificate expired, and Lightsail did not renew the certificate. You can request a new certificate using the `CreateCertificate` action.
Type: String
Valid Values: `PendingAutoRenewal | PendingValidation | Success | Failed`
Required: No

 ** renewalStatusReason **   <a name="Lightsail-Type-RenewalSummary-renewalStatusReason"></a>
The reason for the renewal status of the certificate.
Type: String
Required: No

 ** updatedAt **   <a name="Lightsail-Type-RenewalSummary-updatedAt"></a>
The timestamp when the certificate was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_RenewalSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/RenewalSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/RenewalSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/RenewalSummary)
