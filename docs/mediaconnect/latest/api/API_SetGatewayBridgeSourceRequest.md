---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_SetGatewayBridgeSourceRequest.html
---

# SetGatewayBridgeSourceRequest
<a name="API_SetGatewayBridgeSourceRequest"></a>

 The source configuration for cloud flows receiving a stream from a bridge.

## Contents
<a name="API_SetGatewayBridgeSourceRequest_Contents"></a>

 ** bridgeArn **   <a name="mediaconnect-Type-SetGatewayBridgeSourceRequest-bridgeArn"></a>
 The ARN of the bridge feeding this flow.
Type: String
Pattern: `arn:.+:mediaconnect.+:bridge:.+`
Required: Yes

 ** vpcInterfaceAttachment **   <a name="mediaconnect-Type-SetGatewayBridgeSourceRequest-vpcInterfaceAttachment"></a>
 The name of the VPC interface attachment to use for this bridge source.
Type: [VpcInterfaceAttachment](API_VpcInterfaceAttachment.md) object
Required: No

## See Also
<a name="API_SetGatewayBridgeSourceRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/SetGatewayBridgeSourceRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/SetGatewayBridgeSourceRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/SetGatewayBridgeSourceRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
