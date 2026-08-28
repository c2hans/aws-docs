---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html
---

# DescribeLoadBalancers
<a name="API_DescribeLoadBalancers"></a>

Describes the specified load balancers or all of your load balancers.

To describe the listeners for a load balancer, use [DescribeListeners](API_DescribeListeners.md). To describe the attributes for a load balancer, use [DescribeLoadBalancerAttributes](API_DescribeLoadBalancerAttributes.md).

## Request Parameters
<a name="API_DescribeLoadBalancers_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **LoadBalancerArns.member.N**
The Amazon Resource Names (ARN) of the load balancers. You can specify up to 20 load balancers in a single call.
Type: Array of strings
Required: No

 ** Marker **
The marker for the next set of results. (You received this marker from a previous call.)
Type: String
Required: No

 **Names.member.N**
The names of the load balancers.
Type: Array of strings
Required: No

 ** PageSize **
The maximum number of results to return with this call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 400.
Required: No

## Response Elements
<a name="API_DescribeLoadBalancers_ResponseElements"></a>

The following elements are returned by the service.

 **LoadBalancers.member.N**
Information about the load balancers.
Type: Array of [LoadBalancer](API_LoadBalancer.md) objects

 ** NextMarker **
If there are additional results, this is the marker for the next set of results. Otherwise, this is null.
Type: String

## Errors
<a name="API_DescribeLoadBalancers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

## Examples
<a name="API_DescribeLoadBalancers_Examples"></a>

### Describe a load balancer
<a name="API_DescribeLoadBalancers_Example_1"></a>

This example describes the specified load balancer.

#### Sample Request
<a name="API_DescribeLoadBalancers_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeLoadBalancers
&LoadBalancerArns.member.1=arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeLoadBalancers_Example_1_Response"></a>

```
<DescribeLoadBalancersResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <DescribeLoadBalancersResult>
    <LoadBalancers>
      <member>
        <LoadBalancerArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188</LoadBalancerArn>
        <Scheme>internet-facing</Scheme>
        <LoadBalancerName>my-load-balancer</LoadBalancerName>
        <VpcId>vpc-3ac0fb5f</VpcId>
        <CanonicalHostedZoneId>Z2P70J7EXAMPLE</CanonicalHostedZoneId>
        <CreatedTime>2016-03-25T21:26:12.920Z</CreatedTime>
        <AvailabilityZones>
          <member>
            <SubnetId>subnet-8360a9e7</SubnetId>
            <ZoneName>us-west-2a</ZoneName>
          </member>
          <member>
            <SubnetId>subnet-b7d581c0</SubnetId>
            <ZoneName>us-west-2b</ZoneName>
          </member>
        </AvailabilityZones>
        <SecurityGroups>
          <member>sg-5943793c</member>
        </SecurityGroups>
        <DNSName>my-load-balancer-424835706.us-west-2.elb.amazonaws.com</DNSName>
        <State>
          <Code>active</Code>
        </State>
        <Type>application</Type>
      </member>
    </LoadBalancers>
  </DescribeLoadBalancersResult>
  <ResponseMetadata>
    <RequestId>6581c0ac-f39f-11e5-bb98-57195a6eb84a</RequestId>
  </ResponseMetadata>
</DescribeLoadBalancersResponse>
```

### Describe all load balancers
<a name="API_DescribeLoadBalancers_Example_2"></a>

This example describes all of your load balancers.

#### Sample Request
<a name="API_DescribeLoadBalancers_Example_2_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeLoadBalancers
&Version=2015-12-01
&AUTHPARAMS
```

## See Also
<a name="API_DescribeLoadBalancers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/DescribeLoadBalancers)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
