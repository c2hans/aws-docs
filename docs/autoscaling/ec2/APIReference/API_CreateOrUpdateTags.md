---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CreateOrUpdateTags.html
---

# CreateOrUpdateTags
<a name="API_CreateOrUpdateTags"></a>

Creates or updates tags for the specified Auto Scaling group.

When you specify a tag with a key that already exists, the operation overwrites the previous tag definition, and you do not get an error message.

For more information, see [Tag Auto Scaling groups and instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-tagging.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Request Parameters
<a name="API_CreateOrUpdateTags_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Tags.member.N**
One or more tags.
Type: Array of [Tag](API_Tag.md) objects
Required: Yes

## Errors
<a name="API_CreateOrUpdateTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExists **
You already have an Auto Scaling group or launch configuration with this name.
 ** message **

HTTP Status Code: 400

 ** LimitExceeded **
You have already reached a limit for your Amazon EC2 Auto Scaling resources (for example, Auto Scaling groups, launch configurations, or lifecycle hooks). For more information, see [DescribeAccountLimits](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAccountLimits.html).
 ** message **

HTTP Status Code: 400

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

 ** ResourceInUse **
The operation can't be performed because the resource is in use.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_CreateOrUpdateTags_Examples"></a>

### Example
<a name="API_CreateOrUpdateTags_Example_1"></a>

This example illustrates one usage of CreateOrUpdateTags.

#### Sample Request
<a name="API_CreateOrUpdateTags_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=CreateOrUpdateTags
&Tags.member.1.ResourceId=my-asg
&Tags.member.1.ResourceType=auto-scaling-group
&Tags.member.1.Key=environment
&Tags.member.1.Value=test
&Tags.member.1.PropagateAtLaunch=true
&Version=2011-01-01
&AUTHPARAMS
```

## See Also
<a name="API_CreateOrUpdateTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/CreateOrUpdateTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/CreateOrUpdateTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/CreateOrUpdateTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/CreateOrUpdateTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/CreateOrUpdateTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/CreateOrUpdateTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/CreateOrUpdateTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/CreateOrUpdateTags)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/CreateOrUpdateTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/CreateOrUpdateTags)
