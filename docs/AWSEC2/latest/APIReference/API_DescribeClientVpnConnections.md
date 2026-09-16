---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClientVpnConnections.html
---

# DescribeClientVpnConnections
<a name="API_DescribeClientVpnConnections"></a>

Describes active client connections and connections that have been terminated within the last 60 minutes for the specified Client VPN endpoint.

## Request Parameters
<a name="API_DescribeClientVpnConnections_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientVpnEndpointId**
The ID of the Client VPN endpoint.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters. Filter names and values are case-sensitive.
+  `connection-id` - The ID of the connection.
+  `username` - For Active Directory client authentication, the user name of the client who established the client connection.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the nextToken value.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1000.
Required: No

 **NextToken**
The token to retrieve the next page of results.
Type: String
Required: No

## Response Elements
<a name="API_DescribeClientVpnConnections_ResponseElements"></a>

The following elements are returned by the service.

 **connections**
Information about the active and terminated client connections.
Type: Array of [ClientVpnConnection](API_ClientVpnConnection.md) objects

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeClientVpnConnections_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeClientVpnConnections_Examples"></a>

### Example
<a name="API_DescribeClientVpnConnections_Example_1"></a>

This example describes Client VPN endpoint connections.

#### Sample Request
<a name="API_DescribeClientVpnConnections_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeClientVpnConnections
&ClientVpnEndpointId=cvpn-endpoint-00c5d11fc4EXAMPLE
&TargetNetworkCidr=10.0.0.0/16
&RevokeAllGroups=true
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeClientVpnConnections_Example_1_Response"></a>

```
<DescribeClientVpnConnectionsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>7263df00-d3ed-4f32-a3b9-88177EXAMPLE</requestId>
    <connections>
        <item>
            <clientIp>11.0.0.98</clientIp>
            <commonName>client1</commonName>
            <connectionEndTime>2018-12-13 18:38:10</connectionEndTime>
            <connectionEstablishedTime>2018-12-13 18:32:49</connectionEstablishedTime>
            <connectionId>cvpn-connection-010b1282b7EXAMPLE</connectionId>
            <egressBytes>14891</egressBytes>
            <egressPackets>309</egressPackets>
            <clientVpnEndpointId>cvpn-endpoint-00c5d11fc4EXAMPLE</clientVpnEndpointId>
            <ingressBytes>14947</ingressBytes>
            <ingressPackets>285</ingressPackets>
            <status>
                <code>terminated</code>
            </status>
            <timestamp>2018-12-13 18:38:10</timestamp>
        </item>
    </connections>
</DescribeClientVpnConnectionsResponse>
```

## See Also
<a name="API_DescribeClientVpnConnections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeClientVpnConnections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeClientVpnConnections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeClientVpnConnections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeClientVpnConnections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeClientVpnConnections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeClientVpnConnections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeClientVpnConnections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeClientVpnConnections)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeClientVpnConnections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeClientVpnConnections)
