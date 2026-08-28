---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_RegexMatchSetUpdate.html
---

# RegexMatchSetUpdate
<a name="API_wafRegional_RegexMatchSetUpdate"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

In an [UpdateRegexMatchSet](API_wafRegional_UpdateRegexMatchSet.md) request, `RegexMatchSetUpdate` specifies whether to insert or delete a [RegexMatchTuple](API_wafRegional_RegexMatchTuple.md) and includes the settings for the `RegexMatchTuple`.

## Contents
<a name="API_wafRegional_RegexMatchSetUpdate_Contents"></a>

 ** Action **   <a name="WAF-Type-wafRegional_RegexMatchSetUpdate-Action"></a>
Specifies whether to insert or delete a [RegexMatchTuple](API_wafRegional_RegexMatchTuple.md).
Type: String
Valid Values: `INSERT | DELETE`
Required: Yes

 ** RegexMatchTuple **   <a name="WAF-Type-wafRegional_RegexMatchSetUpdate-RegexMatchTuple"></a>
Information about the part of a web request that you want AWS WAF to inspect and the identifier of the regular expression (regex) pattern that you want AWS WAF to search for. If you specify `DELETE` for the value of `Action`, the `RegexMatchTuple` values must exactly match the values in the `RegexMatchTuple` that you want to delete from the `RegexMatchSet`.
Type: [RegexMatchTuple](API_wafRegional_RegexMatchTuple.md) object
Required: Yes

## See Also
<a name="API_wafRegional_RegexMatchSetUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/RegexMatchSetUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/RegexMatchSetUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/RegexMatchSetUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
