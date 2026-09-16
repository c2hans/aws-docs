---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeConnectionsOnInterconnect.html
---

# DescribeConnectionsOnInterconnect
<a name="API_DescribeConnectionsOnInterconnect"></a>

**Note**
Deprecated. Use [DescribeHostedConnections](API_DescribeHostedConnections.md) instead.

Lists the connections that have been provisioned on the specified interconnect.

**Note**
Intended for use by Direct Connect Partners only.

## Request Syntax
<a name="API_DescribeConnectionsOnInterconnect_RequestSyntax"></a>

```
{
   "interconnectId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeConnectionsOnInterconnect_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [interconnectId](#API_DescribeConnectionsOnInterconnect_RequestSyntax) **   <a name="DX-DescribeConnectionsOnInterconnect-request-interconnectId"></a>
The ID of the interconnect.
Type: String
Required: Yes

## Response Syntax
<a name="API_DescribeConnectionsOnInterconnect_ResponseSyntax"></a>

```
{
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
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeConnectionsOnInterconnect_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [connections](#API_DescribeConnectionsOnInterconnect_ResponseSyntax) **   <a name="DX-DescribeConnectionsOnInterconnect-response-connections"></a>
The connections.
Type: Array of [Connection](API_Connection.md) objects

 ** [nextToken](#API_DescribeConnectionsOnInterconnect_ResponseSyntax) **   <a name="DX-DescribeConnectionsOnInterconnect-response-nextToken"></a>
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

## Errors
<a name="API_DescribeConnectionsOnInterconnect_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_DescribeConnectionsOnInterconnect_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/DescribeConnectionsOnInterconnect)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/DescribeConnectionsOnInterconnect)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/DescribeConnectionsOnInterconnect)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/DescribeConnectionsOnInterconnect)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/DescribeConnectionsOnInterconnect)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/DescribeConnectionsOnInterconnect)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/DescribeConnectionsOnInterconnect)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/DescribeConnectionsOnInterconnect)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/DescribeConnectionsOnInterconnect)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/DescribeConnectionsOnInterconnect)
