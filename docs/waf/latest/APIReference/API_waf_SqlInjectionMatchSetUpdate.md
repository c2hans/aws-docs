---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_SqlInjectionMatchSetUpdate.html
---

# SqlInjectionMatchSetUpdate
<a name="API_waf_SqlInjectionMatchSetUpdate"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Specifies the part of a web request that you want to inspect for snippets of malicious SQL code and indicates whether you want to add the specification to a [SqlInjectionMatchSet](API_waf_SqlInjectionMatchSet.md) or delete it from a `SqlInjectionMatchSet`.

## Contents
<a name="API_waf_SqlInjectionMatchSetUpdate_Contents"></a>

 ** Action **   <a name="WAF-Type-waf_SqlInjectionMatchSetUpdate-Action"></a>
Specify `INSERT` to add a [SqlInjectionMatchSetUpdate](#API_waf_SqlInjectionMatchSetUpdate) to a [SqlInjectionMatchSet](API_waf_SqlInjectionMatchSet.md). Use `DELETE` to remove a `SqlInjectionMatchSetUpdate` from a `SqlInjectionMatchSet`.
Type: String
Valid Values: `INSERT | DELETE`
Required: Yes

 ** SqlInjectionMatchTuple **   <a name="WAF-Type-waf_SqlInjectionMatchSetUpdate-SqlInjectionMatchTuple"></a>
Specifies the part of a web request that you want AWS WAF to inspect for snippets of malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.
Type: [SqlInjectionMatchTuple](API_waf_SqlInjectionMatchTuple.md) object
Required: Yes

## See Also
<a name="API_waf_SqlInjectionMatchSetUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/SqlInjectionMatchSetUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/SqlInjectionMatchSetUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/SqlInjectionMatchSetUpdate)
