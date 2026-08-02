---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TerminateClientVpnConnections.html
---

# TerminateClientVpnConnections
<a name="API_TerminateClientVpnConnections"></a>

Terminates active Client VPN endpoint connections. This action can be used to terminate a specific client connection, or up to five connections established by a specific user.

## Request Parameters
<a name="API_TerminateClientVpnConnections_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientVpnEndpointId**
The ID of the Client VPN endpoint to which the client is connected.
Type: String
Required: Yes

 **ConnectionId**
The ID of the client connection to be terminated.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Username**
The name of the user who initiated the connection. Use this option to terminate all active connections for the specified user. This option can only be used if the user has established up to five connections.
Type: String
Required: No

## Response Elements
<a name="API_TerminateClientVpnConnections_ResponseElements"></a>

The following elements are returned by the service.

 **clientVpnEndpointId**
The ID of the Client VPN endpoint.
Type: String

 **connectionStatuses**
The current state of the client connections.
Type: Array of [TerminateConnectionStatus](API_TerminateConnectionStatus.md) objects

 **requestId**
The ID of the request.
Type: String

 **username**
The user who established the terminated client connections.
Type: String

## Errors
<a name="API_TerminateClientVpnConnections_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_TerminateClientVpnConnections_Examples"></a>

### Example
<a name="API_TerminateClientVpnConnections_Example_1"></a>

This example terminates a Client VPN endpoint connection.

#### Sample Request
<a name="API_TerminateClientVpnConnections_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=TerminateClientVpnConnections
&ClientVpnEndpointId=cvpn-endpoint-00c5d11fc4EXAMPLE
&ConnectionId=cvpn-connection-010b1282b7EXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_TerminateClientVpnConnections_Example_1_Response"></a>

```
<TerminateClientVpnConnectionsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
	<clientVpnEndpointId>cvpn-endpoint-00c5d11fc4EXAMPLE</clientVpnEndpointId>
	<connectionStatuses>
		<Item>
			<connectionId>cvpn-connection-010b1282b7EXAMPLE</connectionId>
		       <currentStatus>
				<code>terminating</code>
		       </currentStatus>
		       <previousStatus>
			       <code>active</code>
		       </previousStatus>
	       </Item>
    </connectionStatuses>
	<requestId>00d80748-708d-40f7-8635-f34acEXAMPLE</requestId>
</TerminateClientVpnConnectionsResponse>
```

## See Also
<a name="API_TerminateClientVpnConnections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/TerminateClientVpnConnections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/TerminateClientVpnConnections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TerminateClientVpnConnections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/TerminateClientVpnConnections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TerminateClientVpnConnections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/TerminateClientVpnConnections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/TerminateClientVpnConnections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/TerminateClientVpnConnections)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/TerminateClientVpnConnections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TerminateClientVpnConnections)
