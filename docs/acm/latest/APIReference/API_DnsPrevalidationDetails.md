---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_DnsPrevalidationDetails.html
---

# DnsPrevalidationDetails
<a name="API_DnsPrevalidationDetails"></a>

DNS prevalidation details including the resource record for validation.

## Contents
<a name="API_DnsPrevalidationDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DomainScope **   <a name="ACM-Type-DnsPrevalidationDetails-DomainScope"></a>
The scope of domains covered by this prevalidation.
Type: [DomainScope](API_DomainScope.md) object
Required: No

 ** HostedZoneId **   <a name="ACM-Type-DnsPrevalidationDetails-HostedZoneId"></a>
The Route 53 hosted zone ID for DNS validation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `Z[A-Z0-9]+`
Required: No

 ** ResourceRecord **   <a name="ACM-Type-DnsPrevalidationDetails-ResourceRecord"></a>
The DNS resource record to create for domain validation.
Type: [ResourceRecord](API_ResourceRecord.md) object
Required: No

## See Also
<a name="API_DnsPrevalidationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/DnsPrevalidationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/DnsPrevalidationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/DnsPrevalidationDetails)
