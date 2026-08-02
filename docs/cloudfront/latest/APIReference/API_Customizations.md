---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_Customizations.html
---

# Customizations
<a name="API_Customizations"></a>

Customizations for the distribution tenant. For each distribution tenant, you can specify the geographic restrictions, and the Amazon Resource Names (ARNs) for the ACM certificate and AWS WAF web ACL. These are specific values that you can override or disable from the multi-tenant distribution that was used to create the distribution tenant.

## Contents
<a name="API_Customizations_Contents"></a>

 ** Certificate **   <a name="cloudfront-Type-Customizations-Certificate"></a>
The AWS Certificate Manager (ACM) certificate.
Type: [Certificate](API_Certificate.md) object
Required: No

 ** GeoRestrictions **   <a name="cloudfront-Type-Customizations-GeoRestrictions"></a>
The geographic restrictions.
Type: [GeoRestrictionCustomization](API_GeoRestrictionCustomization.md) object
Required: No

 ** WebAcl **   <a name="cloudfront-Type-Customizations-WebAcl"></a>
The AWS WAF web ACL.
Type: [WebAclCustomization](API_WebAclCustomization.md) object
Required: No

## See Also
<a name="API_Customizations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/Customizations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/Customizations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/Customizations)
