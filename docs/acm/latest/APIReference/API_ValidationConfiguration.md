---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_ValidationConfiguration.html
---

# ValidationConfiguration
<a name="API_ValidationConfiguration"></a>

Contains the validation method, validation status, and validation challenge details for a domain. This structure appears in [DomainValidationSummary](API_DomainValidationSummary.md) as both the active and requested validation configuration.

## Contents
<a name="API_ValidationConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ValidationChallenge **   <a name="ACM-Type-ValidationConfiguration-ValidationChallenge"></a>
The validation challenge details for this configuration. The structure varies by validation method: for DNS validation, contains a `DnsValidationChallenge` with the CNAME record to add; for email validation, contains an `EmailValidationChallenge` with the validation email addresses.
Type: [ValidationChallenge](API_ValidationChallenge.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** ValidationMethod **   <a name="ACM-Type-ValidationConfiguration-ValidationMethod"></a>
The validation method for this configuration. Valid values:
+  `DNS` – Validation using a CNAME record added to your DNS configuration.
+  `EMAIL` – Validation using an approval email sent to domain contacts.
+  `HTTP` – Validation using an HTTP resource placed on your web server.
Type: String
Valid Values: `EMAIL | DNS | HTTP`
Required: No

 ** ValidationStatus **   <a name="ACM-Type-ValidationConfiguration-ValidationStatus"></a>
The validation status for this domain. Valid values:
+  `PENDING_VALIDATION` – The domain is waiting for validation to complete.
+  `SUCCESS` – Validation completed successfully.
+  `FAILED` – Validation failed.
Type: String
Valid Values: `PENDING_VALIDATION | SUCCESS | FAILED`
Required: No

## See Also
<a name="API_ValidationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/ValidationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/ValidationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/ValidationConfiguration)
