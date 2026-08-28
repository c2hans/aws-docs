---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ByteMatchSetSummary.html
---

# ByteMatchSetSummary
<a name="API_waf_ByteMatchSetSummary"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Returned by [ListByteMatchSets](API_waf_ListByteMatchSets.md). Each `ByteMatchSetSummary` object includes the `Name` and `ByteMatchSetId` for one [ByteMatchSet](API_waf_ByteMatchSet.md).

## Contents
<a name="API_waf_ByteMatchSetSummary_Contents"></a>

 ** ByteMatchSetId **   <a name="WAF-Type-waf_ByteMatchSetSummary-ByteMatchSetId"></a>
The `ByteMatchSetId` for a `ByteMatchSet`. You use `ByteMatchSetId` to get information about a `ByteMatchSet`, update a `ByteMatchSet`, remove a `ByteMatchSet` from a `Rule`, and delete a `ByteMatchSet` from AWS WAF.
 `ByteMatchSetId` is returned by [CreateByteMatchSet](API_waf_CreateByteMatchSet.md) and by [ListByteMatchSets](API_waf_ListByteMatchSets.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** Name **   <a name="WAF-Type-waf_ByteMatchSetSummary-Name"></a>
A friendly name or description of the [ByteMatchSet](API_waf_ByteMatchSet.md). You can't change `Name` after you create a `ByteMatchSet`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_waf_ByteMatchSetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/ByteMatchSetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/ByteMatchSetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/ByteMatchSetSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
