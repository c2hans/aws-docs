---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcEndpointServiceConfiguration.html
---

# ModifyVpcEndpointServiceConfiguration
<a name="API_ModifyVpcEndpointServiceConfiguration"></a>

Modifies the attributes of the specified VPC endpoint service configuration.

If you set or modify the private DNS name, you must prove that you own the private DNS domain name.

## Request Parameters
<a name="API_ModifyVpcEndpointServiceConfiguration_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AcceptanceRequired**
Indicates whether requests to create an endpoint to the service must be accepted.
Type: Boolean
Required: No

 **AddGatewayLoadBalancerArn.N**
The Amazon Resource Names (ARNs) of Gateway Load Balancers to add to the service configuration.
Type: Array of strings
Required: No

 **AddNetworkLoadBalancerArn.N**
The Amazon Resource Names (ARNs) of Network Load Balancers to add to the service configuration.
Type: Array of strings
Required: No

 **AddSupportedIpAddressType.N**
The IP address types to add to the service configuration.
Type: Array of strings
Required: No

 **AddSupportedRegion.N**
The supported Regions to add to the service configuration.
Type: Array of strings
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **PrivateDnsName**
(Interface endpoint configuration) The private DNS name to assign to the endpoint service.
Type: String
Required: No

 **RemoveGatewayLoadBalancerArn.N**
The Amazon Resource Names (ARNs) of Gateway Load Balancers to remove from the service configuration.
Type: Array of strings
Required: No

 **RemoveNetworkLoadBalancerArn.N**
The Amazon Resource Names (ARNs) of Network Load Balancers to remove from the service configuration.
Type: Array of strings
Required: No

 **RemovePrivateDnsName**
(Interface endpoint configuration) Removes the private DNS name of the endpoint service.
Type: Boolean
Required: No

 **RemoveSupportedIpAddressType.N**
The IP address types to remove from the service configuration.
Type: Array of strings
Required: No

 **RemoveSupportedRegion.N**
The supported Regions to remove from the service configuration.
Type: Array of strings
Required: No

 **ServiceId**
The ID of the service.
Type: String
Required: Yes

## Response Elements
<a name="API_ModifyVpcEndpointServiceConfiguration_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Returns `true` if the request succeeds; otherwise, it returns an error.
Type: Boolean

## Errors
<a name="API_ModifyVpcEndpointServiceConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyVpcEndpointServiceConfiguration_Examples"></a>

### Example
<a name="API_ModifyVpcEndpointServiceConfiguration_Example_1"></a>

This example modifies service configuration `vpce-svc-03d5ebb7d9579a2b3` to specify that acceptance is required for interface VPC endpoint connection requests to the service, and to assign a private DNS name to the endpoint service.

#### Sample Request
<a name="API_ModifyVpcEndpointServiceConfiguration_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyVpcEndpointServiceConfiguration
&ServiceId=vpce-svc-03d5ebb7d9579a2b3
&AcceptanceRequired=true
&PrivateDnsName=myexampleservice.com
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyVpcEndpointServiceConfiguration_Example_1_Response"></a>

```
<ModifyVpcEndpointServiceConfigurationResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>08d80840-f750-42db-a6f8-2cd32example</requestId>
    <return>true</return>
</ModifyVpcEndpointServiceConfigurationResponse>
```

## See Also
<a name="API_ModifyVpcEndpointServiceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyVpcEndpointServiceConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyVpcEndpointServiceConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyVpcEndpointServiceConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyVpcEndpointServiceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyVpcEndpointServiceConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyVpcEndpointServiceConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyVpcEndpointServiceConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyVpcEndpointServiceConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyVpcEndpointServiceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyVpcEndpointServiceConfiguration)
