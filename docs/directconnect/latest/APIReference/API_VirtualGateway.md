---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_VirtualGateway.html
---

# VirtualGateway
<a name="API_VirtualGateway"></a>

Information about a virtual private gateway for a private virtual interface.

## Contents
<a name="API_VirtualGateway_Contents"></a>

 ** virtualGatewayId **   <a name="DX-Type-VirtualGateway-virtualGatewayId"></a>
The ID of the virtual private gateway.
Type: String
Required: No

 ** virtualGatewayState **   <a name="DX-Type-VirtualGateway-virtualGatewayState"></a>
The state of the virtual private gateway. The following are the possible values:
+  `pending`: Initial state after creating the virtual private gateway.
+  `available`: Ready for use by a private virtual interface.
+  `deleting`: Initial state after deleting the virtual private gateway.
+  `deleted`: The virtual private gateway is deleted. The private virtual interface is unable to send traffic over this gateway.
Type: String
Required: No

## See Also
<a name="API_VirtualGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/VirtualGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/VirtualGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/VirtualGateway)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
