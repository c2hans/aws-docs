---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachInstances.html
---

# DetachInstances
<a name="API_DetachInstances"></a>

Removes one or more instances from the specified Auto Scaling group.

After the instances are detached, you can manage them independent of the Auto Scaling group.

If you do not specify the option to decrement the desired capacity, Amazon EC2 Auto Scaling launches instances to replace the ones that are detached.

If there is a Classic Load Balancer attached to the Auto Scaling group, the instances are deregistered from the load balancer. If there are target groups attached to the Auto Scaling group, the instances are deregistered from the target groups.

For more information, see [Detach or attach instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-detach-attach-instances.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Request Parameters
<a name="API_DetachInstances_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 **InstanceIds.member.N**
The IDs of the instances. You can specify up to 20 instances.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 19.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** ShouldDecrementDesiredCapacity **
Indicates whether the Auto Scaling group decrements the desired capacity value by the number of instances detached.
Type: Boolean
Required: Yes

## Response Elements
<a name="API_DetachInstances_ResponseElements"></a>

The following element is returned by the service.

 **Activities.member.N**
The activities related to detaching the instances from the Auto Scaling group.
Type: Array of [Activity](API_Activity.md) objects

## Errors
<a name="API_DetachInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

## Examples
<a name="API_DetachInstances_Examples"></a>

### Example
<a name="API_DetachInstances_Example_1"></a>

This example illustrates one usage of DetachInstances.

#### Sample Request
<a name="API_DetachInstances_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=DetachInstances
&AutoScalingGroupName=my-asg
&InstanceIds.member.1=i-1234567890abcdef0
&ShouldDecrementDesiredCapacity=true
&Version=2011-01-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DetachInstances_Example_1_Response"></a>

```
<DetachInstancesResponse xmlns="https://autoscaling.amazonaws.com/doc/2011-01-01/">
  <DetachInstancesResult>
    <Activities>
      <member>
        <ActivityId>12345678-1234-1234-1234-123456789012</ActivityId>
        <AutoScalingGroupName>my-asg</AutoScalingGroupName>
        <Description>Detaching EC2 instance: i-1234567890abcdef0</Description>
        <Cause>At 2022-06-14T00:07:30Z instance i-1234567890abcdef0 was detached in response to a user request, shrinking the capacity from 4 to 3.</Cause>
        <Progress>50</Progress>
        <StartTime>2022-06-14T00:07:30.280Z</StartTime>
        <Details>{"Availability Zone":"us-east-1a","SubnetID":"subnet-057fa0918fEXAMPLE"}</Details>
        <StatusCode>InProgress</StatusCode>
      </member>
    </Activities>
  </DetachInstancesResult>
  <ResponseMetadata>
    <RequestId>7c6e177f-f082-11e1-ac58-3714bEXAMPLE</RequestId>
  </ResponseMetadata>
</DetachInstancesResponse>
```

## See Also
<a name="API_DetachInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/DetachInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/DetachInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/DetachInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/DetachInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/DetachInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/DetachInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/DetachInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/DetachInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/DetachInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/DetachInstances)
