---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateInterconnect.html
---

# CreateInterconnect
<a name="API_CreateInterconnect"></a>

Creates an interconnect between an Direct Connect Partner's network and a specific Direct Connect location.

An interconnect is a connection that is capable of hosting other connections. The Direct Connect Partner can use an interconnect to provide Direct Connect hosted connections to customers through their own network services. Like a standard connection, an interconnect links the partner's network to an Direct Connect location over a standard Ethernet fiber-optic cable. One end is connected to the partner's router, the other to an Direct Connect router.

You can automatically add the new interconnect to a link aggregation group (LAG) by specifying a LAG ID in the request. This ensures that the new interconnect is allocated on the same Direct Connect endpoint that hosts the specified LAG. If there are no available ports on the endpoint, the request fails and no interconnect is created.

For each end customer, the Direct Connect Partner provisions a connection on their interconnect by calling [AllocateHostedConnection](API_AllocateHostedConnection.md). The end customer can then connect to AWS resources by creating a virtual interface on their connection, using the VLAN assigned to them by the Direct Connect Partner.

**Note**
Intended for use by Direct Connect Partners only.

## Request Syntax
<a name="API_CreateInterconnect_RequestSyntax"></a>

```
{
   "bandwidth": "{{string}}",
   "interconnectName": "{{string}}",
   "lagId": "{{string}}",
   "location": "{{string}}",
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
<a name="API_CreateInterconnect_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [bandwidth](#API_CreateInterconnect_RequestSyntax) **   <a name="DX-CreateInterconnect-request-bandwidth"></a>
The port bandwidth, in Gbps. The possible values are 1, 10, and 100.
Type: String
Required: Yes

 ** [interconnectName](#API_CreateInterconnect_RequestSyntax) **   <a name="DX-CreateInterconnect-request-interconnectName"></a>
The name of the interconnect.
Type: String
Required: Yes

 ** [lagId](#API_CreateInterconnect_RequestSyntax) **   <a name="DX-CreateInterconnect-request-lagId"></a>
The ID of the LAG.
Type: String
Required: No

 ** [location](#API_CreateInterconnect_RequestSyntax) **   <a name="DX-CreateInterconnect-request-location"></a>
The location of the interconnect.
Type: String
Required: Yes

 ** [providerName](#API_CreateInterconnect_RequestSyntax) **   <a name="DX-CreateInterconnect-request-providerName"></a>
The name of the service provider associated with the interconnect.
Type: String
Required: No

 ** [requestMACSec](#API_CreateInterconnect_RequestSyntax) **   <a name="DX-CreateInterconnect-request-requestMACSec"></a>
Indicates whether you want the interconnect to support MAC Security (MACsec).
Type: Boolean
Required: No

 ** [tags](#API_CreateInterconnect_RequestSyntax) **   <a name="DX-CreateInterconnect-request-tags"></a>
The tags to associate with the interconnect.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.
Required: No

## Response Syntax
<a name="API_CreateInterconnect_ResponseSyntax"></a>

```
{
   "awsDevice": "string",
   "awsDeviceV2": "string",
   "awsLogicalDeviceId": "string",
   "bandwidth": "string",
   "encryptionMode": "string",
   "hasLogicalRedundancy": "string",
   "interconnectId": "string",
   "interconnectName": "string",
   "interconnectState": "string",
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
   "portEncryptionStatus": "string",
   "providerName": "string",
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
<a name="API_CreateInterconnect_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [awsDevice](#API_CreateInterconnect_ResponseSyntax) **   <a name="DX-CreateInterconnect-response-awsDevice"></a>
 *This parameter has been deprecated.*
The Direct Connect endpoint on which the physical connection terminates.
Type: String

 ** [awsDeviceV2](#API_CreateInterconnect_ResponseSyntax) **   <a name="DX-CreateInterconnect-response-awsDeviceV2"></a>
The Direct Connect endpoint that terminates the physical connection.
Type: String

 ** [awsLogicalDeviceId](#API_CreateInterconnect_ResponseSyntax) **   <a name="DX-CreateInterconnect-response-awsLogicalDeviceId"></a>
The Direct Connect endpoint that terminates the logical connection. This device might be different than the device that terminates the physical connection.
Type: String

 ** [bandwidth](#API_CreateInterconnect_ResponseSyntax) **   <a name="DX-CreateInterconnect-response-bandwidth"></a>
The bandwidth of the connection.
Type: String

 ** [encryptionMode](#API_CreateInterconnect_ResponseSyntax) **   <a name="DX-CreateInterconnect-response-encryptionMode"></a>
The MAC Security (MACsec) encryption mode.
The valid values are `no_encrypt`, `should_encrypt`, and `must_encrypt`.
Type: String

 ** [hasLogicalRedundancy](#API_CreateInterconnect_ResponseSyntax) **   <a name="DX-CreateInterconnect-response-hasLogicalRedundancy"></a>
Indicates whether the interconnect supports a secondary BGP in the same address family (IPv4/IPv6).
Type: String
Valid Values: `unknown | yes | no`

 ** [interconnectId](#API_CreateInterconnect_ResponseSyntax) **   <a name="DX-CreateInterconnect-response-interconnectId"></a>
The ID of the interconnect.
Type: String

 ** [interconnectName](#API_CreateInterconnect_ResponseSyntax) **   <a name="DX-CreateInterconnect-response-interconnectName"></a>
The name of the interconnect.
Type: String

 ** [interconnectState](#API_CreateInterconnect_ResponseSyntax) **   <a name="DX-CreateInterconnect-response-interconnectState"></a>
The state of the interconnect. The following are the possible values:
+  `requested`: The initial state of an interconnect. The interconnect stays in the requested state until the Letter of Authorization (LOA) is sent to the customer.
+  `pending`: The interconnect is approved, and is being initialized.
+  `available`: The network link is up, and the interconnect is ready for use.
+  `down`: The network link is down.
+  `deleting`: The interconnect is being deleted.
+  `deleted`: The interconnect is deleted.
+  `unknown`: The state of the interconnect is not available.
Type: String
Valid Values: `requested | pending | available | down | deleting | deleted | unknown`

 ** [jumboFrameCapable](#API_CreateInterconnect_ResponseSyntax) **   <a name="DX-CreateInterconnect-response-jumboFrameCapable"></a>
Indicates whether jumbo frames are supported.
Type: Boolean

 ** [lagId](#API_CreateInterconnect_ResponseSyntax) **   <a name="DX-CreateInterconnect-response-lagId"></a>
The ID of the LAG.
Type: String

 ** [loaIssueTime](#API_CreateInterconnect_ResponseSyntax) **   <a name="DX-CreateInterconnect-response-loaIssueTime"></a>
The time of the most recent call to [DescribeLoa](API_DescribeLoa.md) for this connection.
Type: Timestamp

 ** [location](#API_CreateInterconnect_ResponseSyntax) **   <a name="DX-CreateInterconnect-response-location"></a>
The location of the connection.
Type: String

 ** [macSecCapable](#API_CreateInterconnect_ResponseSyntax) **   <a name="DX-CreateInterconnect-response-macSecCapable"></a>
Indicates whether the interconnect supports MAC Security (MACsec).
Type: Boolean

 ** [macSecKeys](#API_CreateInterconnect_ResponseSyntax) **   <a name="DX-CreateInterconnect-response-macSecKeys"></a>
The MAC Security (MACsec) security keys.
Type: Array of [MacSecKey](API_MacSecKey.md) objects

 ** [portEncryptionStatus](#API_CreateInterconnect_ResponseSyntax) **   <a name="DX-CreateInterconnect-response-portEncryptionStatus"></a>
The MAC Security (MACsec) port link status.
The valid values are `Encryption Up`, which means that there is an active Connection Key Name, or `Encryption Down`.
Type: String

 ** [providerName](#API_CreateInterconnect_ResponseSyntax) **   <a name="DX-CreateInterconnect-response-providerName"></a>
The name of the service provider associated with the interconnect.
Type: String

 ** [region](#API_CreateInterconnect_ResponseSyntax) **   <a name="DX-CreateInterconnect-response-region"></a>
The AWS Region where the connection is located.
Type: String

 ** [tags](#API_CreateInterconnect_ResponseSyntax) **   <a name="DX-CreateInterconnect-response-tags"></a>
The tags associated with the interconnect.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.

## Errors
<a name="API_CreateInterconnect_Errors"></a>

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
<a name="API_CreateInterconnect_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/CreateInterconnect)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/CreateInterconnect)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/CreateInterconnect)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/CreateInterconnect)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/CreateInterconnect)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/CreateInterconnect)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/CreateInterconnect)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/CreateInterconnect)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/CreateInterconnect)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/CreateInterconnect)
