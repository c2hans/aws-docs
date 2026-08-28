---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeScalingActivities.html
---

# DescribeScalingActivities
<a name="API_DescribeScalingActivities"></a>

Gets information about the scaling activities in the account and Region.

When scaling events occur, you see a record of the scaling activity in the scaling activities. For more information, see [Verify a scaling activity for an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-verify-scaling-activity.html) in the *Amazon EC2 Auto Scaling User Guide*.

If the scaling event succeeds, the value of the `StatusCode` element in the response is `Successful`. If an attempt to launch instances failed, the `StatusCode` value is `Failed` or `Cancelled` and the `StatusMessage` element in the response indicates the cause of the failure. For help interpreting the `StatusMessage`, see [Troubleshooting Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/CHAP_Troubleshooting.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Request Parameters
<a name="API_DescribeScalingActivities_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **ActivityIds.member.N**
 The activity IDs of the desired scaling activities. If unknown activity IDs are requested, they are ignored with no error. Only activities started within the last six weeks can be returned regardless of the activity IDs specified. If other filters are specified with the request, only results matching all filter criteria can be returned.
Array Members: Maximum number of 50 IDs.
Type: Array of strings
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
 Omitting this property performs an account-wide operation, which can result in slower or timed-out requests.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 **Filters.member.N**
 One or more filters to limit the results based on specific criteria. The following filters are supported:
+  `StartTimeLowerBound` - The earliest scaling activities to return based on the activity start time. Scaling activities with a start time earlier than this value are not included in the results. Only activities started within the last six weeks can be returned regardless of the value specified.
+  `StartTimeUpperBound` - The latest scaling activities to return based on the activity start time. Scaling activities with a start time later than this value are not included in the results. Only activities started within the last six weeks can be returned regardless of the value specified.
+  `Status` - The `StatusCode` value of the scaling activity. This filter can only be used in combination with the `AutoScalingGroupName` parameter. For valid `StatusCode` values, see [Activity](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_Activity.html) in the *Amazon EC2 Auto Scaling API Reference*.
 `StartTimeLowerBound` and `StartTimeUpperBound` accept ISO 8601 formatted timestamps. Timestamps without a timezone offset are assumed to be UTC.
+  `2000-01-18T08:15:00Z`
+  `2000-01-18T16:15:00+08:00`
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** IncludeDeletedGroups **
Indicates whether to include scaling activity from deleted Auto Scaling groups.
Type: Boolean
Required: No

 ** MaxRecords **
The maximum number of items to return with this call. The default value is `100` and the maximum value is `100`.
Type: Integer
Required: No

 ** NextToken **
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## Response Elements
<a name="API_DescribeScalingActivities_ResponseElements"></a>

The following elements are returned by the service.

 **Activities.member.N**
The scaling activities. Activities are sorted by start time. Activities still in progress are described first.
Type: Array of [Activity](API_Activity.md) objects

 ** NextToken **
A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the `NextToken` value when requesting the next set of items. This value is null when there are no more items to return.
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

## Errors
<a name="API_DescribeScalingActivities_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextToken **
The `NextToken` value is not valid.
 ** message **

HTTP Status Code: 400

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

## Examples
<a name="API_DescribeScalingActivities_Examples"></a>

### Example
<a name="API_DescribeScalingActivities_Example_1"></a>

This example illustrates one usage of DescribeScalingActivities.

#### Sample Request
<a name="API_DescribeScalingActivities_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=DescribeScalingActivities
&AutoScalingGroupName=my-asg
&Version=2011-01-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeScalingActivities_Example_1_Response"></a>

```
<DescribeScalingActivitiesResponse xmlns="https://ec2.amazonaws.com/doc/2011-01-01/">
  <DescribeScalingActivitiesResult>
    <Activities>
      <member>
        <StatusCode>Failed</StatusCode>
        <Progress>0</Progress>
        <ActivityId>12345678-1234-1234-1234-123456789012</ActivityId>
        <StartTime>2019-04-12T17:32:07.882Z</StartTime>
        <AutoScalingGroupName>my-asg</AutoScalingGroupName>
        <AutoScalingGroupARN>arn:aws:autoscaling:us-east-1:123456789012:autoScalingGroup:12345678-1234-1234-1234-123456789012:autoScalingGroupName/my-asg</AutoScalingGroupARN>
        <Cause>At 2019-04-12T17:31:30Z a user request created an AutoScalingGroup changing the desired capacity from 0 to 1.  At 2019-04-12T17:32:07Z an instance was started in response to a difference between desired and actual capacity, increasing the capacity from 0 to 1.</Cause>
        <Details>{}</Details>
        <Description>Launching a new EC2 instance.  Status Reason: The image id 'ami-xxxxxxxx' does not exist. Launching EC2 instance failed.</Description>
        <EndTime>2019-04-12T17:32:08Z</EndTime>
        <StatusMessage>The image id 'ami-xxxxxxxx' does not exist. Launching EC2 instance failed.</StatusMessage>
      </member>
    </Activities>
  </DescribeScalingActivitiesResult>
  <ResponseMetadata>
    <RequestId>7c6e177f-f082-11e1-ac58-3714bEXAMPLE</RequestId>
  </ResponseMetadata>
</DescribeScalingActivitiesResponse>
```

## See Also
<a name="API_DescribeScalingActivities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/DescribeScalingActivities)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/DescribeScalingActivities)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/DescribeScalingActivities)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/DescribeScalingActivities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/DescribeScalingActivities)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/DescribeScalingActivities)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/DescribeScalingActivities)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/DescribeScalingActivities)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/DescribeScalingActivities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/DescribeScalingActivities)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
