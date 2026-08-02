---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeInstanceRefreshes.html
---

# DescribeInstanceRefreshes
<a name="API_DescribeInstanceRefreshes"></a>

Gets information about the instance refreshes for the specified Auto Scaling group from the previous six weeks.

This operation is part of the [instance refresh feature](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html) in Amazon EC2 Auto Scaling, which helps you update instances in your Auto Scaling group after you make configuration changes.

To help you determine the status of an instance refresh, Amazon EC2 Auto Scaling returns information about the instance refreshes you previously initiated, including their status, start time, end time, the percentage of the instance refresh that is complete, and the number of instances remaining to update before the instance refresh is complete. If a rollback is initiated while an instance refresh is in progress, Amazon EC2 Auto Scaling also returns information about the rollback of the instance refresh.

## Request Parameters
<a name="API_DescribeInstanceRefreshes_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 **InstanceRefreshIds.member.N**
One or more instance refresh IDs.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
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

## Response Elements
<a name="API_DescribeInstanceRefreshes_ResponseElements"></a>

The following elements are returned by the service.

 **InstanceRefreshes.member.N**
The instance refreshes for the specified group, sorted by creation timestamp in descending order.
Type: Array of [InstanceRefresh](API_InstanceRefresh.md) objects

 ** NextToken **
A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the `NextToken` value when requesting the next set of items. This value is null when there are no more items to return.
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

## Errors
<a name="API_DescribeInstanceRefreshes_Errors"></a>

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
<a name="API_DescribeInstanceRefreshes_Examples"></a>

### Example
<a name="API_DescribeInstanceRefreshes_Example_1"></a>

This example illustrates one usage of DescribeInstanceRefreshes.

#### Sample Request
<a name="API_DescribeInstanceRefreshes_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=DescribeInstanceRefreshes
&AutoScalingGroupName=my-asg
&Version=2011-01-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeInstanceRefreshes_Example_1_Response"></a>

```
<DescribeInstanceRefreshesResponse xmlns="https://autoscaling.amazonaws.com/doc/2011-01-01/">
  <DescribeInstanceRefreshesResult>
    <InstanceRefreshes>
      <member>
        <InstanceRefreshId>08b91cf7-8fa6-48af-b6a6-d227f40f1b9b</InstanceRefreshId>
        <AutoScalingGroupName>my-asg</AutoScalingGroupName>
        <Status>InProgress</Status>
        <StatusReason>Waiting for instances to warm up before continuing. For example: i-0645704820a8e83ff is warming up.</StatusReason>
        <PercentageComplete>50</PercentageComplete>
        <InstancesToUpdate>0</InstancesToUpdate>
        <StartTime>2023-06-13T16:46:52Z</StartTime>
        <Preferences>{}</Preferences>
      </member>
    </InstanceRefreshes>
  </DescribeInstanceRefreshesResult>
  <ResponseMetadata>
    <RequestId>7c6e177f-f082-11e1-ac58-3714bEXAMPLE</RequestId>
  </ResponseMetadata>
</DescribeInstanceRefreshesResponse>
```

## See Also
<a name="API_DescribeInstanceRefreshes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/DescribeInstanceRefreshes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/DescribeInstanceRefreshes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/DescribeInstanceRefreshes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/DescribeInstanceRefreshes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/DescribeInstanceRefreshes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/DescribeInstanceRefreshes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/DescribeInstanceRefreshes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/DescribeInstanceRefreshes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/DescribeInstanceRefreshes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/DescribeInstanceRefreshes)
