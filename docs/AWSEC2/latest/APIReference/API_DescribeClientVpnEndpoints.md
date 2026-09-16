---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClientVpnEndpoints.html
---

# DescribeClientVpnEndpoints
<a name="API_DescribeClientVpnEndpoints"></a>

Describes one or more Client VPN endpoints in the account.

## Request Parameters
<a name="API_DescribeClientVpnEndpoints_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientVpnEndpointId.N**
The ID of the Client VPN endpoint.
Type: Array of strings
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters. Filter names and values are case-sensitive.
+  `endpoint-id` - The ID of the Client VPN endpoint.
+  `transport-protocol` - The transport protocol (`tcp` \| `udp`).
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
<a name="API_DescribeClientVpnEndpoints_ResponseElements"></a>

The following elements are returned by the service.

 **clientVpnEndpoint**
Information about the Client VPN endpoints.
Type: Array of [ClientVpnEndpoint](API_ClientVpnEndpoint.md) objects

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeClientVpnEndpoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeClientVpnEndpoints_Examples"></a>

### Example
<a name="API_DescribeClientVpnEndpoints_Example_1"></a>

This example describes the Client VPN endpoints in your account.

#### Sample Request
<a name="API_DescribeClientVpnEndpoints_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeClientVpnEndpointsResponse
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeClientVpnEndpoints_Example_1_Response"></a>

```
<DescribeClientVpnEndpointsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/"">
	<requestId">e69f64d5-e763-4cf5-844e-c278b1946ddf</requestId">
	<clientVpnEndpoint">
		<item">
			<authenticationOptions">
				<item">
					<mutualAuthentication">
						<clientRootCertificateChain">arn:aws:acm:us-east-1:724145273726:certificate/82916b3c-7449-43cf-ab9e-31c18ef401c6</clientRootCertificateChain">
					</mutualAuthentication">
					<type">certificate-authentication</type">
				</item">
			</authenticationOptions">
			<clientCidrBlock">10.0.0.0/24</clientCidrBlock">
			<connectionLogOptions">
				<Enabled">false</Enabled">
			</connectionLogOptions">
			<creationTime">2018-12-11T13:14:10</creationTime">
			<description">ash-test</description">
			<dnsName">cvpn-endpoint-0043a94c5c27c7997.prod.clientvpn.us-east-1.amazonaws.com</dnsName">
			<clientVpnEndpointId">cvpn-endpoint-0043a94c5c27c7997</clientVpnEndpointId">
			<status">
				<code">pending-associate</code">
			</status">
			<serverCertificateArn">arn:aws:acm:us-east-1:724145273726:certificate/82916b3c-7449-43cf-ab9e-31c18ef401c6</serverCertificateArn">
			<splitTunnel">false</splitTunnel">
			<transportProtocol">tcp</transportProtocol">
			<vpnProtocol">openvpn</vpnProtocol">
		<item">
	</clientVpnEndpoint">
</DescribeClientVpnEndpointsResponse">
```

## See Also
<a name="API_DescribeClientVpnEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeClientVpnEndpoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeClientVpnEndpoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeClientVpnEndpoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeClientVpnEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeClientVpnEndpoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeClientVpnEndpoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeClientVpnEndpoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeClientVpnEndpoints)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeClientVpnEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeClientVpnEndpoints)
