---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_SetSecurityGroups.html
---

# SetSecurityGroups
<a name="API_SetSecurityGroups"></a>

Associates the specified security groups with the specified Application Load Balancer or Network Load Balancer. The specified security groups override the previously associated security groups.

You can't perform this operation on a Network Load Balancer unless you specified a security group for the load balancer when you created it.

You can't associate a security group with a Gateway Load Balancer.

## Request Parameters
<a name="API_SetSecurityGroups_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic **
Indicates whether to evaluate inbound security group rules for traffic sent to a Network Load Balancer through AWS PrivateLink. Applies only if the load balancer has an associated security group. The default is `on`.
Type: String
Valid Values: `on | off`
Required: No

 ** LoadBalancerArn **
The Amazon Resource Name (ARN) of the load balancer.
Type: String
Required: Yes

 **SecurityGroups.member.N**
The IDs of the security groups.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_SetSecurityGroups_ResponseElements"></a>

The following elements are returned by the service.

 ** EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic **
Indicates whether to evaluate inbound security group rules for traffic sent to a Network Load Balancer through AWS PrivateLink.
Type: String
Valid Values: `on | off`

 **SecurityGroupIds.member.N**
The IDs of the security groups associated with the load balancer.
Type: Array of strings

## Errors
<a name="API_SetSecurityGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidConfigurationRequest **
The requested configuration is not valid.
HTTP Status Code: 400

 ** InvalidSecurityGroup **
The specified security group does not exist.
HTTP Status Code: 400

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

## Examples
<a name="API_SetSecurityGroups_Examples"></a>

### Associate a security group with a load balancer
<a name="API_SetSecurityGroups_Example_1"></a>

This example associates the specified security group with the specified load balancer.

#### Sample Request
<a name="API_SetSecurityGroups_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=SetSecurityGroups
&LoadBalancerArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188
&SecurityGroups.member.1=sg-5943793c
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_SetSecurityGroups_Example_1_Response"></a>

```
<SetSecurityGroupsResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <SetSecurityGroupsResult>
    <SecurityGroupIds>
      <member>sg-5943793c</member>
    </SecurityGroupIds>
  </SetSecurityGroupsResult>
  <ResponseMetadata>
    <RequestId>a127426b-f3ab-11e5-9192-3fff33344cfa</RequestId>
  </ResponseMetadata>
</SetSecurityGroupsResponse>
```

## See Also
<a name="API_SetSecurityGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/SetSecurityGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/SetSecurityGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/SetSecurityGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/SetSecurityGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/SetSecurityGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/SetSecurityGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/SetSecurityGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/SetSecurityGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/SetSecurityGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/SetSecurityGroups)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
