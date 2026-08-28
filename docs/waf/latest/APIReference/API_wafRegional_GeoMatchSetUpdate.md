---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_GeoMatchSetUpdate.html
---

# GeoMatchSetUpdate
<a name="API_wafRegional_GeoMatchSetUpdate"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Specifies the type of update to perform to an [GeoMatchSet](API_wafRegional_GeoMatchSet.md) with [UpdateGeoMatchSet](API_wafRegional_UpdateGeoMatchSet.md).

## Contents
<a name="API_wafRegional_GeoMatchSetUpdate_Contents"></a>

 ** Action **   <a name="WAF-Type-wafRegional_GeoMatchSetUpdate-Action"></a>
Specifies whether to insert or delete a country with [UpdateGeoMatchSet](API_wafRegional_UpdateGeoMatchSet.md).
Type: String
Valid Values: `INSERT | DELETE`
Required: Yes

 ** GeoMatchConstraint **   <a name="WAF-Type-wafRegional_GeoMatchSetUpdate-GeoMatchConstraint"></a>
The country from which web requests originate that you want AWS WAF to search for.
Type: [GeoMatchConstraint](API_wafRegional_GeoMatchConstraint.md) object
Required: Yes

## See Also
<a name="API_wafRegional_GeoMatchSetUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/GeoMatchSetUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/GeoMatchSetUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/GeoMatchSetUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
