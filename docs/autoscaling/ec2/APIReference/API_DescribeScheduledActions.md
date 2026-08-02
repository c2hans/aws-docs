---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeScheduledActions.html
---

# DescribeScheduledActions
<a name="API_DescribeScheduledActions"></a>

Gets information about the scheduled actions that haven't run or that have not reached their end time.

To describe the scaling activities for scheduled actions that have already run, call the [DescribeScalingActivities](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeScalingActivities.html) API.

## Request Parameters
<a name="API_DescribeScheduledActions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** EndTime **
The latest scheduled start time to return. If scheduled action names are provided, this property is ignored.
Type: Timestamp
Required: No

 ** MaxRecords **
The maximum number of items to return with this call. The default value is `50` and the maximum value is `100`.
Type: Integer
Required: No

 ** NextToken **
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 **ScheduledActionNames.member.N**
The names of one or more scheduled actions. If you omit this property, all scheduled actions are described. If you specify an unknown scheduled action, it is ignored with no error.
Array Members: Maximum number of 50 actions.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** StartTime **
The earliest scheduled start time to return. If scheduled action names are provided, this property is ignored.
Type: Timestamp
Required: No

## Response Elements
<a name="API_DescribeScheduledActions_ResponseElements"></a>

The following elements are returned by the service.

 ** NextToken **
A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the `NextToken` value when requesting the next set of items. This value is null when there are no more items to return.
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

 **ScheduledUpdateGroupActions.member.N**
The scheduled actions.
Type: Array of [ScheduledUpdateGroupAction](API_ScheduledUpdateGroupAction.md) objects

## Errors
<a name="API_DescribeScheduledActions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextToken **
The `NextToken` value is not valid.
 ** message **

HTTP Status Code: 400

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

## See Also
<a name="API_DescribeScheduledActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/DescribeScheduledActions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/DescribeScheduledActions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/DescribeScheduledActions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/DescribeScheduledActions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/DescribeScheduledActions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/DescribeScheduledActions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/DescribeScheduledActions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/DescribeScheduledActions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/DescribeScheduledActions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/DescribeScheduledActions)
