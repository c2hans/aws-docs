---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_RegisterTargets.html
---

# RegisterTargets
<a name="API_RegisterTargets"></a>

Registers the specified targets with the specified target group.

If the target is an EC2 instance, it must be in the `running` state when you register it.

By default, the load balancer routes requests to registered targets using the protocol and port for the target group. Alternatively, you can override the port for a target when you register it. You can register each EC2 instance or IP address with the same target group multiple times using different ports.

For more information, see the following:
+  [Register targets for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-register-targets.html)
+  [Register targets for your Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/target-group-register-targets.html)
+  [Register targets for your Gateway Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/target-group-register-targets.html)

To remove a target from a target group, use [DeregisterTargets](API_DeregisterTargets.md).

## Request Parameters
<a name="API_RegisterTargets_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** TargetGroupArn **
The Amazon Resource Name (ARN) of the target group.
Type: String
Required: Yes

 **Targets.member.N**
The targets.
Type: Array of [TargetDescription](API_TargetDescription.md) objects
Required: Yes

## Errors
<a name="API_RegisterTargets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidTarget **
The specified target does not exist, is not in the same VPC as the target group, or has an unsupported instance type.
HTTP Status Code: 400

 ** TargetGroupNotFound **
The specified target group does not exist.
HTTP Status Code: 400

 ** TooManyRegistrationsForTargetId **
You've reached the limit on the number of times a target can be registered with a load balancer.
HTTP Status Code: 400

 ** TooManyTargets **
You've reached the limit on the number of targets.
HTTP Status Code: 400

## Examples
<a name="API_RegisterTargets_Examples"></a>

### Register targets by instance ID
<a name="API_RegisterTargets_Example_1"></a>

This example registers the specified instance IDs with the specified target group.

#### Sample Request
<a name="API_RegisterTargets_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=RegisterTargets
&TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067
&Targets.member.1.Id=i-80c8dd94
&Targets.member.2.Id=i-ceddcd4d
&Version=2015-12-01
&AUTHPARAMS
```

### Register targets by IP address
<a name="API_RegisterTargets_Example_2"></a>

This example registers the specified IP addresses with the specified target group.

#### Sample Request
<a name="API_RegisterTargets_Example_2_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=RegisterTargets
&TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067
&Targets.member.1.Id=10.0.42.17
&Targets.member.2.Id=192.168.0.3
&Targets.member.2.AvailabilityZone=all
&Version=2015-12-01
&AUTHPARAMS
```

### Register targets by instance ID using port overrides
<a name="API_RegisterTargets_Example_3"></a>

This example registers the specified instance with the specified target group using multiple ports. This enables you to register microservices on the same instance as targets in the target group.

#### Sample Request
<a name="API_RegisterTargets_Example_3_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=RegisterTargets
&TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067
&Targets.member.1.Id=i-80c8dd94
&Targets.member.1.Port=80
&Targets.member.2.Id=i-80c8dd94
&Targets.member.2.Port=766
&Version=2015-12-01
&AUTHPARAMS
```

### Register a Lambda function as a target
<a name="API_RegisterTargets_Example_4"></a>

This example registers the specified Lambda function with the specified target group. You must grant Elastic Load Balancing permission to invoke the Lambda function. For more information, see [Lambda functions as targets](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html) in the *Application Load Balancers Guide*.

#### Sample Request
<a name="API_RegisterTargets_Example_4_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=RegisterTargets
&TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067
&Targets.member.1.Id=aws:lambda:us-west-2:123456789012:function:my-function
&Version=2015-12-01
&AUTHPARAMS
```

## See Also
<a name="API_RegisterTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/RegisterTargets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/RegisterTargets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/RegisterTargets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/RegisterTargets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/RegisterTargets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/RegisterTargets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/RegisterTargets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/RegisterTargets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/RegisterTargets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/RegisterTargets)
