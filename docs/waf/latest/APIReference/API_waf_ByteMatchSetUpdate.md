---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ByteMatchSetUpdate.html
---

# ByteMatchSetUpdate
<a name="API_waf_ByteMatchSetUpdate"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

In an [UpdateByteMatchSet](API_waf_UpdateByteMatchSet.md) request, `ByteMatchSetUpdate` specifies whether to insert or delete a [ByteMatchTuple](API_waf_ByteMatchTuple.md) and includes the settings for the `ByteMatchTuple`.

## Contents
<a name="API_waf_ByteMatchSetUpdate_Contents"></a>

 ** Action **   <a name="WAF-Type-waf_ByteMatchSetUpdate-Action"></a>
Specifies whether to insert or delete a [ByteMatchTuple](API_waf_ByteMatchTuple.md).
Type: String
Valid Values: `INSERT | DELETE`
Required: Yes

 ** ByteMatchTuple **   <a name="WAF-Type-waf_ByteMatchSetUpdate-ByteMatchTuple"></a>
Information about the part of a web request that you want AWS WAF to inspect and the value that you want AWS WAF to search for. If you specify `DELETE` for the value of `Action`, the `ByteMatchTuple` values must exactly match the values in the `ByteMatchTuple` that you want to delete from the `ByteMatchSet`.
Type: [ByteMatchTuple](API_waf_ByteMatchTuple.md) object
Required: Yes

## See Also
<a name="API_waf_ByteMatchSetUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/ByteMatchSetUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/ByteMatchSetUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/ByteMatchSetUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
