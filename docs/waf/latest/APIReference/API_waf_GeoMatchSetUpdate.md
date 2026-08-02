---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GeoMatchSetUpdate.html
---

# GeoMatchSetUpdate
<a name="API_waf_GeoMatchSetUpdate"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Specifies the type of update to perform to an [GeoMatchSet](API_waf_GeoMatchSet.md) with [UpdateGeoMatchSet](API_waf_UpdateGeoMatchSet.md).

## Contents
<a name="API_waf_GeoMatchSetUpdate_Contents"></a>

 ** Action **   <a name="WAF-Type-waf_GeoMatchSetUpdate-Action"></a>
Specifies whether to insert or delete a country with [UpdateGeoMatchSet](API_waf_UpdateGeoMatchSet.md).
Type: String
Valid Values: `INSERT | DELETE`
Required: Yes

 ** GeoMatchConstraint **   <a name="WAF-Type-waf_GeoMatchSetUpdate-GeoMatchConstraint"></a>
The country from which web requests originate that you want AWS WAF to search for.
Type: [GeoMatchConstraint](API_waf_GeoMatchConstraint.md) object
Required: Yes

## See Also
<a name="API_waf_GeoMatchSetUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/GeoMatchSetUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/GeoMatchSetUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/GeoMatchSetUpdate)
