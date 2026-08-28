---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteBGPPeer.html
---

# DeleteBGPPeer
<a name="API_DeleteBGPPeer"></a>

Deletes the specified BGP peer on the specified virtual interface with the specified customer address and ASN.

You cannot delete the last BGP peer from a virtual interface.

## Request Syntax
<a name="API_DeleteBGPPeer_RequestSyntax"></a>

```
{
   "asn": {{number}},
   "asnLong": {{number}},
   "bgpPeerId": "{{string}}",
   "customerAddress": "{{string}}",
   "virtualInterfaceId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteBGPPeer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [asn](#API_DeleteBGPPeer_RequestSyntax) **   <a name="DX-DeleteBGPPeer-request-asn"></a>
The autonomous system number (ASN). The valid range is from 1 to 2147483646 for Border Gateway Protocol (BGP) configuration. If you provide a number greater than the maximum, an error is returned. Use `asnLong` instead.
+ You can use `asnLong` or `asn`, but not both. We recommend using `asnLong` as it supports a greater pool of numbers.
+ If you provide a value in the same API call for both `asn` and `asnLong`, the API will only accept the value for `asnLong`.
+ If you enter a 4-byte ASN for the `asn` parameter, the API returns an error.
+ If you are using a 2-byte ASN, the API response will include the 2-byte value for both the `asn` and `asnLong` fields.
Type: Integer
Required: No

 ** [asnLong](#API_DeleteBGPPeer_RequestSyntax) **   <a name="DX-DeleteBGPPeer-request-asnLong"></a>
The long ASN for the BGP peer to be deleted from a Direct Connect virtual interface. The valid range is from 1 to 4294967294 for BGP configuration.
Note the following limitations when using `asnLong`:
+ You can use `asnLong` or `asn`, but not both. We recommend using `asnLong` as it supports a greater pool of numbers.
+  `asnLong` accepts any valid ASN value, regardless if it's 2-byte or 4-byte.
+ When using a 4-byte `asnLong`, the API response returns `0` for the legacy `asn` attribute since 4-byte ASN values exceed the maximum supported value of 2,147,483,647.
+ If you are using a 2-byte ASN, the API response will include the 2-byte value for both the `asn` and `asnLong` fields.
+ If you provide a value in the same API call for both `asn` and `asnLong`, the API will only accept the value for `asnLong`.
Type: Long
Required: No

 ** [bgpPeerId](#API_DeleteBGPPeer_RequestSyntax) **   <a name="DX-DeleteBGPPeer-request-bgpPeerId"></a>
The ID of the BGP peer.
Type: String
Required: No

 ** [customerAddress](#API_DeleteBGPPeer_RequestSyntax) **   <a name="DX-DeleteBGPPeer-request-customerAddress"></a>
The IP address assigned to the customer interface.
Type: String
Required: No

 ** [virtualInterfaceId](#API_DeleteBGPPeer_RequestSyntax) **   <a name="DX-DeleteBGPPeer-request-virtualInterfaceId"></a>
The ID of the virtual interface.
Type: String
Required: No

## Response Syntax
<a name="API_DeleteBGPPeer_ResponseSyntax"></a>

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
<a name="API_DeleteBGPPeer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [virtualInterface](#API_DeleteBGPPeer_ResponseSyntax) **   <a name="DX-DeleteBGPPeer-response-virtualInterface"></a>
The virtual interface.
Type: [VirtualInterface](API_VirtualInterface.md) object

## Errors
<a name="API_DeleteBGPPeer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_DeleteBGPPeer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/DeleteBGPPeer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/DeleteBGPPeer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/DeleteBGPPeer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/DeleteBGPPeer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/DeleteBGPPeer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/DeleteBGPPeer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/DeleteBGPPeer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/DeleteBGPPeer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/DeleteBGPPeer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/DeleteBGPPeer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
