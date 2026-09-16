---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_ApplySecurityGroupsToLoadBalancer.html
---

# ApplySecurityGroupsToLoadBalancer
<a name="API_ApplySecurityGroupsToLoadBalancer"></a>

Associates one or more security groups with your load balancer in a virtual private cloud (VPC). The specified security groups override the previously associated security groups.

For more information, see [Security groups for your Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-groups.html#elb-vpc-security-groups) in the *User Guide for Classic Load Balancers*.

## Request Parameters
<a name="API_ApplySecurityGroupsToLoadBalancer_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** LoadBalancerName **
The name of the load balancer.
Type: String
Required: Yes

 **SecurityGroups.member.N**
The IDs of the security groups to associate with the load balancer. Note that you cannot specify the name of the security group.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_ApplySecurityGroupsToLoadBalancer_ResponseElements"></a>

The following element is returned by the service.

 **SecurityGroups.member.N**
The IDs of the security groups associated with the load balancer.
Type: Array of strings

## Errors
<a name="API_ApplySecurityGroupsToLoadBalancer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidConfigurationRequest **
The requested configuration change is not valid.
HTTP Status Code: 409

 ** InvalidSecurityGroup **
One or more of the specified security groups do not exist.
HTTP Status Code: 400

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

## Examples
<a name="API_ApplySecurityGroupsToLoadBalancer_Examples"></a>

### Associate a security group
<a name="API_ApplySecurityGroupsToLoadBalancer_Example_1"></a>

This example associates a security group with the specified load balancer in a VPC.

#### Sample Request
<a name="API_ApplySecurityGroupsToLoadBalancer_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=ApplySecurityGroupsToLoadBalancer
&LoadBalancerName=my-vpc-loadbalancer
&SecurityGroups.member.1=sg-123456789
&Version=2012-06-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_ApplySecurityGroupsToLoadBalancer_Example_1_Response"></a>

```
<ApplySecurityGroupsToLoadBalancerResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
  <ApplySecurityGroupsToLoadBalancerResult>
    <SecurityGroups>
      <member>sg-123456789</member>
    </SecurityGroups>
  </ApplySecurityGroupsToLoadBalancerResult>
  <ResponseMetadata>
    <RequestId>06b5decc-102a-11e3-9ad6-bf3e4EXAMPLE</RequestId>
  </ResponseMetadata>
</ApplySecurityGroupsToLoadBalancerResponse>
```

## See Also
<a name="API_ApplySecurityGroupsToLoadBalancer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancing-2012-06-01/ApplySecurityGroupsToLoadBalancer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancing-2012-06-01/ApplySecurityGroupsToLoadBalancer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/ApplySecurityGroupsToLoadBalancer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancing-2012-06-01/ApplySecurityGroupsToLoadBalancer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/ApplySecurityGroupsToLoadBalancer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancing-2012-06-01/ApplySecurityGroupsToLoadBalancer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancing-2012-06-01/ApplySecurityGroupsToLoadBalancer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancing-2012-06-01/ApplySecurityGroupsToLoadBalancer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancing-2012-06-01/ApplySecurityGroupsToLoadBalancer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/ApplySecurityGroupsToLoadBalancer)
