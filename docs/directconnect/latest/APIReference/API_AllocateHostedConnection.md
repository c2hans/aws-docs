---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AllocateHostedConnection.html
---

# AllocateHostedConnection
<a name="API_AllocateHostedConnection"></a>

Creates a hosted connection on the specified interconnect or a link aggregation group (LAG) of interconnects.

Allocates a VLAN number and a specified amount of capacity (bandwidth) for use by a hosted connection on the specified interconnect or LAG of interconnects. AWS polices the hosted connection for the specified capacity and the Direct Connect Partner must also police the hosted connection for the specified capacity.

**Note**
Intended for use by Direct Connect Partners only.

## Request Syntax
<a name="API_AllocateHostedConnection_RequestSyntax"></a>

```
{
   "bandwidth": "{{string}}",
   "connectionId": "{{string}}",
   "connectionName": "{{string}}",
   "ownerAccount": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "vlan": {{number}}
}
```

## Request Parameters
<a name="API_AllocateHostedConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [bandwidth](#API_AllocateHostedConnection_RequestSyntax) **   <a name="DX-AllocateHostedConnection-request-bandwidth"></a>
The bandwidth of the connection. The possible values are 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, 500Mbps, 1Gbps, 2Gbps, 5Gbps, 10Gbps, and 25Gbps. Note that only those Direct Connect Partners who have met specific requirements are allowed to create a 1Gbps, 2Gbps, 5Gbps, 10Gbps, or 25Gbps hosted connection.
Type: String
Required: Yes

 ** [connectionId](#API_AllocateHostedConnection_RequestSyntax) **   <a name="DX-AllocateHostedConnection-request-connectionId"></a>
The ID of the interconnect or LAG.
Type: String
Required: Yes

 ** [connectionName](#API_AllocateHostedConnection_RequestSyntax) **   <a name="DX-AllocateHostedConnection-request-connectionName"></a>
The name of the hosted connection.
Type: String
Required: Yes

 ** [ownerAccount](#API_AllocateHostedConnection_RequestSyntax) **   <a name="DX-AllocateHostedConnection-request-ownerAccount"></a>
The ID of the AWS account ID of the customer for the connection.
Type: String
Required: Yes

 ** [tags](#API_AllocateHostedConnection_RequestSyntax) **   <a name="DX-AllocateHostedConnection-request-tags"></a>
The tags associated with the connection.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [vlan](#API_AllocateHostedConnection_RequestSyntax) **   <a name="DX-AllocateHostedConnection-request-vlan"></a>
The dedicated VLAN provisioned to the hosted connection.
Type: Integer
Required: Yes

## Response Syntax
<a name="API_AllocateHostedConnection_ResponseSyntax"></a>

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
<a name="API_AllocateHostedConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [awsDevice](#API_AllocateHostedConnection_ResponseSyntax) **   <a name="DX-AllocateHostedConnection-response-awsDevice"></a>
 *This parameter has been deprecated.*
The Direct Connect endpoint on which the physical connection terminates.
Type: String

 ** [awsDeviceV2](#API_AllocateHostedConnection_ResponseSyntax) **   <a name="DX-AllocateHostedConnection-response-awsDeviceV2"></a>
The Direct Connect endpoint that terminates the physical connection.
Type: String

 ** [awsLogicalDeviceId](#API_AllocateHostedConnection_ResponseSyntax) **   <a name="DX-AllocateHostedConnection-response-awsLogicalDeviceId"></a>
The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.
Type: String

 ** [bandwidth](#API_AllocateHostedConnection_ResponseSyntax) **   <a name="DX-AllocateHostedConnection-response-bandwidth"></a>
The bandwidth of the connection.
Type: String

 ** [connectionId](#API_AllocateHostedConnection_ResponseSyntax) **   <a name="DX-AllocateHostedConnection-response-connectionId"></a>
The ID of the connection.
Type: String

 ** [connectionName](#API_AllocateHostedConnection_ResponseSyntax) **   <a name="DX-AllocateHostedConnection-response-connectionName"></a>
The name of the connection.
Type: String

 ** [connectionState](#API_AllocateHostedConnection_ResponseSyntax) **   <a name="DX-AllocateHostedConnection-response-connectionState"></a>
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

 ** [encryptionMode](#API_AllocateHostedConnection_ResponseSyntax) **   <a name="DX-AllocateHostedConnection-response-encryptionMode"></a>
The MAC Security (MACsec) connection encryption mode.
The valid values are `no_encrypt`, `should_encrypt`, and `must_encrypt`.
Type: String

 ** [hasLogicalRedundancy](#API_AllocateHostedConnection_ResponseSyntax) **   <a name="DX-AllocateHostedConnection-response-hasLogicalRedundancy"></a>
Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).
Type: String
Valid Values: `unknown | yes | no`

 ** [jumboFrameCapable](#API_AllocateHostedConnection_ResponseSyntax) **   <a name="DX-AllocateHostedConnection-response-jumboFrameCapable"></a>
Indicates whether jumbo frames are supported.
Type: Boolean

 ** [lagId](#API_AllocateHostedConnection_ResponseSyntax) **   <a name="DX-AllocateHostedConnection-response-lagId"></a>
The ID of the LAG.
Type: String

 ** [loaIssueTime](#API_AllocateHostedConnection_ResponseSyntax) **   <a name="DX-AllocateHostedConnection-response-loaIssueTime"></a>
The time of the most recent call to [DescribeLoa](API_DescribeLoa.md) for this connection.
Type: Timestamp

 ** [location](#API_AllocateHostedConnection_ResponseSyntax) **   <a name="DX-AllocateHostedConnection-response-location"></a>
The location of the connection.
Type: String

 ** [macSecCapable](#API_AllocateHostedConnection_ResponseSyntax) **   <a name="DX-AllocateHostedConnection-response-macSecCapable"></a>
Indicates whether the connection supports MAC Security (MACsec).
Type: Boolean

 ** [macSecKeys](#API_AllocateHostedConnection_ResponseSyntax) **   <a name="DX-AllocateHostedConnection-response-macSecKeys"></a>
The MAC Security (MACsec) security keys associated with the connection.
Type: Array of [MacSecKey](API_MacSecKey.md) objects

 ** [ownerAccount](#API_AllocateHostedConnection_ResponseSyntax) **   <a name="DX-AllocateHostedConnection-response-ownerAccount"></a>
The ID of the AWS account that owns the connection.
Type: String

 ** [partnerInterconnectMacSecCapable](#API_AllocateHostedConnection_ResponseSyntax) **   <a name="DX-AllocateHostedConnection-response-partnerInterconnectMacSecCapable"></a>
Indicates whether the interconnect hosting this connection supports MAC Security (MACsec).
Type: Boolean

 ** [partnerName](#API_AllocateHostedConnection_ResponseSyntax) **   <a name="DX-AllocateHostedConnection-response-partnerName"></a>
The name of the Direct Connect service provider associated with the connection.
Type: String

 ** [portEncryptionStatus](#API_AllocateHostedConnection_ResponseSyntax) **   <a name="DX-AllocateHostedConnection-response-portEncryptionStatus"></a>
The MAC Security (MACsec) port link status of the connection.
The valid values are `Encryption Up`, which means that there is an active Connection Key Name, or `Encryption Down`.
Type: String

 ** [providerName](#API_AllocateHostedConnection_ResponseSyntax) **   <a name="DX-AllocateHostedConnection-response-providerName"></a>
The name of the service provider associated with the connection.
Type: String

 ** [rateLimiterStatus](#API_AllocateHostedConnection_ResponseSyntax) **   <a name="DX-AllocateHostedConnection-response-rateLimiterStatus"></a>
The rate limiter status for the connection, including how many rate limiters are in use and the maximum allowed.
Type: [RateLimiterStatus](API_RateLimiterStatus.md) object

 ** [region](#API_AllocateHostedConnection_ResponseSyntax) **   <a name="DX-AllocateHostedConnection-response-region"></a>
The AWS Region where the connection is located.
Type: String

 ** [tags](#API_AllocateHostedConnection_ResponseSyntax) **   <a name="DX-AllocateHostedConnection-response-tags"></a>
The tags associated with the connection.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.

 ** [vlan](#API_AllocateHostedConnection_ResponseSyntax) **   <a name="DX-AllocateHostedConnection-response-vlan"></a>
The ID of the VLAN.
Type: Integer

## Errors
<a name="API_AllocateHostedConnection_Errors"></a>

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

 ** TooManyTagsException **
You have reached the limit on the number of tags that can be assigned.
HTTP Status Code: 400

## See Also
<a name="API_AllocateHostedConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/AllocateHostedConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/AllocateHostedConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/AllocateHostedConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/AllocateHostedConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/AllocateHostedConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/AllocateHostedConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/AllocateHostedConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/AllocateHostedConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/AllocateHostedConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/AllocateHostedConnection)
