---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_Connection.html
---

# Connection
<a name="API_Connection"></a>

Information about an Direct Connect connection.

## Contents
<a name="API_Connection_Contents"></a>

 ** awsDevice **   <a name="DX-Type-Connection-awsDevice"></a>
 *This member has been deprecated.*
The Direct Connect endpoint on which the physical connection terminates.
Type: String
Required: No

 ** awsDeviceV2 **   <a name="DX-Type-Connection-awsDeviceV2"></a>
The Direct Connect endpoint that terminates the physical connection.
Type: String
Required: No

 ** awsLogicalDeviceId **   <a name="DX-Type-Connection-awsLogicalDeviceId"></a>
The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.
Type: String
Required: No

 ** bandwidth **   <a name="DX-Type-Connection-bandwidth"></a>
The bandwidth of the connection.
Type: String
Required: No

 ** billingMode **   <a name="DX-Type-Connection-billingMode"></a>
The billing mode of the connection.
Type: String
Valid Values: `PayAsYouGo | FlatRateTier1 | FlatRateTier2 | FlatRateTier3 | FlatRateTier4 | FlatRateTier5 | PortPairFlatRateTier1 | PortPairFlatRateTier2 | PortPairFlatRateTier3 | PortPairFlatRateTier4 | PortPairFlatRateTier5`
Required: No

 ** connectionId **   <a name="DX-Type-Connection-connectionId"></a>
The ID of the connection.
Type: String
Required: No

 ** connectionName **   <a name="DX-Type-Connection-connectionName"></a>
The name of the connection.
Type: String
Required: No

 ** connectionState **   <a name="DX-Type-Connection-connectionState"></a>
The state of the connection. The following are the possible values:
+  `ordering`: The initial state of a hosted connection provisioned on an interconnect. The connection stays in the ordering state until the owner of the hosted connection confirms or declines the connection order.
+  `requested`: The initial state of a standard connection. The connection stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
+  `pending`: The connection has been approved and is being initialized.
+  `available`: The network link is up and the connection is ready for use.
+  `down`: The network link is down.
+  `deleting`: The connection is being deleted.
+  `deleted`: The connection has been deleted.
+  `rejected`: A hosted connection in the `ordering` state enters the `rejected` state if it is deleted by the customer.
+  `unknown`: The state of the connection is not available.
Type: String
Valid Values: `ordering | requested | pending | available | down | deleting | deleted | rejected | unknown`
Required: No

 ** encryptionMode **   <a name="DX-Type-Connection-encryptionMode"></a>
The MAC Security (MACsec) connection encryption mode.
The valid values are `no_encrypt`, `should_encrypt`, and `must_encrypt`.
Type: String
Required: No

 ** hasLogicalRedundancy **   <a name="DX-Type-Connection-hasLogicalRedundancy"></a>
Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).
Type: String
Valid Values: `unknown | yes | no`
Required: No

 ** jumboFrameCapable **   <a name="DX-Type-Connection-jumboFrameCapable"></a>
Indicates whether jumbo frames are supported.
Type: Boolean
Required: No

 ** lagId **   <a name="DX-Type-Connection-lagId"></a>
The ID of the LAG.
Type: String
Required: No

 ** loaIssueTime **   <a name="DX-Type-Connection-loaIssueTime"></a>
The time of the most recent call to [DescribeLoa](API_DescribeLoa.md) for this connection.
Type: Timestamp
Required: No

 ** location **   <a name="DX-Type-Connection-location"></a>
The location of the connection.
Type: String
Required: No

 ** macSecCapable **   <a name="DX-Type-Connection-macSecCapable"></a>
Indicates whether the connection supports MAC Security (MACsec).
Type: Boolean
Required: No

 ** macSecKeys **   <a name="DX-Type-Connection-macSecKeys"></a>
The MAC Security (MACsec) security keys associated with the connection.
Type: Array of [MacSecKey](API_MacSecKey.md) objects
Required: No

 ** ownerAccount **   <a name="DX-Type-Connection-ownerAccount"></a>
The ID of the AWS account that owns the connection.
Type: String
Required: No

 ** partnerInterconnectMacSecCapable **   <a name="DX-Type-Connection-partnerInterconnectMacSecCapable"></a>
Indicates whether the interconnect hosting this connection supports MAC Security (MACsec).
Type: Boolean
Required: No

 ** partnerName **   <a name="DX-Type-Connection-partnerName"></a>
The name of the Direct Connect service provider associated with the connection.
Type: String
Required: No

 ** portEncryptionStatus **   <a name="DX-Type-Connection-portEncryptionStatus"></a>
The MAC Security (MACsec) port link status of the connection.
The valid values are `Encryption Up`, which means that there is an active Connection Key Name, or `Encryption Down`.
Type: String
Required: No

 ** prefixPoolSizeIpv4 **   <a name="DX-Type-Connection-prefixPoolSizeIpv4"></a>
The total number of inbound IPv4 route prefixes you can allocate across the virtual interfaces on the connection. Not applicable to hosted connections or interconnects.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** prefixPoolSizeIpv6 **   <a name="DX-Type-Connection-prefixPoolSizeIpv6"></a>
The total number of inbound IPv6 route prefixes you can allocate across the virtual interfaces on the connection. Not applicable to hosted connections or interconnects.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** prefixPoolUnallocatedCountIpv4 **   <a name="DX-Type-Connection-prefixPoolUnallocatedCountIpv4"></a>
The number of inbound IPv4 route prefixes in the connection prefix pool not yet allocated to a virtual interface. Not applicable to hosted connections or interconnects.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** prefixPoolUnallocatedCountIpv6 **   <a name="DX-Type-Connection-prefixPoolUnallocatedCountIpv6"></a>
The number of inbound IPv6 route prefixes in the connection prefix pool not yet allocated to a virtual interface. Not applicable to hosted connections or interconnects.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** providerName **   <a name="DX-Type-Connection-providerName"></a>
The name of the service provider associated with the connection.
Type: String
Required: No

 ** rateLimiterStatus **   <a name="DX-Type-Connection-rateLimiterStatus"></a>
The rate limiter status for the connection, including how many rate limiters are in use and the maximum allowed.
Type: [RateLimiterStatus](API_RateLimiterStatus.md) object
Required: No

 ** region **   <a name="DX-Type-Connection-region"></a>
The AWS Region where the connection is located.
Type: String
Required: No

 ** tags **   <a name="DX-Type-Connection-tags"></a>
The tags associated with the connection.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** vlan **   <a name="DX-Type-Connection-vlan"></a>
The ID of the VLAN.
Type: Integer
Required: No

## See Also
<a name="API_Connection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/Connection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/Connection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/Connection)
