---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_UpdateParameters.html
---

# UpdateParameters

What an update requested.

## Contents
<a name="API_UpdateParameters_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** linkConfig **   <a name="rtbfabric-Type-UpdateParameters-linkConfig"></a>
The requested link configuration.
Type: [LinkConfigParameters](API_LinkConfigParameters.md) object
Required: No

 ** linkFlow **   <a name="rtbfabric-Type-UpdateParameters-linkFlow"></a>
The requested link flow.
Type: [LinkFlowParameters](API_LinkFlowParameters.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** responderGatewayConfig **   <a name="rtbfabric-Type-UpdateParameters-responderGatewayConfig"></a>
The requested responder gateway configuration.
Type: [ResponderGatewayConfigParameters](API_ResponderGatewayConfigParameters.md) object
Required: No

 ** routingRule **   <a name="rtbfabric-Type-UpdateParameters-routingRule"></a>
The requested routing rule.
Type: [RoutingRuleParameters](API_RoutingRuleParameters.md) object
Required: No

## See Also
<a name="API_UpdateParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/UpdateParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/UpdateParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/UpdateParameters)
