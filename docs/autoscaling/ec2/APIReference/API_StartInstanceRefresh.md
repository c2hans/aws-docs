---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_StartInstanceRefresh.html
---

# StartInstanceRefresh
<a name="API_StartInstanceRefresh"></a>

Starts an instance refresh.

This operation is part of the [instance refresh feature](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html) in Amazon EC2 Auto Scaling, which helps you update instances in your Auto Scaling group. This feature is helpful, for example, when you have a new AMI or a new user data script. You just need to create a new launch template that specifies the new AMI or user data script. Then start an instance refresh to immediately begin the process of updating instances in the group.

If successful, the request's response contains a unique ID that you can use to track the progress of the instance refresh. To query its status, call the [DescribeInstanceRefreshes](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeInstanceRefreshes.html) API. To describe the instance refreshes that have already run, call the [DescribeInstanceRefreshes](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeInstanceRefreshes.html) API. To cancel an instance refresh that is in progress, use the [CancelInstanceRefresh](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CancelInstanceRefresh.html) API.

An instance refresh might fail for several reasons, such as EC2 launch failures, misconfigured health checks, or not ignoring or allowing the termination of instances that are in `Standby` state or protected from scale in. You can monitor for failed EC2 launches using the scaling activities. To find the scaling activities, call the [DescribeScalingActivities](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeScalingActivities.html) API.

If you enable auto rollback, your Auto Scaling group will be rolled back automatically when the instance refresh fails. You can enable this feature before starting an instance refresh by specifying the `AutoRollback` property in the instance refresh preferences. Otherwise, to roll back an instance refresh before it finishes, use the [RollbackInstanceRefresh](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_RollbackInstanceRefresh.html) API.

## Request Parameters
<a name="API_StartInstanceRefresh_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** DesiredConfiguration **
The desired configuration. For example, the desired configuration can specify a new launch template or a new version of the current launch template.
Once the instance refresh succeeds, Amazon EC2 Auto Scaling updates the settings of the Auto Scaling group to reflect the new desired configuration.
When you specify a new launch template or a new version of the current launch template for your desired configuration, consider enabling the `SkipMatching` property in preferences. If it's enabled, Amazon EC2 Auto Scaling skips replacing instances that already use the specified launch template and instance types. This can help you reduce the number of replacements that are required to apply updates.
Type: [DesiredConfiguration](API_DesiredConfiguration.md) object
Required: No

 ** Preferences **
Sets your preferences for the instance refresh so that it performs as expected when you start it. Includes the instance warmup time, the minimum and maximum healthy percentages, and the behaviors that you want Amazon EC2 Auto Scaling to use if instances that are in `Standby` state or protected from scale in are found. You can also choose to enable additional features, such as the following:
+ Auto rollback
+ Checkpoints
+ CloudWatch alarms
+ Skip matching
+ Bake time
Type: [RefreshPreferences](API_RefreshPreferences.md) object
Required: No

 ** Strategy **
The strategy to use for the instance refresh. The default value is `Rolling`.
Type: String
Valid Values: `Rolling | ReplaceRootVolume`
Required: No

## Response Elements
<a name="API_StartInstanceRefresh_ResponseElements"></a>

The following element is returned by the service.

 ** InstanceRefreshId **
A unique ID for tracking the progress of the instance refresh.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

## Errors
<a name="API_StartInstanceRefresh_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InstanceRefreshInProgress **
The request failed because an active instance refresh already exists for the specified Auto Scaling group.
HTTP Status Code: 400

 ** LimitExceeded **
You have already reached a limit for your Amazon EC2 Auto Scaling resources (for example, Auto Scaling groups, launch configurations, or lifecycle hooks). For more information, see [DescribeAccountLimits](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html).
 ** message **

HTTP Status Code: 400

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

## Examples
<a name="API_StartInstanceRefresh_Examples"></a>

### Example
<a name="API_StartInstanceRefresh_Example_1"></a>

This example illustrates one usage of StartInstanceRefresh.

#### Sample Request
<a name="API_StartInstanceRefresh_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=StartInstanceRefresh
&AutoScalingGroupName=my-asg
&Preferences.AutoRollback=true
&Preferences.InstanceWarmup=200
&Preferences.MinHealthyPercentage=90
&Preferences.MaxHealthyPercentage=120
&Version=2011-01-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_StartInstanceRefresh_Example_1_Response"></a>

```
<StartInstanceRefreshResponse xmlns="https://autoscaling.amazonaws.com/doc/2011-01-01/">
  <StartInstanceRefreshResult>
    <InstanceRefreshId>ccfd3c2f-edb3-470d-af32-52cc57d201ca</InstanceRefreshId>
  </StartInstanceRefreshResult>
  <ResponseMetadata>
    <RequestId>7c6e177f-f082-11e1-ac58-3714bEXAMPLE</RequestId>
  </ResponseMetadata>
</StartInstanceRefreshResponse>
```

## See Also
<a name="API_StartInstanceRefresh_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/StartInstanceRefresh)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/StartInstanceRefresh)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/StartInstanceRefresh)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/StartInstanceRefresh)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/StartInstanceRefresh)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/StartInstanceRefresh)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/StartInstanceRefresh)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/StartInstanceRefresh)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/StartInstanceRefresh)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/StartInstanceRefresh)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
