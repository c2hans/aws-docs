---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ClientVpnConnection.html
---

# ClientVpnConnection
<a name="API_ClientVpnConnection"></a>

Describes a client connection.

## Contents
<a name="API_ClientVpnConnection_Contents"></a>

 ** clientIp **
The IP address of the client.
Type: String
Required: No

 ** clientIpv6Address **
The IPv6 address assigned to the client connection when using a dual-stack Client VPN endpoint. This field is only populated when the endpoint is configured for dual-stack addressing, and the client is using IPv6 for connectivity.
Type: String
Required: No

 ** clientVpnEndpointId **
The ID of the Client VPN endpoint to which the client is connected.
Type: String
Required: No

 ** commonName **
The common name associated with the client. This is either the name of the client certificate, or the Active Directory user name.
Type: String
Required: No

 ** connectionEndTime **
The date and time the client connection was terminated.
Type: String
Required: No

 ** connectionEstablishedTime **
The date and time the client connection was established.
Type: String
Required: No

 ** connectionId **
The ID of the client connection.
Type: String
Required: No

 ** egressBytes **
The number of bytes received by the client.
Type: String
Required: No

 ** egressPackets **
The number of packets received by the client.
Type: String
Required: No

 ** ingressBytes **
The number of bytes sent by the client.
Type: String
Required: No

 ** ingressPackets **
The number of packets sent by the client.
Type: String
Required: No

 ** PostureComplianceStatusSet.N **
The statuses returned by the client connect handler for posture compliance, if applicable.
Type: Array of strings
Required: No

 ** status **
The current state of the client connection.
Type: [ClientVpnConnectionStatus](API_ClientVpnConnectionStatus.md) object
Required: No

 ** timestamp **
The current date and time.
Type: String
Required: No

 ** username **
The username of the client who established the client connection. This information is only provided if Active Directory client authentication is used.
Type: String
Required: No

## See Also
<a name="API_ClientVpnConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ClientVpnConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ClientVpnConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ClientVpnConnection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
