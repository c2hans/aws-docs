---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_IngressGatewayBridge.html
---

# IngressGatewayBridge
<a name="API_IngressGatewayBridge"></a>

Create a bridge with the ingress bridge type. An ingress bridge is a ground-to-cloud bridge. The content originates at your premises and is delivered to the cloud.

## Contents
<a name="API_IngressGatewayBridge_Contents"></a>

 ** maxBitrate **   <a name="mediaconnect-Type-IngressGatewayBridge-maxBitrate"></a>
The maximum expected bitrate (in bps) of the ingress bridge.
Type: Integer
Required: Yes

 ** maxOutputs **   <a name="mediaconnect-Type-IngressGatewayBridge-maxOutputs"></a>
The maximum number of outputs on the ingress bridge.
Type: Integer
Required: Yes

 ** instanceId **   <a name="mediaconnect-Type-IngressGatewayBridge-instanceId"></a>
The ID of the instance running this bridge.
Type: String
Required: No

## See Also
<a name="API_IngressGatewayBridge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/IngressGatewayBridge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/IngressGatewayBridge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/IngressGatewayBridge)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
