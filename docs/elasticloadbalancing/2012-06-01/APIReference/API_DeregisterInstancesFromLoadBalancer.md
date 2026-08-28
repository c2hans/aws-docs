---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DeregisterInstancesFromLoadBalancer.html
---

# DeregisterInstancesFromLoadBalancer
<a name="API_DeregisterInstancesFromLoadBalancer"></a>

Deregisters the specified instances from the specified load balancer. After the instance is deregistered, it no longer receives traffic from the load balancer.

You can use [DescribeLoadBalancers](API_DescribeLoadBalancers.md) to verify that the instance is deregistered from the load balancer.

For more information, see [Register or deregister EC2 Instances](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-deregister-register-instances.html) in the *User Guide for Classic Load Balancers*.

## Request Parameters
<a name="API_DeregisterInstancesFromLoadBalancer_RequestParameters"></a>

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
<a name="API_DeregisterInstancesFromLoadBalancer_ResponseElements"></a>

The following element is returned by the service.

 **Instances.member.N**
The remaining instances registered with the load balancer.
Type: Array of [Instance](API_Instance.md) objects

## Errors
<a name="API_DeregisterInstancesFromLoadBalancer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInstance **
The specified endpoint is not valid.
HTTP Status Code: 400

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

## Examples
<a name="API_DeregisterInstancesFromLoadBalancer_Examples"></a>

### Deregister instances
<a name="API_DeregisterInstancesFromLoadBalancer_Example_1"></a>

This example deregisters the specified instance from the specified load balancer.

#### Sample Request
<a name="API_DeregisterInstancesFromLoadBalancer_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DeregisterInstancesFromLoadBalancer
&LoadBalancerName=my-https-loadbalancer
&Instances.member.1.InstanceId=i-e3677ad7
&Version=2012-06-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeregisterInstancesFromLoadBalancer_Example_1_Response"></a>

```
<DeregisterInstancesFromLoadBalancerResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
  <DeregisterInstancesFromLoadBalancerResult>
    <Instances>
      <member>
        <InstanceId>i-6ec63d59</InstanceId>
      </member>
    </Instances>
  </DeregisterInstancesFromLoadBalancerResult>
  <ResponseMetadata>
    <RequestId>83c88b9d-12b7-11e3-8b82-87b12EXAMPLE</RequestId>
  </ResponseMetadata>
</DeregisterInstancesFromLoadBalancerResponse>
```

## See Also
<a name="API_DeregisterInstancesFromLoadBalancer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancing-2012-06-01/DeregisterInstancesFromLoadBalancer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancing-2012-06-01/DeregisterInstancesFromLoadBalancer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/DeregisterInstancesFromLoadBalancer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancing-2012-06-01/DeregisterInstancesFromLoadBalancer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/DeregisterInstancesFromLoadBalancer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancing-2012-06-01/DeregisterInstancesFromLoadBalancer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancing-2012-06-01/DeregisterInstancesFromLoadBalancer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancing-2012-06-01/DeregisterInstancesFromLoadBalancer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancing-2012-06-01/DeregisterInstancesFromLoadBalancer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/DeregisterInstancesFromLoadBalancer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
