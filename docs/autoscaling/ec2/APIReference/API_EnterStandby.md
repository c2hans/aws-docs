---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_EnterStandby.html
---

# EnterStandby
<a name="API_EnterStandby"></a>

Moves the specified instances into the standby state.

If you choose to decrement the desired capacity of the Auto Scaling group, the instances can enter standby as long as the desired capacity of the Auto Scaling group after the instances are placed into standby is equal to or greater than the minimum capacity of the group.

If you choose not to decrement the desired capacity of the Auto Scaling group, the Auto Scaling group launches new instances to replace the instances on standby.

For more information, see [Temporarily removing instances from your Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-enter-exit-standby.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Request Parameters
<a name="API_EnterStandby_RequestParameters"></a>

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
Indicates whether to decrement the desired capacity of the Auto Scaling group by the number of instances moved to `Standby` mode.
Type: Boolean
Required: Yes

## Response Elements
<a name="API_EnterStandby_ResponseElements"></a>

The following element is returned by the service.

 **Activities.member.N**
The activities related to moving instances into `Standby` mode.
Type: Array of [Activity](API_Activity.md) objects

## Errors
<a name="API_EnterStandby_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

## Examples
<a name="API_EnterStandby_Examples"></a>

### Example
<a name="API_EnterStandby_Example_1"></a>

This example illustrates one usage of EnterStandby.

#### Sample Request
<a name="API_EnterStandby_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=EnterStandby
&AutoScalingGroupName=my-asg
&InstanceIds.member.1=i-1234567890abcdef0
&ShouldDecrementDesiredCapacity=true
&Version=2011-01-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_EnterStandby_Example_1_Response"></a>

```
<EnterStandbyResponse xmlns="https://autoscaling.amazonaws.com/doc/2011-01-01/">
  <EnterStandbyResult>
    <Activities>
      <member>
        <ActivityId>12345678-1234-1234-1234-123456789012</ActivityId>
        <AutoScalingGroupName>my-asg</AutoScalingGroupName>
        <Description>Moving EC2 instance to Standby: i-1234567890abcdef0</Description>
        <Progress>50</Progress>
        <Cause>At 2022-06-13T22:35:50Z instance i-1234567890abcdef0 was moved to standby in response to a user request, shrinking the capacity from 4 to 3.</Cause>
        <StartTime>2022-06-13T22:35:50.884Z</StartTime>
        <Details>{"Availability Zone":"us-east-1a","SubnetID":"subnet-057fa0918fEXAMPLE"}</Details>
        <StatusCode>InProgress</StatusCode>
      </member>
    </Activities>
  </EnterStandbyResult>
  <ResponseMetadata>
    <RequestId>7c6e177f-f082-11e1-ac58-3714bEXAMPLE</RequestId>
  </ResponseMetadata>
</EnterStandbyResponse>
```

## See Also
<a name="API_EnterStandby_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/EnterStandby)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/EnterStandby)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/EnterStandby)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/EnterStandby)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/EnterStandby)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/EnterStandby)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/EnterStandby)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/EnterStandby)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/EnterStandby)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/EnterStandby)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
