---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_NetworkTrafficRule.html
---

# NetworkTrafficRule
<a name="API_NetworkTrafficRule"></a>

A rule that controls network traffic during penetration testing by allowing or denying traffic to specific URL patterns.

## Contents
<a name="API_NetworkTrafficRule_Contents"></a>

 ** effect **   <a name="securityagent-Type-NetworkTrafficRule-effect"></a>
The effect of the rule. Valid values are ALLOW and DENY.
Type: String
Valid Values: `ALLOW | DENY`
Required: No

 ** networkTrafficRuleType **   <a name="securityagent-Type-NetworkTrafficRule-networkTrafficRuleType"></a>
The type of the network traffic rule. Currently, only URL is supported.
Type: String
Valid Values: `URL`
Required: No

 ** pattern **   <a name="securityagent-Type-NetworkTrafficRule-pattern"></a>
The URL pattern to match for the rule.
Type: String
Required: No

## See Also
<a name="API_NetworkTrafficRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/NetworkTrafficRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/NetworkTrafficRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/NetworkTrafficRule)
