---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateGatewayBridgeSourceRequest.html
---

# UpdateGatewayBridgeSourceRequest
<a name="API_UpdateGatewayBridgeSourceRequest"></a>

 The source configuration for cloud flows receiving a stream from a bridge.

## Contents
<a name="API_UpdateGatewayBridgeSourceRequest_Contents"></a>

 ** bridgeArn **   <a name="mediaconnect-Type-UpdateGatewayBridgeSourceRequest-bridgeArn"></a>
 The ARN of the bridge feeding this flow.
Type: String
Pattern: `arn:.+:mediaconnect.+:bridge:.+`
Required: No

 ** vpcInterfaceAttachment **   <a name="mediaconnect-Type-UpdateGatewayBridgeSourceRequest-vpcInterfaceAttachment"></a>
 The name of the VPC interface attachment to use for this bridge source.
Type: [VpcInterfaceAttachment](API_VpcInterfaceAttachment.md) object
Required: No

## See Also
<a name="API_UpdateGatewayBridgeSourceRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/UpdateGatewayBridgeSourceRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/UpdateGatewayBridgeSourceRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/UpdateGatewayBridgeSourceRequest)
