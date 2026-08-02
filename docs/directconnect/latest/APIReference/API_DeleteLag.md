---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteLag.html
---

# DeleteLag
<a name="API_DeleteLag"></a>

Deletes the specified link aggregation group (LAG). You cannot delete a LAG if it has active virtual interfaces or hosted connections.

## Request Syntax
<a name="API_DeleteLag_RequestSyntax"></a>

```
{
   "lagId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteLag_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [lagId](#API_DeleteLag_RequestSyntax) **   <a name="DX-DeleteLag-request-lagId"></a>
The ID of the LAG.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteLag_ResponseSyntax"></a>

```
{
   "allowsHostedConnections": boolean,
   "awsDevice": "string",
   "awsDeviceV2": "string",
   "awsLogicalDeviceId": "string",
   "connections": [
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
   ],
   "connectionsBandwidth": "string",
   "encryptionMode": "string",
   "hasLogicalRedundancy": "string",
   "jumboFrameCapable": boolean,
   "lagId": "string",
   "lagName": "string",
   "lagState": "string",
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
   "minimumLinks": number,
   "numberOfConnections": number,
   "ownerAccount": "string",
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
   ]
}
```

## Response Elements
<a name="API_DeleteLag_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [allowsHostedConnections](#API_DeleteLag_ResponseSyntax) **   <a name="DX-DeleteLag-response-allowsHostedConnections"></a>
Indicates whether the LAG can host other connections.
Type: Boolean

 ** [awsDevice](#API_DeleteLag_ResponseSyntax) **   <a name="DX-DeleteLag-response-awsDevice"></a>
 *This parameter has been deprecated.*
The Direct Connect endpoint that hosts the LAG.
Type: String

 ** [awsDeviceV2](#API_DeleteLag_ResponseSyntax) **   <a name="DX-DeleteLag-response-awsDeviceV2"></a>
The Direct Connect endpoint that hosts the LAG.
Type: String

 ** [awsLogicalDeviceId](#API_DeleteLag_ResponseSyntax) **   <a name="DX-DeleteLag-response-awsLogicalDeviceId"></a>
The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.
Type: String

 ** [connections](#API_DeleteLag_ResponseSyntax) **   <a name="DX-DeleteLag-response-connections"></a>
The connections bundled by the LAG.
Type: Array of [Connection](API_Connection.md) objects

 ** [connectionsBandwidth](#API_DeleteLag_ResponseSyntax) **   <a name="DX-DeleteLag-response-connectionsBandwidth"></a>
The individual bandwidth of the physical connections bundled by the LAG. The possible values are 1Gbps, 10Gbps, 100Gbps, or 400 Gbps..
Type: String

 ** [encryptionMode](#API_DeleteLag_ResponseSyntax) **   <a name="DX-DeleteLag-response-encryptionMode"></a>
The LAG MAC Security (MACsec) encryption mode.
The valid values are `no_encrypt`, `should_encrypt`, and `must_encrypt`.
Type: String

 ** [hasLogicalRedundancy](#API_DeleteLag_ResponseSyntax) **   <a name="DX-DeleteLag-response-hasLogicalRedundancy"></a>
Indicates whether the LAG supports a secondary BGP peer in the same address family (IPv4/IPv6).
Type: String
Valid Values: `unknown | yes | no`

 ** [jumboFrameCapable](#API_DeleteLag_ResponseSyntax) **   <a name="DX-DeleteLag-response-jumboFrameCapable"></a>
Indicates whether jumbo frames are supported.
Type: Boolean

 ** [lagId](#API_DeleteLag_ResponseSyntax) **   <a name="DX-DeleteLag-response-lagId"></a>
The ID of the LAG.
Type: String

 ** [lagName](#API_DeleteLag_ResponseSyntax) **   <a name="DX-DeleteLag-response-lagName"></a>
The name of the LAG.
Type: String

 ** [lagState](#API_DeleteLag_ResponseSyntax) **   <a name="DX-DeleteLag-response-lagState"></a>
The state of the LAG. The following are the possible values:
+  `requested`: The initial state of a LAG. The LAG stays in the requested state until the Letter of Authorization (LOA) is available.
+  `pending`: The LAG has been approved and is being initialized.
+  `available`: The network link is established and the LAG is ready for use.
+  `down`: The network link is down.
+  `deleting`: The LAG is being deleted.
+  `deleted`: The LAG is deleted.
+  `unknown`: The state of the LAG is not available.
Type: String
Valid Values: `requested | pending | available | down | deleting | deleted | unknown`

 ** [location](#API_DeleteLag_ResponseSyntax) **   <a name="DX-DeleteLag-response-location"></a>
The location of the LAG.
Type: String

 ** [macSecCapable](#API_DeleteLag_ResponseSyntax) **   <a name="DX-DeleteLag-response-macSecCapable"></a>
Indicates whether the LAG supports MAC Security (MACsec).
Type: Boolean

 ** [macSecKeys](#API_DeleteLag_ResponseSyntax) **   <a name="DX-DeleteLag-response-macSecKeys"></a>
The MAC Security (MACsec) security keys associated with the LAG.
Type: Array of [MacSecKey](API_MacSecKey.md) objects

 ** [minimumLinks](#API_DeleteLag_ResponseSyntax) **   <a name="DX-DeleteLag-response-minimumLinks"></a>
The minimum number of physical dedicated connections that must be operational for the LAG itself to be operational.
Type: Integer

 ** [numberOfConnections](#API_DeleteLag_ResponseSyntax) **   <a name="DX-DeleteLag-response-numberOfConnections"></a>
The number of physical dedicated connections initially provisioned and bundled by the LAG. You can have a maximum of four connections when the port speed is 1 Gbps or 10 Gbps, or two when the port speed is 100 Gbps or 400 Gbps.
Type: Integer

 ** [ownerAccount](#API_DeleteLag_ResponseSyntax) **   <a name="DX-DeleteLag-response-ownerAccount"></a>
The ID of the AWS account that owns the LAG.
Type: String

 ** [providerName](#API_DeleteLag_ResponseSyntax) **   <a name="DX-DeleteLag-response-providerName"></a>
The name of the service provider associated with the LAG.
Type: String

 ** [rateLimiterStatus](#API_DeleteLag_ResponseSyntax) **   <a name="DX-DeleteLag-response-rateLimiterStatus"></a>
The rate limiter status for the LAG, including how many rate limiters are in use and the maximum allowed.
Type: [RateLimiterStatus](API_RateLimiterStatus.md) object

 ** [region](#API_DeleteLag_ResponseSyntax) **   <a name="DX-DeleteLag-response-region"></a>
The AWS Region where the connection is located.
Type: String

 ** [tags](#API_DeleteLag_ResponseSyntax) **   <a name="DX-DeleteLag-response-tags"></a>
The tags associated with the LAG.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.

## Errors
<a name="API_DeleteLag_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_DeleteLag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/DeleteLag)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/DeleteLag)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/DeleteLag)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/DeleteLag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/DeleteLag)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/DeleteLag)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/DeleteLag)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/DeleteLag)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/DeleteLag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/DeleteLag)
