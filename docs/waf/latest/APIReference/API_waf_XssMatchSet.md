---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_XssMatchSet.html
---

# XssMatchSet
<a name="API_waf_XssMatchSet"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

A complex type that contains `XssMatchTuple` objects, which specify the parts of web requests that you want AWS WAF to inspect for cross-site scripting attacks and, if you want AWS WAF to inspect a header, the name of the header. If a `XssMatchSet` contains more than one `XssMatchTuple` object, a request needs to include cross-site scripting attacks in only one of the specified parts of the request to be considered a match.

## Contents
<a name="API_waf_XssMatchSet_Contents"></a>

 ** XssMatchSetId **   <a name="WAF-Type-waf_XssMatchSet-XssMatchSetId"></a>
A unique identifier for an `XssMatchSet`. You use `XssMatchSetId` to get information about an `XssMatchSet` (see [GetXssMatchSet](API_waf_GetXssMatchSet.md)), update an `XssMatchSet` (see [UpdateXssMatchSet](API_waf_UpdateXssMatchSet.md)), insert an `XssMatchSet` into a `Rule` or delete one from a `Rule` (see [UpdateRule](API_waf_UpdateRule.md)), and delete an `XssMatchSet` from AWS WAF (see [DeleteXssMatchSet](API_waf_DeleteXssMatchSet.md)).
 `XssMatchSetId` is returned by [CreateXssMatchSet](API_waf_CreateXssMatchSet.md) and by [ListXssMatchSets](API_waf_ListXssMatchSets.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** XssMatchTuples **   <a name="WAF-Type-waf_XssMatchSet-XssMatchTuples"></a>
Specifies the parts of web requests that you want to inspect for cross-site scripting attacks.
Type: Array of [XssMatchTuple](API_waf_XssMatchTuple.md) objects
Required: Yes

 ** Name **   <a name="WAF-Type-waf_XssMatchSet-Name"></a>
The name, if any, of the `XssMatchSet`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_waf_XssMatchSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/XssMatchSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/XssMatchSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/XssMatchSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
