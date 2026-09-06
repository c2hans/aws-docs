---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateBridgeFlowSourceRequest.html
---

# UpdateBridgeFlowSourceRequest
<a name="API_UpdateBridgeFlowSourceRequest"></a>

 Update the flow source of the bridge.

## Contents
<a name="API_UpdateBridgeFlowSourceRequest_Contents"></a>

 ** flowArn **   <a name="mediaconnect-Type-UpdateBridgeFlowSourceRequest-flowArn"></a>
 The Amazon Resource Name (ARN) that identifies the MediaConnect resource from which to delete tags.
Type: String
Pattern: `arn:.+:mediaconnect.+:flow:.+`
Required: No

 ** flowVpcInterfaceAttachment **   <a name="mediaconnect-Type-UpdateBridgeFlowSourceRequest-flowVpcInterfaceAttachment"></a>
The name of the VPC interface attachment to use for this source.
Type: [VpcInterfaceAttachment](API_VpcInterfaceAttachment.md) object
Required: No

## See Also
<a name="API_UpdateBridgeFlowSourceRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/UpdateBridgeFlowSourceRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/UpdateBridgeFlowSourceRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/UpdateBridgeFlowSourceRequest)
