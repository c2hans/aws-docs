---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_TransitGatewayPeering.html
---

# TransitGatewayPeering
<a name="API_TransitGatewayPeering"></a>

Describes a transit gateway peering attachment.

## Contents
<a name="API_TransitGatewayPeering_Contents"></a>

 ** Peering **   <a name="networkmanager-Type-TransitGatewayPeering-Peering"></a>
Describes a transit gateway peer connection.
Type: [Peering](API_Peering.md) object
Required: No

 ** TransitGatewayArn **   <a name="networkmanager-Type-TransitGatewayPeering-TransitGatewayArn"></a>
The ARN of the transit gateway.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`
Required: No

 ** TransitGatewayPeeringAttachmentId **   <a name="networkmanager-Type-TransitGatewayPeering-TransitGatewayPeeringAttachmentId"></a>
The ID of the transit gateway peering attachment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^tgw-attach-([0-9a-f]{8,17})$`
Required: No

## See Also
<a name="API_TransitGatewayPeering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/TransitGatewayPeering)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/TransitGatewayPeering)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/TransitGatewayPeering)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
