---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AllocateTransitVirtualInterface.html
---

# AllocateTransitVirtualInterface
<a name="API_AllocateTransitVirtualInterface"></a>

Provisions a transit virtual interface to be owned by the specified AWS account. Use this type of interface to connect a transit gateway to your Direct Connect gateway.

The owner of a connection provisions a transit virtual interface to be owned by the specified AWS account.

After you create a transit virtual interface, it must be confirmed by the owner using [ConfirmTransitVirtualInterface](API_ConfirmTransitVirtualInterface.md). Until this step has been completed, the transit virtual interface is in the `requested` state and is not available to handle traffic.

## Request Syntax
<a name="API_AllocateTransitVirtualInterface_RequestSyntax"></a>

```
{
   "connectionId": "{{string}}",
   "newTransitVirtualInterfaceAllocation": {
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
<a name="API_AllocateTransitVirtualInterface_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [connectionId](#API_AllocateTransitVirtualInterface_RequestSyntax) **   <a name="DX-AllocateTransitVirtualInterface-request-connectionId"></a>
The ID of the connection on which the transit virtual interface is provisioned.
Type: String
Required: Yes

 ** [newTransitVirtualInterfaceAllocation](#API_AllocateTransitVirtualInterface_RequestSyntax) **   <a name="DX-AllocateTransitVirtualInterface-request-newTransitVirtualInterfaceAllocation"></a>
Information about the transit virtual interface.
Type: [NewTransitVirtualInterfaceAllocation](API_NewTransitVirtualInterfaceAllocation.md) object
Required: Yes

 ** [ownerAccount](#API_AllocateTransitVirtualInterface_RequestSyntax) **   <a name="DX-AllocateTransitVirtualInterface-request-ownerAccount"></a>
The ID of the AWS account that owns the transit virtual interface.
Type: String
Required: Yes

## Response Syntax
<a name="API_AllocateTransitVirtualInterface_ResponseSyntax"></a>

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
<a name="API_AllocateTransitVirtualInterface_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [virtualInterface](#API_AllocateTransitVirtualInterface_ResponseSyntax) **   <a name="DX-AllocateTransitVirtualInterface-response-virtualInterface"></a>
Information about the transit virtual interface.
Type: [VirtualInterface](API_VirtualInterface.md) object

## Errors
<a name="API_AllocateTransitVirtualInterface_Errors"></a>

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
<a name="API_AllocateTransitVirtualInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/AllocateTransitVirtualInterface)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/AllocateTransitVirtualInterface)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/AllocateTransitVirtualInterface)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/AllocateTransitVirtualInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/AllocateTransitVirtualInterface)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/AllocateTransitVirtualInterface)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/AllocateTransitVirtualInterface)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/AllocateTransitVirtualInterface)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/AllocateTransitVirtualInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/AllocateTransitVirtualInterface)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
