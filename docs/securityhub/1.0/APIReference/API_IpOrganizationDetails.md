---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_IpOrganizationDetails.html
---

# IpOrganizationDetails
<a name="API_IpOrganizationDetails"></a>

Provides information about an internet provider.

## Contents
<a name="API_IpOrganizationDetails_Contents"></a>

 ** Asn **   <a name="securityhub-Type-IpOrganizationDetails-Asn"></a>
The Autonomous System Number (ASN) of the internet provider
Type: Integer
Required: No

 ** AsnOrg **   <a name="securityhub-Type-IpOrganizationDetails-AsnOrg"></a>
The name of the organization that registered the ASN.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Isp **   <a name="securityhub-Type-IpOrganizationDetails-Isp"></a>
The ISP information for the internet provider.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Org **   <a name="securityhub-Type-IpOrganizationDetails-Org"></a>
The name of the internet provider.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_IpOrganizationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/IpOrganizationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/IpOrganizationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/IpOrganizationDetails)
