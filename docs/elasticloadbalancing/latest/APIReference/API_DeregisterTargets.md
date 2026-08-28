---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DeregisterTargets.html
---

# DeregisterTargets
<a name="API_DeregisterTargets"></a>

Deregisters the specified targets from the specified target group. After the targets are deregistered, they no longer receive traffic from the load balancer.

The load balancer stops sending requests to targets that are deregistering, but uses connection draining to ensure that in-flight traffic completes on the existing connections. This deregistration delay is configured by default but can be updated for each target group.

For more information, see the following:
+  [ Deregistration delay](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/edit-target-group-attributes.html#deregistration-delay) in the *Application Load Balancers User Guide*
+  [ Deregistration delay](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/edit-target-group-attributes.html#deregistration-delay) in the *Network Load Balancers User Guide*
+  [ Deregistration delay](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/edit-target-group-attributes.html#deregistration-delay) in the *Gateway Load Balancers User Guide*

Note: If the specified target does not exist, the action returns successfully.

## Request Parameters
<a name="API_DeregisterTargets_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** TargetGroupArn **
The Amazon Resource Name (ARN) of the target group.
Type: String
Required: Yes

 **Targets.member.N**
The targets. If you specified a port override when you registered a target, you must specify both the target ID and the port when you deregister it.
Type: Array of [TargetDescription](API_TargetDescription.md) objects
Required: Yes

## Errors
<a name="API_DeregisterTargets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidTarget **
The specified target does not exist, is not in the same VPC as the target group, or has an unsupported instance type.
HTTP Status Code: 400

 ** TargetGroupNotFound **
The specified target group does not exist.
HTTP Status Code: 400

## Examples
<a name="API_DeregisterTargets_Examples"></a>

### Deregister an instance from a target group
<a name="API_DeregisterTargets_Example_1"></a>

This example deregisters the specified instance from the specified target group.

#### Sample Request
<a name="API_DeregisterTargets_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DeregisterTargets
&TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067
&Targets.member.1.Id=i-0f76fade435676abd
&Version=2015-12-01
&AUTHPARAMS
```

### Deregister an IP address from a target group
<a name="API_DeregisterTargets_Example_2"></a>

This example deregisters the specified IP address from the specified target group.

#### Sample Request
<a name="API_DeregisterTargets_Example_2_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DeregisterTargets
&TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067
&Targets.member.1.Id=10.0.1.238
&Version=2015-12-01
&AUTHPARAMS
```

## See Also
<a name="API_DeregisterTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/DeregisterTargets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/DeregisterTargets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/DeregisterTargets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/DeregisterTargets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/DeregisterTargets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/DeregisterTargets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/DeregisterTargets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/DeregisterTargets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/DeregisterTargets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/DeregisterTargets)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
