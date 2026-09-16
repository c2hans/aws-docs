---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteClientVpnRoute.html
---

# DeleteClientVpnRoute
<a name="API_DeleteClientVpnRoute"></a>

Deletes a route from a Client VPN endpoint. You can only delete routes that you manually added using the **CreateClientVpnRoute** action. You cannot delete routes that were automatically added when associating a subnet. To remove routes that have been automatically added, disassociate the target subnet from the Client VPN endpoint.

## Request Parameters
<a name="API_DeleteClientVpnRoute_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientVpnEndpointId**
The ID of the Client VPN endpoint from which the route is to be deleted.
Type: String
Required: Yes

 **DestinationCidrBlock**
The IPv4 address range, in CIDR notation, of the route to be deleted.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **TargetVpcSubnetId**
The ID of the target subnet used by the route.
Type: String
Required: No

## Response Elements
<a name="API_DeleteClientVpnRoute_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **status**
The current state of the route.
Type: [ClientVpnRouteStatus](API_ClientVpnRouteStatus.md) object

## Errors
<a name="API_DeleteClientVpnRoute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteClientVpnRoute_Examples"></a>

### Example
<a name="API_DeleteClientVpnRoute_Example_1"></a>

This example deletes a route from a Client VPN endpoint.

#### Sample Request
<a name="API_DeleteClientVpnRoute_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteClientVpnRoute
&ClientVpnEndpointId=cvpn-endpoint-00c5d11fc4EXAMPLE
&DestinationCidrBlock=0.0.0.0/0
&TargetVpcSubnetId=subnet-057fa0918fEXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteClientVpnRoute_Example_1_Response"></a>

```
<DeleteClientVpnRouteResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>00d80748-708d-40f7-8635-f34acEXAMPLE</requestId>
    <status>
        <code>deleting</code>
    </status>
</DeleteClientVpnRouteResponse>
```

## See Also
<a name="API_DeleteClientVpnRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteClientVpnRoute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteClientVpnRoute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteClientVpnRoute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteClientVpnRoute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteClientVpnRoute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteClientVpnRoute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteClientVpnRoute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteClientVpnRoute)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteClientVpnRoute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteClientVpnRoute)
