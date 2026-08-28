---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_BridgeFlowSource.html
---

# BridgeFlowSource
<a name="API_BridgeFlowSource"></a>

 The source of the bridge. A flow source originates in MediaConnect as an existing cloud flow.

## Contents
<a name="API_BridgeFlowSource_Contents"></a>

 ** flowArn **   <a name="mediaconnect-Type-BridgeFlowSource-flowArn"></a>
 The ARN of the cloud flow used as a source of this bridge.
Type: String
Required: Yes

 ** name **   <a name="mediaconnect-Type-BridgeFlowSource-name"></a>
 The name of the flow source.
Type: String
Required: Yes

 ** flowVpcInterfaceAttachment **   <a name="mediaconnect-Type-BridgeFlowSource-flowVpcInterfaceAttachment"></a>
 The name of the VPC interface attachment to use for this source.
Type: [VpcInterfaceAttachment](API_VpcInterfaceAttachment.md) object
Required: No

 ** outputArn **   <a name="mediaconnect-Type-BridgeFlowSource-outputArn"></a>
 The Amazon Resource Number (ARN) of the output.
Type: String
Required: No

## See Also
<a name="API_BridgeFlowSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/BridgeFlowSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/BridgeFlowSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/BridgeFlowSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
