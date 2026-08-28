---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ByteMatchSet.html
---

# ByteMatchSet
<a name="API_waf_ByteMatchSet"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

In a [GetByteMatchSet](API_waf_GetByteMatchSet.md) request, `ByteMatchSet` is a complex type that contains the `ByteMatchSetId` and `Name` of a `ByteMatchSet`, and the values that you specified when you updated the `ByteMatchSet`.

A complex type that contains `ByteMatchTuple` objects, which specify the parts of web requests that you want AWS WAF to inspect and the values that you want AWS WAF to search for. If a `ByteMatchSet` contains more than one `ByteMatchTuple` object, a request needs to match the settings in only one `ByteMatchTuple` to be considered a match.

## Contents
<a name="API_waf_ByteMatchSet_Contents"></a>

 ** ByteMatchSetId **   <a name="WAF-Type-waf_ByteMatchSet-ByteMatchSetId"></a>
The `ByteMatchSetId` for a `ByteMatchSet`. You use `ByteMatchSetId` to get information about a `ByteMatchSet` (see [GetByteMatchSet](API_waf_GetByteMatchSet.md)), update a `ByteMatchSet` (see [UpdateByteMatchSet](API_waf_UpdateByteMatchSet.md)), insert a `ByteMatchSet` into a `Rule` or delete one from a `Rule` (see [UpdateRule](API_waf_UpdateRule.md)), and delete a `ByteMatchSet` from AWS WAF (see [DeleteByteMatchSet](API_waf_DeleteByteMatchSet.md)).
 `ByteMatchSetId` is returned by [CreateByteMatchSet](API_waf_CreateByteMatchSet.md) and by [ListByteMatchSets](API_waf_ListByteMatchSets.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** ByteMatchTuples **   <a name="WAF-Type-waf_ByteMatchSet-ByteMatchTuples"></a>
Specifies the bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests, the location in requests that you want AWS WAF to search, and other settings.
Type: Array of [ByteMatchTuple](API_waf_ByteMatchTuple.md) objects
Required: Yes

 ** Name **   <a name="WAF-Type-waf_ByteMatchSet-Name"></a>
A friendly name or description of the [ByteMatchSet](#API_waf_ByteMatchSet). You can't change `Name` after you create a `ByteMatchSet`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_waf_ByteMatchSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/ByteMatchSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/ByteMatchSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/ByteMatchSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
