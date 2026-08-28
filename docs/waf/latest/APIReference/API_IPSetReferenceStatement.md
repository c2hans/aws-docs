---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_IPSetReferenceStatement.html
---

# IPSetReferenceStatement
<a name="API_IPSetReferenceStatement"></a>

A rule statement used to detect web requests coming from particular IP addresses or address ranges. To use this, create an [IPSet](API_IPSet.md) that specifies the addresses you want to detect, then use the ARN of that set in this statement. To create an IP set, see [CreateIPSet](API_CreateIPSet.md).

Each IP set rule statement references an IP set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.

## Contents
<a name="API_IPSetReferenceStatement_Contents"></a>

 ** ARN **   <a name="WAF-Type-IPSetReferenceStatement-ARN"></a>
The Amazon Resource Name (ARN) of the [IPSet](API_IPSet.md) that this statement references.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*\S.*`
Required: Yes

 ** IPSetForwardedIPConfig **   <a name="WAF-Type-IPSetReferenceStatement-IPSetForwardedIPConfig"></a>
The configuration for inspecting IP addresses in an HTTP header that you specify, instead of using the IP address that's reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name.
If the specified header isn't present in the request, AWS WAF doesn't apply the rule to the web request at all.
Type: [IPSetForwardedIPConfig](API_IPSetForwardedIPConfig.md) object
Required: No

## See Also
<a name="API_IPSetReferenceStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/IPSetReferenceStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/IPSetReferenceStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/IPSetReferenceStatement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
