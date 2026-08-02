---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateLag.html
---

# CreateLag
<a name="API_CreateLag"></a>

Creates a link aggregation group (LAG) with the specified number of bundled physical dedicated connections between the customer network and a specific Direct Connect location. A LAG is a logical interface that uses the Link Aggregation Control Protocol (LACP) to aggregate multiple interfaces, enabling you to treat them as a single interface.

All connections in a LAG must use the same bandwidth (either 1Gbps, 10Gbps, 100Gbps, or 400Gbps) and must terminate at the same Direct Connect endpoint.

You can have up to 10 dedicated connections per location. Regardless of this limit, if you request more connections for the LAG than Direct Connect can allocate on a single endpoint, no LAG is created..

You can specify an existing physical dedicated connection or interconnect to include in the LAG (which counts towards the total number of connections). Doing so interrupts the current physical dedicated connection, and re-establishes them as a member of the LAG. The LAG will be created on the same Direct Connect endpoint to which the dedicated connection terminates. Any virtual interfaces associated with the dedicated connection are automatically disassociated and re-associated with the LAG. The connection ID does not change.

If the AWS account used to create a LAG is a registered Direct Connect Partner, the LAG is automatically enabled to host sub-connections. For a LAG owned by a partner, any associated virtual interfaces cannot be directly configured.

## Request Syntax
<a name="API_CreateLag_RequestSyntax"></a>

```
{
   "childConnectionTags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "connectionId": "{{string}}",
   "connectionsBandwidth": "{{string}}",
   "lagName": "{{string}}",
   "location": "{{string}}",
   "numberOfConnections": {{number}},
   "providerName": "{{string}}",
   "requestMACSec": {{boolean}},
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateLag_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [childConnectionTags](#API_CreateLag_RequestSyntax) **   <a name="DX-CreateLag-request-childConnectionTags"></a>
The tags to associate with the automtically created LAGs.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [connectionId](#API_CreateLag_RequestSyntax) **   <a name="DX-CreateLag-request-connectionId"></a>
The ID of an existing dedicated connection to migrate to the LAG.
Type: String
Required: No

 ** [connectionsBandwidth](#API_CreateLag_RequestSyntax) **   <a name="DX-CreateLag-request-connectionsBandwidth"></a>
The bandwidth of the individual physical dedicated connections bundled by the LAG. The possible values are 1Gbps,10Gbps, 100Gbps, and 400Gbps.
Type: String
Required: Yes

 ** [lagName](#API_CreateLag_RequestSyntax) **   <a name="DX-CreateLag-request-lagName"></a>
The name of the LAG.
Type: String
Required: Yes

 ** [location](#API_CreateLag_RequestSyntax) **   <a name="DX-CreateLag-request-location"></a>
The location for the LAG.
Type: String
Required: Yes

 ** [numberOfConnections](#API_CreateLag_RequestSyntax) **   <a name="DX-CreateLag-request-numberOfConnections"></a>
The number of physical dedicated connections initially provisioned and bundled by the LAG. You can have a maximum of four connections when the port speed is 1Gbps or 10Gbps, or two when the port speed is 100Gbps or 400Gbps.
Type: Integer
Required: Yes

 ** [providerName](#API_CreateLag_RequestSyntax) **   <a name="DX-CreateLag-request-providerName"></a>
The name of the service provider associated with the LAG.
Type: String
Required: No

 ** [requestMACSec](#API_CreateLag_RequestSyntax) **   <a name="DX-CreateLag-request-requestMACSec"></a>
Indicates whether the connection will support MAC Security (MACsec).
All connections in the LAG must be capable of supporting MAC Security (MACsec). For information about MAC Security (MACsec) prerequisties, see [MACsec prerequisties](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-mac-sec-getting-started.html#mac-sec-prerequisites) in the * Direct Connect User Guide*.
Type: Boolean
Required: No

 ** [tags](#API_CreateLag_RequestSyntax) **   <a name="DX-CreateLag-request-tags"></a>
The tags to associate with the LAG.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.
Required: No

## Response Syntax
<a name="API_CreateLag_ResponseSyntax"></a>

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
<a name="API_CreateLag_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [allowsHostedConnections](#API_CreateLag_ResponseSyntax) **   <a name="DX-CreateLag-response-allowsHostedConnections"></a>
Indicates whether the LAG can host other connections.
Type: Boolean

 ** [awsDevice](#API_CreateLag_ResponseSyntax) **   <a name="DX-CreateLag-response-awsDevice"></a>
 *This parameter has been deprecated.*
The Direct Connect endpoint that hosts the LAG.
Type: String

 ** [awsDeviceV2](#API_CreateLag_ResponseSyntax) **   <a name="DX-CreateLag-response-awsDeviceV2"></a>
The Direct Connect endpoint that hosts the LAG.
Type: String

 ** [awsLogicalDeviceId](#API_CreateLag_ResponseSyntax) **   <a name="DX-CreateLag-response-awsLogicalDeviceId"></a>
The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.
Type: String

 ** [connections](#API_CreateLag_ResponseSyntax) **   <a name="DX-CreateLag-response-connections"></a>
The connections bundled by the LAG.
Type: Array of [Connection](API_Connection.md) objects

 ** [connectionsBandwidth](#API_CreateLag_ResponseSyntax) **   <a name="DX-CreateLag-response-connectionsBandwidth"></a>
The individual bandwidth of the physical connections bundled by the LAG. The possible values are 1Gbps, 10Gbps, 100Gbps, or 400 Gbps..
Type: String

 ** [encryptionMode](#API_CreateLag_ResponseSyntax) **   <a name="DX-CreateLag-response-encryptionMode"></a>
The LAG MAC Security (MACsec) encryption mode.
The valid values are `no_encrypt`, `should_encrypt`, and `must_encrypt`.
Type: String

 ** [hasLogicalRedundancy](#API_CreateLag_ResponseSyntax) **   <a name="DX-CreateLag-response-hasLogicalRedundancy"></a>
Indicates whether the LAG supports a secondary BGP peer in the same address family (IPv4/IPv6).
Type: String
Valid Values: `unknown | yes | no`

 ** [jumboFrameCapable](#API_CreateLag_ResponseSyntax) **   <a name="DX-CreateLag-response-jumboFrameCapable"></a>
Indicates whether jumbo frames are supported.
Type: Boolean

 ** [lagId](#API_CreateLag_ResponseSyntax) **   <a name="DX-CreateLag-response-lagId"></a>
The ID of the LAG.
Type: String

 ** [lagName](#API_CreateLag_ResponseSyntax) **   <a name="DX-CreateLag-response-lagName"></a>
The name of the LAG.
Type: String

 ** [lagState](#API_CreateLag_ResponseSyntax) **   <a name="DX-CreateLag-response-lagState"></a>
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

 ** [location](#API_CreateLag_ResponseSyntax) **   <a name="DX-CreateLag-response-location"></a>
The location of the LAG.
Type: String

 ** [macSecCapable](#API_CreateLag_ResponseSyntax) **   <a name="DX-CreateLag-response-macSecCapable"></a>
Indicates whether the LAG supports MAC Security (MACsec).
Type: Boolean

 ** [macSecKeys](#API_CreateLag_ResponseSyntax) **   <a name="DX-CreateLag-response-macSecKeys"></a>
The MAC Security (MACsec) security keys associated with the LAG.
Type: Array of [MacSecKey](API_MacSecKey.md) objects

 ** [minimumLinks](#API_CreateLag_ResponseSyntax) **   <a name="DX-CreateLag-response-minimumLinks"></a>
The minimum number of physical dedicated connections that must be operational for the LAG itself to be operational.
Type: Integer

 ** [numberOfConnections](#API_CreateLag_ResponseSyntax) **   <a name="DX-CreateLag-response-numberOfConnections"></a>
The number of physical dedicated connections initially provisioned and bundled by the LAG. You can have a maximum of four connections when the port speed is 1 Gbps or 10 Gbps, or two when the port speed is 100 Gbps or 400 Gbps.
Type: Integer

 ** [ownerAccount](#API_CreateLag_ResponseSyntax) **   <a name="DX-CreateLag-response-ownerAccount"></a>
The ID of the AWS account that owns the LAG.
Type: String

 ** [providerName](#API_CreateLag_ResponseSyntax) **   <a name="DX-CreateLag-response-providerName"></a>
The name of the service provider associated with the LAG.
Type: String

 ** [rateLimiterStatus](#API_CreateLag_ResponseSyntax) **   <a name="DX-CreateLag-response-rateLimiterStatus"></a>
The rate limiter status for the LAG, including how many rate limiters are in use and the maximum allowed.
Type: [RateLimiterStatus](API_RateLimiterStatus.md) object

 ** [region](#API_CreateLag_ResponseSyntax) **   <a name="DX-CreateLag-response-region"></a>
The AWS Region where the connection is located.
Type: String

 ** [tags](#API_CreateLag_ResponseSyntax) **   <a name="DX-CreateLag-response-tags"></a>
The tags associated with the LAG.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.

## Errors
<a name="API_CreateLag_Errors"></a>

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
<a name="API_CreateLag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/CreateLag)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/CreateLag)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/CreateLag)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/CreateLag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/CreateLag)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/CreateLag)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/CreateLag)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/CreateLag)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/CreateLag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/CreateLag)
