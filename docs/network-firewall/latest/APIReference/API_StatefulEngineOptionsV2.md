---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_StatefulEngineOptionsV2.html
---

# StatefulEngineOptionsV2
<a name="API_StatefulEngineOptionsV2"></a>

Configuration settings for the handling of stateful traffic in a Next Generation policy.

## Contents
<a name="API_StatefulEngineOptionsV2_Contents"></a>

 ** FlowTimeouts **   <a name="networkfirewall-Type-StatefulEngineOptionsV2-FlowTimeouts"></a>
The amount of time that can pass without any traffic sent through the firewall before the firewall determines that the connection is idle.
Type: [FlowTimeouts](API_FlowTimeouts.md) object
Required: No

 ** StreamExceptionPolicy **   <a name="networkfirewall-Type-StatefulEngineOptionsV2-StreamExceptionPolicy"></a>
How AWS Network Firewall handles traffic on a network connection that breaks midstream. A Next Generation policy supports `DROP` and `REJECT`. For more information, see [Stream exception policy options in your firewall policy](https://docs.aws.amazon.com/network-firewall/latest/developerguide/stream-exception-policy.html) in the * AWS Network Firewall Developer Guide*.
Type: String
Valid Values: `DROP | REJECT`
Required: No

## See Also
<a name="API_StatefulEngineOptionsV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/StatefulEngineOptionsV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/StatefulEngineOptionsV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/StatefulEngineOptionsV2)
