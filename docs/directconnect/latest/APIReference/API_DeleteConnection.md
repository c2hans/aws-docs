---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteConnection.html
---

# DeleteConnection
<a name="API_DeleteConnection"></a>

Deletes the specified connection.

Deleting a connection only stops the Direct Connect port hour and data transfer charges. If you are partnering with any third parties to connect with the Direct Connect location, you must cancel your service with them separately.

## Request Syntax
<a name="API_DeleteConnection_RequestSyntax"></a>

```
{
   "connectionId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [connectionId](#API_DeleteConnection_RequestSyntax) **   <a name="DX-DeleteConnection-request-connectionId"></a>
The ID of the connection.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteConnection_ResponseSyntax"></a>

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
<a name="API_DeleteConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [awsDevice](#API_DeleteConnection_ResponseSyntax) **   <a name="DX-DeleteConnection-response-awsDevice"></a>
 *This parameter has been deprecated.*
The Direct Connect endpoint on which the physical connection terminates.
Type: String

 ** [awsDeviceV2](#API_DeleteConnection_ResponseSyntax) **   <a name="DX-DeleteConnection-response-awsDeviceV2"></a>
The Direct Connect endpoint that terminates the physical connection.
Type: String

 ** [awsLogicalDeviceId](#API_DeleteConnection_ResponseSyntax) **   <a name="DX-DeleteConnection-response-awsLogicalDeviceId"></a>
The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.
Type: String

 ** [bandwidth](#API_DeleteConnection_ResponseSyntax) **   <a name="DX-DeleteConnection-response-bandwidth"></a>
The bandwidth of the connection.
Type: String

 ** [connectionId](#API_DeleteConnection_ResponseSyntax) **   <a name="DX-DeleteConnection-response-connectionId"></a>
The ID of the connection.
Type: String

 ** [connectionName](#API_DeleteConnection_ResponseSyntax) **   <a name="DX-DeleteConnection-response-connectionName"></a>
The name of the connection.
Type: String

 ** [connectionState](#API_DeleteConnection_ResponseSyntax) **   <a name="DX-DeleteConnection-response-connectionState"></a>
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

 ** [encryptionMode](#API_DeleteConnection_ResponseSyntax) **   <a name="DX-DeleteConnection-response-encryptionMode"></a>
The MAC Security (MACsec) connection encryption mode.
The valid values are `no_encrypt`, `should_encrypt`, and `must_encrypt`.
Type: String

 ** [hasLogicalRedundancy](#API_DeleteConnection_ResponseSyntax) **   <a name="DX-DeleteConnection-response-hasLogicalRedundancy"></a>
Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).
Type: String
Valid Values: `unknown | yes | no`

 ** [jumboFrameCapable](#API_DeleteConnection_ResponseSyntax) **   <a name="DX-DeleteConnection-response-jumboFrameCapable"></a>
Indicates whether jumbo frames are supported.
Type: Boolean

 ** [lagId](#API_DeleteConnection_ResponseSyntax) **   <a name="DX-DeleteConnection-response-lagId"></a>
The ID of the LAG.
Type: String

 ** [loaIssueTime](#API_DeleteConnection_ResponseSyntax) **   <a name="DX-DeleteConnection-response-loaIssueTime"></a>
The time of the most recent call to [DescribeLoa](API_DescribeLoa.md) for this connection.
Type: Timestamp

 ** [location](#API_DeleteConnection_ResponseSyntax) **   <a name="DX-DeleteConnection-response-location"></a>
The location of the connection.
Type: String

 ** [macSecCapable](#API_DeleteConnection_ResponseSyntax) **   <a name="DX-DeleteConnection-response-macSecCapable"></a>
Indicates whether the connection supports MAC Security (MACsec).
Type: Boolean

 ** [macSecKeys](#API_DeleteConnection_ResponseSyntax) **   <a name="DX-DeleteConnection-response-macSecKeys"></a>
The MAC Security (MACsec) security keys associated with the connection.
Type: Array of [MacSecKey](API_MacSecKey.md) objects

 ** [ownerAccount](#API_DeleteConnection_ResponseSyntax) **   <a name="DX-DeleteConnection-response-ownerAccount"></a>
The ID of the AWS account that owns the connection.
Type: String

 ** [partnerInterconnectMacSecCapable](#API_DeleteConnection_ResponseSyntax) **   <a name="DX-DeleteConnection-response-partnerInterconnectMacSecCapable"></a>
Indicates whether the interconnect hosting this connection supports MAC Security (MACsec).
Type: Boolean

 ** [partnerName](#API_DeleteConnection_ResponseSyntax) **   <a name="DX-DeleteConnection-response-partnerName"></a>
The name of the Direct Connect service provider associated with the connection.
Type: String

 ** [portEncryptionStatus](#API_DeleteConnection_ResponseSyntax) **   <a name="DX-DeleteConnection-response-portEncryptionStatus"></a>
The MAC Security (MACsec) port link status of the connection.
The valid values are `Encryption Up`, which means that there is an active Connection Key Name, or `Encryption Down`.
Type: String

 ** [providerName](#API_DeleteConnection_ResponseSyntax) **   <a name="DX-DeleteConnection-response-providerName"></a>
The name of the service provider associated with the connection.
Type: String

 ** [rateLimiterStatus](#API_DeleteConnection_ResponseSyntax) **   <a name="DX-DeleteConnection-response-rateLimiterStatus"></a>
The rate limiter status for the connection, including how many rate limiters are in use and the maximum allowed.
Type: [RateLimiterStatus](API_RateLimiterStatus.md) object

 ** [region](#API_DeleteConnection_ResponseSyntax) **   <a name="DX-DeleteConnection-response-region"></a>
The AWS Region where the connection is located.
Type: String

 ** [tags](#API_DeleteConnection_ResponseSyntax) **   <a name="DX-DeleteConnection-response-tags"></a>
The tags associated with the connection.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.

 ** [vlan](#API_DeleteConnection_ResponseSyntax) **   <a name="DX-DeleteConnection-response-vlan"></a>
The ID of the VLAN.
Type: Integer

## Errors
<a name="API_DeleteConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_DeleteConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/DeleteConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/DeleteConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/DeleteConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/DeleteConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/DeleteConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/DeleteConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/DeleteConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/DeleteConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/DeleteConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/DeleteConnection)
