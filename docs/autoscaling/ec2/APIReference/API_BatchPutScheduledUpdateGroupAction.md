---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_BatchPutScheduledUpdateGroupAction.html
---

# BatchPutScheduledUpdateGroupAction
<a name="API_BatchPutScheduledUpdateGroupAction"></a>

Creates or updates one or more scheduled scaling actions for an Auto Scaling group.

## Request Parameters
<a name="API_BatchPutScheduledUpdateGroupAction_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 **ScheduledUpdateGroupActions.member.N**
One or more scheduled actions. The maximum number allowed is 50.
Type: Array of [ScheduledUpdateGroupActionRequest](API_ScheduledUpdateGroupActionRequest.md) objects
Required: Yes

## Response Elements
<a name="API_BatchPutScheduledUpdateGroupAction_ResponseElements"></a>

The following element is returned by the service.

 **FailedScheduledUpdateGroupActions.member.N**
The names of the scheduled actions that could not be created or updated, including an error message.
Type: Array of [FailedScheduledUpdateGroupActionRequest](API_FailedScheduledUpdateGroupActionRequest.md) objects

## Errors
<a name="API_BatchPutScheduledUpdateGroupAction_Errors"></a>

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

## See Also
<a name="API_BatchPutScheduledUpdateGroupAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/BatchPutScheduledUpdateGroupAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/BatchPutScheduledUpdateGroupAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/BatchPutScheduledUpdateGroupAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/BatchPutScheduledUpdateGroupAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/BatchPutScheduledUpdateGroupAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/BatchPutScheduledUpdateGroupAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/BatchPutScheduledUpdateGroupAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/BatchPutScheduledUpdateGroupAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/BatchPutScheduledUpdateGroupAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/BatchPutScheduledUpdateGroupAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
