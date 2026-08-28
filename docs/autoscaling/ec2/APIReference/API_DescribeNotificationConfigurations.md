---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeNotificationConfigurations.html
---

# DescribeNotificationConfigurations
<a name="API_DescribeNotificationConfigurations"></a>

Gets information about the Amazon SNS notifications that are configured for one or more Auto Scaling groups.

## Request Parameters
<a name="API_DescribeNotificationConfigurations_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **AutoScalingGroupNames.member.N**
The name of the Auto Scaling group.
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
<a name="API_DescribeNotificationConfigurations_ResponseElements"></a>

The following elements are returned by the service.

 ** NextToken **
A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the `NextToken` value when requesting the next set of items. This value is null when there are no more items to return.
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

 **NotificationConfigurations.member.N**
The notification configurations.
Type: Array of [NotificationConfiguration](API_NotificationConfiguration.md) objects

## Errors
<a name="API_DescribeNotificationConfigurations_Errors"></a>

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
<a name="API_DescribeNotificationConfigurations_Examples"></a>

### Example
<a name="API_DescribeNotificationConfigurations_Example_1"></a>

This example illustrates one usage of DescribeNotificationConfigurations.

#### Sample Request
<a name="API_DescribeNotificationConfigurations_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Version=2011-01-01&Action=DescribeNotificationConfigurations
&AutoScalingGroupNames.member.1=my-asg
&Version=2011-01-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeNotificationConfigurations_Example_1_Response"></a>

```
<DescribeNotificationConfigurationsResponse xmlns="https://autoscaling.amazonaws.com/doc/2011-01-01/">
  <DescribeNotificationConfigurationsResult>
    <NotificationConfigurations>
      <member>
        <AutoScalingGroupName>my-asg</AutoScalingGroupName>
        <NotificationType>autoscaling:EC2_INSTANCE_LAUNCH</NotificationType>
        <TopicARN>arn:aws:sns:us-east-1:123456789012:my-sns-topic</TopicARN>
      </member>
    </NotificationConfigurations>
  </DescribeNotificationConfigurationsResult>
  <ResponseMetadata>
    <RequestId>7c6e177f-f082-11e1-ac58-3714bEXAMPLE</RequestId>
  </ResponseMetadata>
</DescribeNotificationConfigurationsResponse>
```

## See Also
<a name="API_DescribeNotificationConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/DescribeNotificationConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/DescribeNotificationConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/DescribeNotificationConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/DescribeNotificationConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/DescribeNotificationConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/DescribeNotificationConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/DescribeNotificationConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/DescribeNotificationConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/DescribeNotificationConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/DescribeNotificationConfigurations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
