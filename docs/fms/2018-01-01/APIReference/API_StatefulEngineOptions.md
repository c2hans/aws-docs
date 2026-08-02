---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_StatefulEngineOptions.html
---

# StatefulEngineOptions
<a name="API_StatefulEngineOptions"></a>

Configuration settings for the handling of the stateful rule groups in a Network Firewall firewall policy.

## Contents
<a name="API_StatefulEngineOptions_Contents"></a>

 ** RuleOrder **   <a name="fms-Type-StatefulEngineOptions-RuleOrder"></a>
Indicates how to manage the order of stateful rule evaluation for the policy. Stateful rules are provided to the rule engine as Suricata compatible strings, and Suricata evaluates them based on certain settings. For more information, see [Evaluation order for stateful rules](https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html) in the * AWS Network Firewall Developer Guide*.
Default: `DEFAULT_ACTION_ORDER`
Type: String
Valid Values: `STRICT_ORDER | DEFAULT_ACTION_ORDER`
Required: No

 ** StreamExceptionPolicy **   <a name="fms-Type-StatefulEngineOptions-StreamExceptionPolicy"></a>
Indicates how Network Firewall should handle traffic when a network connection breaks midstream.
+  `DROP` - Fail closed and drop all subsequent traffic going to the firewall.
+  `CONTINUE` - Continue to apply rules to subsequent traffic without context from traffic before the break. This impacts the behavior of rules that depend on context. For example, with a stateful rule that drops HTTP traffic, Network Firewall won't match subsequent traffic because the it won't have the context from session initialization, which defines the application layer protocol as HTTP. However, a TCP-layer rule using a `flow:stateless` rule would still match, and so would the `aws:drop_strict` default action.
+  `REJECT` - Fail closed and drop all subsequent traffic going to the firewall. With this option, Network Firewall also sends a TCP reject packet back to the client so the client can immediately establish a new session. With the new session, Network Firewall will have context and will apply rules appropriately.

  For applications that are reliant on long-lived TCP connections that trigger Gateway Load Balancer idle timeouts, this is the recommended setting.
+  `FMS_IGNORE` - Firewall Manager doesn't monitor or modify the Network Firewall stream exception policy settings.
For more information, see [Stream exception policy in your firewall policy](https://docs.aws.amazon.com/network-firewall/latest/developerguide/stream-exception-policy.html) in the * AWS Network Firewall Developer Guide*.
Default: `FMS_IGNORE`
Type: String
Valid Values: `DROP | CONTINUE | REJECT | FMS_IGNORE`
Required: No

## See Also
<a name="API_StatefulEngineOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/StatefulEngineOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/StatefulEngineOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/StatefulEngineOptions)
