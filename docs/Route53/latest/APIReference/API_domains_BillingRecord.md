---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_BillingRecord.html
---

# BillingRecord
<a name="API_domains_BillingRecord"></a>

Information for one billing record.

## Contents
<a name="API_domains_BillingRecord_Contents"></a>

 ** BillDate **   <a name="Route53Domains-Type-domains_BillingRecord-BillDate"></a>
The date that the operation was billed, in Unix format.
Type: Timestamp
Required: No

 ** DomainName **   <a name="Route53Domains-Type-domains_BillingRecord-DomainName"></a>
The name of the domain that the billing record applies to. If the domain name contains characters other than a-z, 0-9, and - (hyphen), such as an internationalized domain name, then this value is in Punycode. For more information, see [DNS Domain Name Format](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html) in the *Amazon Route 53 Developer Guide*.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** InvoiceId **   <a name="Route53Domains-Type-domains_BillingRecord-InvoiceId"></a>
Deprecated property. This field is retained in report structure for backwards compatibility, but will appear blank.
Type: String
Required: No

 ** Operation **   <a name="Route53Domains-Type-domains_BillingRecord-Operation"></a>
The operation that you were charged for.
Type: String
Valid Values: `REGISTER_DOMAIN | DELETE_DOMAIN | TRANSFER_IN_DOMAIN | UPDATE_DOMAIN_CONTACT | UPDATE_NAMESERVER | CHANGE_PRIVACY_PROTECTION | DOMAIN_LOCK | ENABLE_AUTORENEW | DISABLE_AUTORENEW | ADD_DNSSEC | REMOVE_DNSSEC | EXPIRE_DOMAIN | TRANSFER_OUT_DOMAIN | CHANGE_DOMAIN_OWNER | RENEW_DOMAIN | PUSH_DOMAIN | INTERNAL_TRANSFER_OUT_DOMAIN | INTERNAL_TRANSFER_IN_DOMAIN | RELEASE_TO_GANDI | TRANSFER_ON_RENEW | RESTORE_DOMAIN`
Required: No

 ** Price **   <a name="Route53Domains-Type-domains_BillingRecord-Price"></a>
The price that you were charged for the operation, in US dollars.
Example value: 12.0
Type: Double
Valid Range: Minimum value of 0.0.
Required: No

## See Also
<a name="API_domains_BillingRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/BillingRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/BillingRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/BillingRecord)
