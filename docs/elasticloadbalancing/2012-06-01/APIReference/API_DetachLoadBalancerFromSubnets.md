---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DetachLoadBalancerFromSubnets.html
---

# DetachLoadBalancerFromSubnets
<a name="API_DetachLoadBalancerFromSubnets"></a>

Removes the specified subnets from the set of configured subnets for the load balancer.

After a subnet is removed, all EC2 instances registered with the load balancer in the removed subnet go into the `OutOfService` state. Then, the load balancer balances the traffic among the remaining routable subnets.

## Request Parameters
<a name="API_DetachLoadBalancerFromSubnets_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** LoadBalancerName **
The name of the load balancer.
Type: String
Required: Yes

 **Subnets.member.N**
The IDs of the subnets.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_DetachLoadBalancerFromSubnets_ResponseElements"></a>

The following element is returned by the service.

 **Subnets.member.N**
The IDs of the remaining subnets for the load balancer.
Type: Array of strings

## Errors
<a name="API_DetachLoadBalancerFromSubnets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidConfigurationRequest **
The requested configuration change is not valid.
HTTP Status Code: 409

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

## Examples
<a name="API_DetachLoadBalancerFromSubnets_Examples"></a>

### Detach a load balancer
<a name="API_DetachLoadBalancerFromSubnets_Example_1"></a>

This example detaches the specified subnet from the specified load balancer.

#### Sample Request
<a name="API_DetachLoadBalancerFromSubnets_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DetachLoadBalancerFromSubnets
&LoadBalancerName=my-vpc-loadbalancer
&Subnets.member.1=subnet-119f0078
&Version=2012-06-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DetachLoadBalancerFromSubnets_Example_1_Response"></a>

```
<DetachLoadBalancerFromSubnetsResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
  <DetachLoadBalancerFromSubnetsResult>
    <Subnets>
      <member>subnet-159f007c</member>
      <member>subnet-3561b05e</member>
    </Subnets>
  </DetachLoadBalancerFromSubnetsResult>
  <ResponseMetadata>
    <RequestId>07b1ecbc-1100-11e3-acaf-dd7edEXAMPLE</RequestId>
  </ResponseMetadata>
</DetachLoadBalancerFromSubnetsResponse>
```

## See Also
<a name="API_DetachLoadBalancerFromSubnets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancing-2012-06-01/DetachLoadBalancerFromSubnets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancing-2012-06-01/DetachLoadBalancerFromSubnets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/DetachLoadBalancerFromSubnets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancing-2012-06-01/DetachLoadBalancerFromSubnets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/DetachLoadBalancerFromSubnets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancing-2012-06-01/DetachLoadBalancerFromSubnets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancing-2012-06-01/DetachLoadBalancerFromSubnets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancing-2012-06-01/DetachLoadBalancerFromSubnets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancing-2012-06-01/DetachLoadBalancerFromSubnets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/DetachLoadBalancerFromSubnets)
