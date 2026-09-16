---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateBGPPeer.html
---

# CreateBGPPeer
<a name="API_CreateBGPPeer"></a>

Creates a BGP peer on the specified virtual interface.

You must create a BGP peer for the corresponding address family (IPv4/IPv6) in order to access AWS resources that also use that address family.

If logical redundancy is not supported by the connection, interconnect, or LAG, the BGP peer cannot be in the same address family as an existing BGP peer on the virtual interface.

When creating a IPv6 BGP peer, omit the Amazon address and customer address. IPv6 addresses are automatically assigned from the Amazon pool of IPv6 addresses; you cannot specify custom IPv6 addresses.

**Important**
If you let AWS auto-assign IPv4 addresses, a /30 CIDR will be allocated from 169.254.0.0/16. AWS does not recommend this option if you intend to use the customer router peer IP address as the source and destination for traffic. Instead you should use RFC 1918 or other addressing, and specify the address yourself. For more information about RFC 1918 see [ Address Allocation for Private Internets](https://datatracker.ietf.org/doc/html/rfc1918).

For a public virtual interface, the Autonomous System Number (ASN) must be private or already on the allow list for the virtual interface.

## Request Syntax
<a name="API_CreateBGPPeer_RequestSyntax"></a>

```
{
   "newBGPPeer": {
      "addressFamily": "{{string}}",
      "amazonAddress": "{{string}}",
      "asn": {{number}},
      "asnLong": {{number}},
      "authKey": "{{string}}",
      "customerAddress": "{{string}}"
   },
   "virtualInterfaceId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateBGPPeer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [newBGPPeer](#API_CreateBGPPeer_RequestSyntax) **   <a name="DX-CreateBGPPeer-request-newBGPPeer"></a>
Information about the BGP peer.
Type: [NewBGPPeer](API_NewBGPPeer.md) object
Required: No

 ** [virtualInterfaceId](#API_CreateBGPPeer_RequestSyntax) **   <a name="DX-CreateBGPPeer-request-virtualInterfaceId"></a>
The ID of the virtual interface.
Type: String
Required: No

## Response Syntax
<a name="API_CreateBGPPeer_ResponseSyntax"></a>

```
{
   "virtualInterface": {
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
}
```

## Response Elements
<a name="API_CreateBGPPeer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [virtualInterface](#API_CreateBGPPeer_ResponseSyntax) **   <a name="DX-CreateBGPPeer-response-virtualInterface"></a>
The virtual interface.
Type: [VirtualInterface](API_VirtualInterface.md) object

## Errors
<a name="API_CreateBGPPeer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_CreateBGPPeer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/CreateBGPPeer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/CreateBGPPeer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/CreateBGPPeer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/CreateBGPPeer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/CreateBGPPeer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/CreateBGPPeer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/CreateBGPPeer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/CreateBGPPeer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/CreateBGPPeer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/CreateBGPPeer)
