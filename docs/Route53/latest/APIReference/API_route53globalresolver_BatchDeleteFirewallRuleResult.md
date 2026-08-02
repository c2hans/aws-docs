---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_BatchDeleteFirewallRuleResult.html
---

# BatchDeleteFirewallRuleResult
<a name="API_route53globalresolver_BatchDeleteFirewallRuleResult"></a>

Information about a firewall rule that was deleted in a batch operation.

## Contents
<a name="API_route53globalresolver_BatchDeleteFirewallRuleResult_Contents"></a>

 ** id **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchDeleteFirewallRuleResult-id"></a>
The unique identifier of the deleted firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

 ** clientToken **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchDeleteFirewallRuleResult-clientToken"></a>
The unique string that identified the request and ensured idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** name **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchDeleteFirewallRuleResult-name"></a>
The name of the deleted firewall rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`
Required: No

 ** status **   <a name="Route53GlobalResolver-Type-route53globalresolver_BatchDeleteFirewallRuleResult-status"></a>
The final status of the deleted firewall rule.
Type: String
Valid Values: `CREATING | OPERATIONAL | UPDATING | DELETING`
Required: No

## See Also
<a name="API_route53globalresolver_BatchDeleteFirewallRuleResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/BatchDeleteFirewallRuleResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/BatchDeleteFirewallRuleResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/BatchDeleteFirewallRuleResult)
