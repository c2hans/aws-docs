---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ActionDefinition.html
---

# ActionDefinition
<a name="API_ActionDefinition"></a>

A custom action to use in stateless rule actions settings. This is used in [CustomAction](API_CustomAction.md).

## Contents
<a name="API_ActionDefinition_Contents"></a>

 ** PublishMetricAction **   <a name="networkfirewall-Type-ActionDefinition-PublishMetricAction"></a>
Stateless inspection criteria that publishes the specified metrics to Amazon CloudWatch for the matching packet. This setting defines a CloudWatch dimension value to be published.
You can pair this custom action with any of the standard stateless rule actions. For example, you could pair this in a rule action with the standard action that forwards the packet for stateful inspection. Then, when a packet matches the rule, Network Firewall publishes metrics for the packet and forwards it.
Type: [PublishMetricAction](API_PublishMetricAction.md) object
Required: No

## See Also
<a name="API_ActionDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ActionDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ActionDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ActionDefinition)
