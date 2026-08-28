---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_Lag.html
---

# Lag
<a name="API_Lag"></a>

Information about a link aggregation group (LAG).

## Contents
<a name="API_Lag_Contents"></a>

 ** allowsHostedConnections **   <a name="DX-Type-Lag-allowsHostedConnections"></a>
Indicates whether the LAG can host other connections.
Type: Boolean
Required: No

 ** awsDevice **   <a name="DX-Type-Lag-awsDevice"></a>
 *This member has been deprecated.*
The Direct Connect endpoint that hosts the LAG.
Type: String
Required: No

 ** awsDeviceV2 **   <a name="DX-Type-Lag-awsDeviceV2"></a>
The Direct Connect endpoint that hosts the LAG.
Type: String
Required: No

 ** awsLogicalDeviceId **   <a name="DX-Type-Lag-awsLogicalDeviceId"></a>
The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.
Type: String
Required: No

 ** connections **   <a name="DX-Type-Lag-connections"></a>
The connections bundled by the LAG.
Type: Array of [Connection](API_Connection.md) objects
Required: No

 ** connectionsBandwidth **   <a name="DX-Type-Lag-connectionsBandwidth"></a>
The individual bandwidth of the physical connections bundled by the LAG. The possible values are 1Gbps, 10Gbps, 100Gbps, or 400 Gbps..
Type: String
Required: No

 ** encryptionMode **   <a name="DX-Type-Lag-encryptionMode"></a>
The LAG MAC Security (MACsec) encryption mode.
The valid values are `no_encrypt`, `should_encrypt`, and `must_encrypt`.
Type: String
Required: No

 ** hasLogicalRedundancy **   <a name="DX-Type-Lag-hasLogicalRedundancy"></a>
Indicates whether the LAG supports a secondary BGP peer in the same address family (IPv4/IPv6).
Type: String
Valid Values: `unknown | yes | no`
Required: No

 ** jumboFrameCapable **   <a name="DX-Type-Lag-jumboFrameCapable"></a>
Indicates whether jumbo frames are supported.
Type: Boolean
Required: No

 ** lagId **   <a name="DX-Type-Lag-lagId"></a>
The ID of the LAG.
Type: String
Required: No

 ** lagName **   <a name="DX-Type-Lag-lagName"></a>
The name of the LAG.
Type: String
Required: No

 ** lagState **   <a name="DX-Type-Lag-lagState"></a>
The state of the LAG. The following are the possible values:
+  `requested`: The initial state of a LAG. The LAG stays in the requested state until the Letter of Authorization (LOA) is available.
+  `pending`: The LAG has been approved and is being initialized.
+  `available`: The network link is established and the LAG is ready for use.
+  `down`: The network link is down.
+  `deleting`: The LAG is being deleted.
+  `deleted`: The LAG is deleted.
+  `unknown`: The state of the LAG is not available.
Type: String
Valid Values: `requested | pending | available | down | deleting | deleted | unknown`
Required: No

 ** location **   <a name="DX-Type-Lag-location"></a>
The location of the LAG.
Type: String
Required: No

 ** macSecCapable **   <a name="DX-Type-Lag-macSecCapable"></a>
Indicates whether the LAG supports MAC Security (MACsec).
Type: Boolean
Required: No

 ** macSecKeys **   <a name="DX-Type-Lag-macSecKeys"></a>
The MAC Security (MACsec) security keys associated with the LAG.
Type: Array of [MacSecKey](API_MacSecKey.md) objects
Required: No

 ** minimumLinks **   <a name="DX-Type-Lag-minimumLinks"></a>
The minimum number of physical dedicated connections that must be operational for the LAG itself to be operational.
Type: Integer
Required: No

 ** numberOfConnections **   <a name="DX-Type-Lag-numberOfConnections"></a>
The number of physical dedicated connections initially provisioned and bundled by the LAG. You can have a maximum of four connections when the port speed is 1 Gbps or 10 Gbps, or two when the port speed is 100 Gbps or 400 Gbps.
Type: Integer
Required: No

 ** ownerAccount **   <a name="DX-Type-Lag-ownerAccount"></a>
The ID of the AWS account that owns the LAG.
Type: String
Required: No

 ** prefixPoolSizeIpv4 **   <a name="DX-Type-Lag-prefixPoolSizeIpv4"></a>
The total number of inbound IPv4 route prefixes you can allocate across the virtual interfaces on the LAG. Not applicable to LAGs that are interconnects and support hosted connections.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** prefixPoolSizeIpv6 **   <a name="DX-Type-Lag-prefixPoolSizeIpv6"></a>
The total number of inbound IPv6 route prefixes you can allocate across the virtual interfaces on the LAG. Not applicable to LAGs that are interconnects and support hosted connections.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** prefixPoolUnallocatedCountIpv4 **   <a name="DX-Type-Lag-prefixPoolUnallocatedCountIpv4"></a>
The number of inbound IPv4 route prefixes in the LAG prefix pool not yet allocated to a virtual interface. Not applicable to LAGs that are interconnects and support hosted connections.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** prefixPoolUnallocatedCountIpv6 **   <a name="DX-Type-Lag-prefixPoolUnallocatedCountIpv6"></a>
The number of inbound IPv6 route prefixes in the LAG prefix pool not yet allocated to a virtual interface. Not applicable to LAGs that are interconnects and support hosted connections.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** providerName **   <a name="DX-Type-Lag-providerName"></a>
The name of the service provider associated with the LAG.
Type: String
Required: No

 ** rateLimiterStatus **   <a name="DX-Type-Lag-rateLimiterStatus"></a>
The rate limiter status for the LAG, including how many rate limiters are in use and the maximum allowed.
Type: [RateLimiterStatus](API_RateLimiterStatus.md) object
Required: No

 ** region **   <a name="DX-Type-Lag-region"></a>
The AWS Region where the connection is located.
Type: String
Required: No

 ** tags **   <a name="DX-Type-Lag-tags"></a>
The tags associated with the LAG.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_Lag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/Lag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/Lag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/Lag)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
