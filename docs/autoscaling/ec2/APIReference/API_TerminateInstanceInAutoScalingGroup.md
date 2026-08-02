---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_TerminateInstanceInAutoScalingGroup.html
---

# TerminateInstanceInAutoScalingGroup
<a name="API_TerminateInstanceInAutoScalingGroup"></a>

Terminates the specified instance and optionally adjusts the desired group size. This operation cannot be called on instances in a warm pool.

This call simply makes a termination request. The instance is not terminated immediately. When an instance is terminated, the instance status changes to `terminated`. You can't connect to or start an instance after you've terminated it.

If you do not specify the option to decrement the desired capacity, Amazon EC2 Auto Scaling launches instances to replace the ones that are terminated.

By default, Amazon EC2 Auto Scaling balances instances across all Availability Zones. If you decrement the desired capacity, your Auto Scaling group can become unbalanced between Availability Zones. Amazon EC2 Auto Scaling tries to rebalance the group, and rebalancing might terminate instances in other zones. For more information, see [Manual scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scaling-manually.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Request Parameters
<a name="API_TerminateInstanceInAutoScalingGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** InstanceId **
The ID of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** ShouldDecrementDesiredCapacity **
Indicates whether terminating the instance also decrements the size of the Auto Scaling group.
Type: Boolean
Required: Yes

## Response Elements
<a name="API_TerminateInstanceInAutoScalingGroup_ResponseElements"></a>

The following element is returned by the service.

 ** Activity **
A scaling activity.
Type: [Activity](API_Activity.md) object

## Errors
<a name="API_TerminateInstanceInAutoScalingGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

 ** ScalingActivityInProgress **
The operation can't be performed because there are scaling activities in progress.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_TerminateInstanceInAutoScalingGroup_Examples"></a>

### Example
<a name="API_TerminateInstanceInAutoScalingGroup_Example_1"></a>

This example illustrates one usage of TerminateInstanceInAutoScalingGroup.

#### Sample Request
<a name="API_TerminateInstanceInAutoScalingGroup_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=TerminateInstanceInAutoScalingGroup
&InstanceId=i-1234567890abcdef0
&ShouldDecrementDesiredCapacity=true
&Version=2011-01-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_TerminateInstanceInAutoScalingGroup_Example_1_Response"></a>

```
<TerminateInstanceInAutoScalingGroupResponse xmlns="https://autoscaling.amazonaws.com/doc/2011-01-01/">
  <TerminateInstanceInAutoScalingGroupResult>
    <Activity>
      <AutoScalingGroupName>my-asg</AutoScalingGroupName>
      <ActivityId>12345678-1234-1234-1234-123456789012</ActivityId>
      <Description>Terminating EC2 instance: i-1234567890abcdef0</Description>
      <Cause>At 2022-06-14T00:07:30Z instance i-1234567890abcdef0 was taken out of service in response to a user request, shrinking the capacity from 4 to 3.</Cause>
      <StartTime>2022-06-14T00:07:30.280Z</StartTime>
      <Details>{"Availability Zone":"us-east-1a","SubnetID":"subnet-057fa0918fEXAMPLE"}</Details>
      <Progress>0</Progress>
      <StatusCode>InProgress</StatusCode>
    </Activity>
  </TerminateInstanceInAutoScalingGroupResult>
  <ResponseMetadata>
    <RequestId>7c6e177f-f082-11e1-ac58-3714bEXAMPLE</RequestId>
  </ResponseMetadata>
</TerminateInstanceInAutoScalingGroupResponse>
```

## See Also
<a name="API_TerminateInstanceInAutoScalingGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/TerminateInstanceInAutoScalingGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/TerminateInstanceInAutoScalingGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/TerminateInstanceInAutoScalingGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/TerminateInstanceInAutoScalingGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/TerminateInstanceInAutoScalingGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/TerminateInstanceInAutoScalingGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/TerminateInstanceInAutoScalingGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/TerminateInstanceInAutoScalingGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/TerminateInstanceInAutoScalingGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/TerminateInstanceInAutoScalingGroup)
