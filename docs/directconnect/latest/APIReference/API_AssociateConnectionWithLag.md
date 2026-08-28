---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AssociateConnectionWithLag.html
---

# AssociateConnectionWithLag
<a name="API_AssociateConnectionWithLag"></a>

Associates an existing connection with a link aggregation group (LAG). The connection is interrupted and re-established as a member of the LAG (connectivity to AWS is interrupted). The connection must be hosted on the same Direct Connect endpoint as the LAG, and its bandwidth must match the bandwidth for the LAG. You can re-associate a connection that's currently associated with a different LAG; however, if removing the connection would cause the original LAG to fall below its setting for minimum number of operational connections, the request fails.

Any virtual interfaces that are directly associated with the connection are automatically re-associated with the LAG. If the connection was originally associated with a different LAG, the virtual interfaces remain associated with the original LAG.

For interconnects, any hosted connections are automatically re-associated with the LAG. If the interconnect was originally associated with a different LAG, the hosted connections remain associated with the original LAG.

## Request Syntax
<a name="API_AssociateConnectionWithLag_RequestSyntax"></a>

```
{
   "connectionId": "{{string}}",
   "lagId": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateConnectionWithLag_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [connectionId](#API_AssociateConnectionWithLag_RequestSyntax) **   <a name="DX-AssociateConnectionWithLag-request-connectionId"></a>
The ID of the connection.
Type: String
Required: Yes

 ** [lagId](#API_AssociateConnectionWithLag_RequestSyntax) **   <a name="DX-AssociateConnectionWithLag-request-lagId"></a>
The ID of the LAG with which to associate the connection.
Type: String
Required: Yes

## Response Syntax
<a name="API_AssociateConnectionWithLag_ResponseSyntax"></a>

```
{
   "awsDevice": "string",
   "awsDeviceV2": "string",
   "awsLogicalDeviceId": "string",
   "bandwidth": "string",
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
<a name="API_AssociateConnectionWithLag_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [awsDevice](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-awsDevice"></a>
 *This parameter has been deprecated.*
The Direct Connect endpoint on which the physical connection terminates.
Type: String

 ** [awsDeviceV2](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-awsDeviceV2"></a>
The Direct Connect endpoint that terminates the physical connection.
Type: String

 ** [awsLogicalDeviceId](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-awsLogicalDeviceId"></a>
The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.
Type: String

 ** [bandwidth](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-bandwidth"></a>
The bandwidth of the connection.
Type: String

 ** [connectionId](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-connectionId"></a>
The ID of the connection.
Type: String

 ** [connectionName](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-connectionName"></a>
The name of the connection.
Type: String

 ** [connectionState](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-connectionState"></a>
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

 ** [encryptionMode](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-encryptionMode"></a>
The MAC Security (MACsec) connection encryption mode.
The valid values are `no_encrypt`, `should_encrypt`, and `must_encrypt`.
Type: String

 ** [hasLogicalRedundancy](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-hasLogicalRedundancy"></a>
Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).
Type: String
Valid Values: `unknown | yes | no`

 ** [jumboFrameCapable](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-jumboFrameCapable"></a>
Indicates whether jumbo frames are supported.
Type: Boolean

 ** [lagId](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-lagId"></a>
The ID of the LAG.
Type: String

 ** [loaIssueTime](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-loaIssueTime"></a>
The time of the most recent call to [DescribeLoa](API_DescribeLoa.md) for this connection.
Type: Timestamp

 ** [location](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-location"></a>
The location of the connection.
Type: String

 ** [macSecCapable](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-macSecCapable"></a>
Indicates whether the connection supports MAC Security (MACsec).
Type: Boolean

 ** [macSecKeys](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-macSecKeys"></a>
The MAC Security (MACsec) security keys associated with the connection.
Type: Array of [MacSecKey](API_MacSecKey.md) objects

 ** [ownerAccount](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-ownerAccount"></a>
The ID of the AWS account that owns the connection.
Type: String

 ** [partnerInterconnectMacSecCapable](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-partnerInterconnectMacSecCapable"></a>
Indicates whether the interconnect hosting this connection supports MAC Security (MACsec).
Type: Boolean

 ** [partnerName](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-partnerName"></a>
The name of the Direct Connect service provider associated with the connection.
Type: String

 ** [portEncryptionStatus](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-portEncryptionStatus"></a>
The MAC Security (MACsec) port link status of the connection.
The valid values are `Encryption Up`, which means that there is an active Connection Key Name, or `Encryption Down`.
Type: String

 ** [prefixPoolSizeIpv4](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-prefixPoolSizeIpv4"></a>
The total number of inbound IPv4 route prefixes you can allocate across the virtual interfaces on the connection. Not applicable to hosted connections or interconnects.
Type: Integer
Valid Range: Minimum value of 0.

 ** [prefixPoolSizeIpv6](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-prefixPoolSizeIpv6"></a>
The total number of inbound IPv6 route prefixes you can allocate across the virtual interfaces on the connection. Not applicable to hosted connections or interconnects.
Type: Integer
Valid Range: Minimum value of 0.

 ** [prefixPoolUnallocatedCountIpv4](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-prefixPoolUnallocatedCountIpv4"></a>
The number of inbound IPv4 route prefixes in the connection prefix pool not yet allocated to a virtual interface. Not applicable to hosted connections or interconnects.
Type: Integer
Valid Range: Minimum value of 0.

 ** [prefixPoolUnallocatedCountIpv6](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-prefixPoolUnallocatedCountIpv6"></a>
The number of inbound IPv6 route prefixes in the connection prefix pool not yet allocated to a virtual interface. Not applicable to hosted connections or interconnects.
Type: Integer
Valid Range: Minimum value of 0.

 ** [providerName](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-providerName"></a>
The name of the service provider associated with the connection.
Type: String

 ** [rateLimiterStatus](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-rateLimiterStatus"></a>
The rate limiter status for the connection, including how many rate limiters are in use and the maximum allowed.
Type: [RateLimiterStatus](API_RateLimiterStatus.md) object

 ** [region](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-region"></a>
The AWS Region where the connection is located.
Type: String

 ** [tags](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-tags"></a>
The tags associated with the connection.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.

 ** [vlan](#API_AssociateConnectionWithLag_ResponseSyntax) **   <a name="DX-AssociateConnectionWithLag-response-vlan"></a>
The ID of the VLAN.
Type: Integer

## Errors
<a name="API_AssociateConnectionWithLag_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

 ** LimitExceededException **
The rate limiter limit has been exceeded for the connection. You cannot add more rate limiters to virtual interfaces on this connection.
HTTP Status Code: 400

## See Also
<a name="API_AssociateConnectionWithLag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/AssociateConnectionWithLag)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/AssociateConnectionWithLag)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/AssociateConnectionWithLag)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/AssociateConnectionWithLag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/AssociateConnectionWithLag)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/AssociateConnectionWithLag)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/AssociateConnectionWithLag)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/AssociateConnectionWithLag)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/AssociateConnectionWithLag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/AssociateConnectionWithLag)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
