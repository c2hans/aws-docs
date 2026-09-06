---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_RuleUpdate.html
---

# RuleUpdate
<a name="API_waf_RuleUpdate"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Specifies a `Predicate` (such as an `IPSet`) and indicates whether you want to add it to a `Rule` or delete it from a `Rule`.

## Contents
<a name="API_waf_RuleUpdate_Contents"></a>

 ** Action **   <a name="WAF-Type-waf_RuleUpdate-Action"></a>
Specify `INSERT` to add a `Predicate` to a `Rule`. Use `DELETE` to remove a `Predicate` from a `Rule`.
Type: String
Valid Values: `INSERT | DELETE`
Required: Yes

 ** Predicate **   <a name="WAF-Type-waf_RuleUpdate-Predicate"></a>
The ID of the `Predicate` (such as an `IPSet`) that you want to add to a `Rule`.
Type: [Predicate](API_waf_Predicate.md) object
Required: Yes

## See Also
<a name="API_waf_RuleUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/RuleUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/RuleUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/RuleUpdate)
