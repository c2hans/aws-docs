---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_SetIpAddressType.html
---

# SetIpAddressType
<a name="API_SetIpAddressType"></a>

Sets the type of IP addresses used by the subnets of the specified load balancer.

## Request Parameters
<a name="API_SetIpAddressType_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** IpAddressType **
The IP address type. Internal load balancers must use `ipv4`.
[Application Load Balancers] The possible values are `ipv4` (IPv4 addresses), `dualstack` (IPv4 and IPv6 addresses), and `dualstack-without-public-ipv4` (public IPv6 addresses and private IPv4 and IPv6 addresses).
Application Load Balancer authentication supports IPv4 addresses only when connecting to an Identity Provider (IdP) or Amazon Cognito endpoint. Without a public IPv4 address the load balancer can't complete the authentication process, resulting in HTTP 500 errors.
[Network Load Balancers and Gateway Load Balancers] The possible values are `ipv4` (IPv4 addresses) and `dualstack` (IPv4 and IPv6 addresses).
Type: String
Valid Values: `ipv4 | dualstack | dualstack-without-public-ipv4`
Required: Yes

 ** LoadBalancerArn **
The Amazon Resource Name (ARN) of the load balancer.
Type: String
Required: Yes

## Response Elements
<a name="API_SetIpAddressType_ResponseElements"></a>

The following element is returned by the service.

 ** IpAddressType **
The IP address type.
Type: String
Valid Values: `ipv4 | dualstack | dualstack-without-public-ipv4`

## Errors
<a name="API_SetIpAddressType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidConfigurationRequest **
The requested configuration is not valid.
HTTP Status Code: 400

 ** InvalidSubnet **
The specified subnet is out of available addresses.
HTTP Status Code: 400

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

## Examples
<a name="API_SetIpAddressType_Examples"></a>

### Set the IP address type of a load balancer
<a name="API_SetIpAddressType_Example_1"></a>

This example sets the IP address type of the specified load balancer to `dualstack` to support IPv4 and IPv6 addresses. The load balancer subnets must have associated IPv6 CIDR blocks.

#### Sample Request
<a name="API_SetIpAddressType_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=SetIpAddressType
&LoadBalancerArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188
&IpAddressType=dualstack
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_SetIpAddressType_Example_1_Response"></a>

```
<SetIpAddressTypeResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <SetIpAddressTypeResult>
    <IpAddressType>dualstack</IpAddressType>
  </SetIpAddressTypeResult>
  <ResponseMetadata>
    <RequestId>a127426b-f3ab-11e5-9192-3fff33344cfa</RequestId>
  </ResponseMetadata>
</SetIpAddressTypeResponse>
```

## See Also
<a name="API_SetIpAddressType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/SetIpAddressType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/SetIpAddressType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/SetIpAddressType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/SetIpAddressType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/SetIpAddressType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/SetIpAddressType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/SetIpAddressType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/SetIpAddressType)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/SetIpAddressType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/SetIpAddressType)
