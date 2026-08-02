---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpnConnection.html
---

# DeleteVpnConnection
<a name="API_DeleteVpnConnection"></a>

Deletes the specified VPN connection.

If you're deleting the VPC and its associated components, we recommend that you detach the virtual private gateway from the VPC and delete the VPC before deleting the VPN connection. If you believe that the tunnel credentials for your VPN connection have been compromised, you can delete the VPN connection and create a new one that has new keys, without needing to delete the VPC or virtual private gateway. If you create a new VPN connection, you must reconfigure the customer gateway device using the new configuration information returned with the new VPN connection ID.

For certificate-based authentication, delete all AWS Certificate Manager (ACM) private certificates used for the AWS-side tunnel endpoints for the VPN connection before deleting the VPN connection.

## Request Parameters
<a name="API_DeleteVpnConnection_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **VpnConnectionId**
The ID of the VPN connection.
Type: String
Required: Yes

## Response Elements
<a name="API_DeleteVpnConnection_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_DeleteVpnConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteVpnConnection_Examples"></a>

### Example
<a name="API_DeleteVpnConnection_Example_1"></a>

This example deletes the specified VPN connection.

#### Sample Request
<a name="API_DeleteVpnConnection_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteVpnConnection
&vpnConnectionId=vpn-44a8938f
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteVpnConnection_Example_1_Response"></a>

```
<DeleteVpnConnectionResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
   <return>true</return>
</DeleteVpnConnectionResponse>
```

## See Also
<a name="API_DeleteVpnConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteVpnConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteVpnConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteVpnConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteVpnConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteVpnConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteVpnConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteVpnConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteVpnConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteVpnConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteVpnConnection)
