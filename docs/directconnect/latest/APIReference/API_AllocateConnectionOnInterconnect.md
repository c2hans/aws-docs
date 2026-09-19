---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AllocateConnectionOnInterconnect.html
---

# AllocateConnectionOnInterconnect
<a name="API_AllocateConnectionOnInterconnect"></a>

**Note**
Deprecated. Use [AllocateHostedConnection](API_AllocateHostedConnection.md) instead.

Creates a hosted connection on an interconnect.

Allocates a VLAN number and a specified amount of bandwidth for use by a hosted connection on the specified interconnect.

**Note**
Intended for use by Direct Connect Partners only.

## Request Syntax
<a name="API_AllocateConnectionOnInterconnect_RequestSyntax"></a>

```
{
   "bandwidth": "{{string}}",
   "connectionName": "{{string}}",
   "interconnectId": "{{string}}",
   "ownerAccount": "{{string}}",
   "vlan": {{number}}
}
```

## Request Parameters
<a name="API_AllocateConnectionOnInterconnect_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [bandwidth](#API_AllocateConnectionOnInterconnect_RequestSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-request-bandwidth"></a>
The bandwidth of the connection. The possible values are 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, 500Mbps, 1Gbps, 2Gbps, 5Gbps, and 10Gbps. Note that only those Direct Connect Partners who have met specific requirements are allowed to create a 1Gbps, 2Gbps, 5Gbps or 10Gbps hosted connection.
Type: String
Required: Yes

 ** [connectionName](#API_AllocateConnectionOnInterconnect_RequestSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-request-connectionName"></a>
The name of the provisioned connection.
Type: String
Required: Yes

 ** [interconnectId](#API_AllocateConnectionOnInterconnect_RequestSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-request-interconnectId"></a>
The ID of the interconnect on which the connection will be provisioned.
Type: String
Required: Yes

 ** [ownerAccount](#API_AllocateConnectionOnInterconnect_RequestSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-request-ownerAccount"></a>
The ID of the AWS account of the customer for whom the connection will be provisioned.
Type: String
Required: Yes

 ** [vlan](#API_AllocateConnectionOnInterconnect_RequestSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-request-vlan"></a>
The dedicated VLAN provisioned to the connection.
Type: Integer
Required: Yes

## Response Syntax
<a name="API_AllocateConnectionOnInterconnect_ResponseSyntax"></a>

```
{
   "awsDevice": "string",
   "awsDeviceV2": "string",
   "awsLogicalDeviceId": "string",
   "bandwidth": "string",
   "billingMode": "string",
   "connectionId": "string",
   "connectionName": "string",
   "connectionState": "string",
   "encryptionMode": "string",
   "hasLogicalRedundancy": "string",
   "jumboFrameCapable": boolean,
   "lagId": "string",
   "loaIssueTime": number,
   "location": "string",
   "macSecCapable": boolean,
   "macSecKeys": [
      {
         "ckn": "string",
         "secretARN": "string",
         "startOn": "string",
         "state": "string"
      }
   ],
   "ownerAccount": "string",
   "partnerInterconnectMacSecCapable": boolean,
   "partnerName": "string",
   "portEncryptionStatus": "string",
   "prefixPoolSizeIpv4": number,
   "prefixPoolSizeIpv6": number,
   "prefixPoolUnallocatedCountIpv4": number,
   "prefixPoolUnallocatedCountIpv6": number,
   "providerName": "string",
   "rateLimiterStatus": {
      "inUse": number,
      "maxAllowed": number,
      "remaining": number,
      "totalBandwidth": "string"
   },
   "region": "string",
   "tags": [
      {
         "key": "string",
         "value": "string"
      }
   ],
   "vlan": number
}
```

## Response Elements
<a name="API_AllocateConnectionOnInterconnect_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [awsDevice](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-awsDevice"></a>
 *This parameter has been deprecated.*
The Direct Connect endpoint on which the physical connection terminates.
Type: String

 ** [awsDeviceV2](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-awsDeviceV2"></a>
The Direct Connect endpoint that terminates the physical connection.
Type: String

 ** [awsLogicalDeviceId](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-awsLogicalDeviceId"></a>
The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.
Type: String

 ** [bandwidth](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-bandwidth"></a>
The bandwidth of the connection.
Type: String

 ** [billingMode](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-billingMode"></a>
The billing mode of the connection.
Type: String
Valid Values: `PayAsYouGo | FlatRateTier1 | FlatRateTier2 | FlatRateTier3 | FlatRateTier4 | FlatRateTier5 | PortPairFlatRateTier1 | PortPairFlatRateTier2 | PortPairFlatRateTier3 | PortPairFlatRateTier4 | PortPairFlatRateTier5`

 ** [connectionId](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-connectionId"></a>
The ID of the connection.
Type: String

 ** [connectionName](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-connectionName"></a>
The name of the connection.
Type: String

 ** [connectionState](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-connectionState"></a>
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

 ** [encryptionMode](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-encryptionMode"></a>
The MAC Security (MACsec) connection encryption mode.
The valid values are `no_encrypt`, `should_encrypt`, and `must_encrypt`.
Type: String

 ** [hasLogicalRedundancy](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-hasLogicalRedundancy"></a>
Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).
Type: String
Valid Values: `unknown | yes | no`

 ** [jumboFrameCapable](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-jumboFrameCapable"></a>
Indicates whether jumbo frames are supported.
Type: Boolean

 ** [lagId](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-lagId"></a>
The ID of the LAG.
Type: String

 ** [loaIssueTime](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-loaIssueTime"></a>
The time of the most recent call to [DescribeLoa](API_DescribeLoa.md) for this connection.
Type: Timestamp

 ** [location](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-location"></a>
The location of the connection.
Type: String

 ** [macSecCapable](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-macSecCapable"></a>
Indicates whether the connection supports MAC Security (MACsec).
Type: Boolean

 ** [macSecKeys](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-macSecKeys"></a>
The MAC Security (MACsec) security keys associated with the connection.
Type: Array of [MacSecKey](API_MacSecKey.md) objects

 ** [ownerAccount](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-ownerAccount"></a>
The ID of the AWS account that owns the connection.
Type: String

 ** [partnerInterconnectMacSecCapable](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-partnerInterconnectMacSecCapable"></a>
Indicates whether the interconnect hosting this connection supports MAC Security (MACsec).
Type: Boolean

 ** [partnerName](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-partnerName"></a>
The name of the Direct Connect service provider associated with the connection.
Type: String

 ** [portEncryptionStatus](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-portEncryptionStatus"></a>
The MAC Security (MACsec) port link status of the connection.
The valid values are `Encryption Up`, which means that there is an active Connection Key Name, or `Encryption Down`.
Type: String

 ** [prefixPoolSizeIpv4](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-prefixPoolSizeIpv4"></a>
The total number of inbound IPv4 route prefixes you can allocate across the virtual interfaces on the connection. Not applicable to hosted connections or interconnects.
Type: Integer
Valid Range: Minimum value of 0.

 ** [prefixPoolSizeIpv6](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-prefixPoolSizeIpv6"></a>
The total number of inbound IPv6 route prefixes you can allocate across the virtual interfaces on the connection. Not applicable to hosted connections or interconnects.
Type: Integer
Valid Range: Minimum value of 0.

 ** [prefixPoolUnallocatedCountIpv4](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-prefixPoolUnallocatedCountIpv4"></a>
The number of inbound IPv4 route prefixes in the connection prefix pool not yet allocated to a virtual interface. Not applicable to hosted connections or interconnects.
Type: Integer
Valid Range: Minimum value of 0.

 ** [prefixPoolUnallocatedCountIpv6](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-prefixPoolUnallocatedCountIpv6"></a>
The number of inbound IPv6 route prefixes in the connection prefix pool not yet allocated to a virtual interface. Not applicable to hosted connections or interconnects.
Type: Integer
Valid Range: Minimum value of 0.

 ** [providerName](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-providerName"></a>
The name of the service provider associated with the connection.
Type: String

 ** [rateLimiterStatus](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-rateLimiterStatus"></a>
The rate limiter status for the connection, including how many rate limiters are in use and the maximum allowed.
Type: [RateLimiterStatus](API_RateLimiterStatus.md) object

 ** [region](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-region"></a>
The AWS Region where the connection is located.
Type: String

 ** [tags](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-tags"></a>
The tags associated with the connection.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.

 ** [vlan](#API_AllocateConnectionOnInterconnect_ResponseSyntax) **   <a name="DX-AllocateConnectionOnInterconnect-response-vlan"></a>
The ID of the VLAN.
Type: Integer

## Errors
<a name="API_AllocateConnectionOnInterconnect_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_AllocateConnectionOnInterconnect_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/AllocateConnectionOnInterconnect)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/AllocateConnectionOnInterconnect)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/AllocateConnectionOnInterconnect)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/AllocateConnectionOnInterconnect)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/AllocateConnectionOnInterconnect)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/AllocateConnectionOnInterconnect)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/AllocateConnectionOnInterconnect)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/AllocateConnectionOnInterconnect)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/AllocateConnectionOnInterconnect)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/AllocateConnectionOnInterconnect)
