---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_WebACLSummary.html
---

# WebACLSummary
<a name="API_waf_WebACLSummary"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Contains the identifier and the name or description of the [WebACL](API_waf_WebACL.md).

## Contents
<a name="API_waf_WebACLSummary_Contents"></a>

 ** Name **   <a name="WAF-Type-waf_WebACLSummary-Name"></a>
A friendly name or description of the [WebACL](API_waf_WebACL.md). You can't change the name of a `WebACL` after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** WebACLId **   <a name="WAF-Type-waf_WebACLSummary-WebACLId"></a>
A unique identifier for a `WebACL`. You use `WebACLId` to get information about a `WebACL` (see [GetWebACL](API_waf_GetWebACL.md)), update a `WebACL` (see [UpdateWebACL](API_waf_UpdateWebACL.md)), and delete a `WebACL` from AWS WAF (see [DeleteWebACL](API_waf_DeleteWebACL.md)).
 `WebACLId` is returned by [CreateWebACL](API_waf_CreateWebACL.md) and by [ListWebACLs](API_waf_ListWebACLs.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_waf_WebACLSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/WebACLSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/WebACLSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/WebACLSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
