---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_Bridge.html
---

# Bridge
<a name="API_Bridge"></a>

 A Bridge is the connection between your data center's Instances and the AWS cloud. A bridge can be used to send video from the AWS cloud to your data center or from your data center to the AWS cloud.

## Contents
<a name="API_Bridge_Contents"></a>

 ** bridgeArn **   <a name="mediaconnect-Type-Bridge-bridgeArn"></a>
 The Amazon Resource Number (ARN) of the bridge.
Type: String
Required: Yes

 ** bridgeState **   <a name="mediaconnect-Type-Bridge-bridgeState"></a>
The state of the bridge.
Type: String
Valid Values: `CREATING | STANDBY | STARTING | DEPLOYING | ACTIVE | STOPPING | DELETING | DELETED | START_FAILED | START_PENDING | STOP_FAILED | UPDATING`
Required: Yes

 ** name **   <a name="mediaconnect-Type-Bridge-name"></a>
 The name of the bridge.
Type: String
Required: Yes

 ** placementArn **   <a name="mediaconnect-Type-Bridge-placementArn"></a>
 The placement Amazon Resource Number (ARN) of the bridge.
Type: String
Required: Yes

 ** bridgeMessages **   <a name="mediaconnect-Type-Bridge-bridgeMessages"></a>
 Messages with details about the bridge.
Type: Array of [MessageDetail](API_MessageDetail.md) objects
Required: No

 ** egressGatewayBridge **   <a name="mediaconnect-Type-Bridge-egressGatewayBridge"></a>
 An egress bridge is a cloud-to-ground bridge. The content comes from an existing MediaConnect flow and is delivered to your premises.
Type: [EgressGatewayBridge](API_EgressGatewayBridge.md) object
Required: No

 ** ingressGatewayBridge **   <a name="mediaconnect-Type-Bridge-ingressGatewayBridge"></a>
 An ingress bridge is a ground-to-cloud bridge. The content originates at your premises and is delivered to the cloud.
Type: [IngressGatewayBridge](API_IngressGatewayBridge.md) object
Required: No

 ** outputs **   <a name="mediaconnect-Type-Bridge-outputs"></a>
 The outputs on this bridge.
Type: Array of [BridgeOutput](API_BridgeOutput.md) objects
Required: No

 ** sourceFailoverConfig **   <a name="mediaconnect-Type-Bridge-sourceFailoverConfig"></a>
 The settings for source failover.
Type: [FailoverConfig](API_FailoverConfig.md) object
Required: No

 ** sources **   <a name="mediaconnect-Type-Bridge-sources"></a>
 The sources on this bridge.
Type: Array of [BridgeSource](API_BridgeSource.md) objects
Required: No

## See Also
<a name="API_Bridge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/Bridge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/Bridge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/Bridge)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
