---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_AttachLoadBalancerToSubnets.html
---

# AttachLoadBalancerToSubnets
<a name="API_AttachLoadBalancerToSubnets"></a>

Adds one or more subnets to the set of configured subnets for the specified load balancer.

The load balancer evenly distributes requests across all registered subnets. For more information, see [Add or remove subnets for your Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-manage-subnets.html) in the *User Guide for Classic Load Balancers*.

## Request Parameters
<a name="API_AttachLoadBalancerToSubnets_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** LoadBalancerName **
The name of the load balancer.
Type: String
Required: Yes

 **Subnets.member.N**
The IDs of the subnets to add. You can add only one subnet per Availability Zone.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_AttachLoadBalancerToSubnets_ResponseElements"></a>

The following element is returned by the service.

 **Subnets.member.N**
The IDs of the subnets attached to the load balancer.
Type: Array of strings

## Errors
<a name="API_AttachLoadBalancerToSubnets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidConfigurationRequest **
The requested configuration change is not valid.
HTTP Status Code: 409

 ** InvalidSubnet **
The specified VPC has no associated Internet gateway.
HTTP Status Code: 400

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

 ** SubnetNotFound **
One or more of the specified subnets do not exist.
HTTP Status Code: 400

## Examples
<a name="API_AttachLoadBalancerToSubnets_Examples"></a>

### Attach subnets
<a name="API_AttachLoadBalancerToSubnets_Example_1"></a>

This example adds the specified subnet to the set of configured subnets for the specified load balancer.

#### Sample Request
<a name="API_AttachLoadBalancerToSubnets_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=AttachLoadBalancerToSubnets
&LoadBalancerName=my-vpc-loadbalancer
&Subnets.member.1=subnet-3561b05e
&Version=2012-06-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_AttachLoadBalancerToSubnets_Example_1_Response"></a>

```
<AttachLoadBalancerToSubnetsResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
  <AttachLoadBalancerToSubnetsResult>
    <Subnets>
      <member>subnet-119f0078</member>
      <member>subnet-3561b05e</member>
    </Subnets>
  </AttachLoadBalancerToSubnetsResult>
  <ResponseMetadata>
    <RequestId>07b1ecbc-1100-11e3-acaf-dd7edEXAMPLE</RequestId>
  </ResponseMetadata>
</AttachLoadBalancerToSubnetsResponse>
```

## See Also
<a name="API_AttachLoadBalancerToSubnets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancing-2012-06-01/AttachLoadBalancerToSubnets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancing-2012-06-01/AttachLoadBalancerToSubnets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/AttachLoadBalancerToSubnets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancing-2012-06-01/AttachLoadBalancerToSubnets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/AttachLoadBalancerToSubnets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancing-2012-06-01/AttachLoadBalancerToSubnets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancing-2012-06-01/AttachLoadBalancerToSubnets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancing-2012-06-01/AttachLoadBalancerToSubnets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancing-2012-06-01/AttachLoadBalancerToSubnets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/AttachLoadBalancerToSubnets)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
