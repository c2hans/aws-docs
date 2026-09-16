---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_RegisterInstancesWithLoadBalancer.html
---

# RegisterInstancesWithLoadBalancer
<a name="API_RegisterInstancesWithLoadBalancer"></a>

Adds the specified instances to the specified load balancer.

The instance must be a running instance in the same network as the load balancer (EC2-Classic or the same VPC). If you have EC2-Classic instances and a load balancer in a VPC with ClassicLink enabled, you can link the EC2-Classic instances to that VPC and then register the linked EC2-Classic instances with the load balancer in the VPC.

Note that `RegisterInstanceWithLoadBalancer` completes when the request has been registered. Instance registration takes a little time to complete. To check the state of the registered instances, use [DescribeLoadBalancers](API_DescribeLoadBalancers.md) or [DescribeInstanceHealth](API_DescribeInstanceHealth.md).

After the instance is registered, it starts receiving traffic and requests from the load balancer. Any instance that is not in one of the Availability Zones registered for the load balancer is moved to the `OutOfService` state. If an Availability Zone is added to the load balancer later, any instances registered with the load balancer move to the `InService` state.

To deregister instances from a load balancer, use [DeregisterInstancesFromLoadBalancer](API_DeregisterInstancesFromLoadBalancer.md).

For more information, see [Register or deregister EC2 instances](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-deregister-register-instances.html) in the *User Guide for Classic Load Balancers*.

## Request Parameters
<a name="API_RegisterInstancesWithLoadBalancer_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Instances.member.N**
The IDs of the instances.
Type: Array of [Instance](API_Instance.md) objects
Required: Yes

 ** LoadBalancerName **
The name of the load balancer.
Type: String
Required: Yes

## Response Elements
<a name="API_RegisterInstancesWithLoadBalancer_ResponseElements"></a>

The following element is returned by the service.

 **Instances.member.N**
The updated list of instances for the load balancer.
Type: Array of [Instance](API_Instance.md) objects

## Errors
<a name="API_RegisterInstancesWithLoadBalancer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInstance **
The specified endpoint is not valid.
HTTP Status Code: 400

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

## Examples
<a name="API_RegisterInstancesWithLoadBalancer_Examples"></a>

### Register instances
<a name="API_RegisterInstancesWithLoadBalancer_Example_1"></a>

This example registers the specified instance with the specified load balancer.

#### Sample Request
<a name="API_RegisterInstancesWithLoadBalancer_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=RegisterInstancesWithLoadBalancer
&LoadBalancerName=my-loadbalancer
&Instances.member.1.InstanceId=i-315b7e51
&Version=2012-06-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_RegisterInstancesWithLoadBalancer_Example_1_Response"></a>

```
<RegisterInstancesWithLoadBalancerResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
  <RegisterInstancesWithLoadBalancerResult>
    <Instances>
      <member>
        <InstanceId>i-315b7e51</InstanceId>
      </member>
    </Instances>
  </RegisterInstancesWithLoadBalancerResult>
  <ResponseMetadata>
    <RequestId>83c88b9d-12b7-11e3-8b82-87b12EXAMPLE</RequestId>
  </ResponseMetadata>
</RegisterInstancesWithLoadBalancerResponse>
```

## See Also
<a name="API_RegisterInstancesWithLoadBalancer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancing-2012-06-01/RegisterInstancesWithLoadBalancer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancing-2012-06-01/RegisterInstancesWithLoadBalancer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/RegisterInstancesWithLoadBalancer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancing-2012-06-01/RegisterInstancesWithLoadBalancer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/RegisterInstancesWithLoadBalancer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancing-2012-06-01/RegisterInstancesWithLoadBalancer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancing-2012-06-01/RegisterInstancesWithLoadBalancer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancing-2012-06-01/RegisterInstancesWithLoadBalancer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancing-2012-06-01/RegisterInstancesWithLoadBalancer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/RegisterInstancesWithLoadBalancer)
