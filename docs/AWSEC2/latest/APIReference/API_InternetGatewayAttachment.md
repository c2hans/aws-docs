---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InternetGatewayAttachment.html
---

# InternetGatewayAttachment
<a name="API_InternetGatewayAttachment"></a>

Describes the attachment of a VPC to an internet gateway or an egress-only internet gateway.

## Contents
<a name="API_InternetGatewayAttachment_Contents"></a>

 ** state **
The current state of the attachment. For an internet gateway, the state is `available` when attached to a VPC; otherwise, this value is not returned.
Type: String
Valid Values: `attaching | attached | detaching | detached`
Required: No

 ** vpcId **
The ID of the VPC.
Type: String
Required: No

## See Also
<a name="API_InternetGatewayAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InternetGatewayAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InternetGatewayAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InternetGatewayAttachment)
