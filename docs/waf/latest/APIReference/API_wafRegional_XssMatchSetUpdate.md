---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_XssMatchSetUpdate.html
---

# XssMatchSetUpdate
<a name="API_wafRegional_XssMatchSetUpdate"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Specifies the part of a web request that you want to inspect for cross-site scripting attacks and indicates whether you want to add the specification to an [XssMatchSet](API_wafRegional_XssMatchSet.md) or delete it from an `XssMatchSet`.

## Contents
<a name="API_wafRegional_XssMatchSetUpdate_Contents"></a>

 ** Action **   <a name="WAF-Type-wafRegional_XssMatchSetUpdate-Action"></a>
Specify `INSERT` to add an [XssMatchSetUpdate](#API_wafRegional_XssMatchSetUpdate) to an [XssMatchSet](API_wafRegional_XssMatchSet.md). Use `DELETE` to remove an `XssMatchSetUpdate` from an `XssMatchSet`.
Type: String
Valid Values: `INSERT | DELETE`
Required: Yes

 ** XssMatchTuple **   <a name="WAF-Type-wafRegional_XssMatchSetUpdate-XssMatchTuple"></a>
Specifies the part of a web request that you want AWS WAF to inspect for cross-site scripting attacks and, if you want AWS WAF to inspect a header, the name of the header.
Type: [XssMatchTuple](API_wafRegional_XssMatchTuple.md) object
Required: Yes

## See Also
<a name="API_wafRegional_XssMatchSetUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/XssMatchSetUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/XssMatchSetUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/XssMatchSetUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
