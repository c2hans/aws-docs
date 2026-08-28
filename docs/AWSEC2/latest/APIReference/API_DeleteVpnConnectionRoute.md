---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpnConnectionRoute.html
---

# DeleteVpnConnectionRoute
<a name="API_DeleteVpnConnectionRoute"></a>

Deletes the specified static route associated with a VPN connection between an existing virtual private gateway and a VPN customer gateway. The static route allows traffic to be routed from the virtual private gateway to the VPN customer gateway.

## Request Parameters
<a name="API_DeleteVpnConnectionRoute_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DestinationCidrBlock**
The CIDR block associated with the local subnet of the customer network.
Type: String
Required: Yes

 **VpnConnectionId**
The ID of the VPN connection.
Type: String
Required: Yes

## Response Elements
<a name="API_DeleteVpnConnectionRoute_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_DeleteVpnConnectionRoute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteVpnConnectionRoute_Examples"></a>

### Example
<a name="API_DeleteVpnConnectionRoute_Example_1"></a>

This example deletes a static route to the destination CIDR block `11.12.0.0/16` associated with the VPN connection with the ID `vpn-83ad48ea`. Note that when using the Query API, the "/" is denoted as "%2F".

#### Sample Request
<a name="API_DeleteVpnConnectionRoute_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteVpnConnectionRoute
&DestinationCidrBlock=11.12.0.0%2F16
&VpnConnectionId=vpn-83ad48ea
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteVpnConnectionRoute_Example_1_Response"></a>

```
<DeleteVpnConnectionRouteResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>4f35a1b2-c2c3-4093-b51f-abb9d7311990</requestId>
    <return>true</return>
</DeleteVpnConnectionRouteResponse>
```

## See Also
<a name="API_DeleteVpnConnectionRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteVpnConnectionRoute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteVpnConnectionRoute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteVpnConnectionRoute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteVpnConnectionRoute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteVpnConnectionRoute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteVpnConnectionRoute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteVpnConnectionRoute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteVpnConnectionRoute)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteVpnConnectionRoute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteVpnConnectionRoute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
