---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeVirtualInterfaces.html
---

# DescribeVirtualInterfaces
<a name="API_DescribeVirtualInterfaces"></a>

Displays all virtual interfaces for an AWS account. Virtual interfaces deleted fewer than 15 minutes before you make the request are also returned. If you specify a connection ID, only the virtual interfaces associated with the connection are returned. If you specify a virtual interface ID, then only a single virtual interface is returned.

A virtual interface (VLAN) transmits the traffic between the Direct Connect location and the customer network.
+ If you're using an `asn`, the response includes the ASN value in both the `asn` and `asnLong` fields.
+ If you're using `asnLong`, the response returns a value of `0` (zero) for the `asn` attribute because it exceeds the highest ASN value of 2,147,483,647 that it can support

## Request Syntax
<a name="API_DescribeVirtualInterfaces_RequestSyntax"></a>

```
{
   "connectionId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "virtualInterfaceId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeVirtualInterfaces_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [connectionId](#API_DescribeVirtualInterfaces_RequestSyntax) **   <a name="DX-DescribeVirtualInterfaces-request-connectionId"></a>
The ID of the connection.
Type: String
Required: No

 ** [maxResults](#API_DescribeVirtualInterfaces_RequestSyntax) **   <a name="DX-DescribeVirtualInterfaces-request-maxResults"></a>
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
If `MaxResults` is given a value larger than 100, only 100 results are returned.
Type: Integer
Required: No

 ** [nextToken](#API_DescribeVirtualInterfaces_RequestSyntax) **   <a name="DX-DescribeVirtualInterfaces-request-nextToken"></a>
The token for the next page of results.
Type: String
Required: No

 ** [virtualInterfaceId](#API_DescribeVirtualInterfaces_RequestSyntax) **   <a name="DX-DescribeVirtualInterfaces-request-virtualInterfaceId"></a>
The ID of the virtual interface.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeVirtualInterfaces_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "virtualInterfaces": [
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
   ]
}
```

## Response Elements
<a name="API_DescribeVirtualInterfaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_DescribeVirtualInterfaces_ResponseSyntax) **   <a name="DX-DescribeVirtualInterfaces-response-nextToken"></a>
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 ** [virtualInterfaces](#API_DescribeVirtualInterfaces_ResponseSyntax) **   <a name="DX-DescribeVirtualInterfaces-response-virtualInterfaces"></a>
The virtual interfaces
Type: Array of [VirtualInterface](API_VirtualInterface.md) objects

## Errors
<a name="API_DescribeVirtualInterfaces_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_DescribeVirtualInterfaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/DescribeVirtualInterfaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/DescribeVirtualInterfaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/DescribeVirtualInterfaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/DescribeVirtualInterfaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/DescribeVirtualInterfaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/DescribeVirtualInterfaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/DescribeVirtualInterfaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/DescribeVirtualInterfaces)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/DescribeVirtualInterfaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/DescribeVirtualInterfaces)
