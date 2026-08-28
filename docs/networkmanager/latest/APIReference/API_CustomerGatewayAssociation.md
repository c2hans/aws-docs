---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_CustomerGatewayAssociation.html
---

# CustomerGatewayAssociation
<a name="API_CustomerGatewayAssociation"></a>

Describes the association between a customer gateway, a device, and a link.

## Contents
<a name="API_CustomerGatewayAssociation_Contents"></a>

 ** CustomerGatewayArn **   <a name="networkmanager-Type-CustomerGatewayAssociation-CustomerGatewayArn"></a>
The Amazon Resource Name (ARN) of the customer gateway.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`
Required: No

 ** DeviceId **   <a name="networkmanager-Type-CustomerGatewayAssociation-DeviceId"></a>
The ID of the device.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** GlobalNetworkId **   <a name="networkmanager-Type-CustomerGatewayAssociation-GlobalNetworkId"></a>
The ID of the global network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** LinkId **   <a name="networkmanager-Type-CustomerGatewayAssociation-LinkId"></a>
The ID of the link.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** State **   <a name="networkmanager-Type-CustomerGatewayAssociation-State"></a>
The association state.
Type: String
Valid Values: `PENDING | AVAILABLE | DELETING | DELETED`
Required: No

## See Also
<a name="API_CustomerGatewayAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/CustomerGatewayAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/CustomerGatewayAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/CustomerGatewayAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
