---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_WafAction.html
---

# WafAction
<a name="API_wafRegional_WafAction"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

For the action that is associated with a rule in a `WebACL`, specifies the action that you want AWS WAF to perform when a web request matches all of the conditions in a rule. For the default action in a `WebACL`, specifies the action that you want AWS WAF to take when a web request doesn't match all of the conditions in any of the rules in a `WebACL`.

## Contents
<a name="API_wafRegional_WafAction_Contents"></a>

 ** Type **   <a name="WAF-Type-wafRegional_WafAction-Type"></a>
Specifies how you want AWS WAF to respond to requests that match the settings in a `Rule`. Valid settings include the following:
+  `ALLOW`: AWS WAF allows requests
+  `BLOCK`: AWS WAF blocks requests
+  `COUNT`: AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify `COUNT` for the default action for a `WebACL`.
Type: String
Valid Values: `BLOCK | ALLOW | COUNT`
Required: Yes

## See Also
<a name="API_wafRegional_WafAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/WafAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/WafAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/WafAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
