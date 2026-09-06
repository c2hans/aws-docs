---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_Interconnect.html
---

# Interconnect
<a name="API_Interconnect"></a>

Information about an interconnect.

## Contents
<a name="API_Interconnect_Contents"></a>

 ** awsDevice **   <a name="DX-Type-Interconnect-awsDevice"></a>
 *This member has been deprecated.*
The Direct Connect endpoint on which the physical connection terminates.
Type: String
Required: No

 ** awsDeviceV2 **   <a name="DX-Type-Interconnect-awsDeviceV2"></a>
The Direct Connect endpoint that terminates the physical connection.
Type: String
Required: No

 ** awsLogicalDeviceId **   <a name="DX-Type-Interconnect-awsLogicalDeviceId"></a>
The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.
Type: String
Required: No

 ** bandwidth **   <a name="DX-Type-Interconnect-bandwidth"></a>
The bandwidth of the connection.
Type: String
Required: No

 ** encryptionMode **   <a name="DX-Type-Interconnect-encryptionMode"></a>
The MAC Security (MACsec) encryption mode.
The valid values are `no_encrypt`, `should_encrypt`, and `must_encrypt`.
Type: String
Required: No

 ** hasLogicalRedundancy **   <a name="DX-Type-Interconnect-hasLogicalRedundancy"></a>
Indicates whether the interconnect supports a secondary BGP in the same address family (IPv4/IPv6).
Type: String
Valid Values: `unknown | yes | no`
Required: No

 ** interconnectId **   <a name="DX-Type-Interconnect-interconnectId"></a>
The ID of the interconnect.
Type: String
Required: No

 ** interconnectName **   <a name="DX-Type-Interconnect-interconnectName"></a>
The name of the interconnect.
Type: String
Required: No

 ** interconnectState **   <a name="DX-Type-Interconnect-interconnectState"></a>
The state of the interconnect. The following are the possible values:
+  `requested`: The initial state of an interconnect. The interconnect stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
+  `pending`: The interconnect is approved, and is being initialized.
+  `available`: The network link is up, and the interconnect is ready for use.
+  `down`: The network link is down.
+  `deleting`: The interconnect is being deleted.
+  `deleted`: The interconnect is deleted.
+  `unknown`: The state of the interconnect is not available.
Type: String
Valid Values: `requested | pending | available | down | deleting | deleted | unknown`
Required: No

 ** jumboFrameCapable **   <a name="DX-Type-Interconnect-jumboFrameCapable"></a>
Indicates whether jumbo frames are supported.
Type: Boolean
Required: No

 ** lagId **   <a name="DX-Type-Interconnect-lagId"></a>
The ID of the LAG.
Type: String
Required: No

 ** loaIssueTime **   <a name="DX-Type-Interconnect-loaIssueTime"></a>
The time of the most recent call to [DescribeLoa](API_DescribeLoa.md) for this connection.
Type: Timestamp
Required: No

 ** location **   <a name="DX-Type-Interconnect-location"></a>
The location of the connection.
Type: String
Required: No

 ** macSecCapable **   <a name="DX-Type-Interconnect-macSecCapable"></a>
Indicates whether the interconnect supports MAC Security (MACsec).
Type: Boolean
Required: No

 ** macSecKeys **   <a name="DX-Type-Interconnect-macSecKeys"></a>
The MAC Security (MACsec) security keys.
Type: Array of [MacSecKey](API_MacSecKey.md) objects
Required: No

 ** portEncryptionStatus **   <a name="DX-Type-Interconnect-portEncryptionStatus"></a>
The MAC Security (MACsec) port link status.
The valid values are `Encryption Up`, which means that there is an active Connection Key Name, or `Encryption Down`.
Type: String
Required: No

 ** providerName **   <a name="DX-Type-Interconnect-providerName"></a>
The name of the service provider associated with the interconnect.
Type: String
Required: No

 ** region **   <a name="DX-Type-Interconnect-region"></a>
The AWS Region where the connection is located.
Type: String
Required: No

 ** tags **   <a name="DX-Type-Interconnect-tags"></a>
The tags associated with the interconnect.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_Interconnect_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/Interconnect)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/Interconnect)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/Interconnect)
