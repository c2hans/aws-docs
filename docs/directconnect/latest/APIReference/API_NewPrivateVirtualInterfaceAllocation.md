---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_NewPrivateVirtualInterfaceAllocation.html
---

# NewPrivateVirtualInterfaceAllocation
<a name="API_NewPrivateVirtualInterfaceAllocation"></a>

Information about a private virtual interface to be provisioned on a connection.

## Contents
<a name="API_NewPrivateVirtualInterfaceAllocation_Contents"></a>

 ** virtualInterfaceName **   <a name="DX-Type-NewPrivateVirtualInterfaceAllocation-virtualInterfaceName"></a>
The name of the virtual interface assigned by the customer network. The name has a maximum of 100 characters. The following are valid characters: a-z, 0-9 and a hyphen (-).
Type: String
Required: Yes

 ** vlan **   <a name="DX-Type-NewPrivateVirtualInterfaceAllocation-vlan"></a>
The ID of the VLAN.
Type: Integer
Required: Yes

 ** addressFamily **   <a name="DX-Type-NewPrivateVirtualInterfaceAllocation-addressFamily"></a>
The address family for the BGP peer.
Type: String
Valid Values: `ipv4 | ipv6`
Required: No

 ** amazonAddress **   <a name="DX-Type-NewPrivateVirtualInterfaceAllocation-amazonAddress"></a>
The IP address assigned to the Amazon interface.
Type: String
Required: No

 ** asn **   <a name="DX-Type-NewPrivateVirtualInterfaceAllocation-asn"></a>
The autonomous system number (ASN). The valid range is from 1 to 2147483646 for Border Gateway Protocol (BGP) configuration. If you provide a number greater than the maximum, an error is returned. Use `asnLong` instead.
+ You can use `asnLong` or `asn`, but not both. We recommend using `asnLong` as it supports a greater pool of numbers.
+ If you provide a value in the same API call for both `asn` and `asnLong`, the API will only accept the value for `asnLong`.
+ If you enter a 4-byte ASN for the `asn` parameter, the API returns an error.
+ If you are using a 2-byte ASN, the API response will include the 2-byte value for both the `asn` and `asnLong` fields.
The valid values are 1-2147483646.
Type: Integer
Required: No

 ** asnLong **   <a name="DX-Type-NewPrivateVirtualInterfaceAllocation-asnLong"></a>
The ASN when allocating a new private virtual interface. The valid range is from 1 to 4294967294 for BGP configuration.
Note the following limitations when using `asnLong`:
+ You can use `asnLong` or `asn`, but not both. We recommend using `asnLong` as it supports a greater pool of numbers.
+  `asnLong` accepts any valid ASN value, regardless if it's 2-byte or 4-byte.
+ When using a 4-byte `asnLong`, the API response returns `0` for the legacy `asn` attribute since 4-byte ASN values exceed the maximum supported value of 2,147,483,647.
+ If you are using a 2-byte ASN, the API response will include the 2-byte value for both the `asn` and `asnLong` fields.
+ If you provide a value in the same API call for both `asn` and `asnLong`, the API will only accept the value for `asnLong`.
Type: Long
Required: No

 ** authKey **   <a name="DX-Type-NewPrivateVirtualInterfaceAllocation-authKey"></a>
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.
Type: String
Required: No

 ** customerAddress **   <a name="DX-Type-NewPrivateVirtualInterfaceAllocation-customerAddress"></a>
The IP address assigned to the customer interface.
Type: String
Required: No

 ** mtu **   <a name="DX-Type-NewPrivateVirtualInterfaceAllocation-mtu"></a>
The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 8500. The default value is 1500.
Type: Integer
Required: No

 ** rateLimit **   <a name="DX-Type-NewPrivateVirtualInterfaceAllocation-rateLimit"></a>
The rate limit (bandwidth allocation) to apply to the virtual interface. The rate limit restricts the maximum bandwidth that the virtual interface can use on the parent connection.
Type: String
Required: No

 ** tags **   <a name="DX-Type-NewPrivateVirtualInterfaceAllocation-tags"></a>
The tags associated with the private virtual interface.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_NewPrivateVirtualInterfaceAllocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/NewPrivateVirtualInterfaceAllocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/NewPrivateVirtualInterfaceAllocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/NewPrivateVirtualInterfaceAllocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
