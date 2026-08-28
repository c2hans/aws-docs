---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AllocatePrivateVirtualInterface.html
---

# AllocatePrivateVirtualInterface
<a name="API_AllocatePrivateVirtualInterface"></a>

Provisions a private virtual interface to be owned by the specified AWS account.

Virtual interfaces created using this action must be confirmed by the owner using [ConfirmPrivateVirtualInterface](API_ConfirmPrivateVirtualInterface.md). Until then, the virtual interface is in the `Confirming` state and is not available to handle traffic.

## Request Syntax
<a name="API_AllocatePrivateVirtualInterface_RequestSyntax"></a>

```
{
   "connectionId": "{{string}}",
   "newPrivateVirtualInterfaceAllocation": {
      "addressFamily": "{{string}}",
      "amazonAddress": "{{string}}",
      "asn": {{number}},
      "asnLong": {{number}},
      "authKey": "{{string}}",
      "customerAddress": "{{string}}",
      "mtu": {{number}},
      "rateLimit": "{{string}}",
      "tags": [
         {
            "key": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "virtualInterfaceName": "{{string}}",
      "vlan": {{number}}
   },
   "ownerAccount": "{{string}}"
}
```

## Request Parameters
<a name="API_AllocatePrivateVirtualInterface_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [connectionId](#API_AllocatePrivateVirtualInterface_RequestSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-request-connectionId"></a>
The ID of the connection on which the private virtual interface is provisioned.
Type: String
Required: Yes

 ** [newPrivateVirtualInterfaceAllocation](#API_AllocatePrivateVirtualInterface_RequestSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-request-newPrivateVirtualInterfaceAllocation"></a>
Information about the private virtual interface.
Type: [NewPrivateVirtualInterfaceAllocation](API_NewPrivateVirtualInterfaceAllocation.md) object
Required: Yes

 ** [ownerAccount](#API_AllocatePrivateVirtualInterface_RequestSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-request-ownerAccount"></a>
The ID of the AWS account that owns the virtual private interface.
Type: String
Required: Yes

## Response Syntax
<a name="API_AllocatePrivateVirtualInterface_ResponseSyntax"></a>

```
{
   "addressFamily": "string",
   "amazonAddress": "string",
   "amazonSideAsn": number,
   "asn": number,
   "asnLong": number,
   "authKey": "string",
   "awsDeviceV2": "string",
   "awsLogicalDeviceId": "string",
   "bgpPeers": [
      {
         "addressFamily": "string",
         "amazonAddress": "string",
         "asn": number,
         "asnLong": number,
         "authKey": "string",
         "awsDeviceV2": "string",
         "awsLogicalDeviceId": "string",
         "bgpPeerId": "string",
         "bgpPeerState": "string",
         "bgpStatus": "string",
         "customerAddress": "string"
      }
   ],
   "connectionId": "string",
   "customerAddress": "string",
   "customerRouterConfig": "string",
   "directConnectGatewayId": "string",
   "jumboFrameCapable": boolean,
   "location": "string",
   "mtu": number,
   "ownerAccount": "string",
   "prefixPoolAllocatedCountIpv4": number,
   "prefixPoolAllocatedCountIpv6": number,
   "rateLimit": "string",
   "region": "string",
   "routeFilterPrefixes": [
      {
         "cidr": "string"
      }
   ],
   "siteLinkEnabled": boolean,
   "tags": [
      {
         "key": "string",
         "value": "string"
      }
   ],
   "virtualGatewayId": "string",
   "virtualInterfaceId": "string",
   "virtualInterfaceName": "string",
   "virtualInterfaceState": "string",
   "virtualInterfaceType": "string",
   "vlan": number
}
```

## Response Elements
<a name="API_AllocatePrivateVirtualInterface_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [addressFamily](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-addressFamily"></a>
The address family for the BGP peer.
Type: String
Valid Values: `ipv4 | ipv6`

 ** [amazonAddress](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-amazonAddress"></a>
The IP address assigned to the Amazon interface.
Type: String

 ** [amazonSideAsn](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-amazonSideAsn"></a>
The autonomous system number (AS) for the Amazon side of the connection.
Type: Long

 ** [asn](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-asn"></a>
The autonomous system number (ASN). The valid range is from 1 to 2147483646 for Border Gateway Protocol (BGP) configuration. If you provide a number greater than the maximum, an error is returned. Use `asnLong` instead.
+ You can use `asnLong` or `asn`, but not both. We recommend using `asnLong` as it supports a greater pool of numbers.
+ If you provide a value in the same API call for both `asn` and `asnLong`, the API will only accept the value for `asnLong`.
+ If you enter a 4-byte ASN for the `asn` parameter, the API returns an error.
+ If you are using a 2-byte ASN, the API response will include the 2-byte value for both the `asn` and `asnLong` fields.
Type: Integer

 ** [asnLong](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-asnLong"></a>
The long ASN for the virtual interface. The valid range is from 1 to 4294967294 for BGP configuration.
Note the following limitations when using `asnLong`:
+ You can use `asnLong` or `asn`, but not both. We recommend using `asnLong` as it supports a greater pool of numbers.
+  `asnLong` accepts any valid ASN value, regardless if it's 2-byte or 4-byte.
+ When using a 4-byte `asnLong`, the API response returns `0` for the legacy `asn` attribute since 4-byte ASN values exceed the maximum supported value of 2,147,483,647.
+ If you are using a 2-byte ASN, the API response will include the 2-byte value for both the `asn` and `asnLong` fields.
+ If you provide a value in the same API call for both `asn` and `asnLong`, the API will only accept the value for `asnLong`.
Type: Long

 ** [authKey](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-authKey"></a>
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.
Type: String

 ** [awsDeviceV2](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-awsDeviceV2"></a>
The Direct Connect endpoint that terminates the physical connection.
Type: String

 ** [awsLogicalDeviceId](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-awsLogicalDeviceId"></a>
The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.
Type: String

 ** [bgpPeers](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-bgpPeers"></a>
The BGP peers configured on this virtual interface.
Type: Array of [BGPPeer](API_BGPPeer.md) objects

 ** [connectionId](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-connectionId"></a>
The ID of the connection.
Type: String

 ** [customerAddress](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-customerAddress"></a>
The IP address assigned to the customer interface.
Type: String

 ** [customerRouterConfig](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-customerRouterConfig"></a>
The customer router configuration.
Type: String

 ** [directConnectGatewayId](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-directConnectGatewayId"></a>
The ID of the Direct Connect gateway.
Type: String

 ** [jumboFrameCapable](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-jumboFrameCapable"></a>
Indicates whether jumbo frames are supported.
Type: Boolean

 ** [location](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-location"></a>
The location of the connection.
Type: String

 ** [mtu](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-mtu"></a>
The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 8500. The default value is 1500
Type: Integer

 ** [ownerAccount](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-ownerAccount"></a>
The ID of the AWS account that owns the virtual interface.
Type: String

 ** [prefixPoolAllocatedCountIpv4](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-prefixPoolAllocatedCountIpv4"></a>
The number of inbound IPv4 route prefixes allocated to the virtual interface. Not applicable to public virtual interfaces.
Type: Integer
Valid Range: Minimum value of 0.

 ** [prefixPoolAllocatedCountIpv6](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-prefixPoolAllocatedCountIpv6"></a>
The number of inbound IPv6 route prefixes allocated to the virtual interface. Not applicable to public virtual interfaces.
Type: Integer
Valid Range: Minimum value of 0.

 ** [rateLimit](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-rateLimit"></a>
The rate limit (bandwidth allocation) applied to the virtual interface. The value must be one of the supported bandwidth values and cannot exceed the bandwidth of the parent connection or LAG. Supported values: `50Mbps`, `100Mbps`, `200Mbps`, `300Mbps`, `400Mbps`, `500Mbps`, `600Mbps`, `700Mbps`, `800Mbps`, `900Mbps`, `1Gbps`, `1.2Gbps`, `1.5Gbps`, `1.8Gbps`, `2Gbps`, `2.1Gbps`, `2.4Gbps`, `2.7Gbps`, `3Gbps`, `3.2Gbps`, `3.6Gbps`, `4Gbps`, `5Gbps`, `6Gbps`, `7Gbps`, `8Gbps`, `9Gbps`, `10Gbps`, `12Gbps`, `15Gbps`, `18Gbps`, `20Gbps`, `21Gbps`, `24Gbps`, `27Gbps`, `30Gbps`, `32Gbps`, `36Gbps`, `40Gbps`, `50Gbps`, `60Gbps`, `70Gbps`, `80Gbps`, `100Gbps`, `120Gbps`, `150Gbps`, `180Gbps`, `200Gbps`, `210Gbps`, `240Gbps`, `270Gbps`, `300Gbps`, `320Gbps`, `360Gbps`, `400Gbps`, `450Gbps`, `480Gbps`, `500Gbps`, `540Gbps`, `600Gbps`, `700Gbps`, `800Gbps`, `900Gbps`, `1Tbps`, `1.1Tbps`, `1.2Tbps`, `1.3Tbps`, `1.4Tbps`, `1.5Tbps`, `1.6Tbps`.
Type: String

 ** [region](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-region"></a>
The AWS Region where the virtual interface is located.
Type: String

 ** [routeFilterPrefixes](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-routeFilterPrefixes"></a>
The routes to be advertised to the AWS network in this Region. Applies to public virtual interfaces.
Type: Array of [RouteFilterPrefix](API_RouteFilterPrefix.md) objects

 ** [siteLinkEnabled](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-siteLinkEnabled"></a>
Indicates whether SiteLink is enabled.
Type: Boolean

 ** [tags](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-tags"></a>
The tags associated with the virtual interface.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.

 ** [virtualGatewayId](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-virtualGatewayId"></a>
The ID of the virtual private gateway. Applies only to private virtual interfaces.
Type: String

 ** [virtualInterfaceId](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-virtualInterfaceId"></a>
The ID of the virtual interface.
Type: String

 ** [virtualInterfaceName](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-virtualInterfaceName"></a>
The name of the virtual interface assigned by the customer network. The name has a maximum of 100 characters. The following are valid characters: a-z, 0-9 and a hyphen (-).
Type: String

 ** [virtualInterfaceState](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-virtualInterfaceState"></a>
The state of the virtual interface. The following are the possible values:
+  `confirming`: The creation of the virtual interface is pending confirmation from the virtual interface owner. If the owner of the virtual interface is different from the owner of the connection on which it is provisioned, then the virtual interface will remain in this state until it is confirmed by the virtual interface owner.
+  `verifying`: This state only applies to public virtual interfaces. Each public virtual interface needs validation before the virtual interface can be created.
+  `pending`: A virtual interface is in this state from the time that it is created until the virtual interface is ready to forward traffic.
+  `available`: A virtual interface that is able to forward traffic.
+  `down`: A virtual interface that is BGP down.
+  `testing`: A virtual interface is in this state immediately after calling [StartBgpFailoverTest](API_StartBgpFailoverTest.md) and remains in this state during the duration of the test.
+  `deleting`: A virtual interface is in this state immediately after calling [DeleteVirtualInterface](API_DeleteVirtualInterface.md) until it can no longer forward traffic.
+  `deleted`: A virtual interface that cannot forward traffic.
+  `rejected`: The virtual interface owner has declined creation of the virtual interface. If a virtual interface in the `Confirming` state is deleted by the virtual interface owner, the virtual interface enters the `Rejected` state.
+  `unknown`: The state of the virtual interface is not available.
Type: String
Valid Values: `confirming | verifying | pending | available | down | testing | deleting | deleted | rejected | unknown`

 ** [virtualInterfaceType](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-virtualInterfaceType"></a>
The type of virtual interface. The possible values are `private`, `public` and `transit`.
Type: String

 ** [vlan](#API_AllocatePrivateVirtualInterface_ResponseSyntax) **   <a name="DX-AllocatePrivateVirtualInterface-response-vlan"></a>
The ID of the VLAN.
Type: Integer

## Errors
<a name="API_AllocatePrivateVirtualInterface_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

 ** DuplicateTagKeysException **
A tag key was specified more than once.
HTTP Status Code: 400

 ** LimitExceededException **
The rate limiter limit has been exceeded for the connection. You cannot add more rate limiters to virtual interfaces on this connection.
HTTP Status Code: 400

 ** TooManyTagsException **
You have reached the limit on the number of tags that can be assigned.
HTTP Status Code: 400

## See Also
<a name="API_AllocatePrivateVirtualInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/AllocatePrivateVirtualInterface)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/AllocatePrivateVirtualInterface)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/AllocatePrivateVirtualInterface)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/AllocatePrivateVirtualInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/AllocatePrivateVirtualInterface)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/AllocatePrivateVirtualInterface)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/AllocatePrivateVirtualInterface)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/AllocatePrivateVirtualInterface)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/AllocatePrivateVirtualInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/AllocatePrivateVirtualInterface)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
