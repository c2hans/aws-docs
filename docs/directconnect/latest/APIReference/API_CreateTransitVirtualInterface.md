---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateTransitVirtualInterface.html
---

# CreateTransitVirtualInterface
<a name="API_CreateTransitVirtualInterface"></a>

Creates a transit virtual interface. A transit virtual interface should be used to access one or more transit gateways associated with Direct Connect gateways. A transit virtual interface enables the connection of multiple VPCs attached to a transit gateway to a Direct Connect gateway.

**Important**
If you associate your transit gateway with one or more Direct Connect gateways, the Autonomous System Number (ASN) used by the transit gateway and the Direct Connect gateway must be different. For example, if you use the default ASN 64512 for both your the transit gateway and Direct Connect gateway, the association request fails.

A jumbo MTU value must be either 1500 or 8500. No other values will be accepted. Setting the MTU of a virtual interface to 8500 (jumbo frames) can cause an update to the underlying physical connection if it wasn't updated to support jumbo frames. Updating the connection disrupts network connectivity for all virtual interfaces associated with the connection for up to 30 seconds. To check whether your connection supports jumbo frames, call [DescribeConnections](API_DescribeConnections.md). To check whether your virtual interface supports jumbo frames, call [DescribeVirtualInterfaces](API_DescribeVirtualInterfaces.md).

## Request Syntax
<a name="API_CreateTransitVirtualInterface_RequestSyntax"></a>

```
{
   "connectionId": "{{string}}",
   "newTransitVirtualInterface": {
      "addressFamily": "{{string}}",
      "amazonAddress": "{{string}}",
      "asn": {{number}},
      "asnLong": {{number}},
      "authKey": "{{string}}",
      "customerAddress": "{{string}}",
      "directConnectGatewayId": "{{string}}",
      "enableSiteLink": {{boolean}},
      "mtu": {{number}},
      "prefixPoolAllocatedCountIpv4": {{number}},
      "prefixPoolAllocatedCountIpv6": {{number}},
      "rateLimit": "{{string}}",
      "tags": [
         {
            "key": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "virtualInterfaceName": "{{string}}",
      "vlan": {{number}}
   }
}
```

## Request Parameters
<a name="API_CreateTransitVirtualInterface_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [connectionId](#API_CreateTransitVirtualInterface_RequestSyntax) **   <a name="DX-CreateTransitVirtualInterface-request-connectionId"></a>
The ID of the connection.
Type: String
Required: Yes

 ** [newTransitVirtualInterface](#API_CreateTransitVirtualInterface_RequestSyntax) **   <a name="DX-CreateTransitVirtualInterface-request-newTransitVirtualInterface"></a>
Information about the transit virtual interface.
Type: [NewTransitVirtualInterface](API_NewTransitVirtualInterface.md) object
Required: Yes

## Response Syntax
<a name="API_CreateTransitVirtualInterface_ResponseSyntax"></a>

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
<a name="API_CreateTransitVirtualInterface_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [virtualInterface](#API_CreateTransitVirtualInterface_ResponseSyntax) **   <a name="DX-CreateTransitVirtualInterface-response-virtualInterface"></a>
Information about a virtual interface.
Type: [VirtualInterface](API_VirtualInterface.md) object

## Errors
<a name="API_CreateTransitVirtualInterface_Errors"></a>

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
<a name="API_CreateTransitVirtualInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/CreateTransitVirtualInterface)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/CreateTransitVirtualInterface)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/CreateTransitVirtualInterface)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/CreateTransitVirtualInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/CreateTransitVirtualInterface)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/CreateTransitVirtualInterface)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/CreateTransitVirtualInterface)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/CreateTransitVirtualInterface)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/CreateTransitVirtualInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/CreateTransitVirtualInterface)
