---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateClientVpnRoute.html
---

# CreateClientVpnRoute
<a name="API_CreateClientVpnRoute"></a>

Adds a route to a network to a Client VPN endpoint. Each Client VPN endpoint has a route table that describes the available destination network routes. Each route in the route table specifies the path for traﬃc to speciﬁc resources or networks.

## Request Parameters
<a name="API_CreateClientVpnRoute_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **ClientVpnEndpointId**
The ID of the Client VPN endpoint to which to add the route.
Type: String
Required: Yes

 **Description**
A brief description of the route.
Type: String
Required: No

 **DestinationCidrBlock**
The IPv4 address range, in CIDR notation, of the route destination. For example:
+ To add a route for Internet access, enter `0.0.0.0/0`
+ To add a route for a peered VPC, enter the peered VPC's IPv4 CIDR range
+ To add a route for an on-premises network, enter the AWS Site-to-Site VPN connection's IPv4 CIDR range
+ To add a route for the local network, enter the client CIDR range
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **TargetVpcSubnetId**
The ID of the subnet through which you want to route traffic. The specified subnet must be an existing target network of the Client VPN endpoint.
Alternatively, if you're adding a route for the local network, specify `local`.
This parameter is required for VPC-based Client VPN endpoints. For Transit Gateway-based endpoints, this parameter is not required.
Type: String
Required: No

## Response Elements
<a name="API_CreateClientVpnRoute_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **status**
The current state of the route.
Type: [ClientVpnRouteStatus](API_ClientVpnRouteStatus.md) object

## Errors
<a name="API_CreateClientVpnRoute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateClientVpnRoute_Examples"></a>

### Example
<a name="API_CreateClientVpnRoute_Example_1"></a>

This example adds a route for Internet access to the Client VPN endpoint.

#### Sample Request
<a name="API_CreateClientVpnRoute_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateClientVpnRoute
&ClientVpnEndpointId=cvpn-endpoint-00c5d11fc4EXAMPLE
&DestinationCidrBlock=0.0.0.0/0
&TargetVpcSubnetId=subnet-057fa0918fEXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateClientVpnRoute_Example_1_Response"></a>

```
<CreateClientVpnRouteResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>5b301186-e6d3-436b-87d6-7c400EXAMPLE</requestId>
    <status>
        <code>creating</code>
    </status>
</CreateClientVpnRouteResponse>
```

## See Also
<a name="API_CreateClientVpnRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateClientVpnRoute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateClientVpnRoute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateClientVpnRoute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateClientVpnRoute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateClientVpnRoute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateClientVpnRoute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateClientVpnRoute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateClientVpnRoute)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateClientVpnRoute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateClientVpnRoute)
