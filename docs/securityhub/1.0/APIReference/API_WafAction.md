---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_WafAction.html
---

# WafAction
<a name="API_WafAction"></a>

Details about the action that CloudFront or AWS WAF takes when a web request matches the conditions in the rule.

## Contents
<a name="API_WafAction_Contents"></a>

 ** Type **   <a name="securityhub-Type-WafAction-Type"></a>
Specifies how you want AWS WAF to respond to requests that match the settings in a rule.
Valid settings include the following:
+  `ALLOW` - AWS WAF allows requests
+  `BLOCK` - AWS WAF blocks requests
+  `COUNT` - AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify `COUNT` for the default action for a web ACL.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_WafAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/WafAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/WafAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/WafAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
