---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_BGPPeer.html
---

# BGPPeer
<a name="API_BGPPeer"></a>

Information about a BGP peer.

## Contents
<a name="API_BGPPeer_Contents"></a>

 ** addressFamily **   <a name="DX-Type-BGPPeer-addressFamily"></a>
The address family for the BGP peer.
Type: String
Valid Values: `ipv4 | ipv6`
Required: No

 ** amazonAddress **   <a name="DX-Type-BGPPeer-amazonAddress"></a>
The IP address assigned to the Amazon interface.
Type: String
Required: No

 ** asn **   <a name="DX-Type-BGPPeer-asn"></a>
The autonomous system number (ASN). The valid range is from 1 to 2147483646 for Border Gateway Protocol (BGP) configuration. If you provide a number greater than the maximum, an error is returned. Use `asnLong` instead.
+ You can use `asnLong` or `asn`, but not both. We recommend using `asnLong` as it supports a greater pool of numbers.
+ If you provide a value in the same API call for both `asn` and `asnLong`, the API will only accept the value for `asnLong`.
+ If you enter a 4-byte ASN for the `asn` parameter, the API returns an error.
+ If you are using a 2-byte ASN, the API response will include the 2-byte value for both the `asn` and `asnLong` fields.
Type: Integer
Required: No

 ** asnLong **   <a name="DX-Type-BGPPeer-asnLong"></a>
The long ASN for the BGP peer. The valid range is from 1 to 4294967294 for BGP configuration.
Note the following limitations when using `asnLong`:
+ You can use `asnLong` or `asn`, but not both. We recommend using `asnLong` as it supports a greater pool of numbers.
+  `asnLong` accepts any valid ASN value, regardless if it's 2-byte or 4-byte.
+ When using a 4-byte `asnLong`, the API response returns `0` for the legacy `asn` attribute since 4-byte ASN values exceed the maximum supported value of 2,147,483,647.
+ If you are using a 2-byte ASN, the API response will include the 2-byte value for both the `asn` and `asnLong` fields.
+ If you provide a value in the same API call for both `asn` and `asnLong`, the API will only accept the value for `asnLong`.
Type: Long
Required: No

 ** authKey **   <a name="DX-Type-BGPPeer-authKey"></a>
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.
Type: String
Required: No

 ** awsDeviceV2 **   <a name="DX-Type-BGPPeer-awsDeviceV2"></a>
The Direct Connect endpoint that terminates the BGP peer.
Type: String
Required: No

 ** awsLogicalDeviceId **   <a name="DX-Type-BGPPeer-awsLogicalDeviceId"></a>
The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.
Type: String
Required: No

 ** bgpPeerId **   <a name="DX-Type-BGPPeer-bgpPeerId"></a>
The ID of the BGP peer.
Type: String
Required: No

 ** bgpPeerState **   <a name="DX-Type-BGPPeer-bgpPeerState"></a>
The state of the BGP peer. The following are the possible values:
+  `verifying`: The BGP peering addresses or ASN require validation before the BGP peer can be created. This state applies only to public virtual interfaces.
+  `pending`: The BGP peer is created, and remains in this state until it is ready to be established.
+  `available`: The BGP peer is ready to be established.
+  `deleting`: The BGP peer is being deleted.
+  `deleted`: The BGP peer is deleted and cannot be established.
Type: String
Valid Values: `verifying | pending | available | deleting | deleted`
Required: No

 ** bgpStatus **   <a name="DX-Type-BGPPeer-bgpStatus"></a>
The status of the BGP peer. The following are the possible values:
+  `up`: The BGP peer is established. This state does not indicate the state of the routing function. Ensure that you are receiving routes over the BGP session.
+  `down`: The BGP peer is down.
+  `unknown`: The BGP peer status is not available.
Type: String
Valid Values: `up | down | unknown`
Required: No

 ** customerAddress **   <a name="DX-Type-BGPPeer-customerAddress"></a>
The IP address assigned to the customer interface.
Type: String
Required: No

## See Also
<a name="API_BGPPeer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/BGPPeer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/BGPPeer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/BGPPeer)
