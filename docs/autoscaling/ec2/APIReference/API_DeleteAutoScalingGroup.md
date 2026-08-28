---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeleteAutoScalingGroup.html
---

# DeleteAutoScalingGroup
<a name="API_DeleteAutoScalingGroup"></a>

Deletes the specified Auto Scaling group.

If the group has instances or scaling activities in progress, you must specify the option to force the deletion in order for it to succeed. The force delete operation will also terminate the EC2 instances. If the group has a warm pool, the force delete option also deletes the warm pool.

To remove instances from the Auto Scaling group before deleting it, call the [DetachInstances](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachInstances.html) API with the list of instances and the option to decrement the desired capacity. This ensures that Amazon EC2 Auto Scaling does not launch replacement instances.

To terminate all instances before deleting the Auto Scaling group, call the [UpdateAutoScalingGroup](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_UpdateAutoScalingGroup.html) API and set the minimum size and desired capacity of the Auto Scaling group to zero.

If the group has scaling policies, deleting the group deletes the policies, the underlying alarm actions, and any alarm that no longer has an associated action.

For more information, see [Delete your Auto Scaling infrastructure](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-process-shutdown.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Request Parameters
<a name="API_DeleteAutoScalingGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** ForceDelete **
Specifies that the group is to be deleted along with all instances associated with the group, without waiting for all instances to be terminated. This action also deletes any outstanding lifecycle actions associated with the group.
Type: Boolean
Required: No

## Errors
<a name="API_DeleteAutoScalingGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

 ** ResourceInUse **
The operation can't be performed because the resource is in use.
 ** message **

HTTP Status Code: 400

 ** ScalingActivityInProgress **
The operation can't be performed because there are scaling activities in progress.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_DeleteAutoScalingGroup_Examples"></a>

### Example
<a name="API_DeleteAutoScalingGroup_Example_1"></a>

This example illustrates one usage of DeleteAutoScalingGroup.

#### Sample Request
<a name="API_DeleteAutoScalingGroup_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=DeleteAutoScalingGroup
&AutoScalingGroupName=my-asg
&ForceDelete=true
&Version=2011-01-01
&AUTHPARAMS
```

## See Also
<a name="API_DeleteAutoScalingGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/DeleteAutoScalingGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/DeleteAutoScalingGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/DeleteAutoScalingGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/DeleteAutoScalingGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/DeleteAutoScalingGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/DeleteAutoScalingGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/DeleteAutoScalingGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/DeleteAutoScalingGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/DeleteAutoScalingGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/DeleteAutoScalingGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
