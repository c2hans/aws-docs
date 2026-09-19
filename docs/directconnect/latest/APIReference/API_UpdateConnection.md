---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_UpdateConnection.html
---

# UpdateConnection
<a name="API_UpdateConnection"></a>

Updates the Direct Connect connection configuration.

You can update the following parameters for a connection:
+ The connection name
+ The connection's MAC Security (MACsec) encryption mode.

## Request Syntax
<a name="API_UpdateConnection_RequestSyntax"></a>

```
{
   "connectionId": "{{string}}",
   "connectionName": "{{string}}",
   "encryptionMode": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [connectionId](#API_UpdateConnection_RequestSyntax) **   <a name="DX-UpdateConnection-request-connectionId"></a>
The ID of the connection.
You can use [DescribeConnections](API_DescribeConnections.md) to retrieve the connection ID.
Type: String
Required: Yes

 ** [connectionName](#API_UpdateConnection_RequestSyntax) **   <a name="DX-UpdateConnection-request-connectionName"></a>
The name of the connection.
Type: String
Required: No

 ** [encryptionMode](#API_UpdateConnection_RequestSyntax) **   <a name="DX-UpdateConnection-request-encryptionMode"></a>
The connection MAC Security (MACsec) encryption mode.
The valid values are `no_encrypt`, `should_encrypt`, and `must_encrypt`.
Type: String
Required: No

## Response Syntax
<a name="API_UpdateConnection_ResponseSyntax"></a>

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
<a name="API_UpdateConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [awsDevice](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-awsDevice"></a>
 *This parameter has been deprecated.*
The Direct Connect endpoint on which the physical connection terminates.
Type: String

 ** [awsDeviceV2](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-awsDeviceV2"></a>
The Direct Connect endpoint that terminates the physical connection.
Type: String

 ** [awsLogicalDeviceId](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-awsLogicalDeviceId"></a>
The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.
Type: String

 ** [bandwidth](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-bandwidth"></a>
The bandwidth of the connection.
Type: String

 ** [billingMode](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-billingMode"></a>
The billing mode of the connection.
Type: String
Valid Values: `PayAsYouGo | FlatRateTier1 | FlatRateTier2 | FlatRateTier3 | FlatRateTier4 | FlatRateTier5 | PortPairFlatRateTier1 | PortPairFlatRateTier2 | PortPairFlatRateTier3 | PortPairFlatRateTier4 | PortPairFlatRateTier5`

 ** [connectionId](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-connectionId"></a>
The ID of the connection.
Type: String

 ** [connectionName](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-connectionName"></a>
The name of the connection.
Type: String

 ** [connectionState](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-connectionState"></a>
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

 ** [encryptionMode](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-encryptionMode"></a>
The MAC Security (MACsec) connection encryption mode.
The valid values are `no_encrypt`, `should_encrypt`, and `must_encrypt`.
Type: String

 ** [hasLogicalRedundancy](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-hasLogicalRedundancy"></a>
Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).
Type: String
Valid Values: `unknown | yes | no`

 ** [jumboFrameCapable](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-jumboFrameCapable"></a>
Indicates whether jumbo frames are supported.
Type: Boolean

 ** [lagId](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-lagId"></a>
The ID of the LAG.
Type: String

 ** [loaIssueTime](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-loaIssueTime"></a>
The time of the most recent call to [DescribeLoa](API_DescribeLoa.md) for this connection.
Type: Timestamp

 ** [location](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-location"></a>
The location of the connection.
Type: String

 ** [macSecCapable](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-macSecCapable"></a>
Indicates whether the connection supports MAC Security (MACsec).
Type: Boolean

 ** [macSecKeys](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-macSecKeys"></a>
The MAC Security (MACsec) security keys associated with the connection.
Type: Array of [MacSecKey](API_MacSecKey.md) objects

 ** [ownerAccount](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-ownerAccount"></a>
The ID of the AWS account that owns the connection.
Type: String

 ** [partnerInterconnectMacSecCapable](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-partnerInterconnectMacSecCapable"></a>
Indicates whether the interconnect hosting this connection supports MAC Security (MACsec).
Type: Boolean

 ** [partnerName](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-partnerName"></a>
The name of the Direct Connect service provider associated with the connection.
Type: String

 ** [portEncryptionStatus](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-portEncryptionStatus"></a>
The MAC Security (MACsec) port link status of the connection.
The valid values are `Encryption Up`, which means that there is an active Connection Key Name, or `Encryption Down`.
Type: String

 ** [prefixPoolSizeIpv4](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-prefixPoolSizeIpv4"></a>
The total number of inbound IPv4 route prefixes you can allocate across the virtual interfaces on the connection. Not applicable to hosted connections or interconnects.
Type: Integer
Valid Range: Minimum value of 0.

 ** [prefixPoolSizeIpv6](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-prefixPoolSizeIpv6"></a>
The total number of inbound IPv6 route prefixes you can allocate across the virtual interfaces on the connection. Not applicable to hosted connections or interconnects.
Type: Integer
Valid Range: Minimum value of 0.

 ** [prefixPoolUnallocatedCountIpv4](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-prefixPoolUnallocatedCountIpv4"></a>
The number of inbound IPv4 route prefixes in the connection prefix pool not yet allocated to a virtual interface. Not applicable to hosted connections or interconnects.
Type: Integer
Valid Range: Minimum value of 0.

 ** [prefixPoolUnallocatedCountIpv6](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-prefixPoolUnallocatedCountIpv6"></a>
The number of inbound IPv6 route prefixes in the connection prefix pool not yet allocated to a virtual interface. Not applicable to hosted connections or interconnects.
Type: Integer
Valid Range: Minimum value of 0.

 ** [providerName](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-providerName"></a>
The name of the service provider associated with the connection.
Type: String

 ** [rateLimiterStatus](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-rateLimiterStatus"></a>
The rate limiter status for the connection, including how many rate limiters are in use and the maximum allowed.
Type: [RateLimiterStatus](API_RateLimiterStatus.md) object

 ** [region](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-region"></a>
The AWS Region where the connection is located.
Type: String

 ** [tags](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-tags"></a>
The tags associated with the connection.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.

 ** [vlan](#API_UpdateConnection_ResponseSyntax) **   <a name="DX-UpdateConnection-response-vlan"></a>
The ID of the VLAN.
Type: Integer

## Errors
<a name="API_UpdateConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_UpdateConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/UpdateConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/UpdateConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/UpdateConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/UpdateConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/UpdateConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/UpdateConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/UpdateConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/UpdateConnection)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/UpdateConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/UpdateConnection)
