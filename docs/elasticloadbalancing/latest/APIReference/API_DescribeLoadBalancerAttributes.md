---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancerAttributes.html
---

# DescribeLoadBalancerAttributes
<a name="API_DescribeLoadBalancerAttributes"></a>

Describes the attributes for the specified Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.

For more information, see the following:
+  [Load balancer attributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html#load-balancer-attributes) in the *Application Load Balancers Guide*
+  [Load balancer attributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html#load-balancer-attributes) in the *Network Load Balancers Guide*
+  [Load balancer attributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/gateway-load-balancers.html#load-balancer-attributes) in the *Gateway Load Balancers Guide*

## Request Parameters
<a name="API_DescribeLoadBalancerAttributes_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** LoadBalancerArn **
The Amazon Resource Name (ARN) of the load balancer.
Type: String
Required: Yes

## Response Elements
<a name="API_DescribeLoadBalancerAttributes_ResponseElements"></a>

The following element is returned by the service.

 **Attributes.member.N**
Information about the load balancer attributes.
Type: Array of [LoadBalancerAttribute](API_LoadBalancerAttribute.md) objects
Array Members: Maximum number of 20 items.

## Errors
<a name="API_DescribeLoadBalancerAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

## Examples
<a name="API_DescribeLoadBalancerAttributes_Examples"></a>

### Describe load balancer attributes
<a name="API_DescribeLoadBalancerAttributes_Example_1"></a>

This example describes the attributes of the specified load balancer.

#### Sample Request
<a name="API_DescribeLoadBalancerAttributes_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeLoadBalancerAttributes
&LoadBalancerArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeLoadBalancerAttributes_Example_1_Response"></a>

```
<DescribeLoadBalancerAttributesResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <DescribeLoadBalancerAttributesResult>
    <Attributes>
      <member>
        <Value>false</Value>
        <Key>access_logs.s3.enabled</Key>
      </member>
      <member>
        <Value>60</Value>
        <Key>idle_timeout.timeout_seconds</Key>
      </member>
      <member>
        <Value />
        <Key>access_logs.s3.prefix</Key>
      </member>
      <member>
        <Value>false</Value>
        <Key>deletion_protection.enabled</Key>
      </member>
      <member>
        <Value />
        <Key>access_logs.s3.bucket</Key>
      </member>
    </Attributes>
  </DescribeLoadBalancerAttributesResult>
  <ResponseMetadata>
    <RequestId>1528a9a4-f38e-11e5-8ead-f1e91be31786</RequestId>
  </ResponseMetadata>
</DescribeLoadBalancerAttributesResponse>
```

## See Also
<a name="API_DescribeLoadBalancerAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancerAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancerAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancerAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancerAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancerAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancerAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancerAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancerAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancerAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancerAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
