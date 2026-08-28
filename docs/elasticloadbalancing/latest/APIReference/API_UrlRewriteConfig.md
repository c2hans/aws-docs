---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_UrlRewriteConfig.html
---

# UrlRewriteConfig
<a name="API_UrlRewriteConfig"></a>

Information about a URL rewrite transform. This transform matches a pattern in the request URL and replaces it with the specified string.

## Contents
<a name="API_UrlRewriteConfig_Contents"></a>

 ** Rewrites.member.N **
The URL rewrite transform to apply to the request. The transform consists of a regular expression to match and a replacement string.
Type: Array of [RewriteConfig](API_RewriteConfig.md) objects
Required: No

## See Also
<a name="API_UrlRewriteConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/UrlRewriteConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/UrlRewriteConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/UrlRewriteConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
