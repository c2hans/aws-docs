---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayPrefixListAttachment.html
---

# TransitGatewayPrefixListAttachment
<a name="API_TransitGatewayPrefixListAttachment"></a>

Describes a transit gateway prefix list attachment.

## Contents
<a name="API_TransitGatewayPrefixListAttachment_Contents"></a>

 ** resourceId **
The ID of the resource.
Type: String
Required: No

 ** resourceType **
The resource type. Note that the `tgw-peering` resource type has been deprecated.
Type: String
Valid Values: `vpc | vpn | vpn-concentrator | direct-connect-gateway | connect | peering | tgw-peering | client-vpn`
Required: No

 ** transitGatewayAttachmentId **
The ID of the attachment.
Type: String
Required: No

## See Also
<a name="API_TransitGatewayPrefixListAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayPrefixListAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayPrefixListAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayPrefixListAttachment)
