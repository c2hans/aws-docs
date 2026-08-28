---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_HostHeaderRewriteConfig.html
---

# HostHeaderRewriteConfig
<a name="API_HostHeaderRewriteConfig"></a>

Information about a host header rewrite transform. This transform matches a pattern in the host header in an HTTP request and replaces it with the specified string.

## Contents
<a name="API_HostHeaderRewriteConfig_Contents"></a>

 ** Rewrites.member.N **
The host header rewrite transform. Each transform consists of a regular expression to match and a replacement string.
Type: Array of [RewriteConfig](API_RewriteConfig.md) objects
Required: No

## See Also
<a name="API_HostHeaderRewriteConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/HostHeaderRewriteConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/HostHeaderRewriteConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/HostHeaderRewriteConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
