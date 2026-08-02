---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GeoRestrictionCustomization.html
---

# GeoRestrictionCustomization
<a name="API_GeoRestrictionCustomization"></a>

The customizations that you specified for the distribution tenant for geographic restrictions.

## Contents
<a name="API_GeoRestrictionCustomization_Contents"></a>

 ** RestrictionType **   <a name="cloudfront-Type-GeoRestrictionCustomization-RestrictionType"></a>
The method that you want to use to restrict distribution of your content by country:
+  `none`: No geographic restriction is enabled, meaning access to content is not restricted by client geo location.
+  `blacklist`: The `Location` elements specify the countries in which you don't want CloudFront to distribute your content.
+  `whitelist`: The `Location` elements specify the countries in which you want CloudFront to distribute your content.
Type: String
Valid Values: `blacklist | whitelist | none`
Required: Yes

 ** Locations **   <a name="cloudfront-Type-GeoRestrictionCustomization-Locations"></a>
The locations for geographic restrictions.
Type: Array of strings
Required: No

## See Also
<a name="API_GeoRestrictionCustomization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GeoRestrictionCustomization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GeoRestrictionCustomization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GeoRestrictionCustomization)
