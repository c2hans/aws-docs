---
source_url: https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ResponseAction.html
---

# ResponseAction
<a name="API_ResponseAction"></a>

Specifies the action setting that Shield Advanced should use in the AWS WAF rules that it creates on behalf of the protected resource in response to DDoS attacks. You specify this as part of the configuration for the automatic application layer DDoS mitigation feature, when you enable or update automatic mitigation. Shield Advanced creates the AWS WAF rules in a Shield Advanced-managed rule group, inside the web ACL that you have associated with the resource.

## Contents
<a name="API_ResponseAction_Contents"></a>

 ** Block **   <a name="AWSShield-Type-ResponseAction-Block"></a>
Specifies that Shield Advanced should configure its AWS WAF rules with the AWS WAF `Block` action.
You must specify exactly one action, either `Block` or `Count`.
Type: [BlockAction](API_BlockAction.md) object
Required: No

 ** Count **   <a name="AWSShield-Type-ResponseAction-Count"></a>
Specifies that Shield Advanced should configure its AWS WAF rules with the AWS WAF `Count` action.
You must specify exactly one action, either `Block` or `Count`.
Type: [CountAction](API_CountAction.md) object
Required: No

## See Also
<a name="API_ResponseAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/ResponseAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/ResponseAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/ResponseAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
