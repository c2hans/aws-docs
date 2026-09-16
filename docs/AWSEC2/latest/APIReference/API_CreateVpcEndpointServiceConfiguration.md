---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcEndpointServiceConfiguration.html
---

# CreateVpcEndpointServiceConfiguration
<a name="API_CreateVpcEndpointServiceConfiguration"></a>

Creates a VPC endpoint service to which service consumers (AWS accounts, users, and IAM roles) can connect.

Before you create an endpoint service, you must create one of the following for your service:
+ A [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/). Service consumers connect to your service using an interface endpoint.
+ A [Gateway Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/). Service consumers connect to your service using a Gateway Load Balancer endpoint.

If you set the private DNS name, you must prove that you own the private DNS domain name.

For more information, see the [AWS PrivateLink Guide](https://docs.aws.amazon.com/vpc/latest/privatelink/).

## Request Parameters
<a name="API_CreateVpcEndpointServiceConfiguration_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AcceptanceRequired**
Indicates whether requests from service consumers to create an endpoint to your service must be accepted manually.
To accept a request manually, use [AcceptVpcEndpointConnections](API_AcceptVpcEndpointConnections.md). To reject a request, use [RejectVpcEndpointConnections](API_RejectVpcEndpointConnections.md).
Type: Boolean
Required: No

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [How to ensure idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **GatewayLoadBalancerArn.N**
The Amazon Resource Names (ARNs) of the Gateway Load Balancers.
Type: Array of strings
Required: No

 **NetworkLoadBalancerArn.N**
The Amazon Resource Names (ARNs) of the Network Load Balancers.
Type: Array of strings
Required: No

 **PrivateDnsName**
(Interface endpoint configuration) The private DNS name to assign to the VPC endpoint service.
Type: String
Required: No

 **SupportedIpAddressType.N**
The supported IP address types. The possible values are `ipv4` and `ipv6`.
Type: Array of strings
Required: No

 **SupportedRegion.N**
The Regions from which service consumers can access the service.
Type: Array of strings
Required: No

 **TagSpecification.N**
The tags to associate with the service.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateVpcEndpointServiceConfiguration_ResponseElements"></a>

The following elements are returned by the service.

 **clientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String

 **requestId**
The ID of the request.
Type: String

 **serviceConfiguration**
Information about the service configuration.
Type: [ServiceConfiguration](API_ServiceConfiguration.md) object

## Errors
<a name="API_CreateVpcEndpointServiceConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateVpcEndpointServiceConfiguration_Examples"></a>

### Example 1
<a name="API_CreateVpcEndpointServiceConfiguration_Example_1"></a>

This example creates a VPC endpoint service configuration using the specified Network Load Balancer. This example also specifies that requests to connect to the service through a VPC endpoint must be accepted or rejected manually.

#### Sample Request
<a name="API_CreateVpcEndpointServiceConfiguration_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateVpcEndpointServiceConfiguration
&NetworkLoadBalancerArn.1=arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/net/my-nlb/e94221227f1ba532
&AcceptanceRequired=true
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateVpcEndpointServiceConfiguration_Example_1_Response"></a>

```
<CreateVpcEndpointServiceConfigurationResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>1b2f25d4-9d9f-4256-a8e3-297f7example</requestId>
    <serviceConfiguration>
        <serviceState>Available</serviceState>
        <serviceType>
            <item>
                <serviceType>Interface</serviceType>
            </item>
        </serviceType>
        <baseEndpointDnsNameSet>
            <item>vpce-svc-0552b9c1298c4f123.us-east-1.vpce.amazonaws.com</item>
        </baseEndpointDnsNameSet>
        <acceptanceRequired>true</acceptanceRequired>
        <availabilityZoneSet>
            <item>us-east-1d</item>
        </availabilityZoneSet>
        <serviceId>vpce-svc-0552b9c1298c4f123</serviceId>
        <serviceName>com.amazonaws.vpce.us-east-1.vpce-svc-0552b9c1298c4f123</serviceName>
        <networkLoadBalancerArnSet>
            <item>arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/net/my-nlb/e94221227f1ba532</item>
        </networkLoadBalancerArnSet>
    </serviceConfiguration>
</CreateVpcEndpointServiceConfigurationResponse>
```

### Example 2
<a name="API_CreateVpcEndpointServiceConfiguration_Example_2"></a>

This example creates a VPC endpoint service configuration using the specified Gateway Load Balancer. This example also specifies that all requests to connect to the service are accepted automatically.

#### Sample Request
<a name="API_CreateVpcEndpointServiceConfiguration_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateVpcEndpointServiceConfiguration
&GatewayLoadBalancerArn.1=arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/gwy/GWLBService/abc210844e429abc
&AcceptanceRequired=false
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateVpcEndpointServiceConfiguration_Example_2_Response"></a>

```
<CreateVpcEndpointServiceConfigurationResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>1b2f25d4-9d9f-4256-a8e3-297f7example</requestId>
    <serviceConfiguration>
        <serviceState>Available</serviceState>
        <serviceType>
            <item>
                <serviceType>GatewayLoadBalancer</serviceType>
            </item>
        </serviceType>
        <acceptanceRequired>false</acceptanceRequired>
        <availabilityZoneSet>
            <item>us-east-1d</item>
        </availabilityZoneSet>
        <serviceId>vpce-svc-123abcc1298abc123</serviceId>
        <serviceName>com.amazonaws.vpce.us-east-1.vpce-svc-123abcc1298abc123</serviceName>
        <gatewayLoadBalancerArnSet>
            <item>arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/gwy/GWLBService/abc210844e429abc</item>
        </gatewayLoadBalancerArnSet>
    </serviceConfiguration>
</CreateVpcEndpointServiceConfigurationResponse>
```

## See Also
<a name="API_CreateVpcEndpointServiceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateVpcEndpointServiceConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateVpcEndpointServiceConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateVpcEndpointServiceConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateVpcEndpointServiceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateVpcEndpointServiceConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateVpcEndpointServiceConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateVpcEndpointServiceConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateVpcEndpointServiceConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateVpcEndpointServiceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateVpcEndpointServiceConfiguration)
