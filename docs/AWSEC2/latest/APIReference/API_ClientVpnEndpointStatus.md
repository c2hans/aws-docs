---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ClientVpnEndpointStatus.html
---

# ClientVpnEndpointStatus
<a name="API_ClientVpnEndpointStatus"></a>

Describes the state of a Client VPN endpoint.

## Contents
<a name="API_ClientVpnEndpointStatus_Contents"></a>

 ** code **
The state of the Client VPN endpoint. Possible states include:
+  `pending-associate` - The Client VPN endpoint has been created but no target networks have been associated. The Client VPN endpoint cannot accept connections.
+  `available` - The Client VPN endpoint has been created and a target network has been associated. The Client VPN endpoint can accept connections.
+  `deleting` - The Client VPN endpoint is being deleted. The Client VPN endpoint cannot accept connections.
+  `deleted` - The Client VPN endpoint has been deleted. The Client VPN endpoint cannot accept connections.
+  `pending` - The Client VPN endpoint has been created with a Transit Gateway configuration and is waiting for the Transit Gateway attachment to be accepted. The Client VPN endpoint cannot accept connections.
Type: String
Valid Values: `pending-associate | available | deleting | deleted | pending`
Required: No

 ** message **
A message about the status of the Client VPN endpoint.
Type: String
Required: No

## See Also
<a name="API_ClientVpnEndpointStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ClientVpnEndpointStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ClientVpnEndpointStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ClientVpnEndpointStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
