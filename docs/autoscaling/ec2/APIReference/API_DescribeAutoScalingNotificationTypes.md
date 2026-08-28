---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAutoScalingNotificationTypes.html
---

# DescribeAutoScalingNotificationTypes
<a name="API_DescribeAutoScalingNotificationTypes"></a>

Describes the notification types that are supported by Amazon EC2 Auto Scaling.

## Response Elements
<a name="API_DescribeAutoScalingNotificationTypes_ResponseElements"></a>

The following element is returned by the service.

 **AutoScalingNotificationTypes.member.N**
The notification types.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

## Errors
<a name="API_DescribeAutoScalingNotificationTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

## Examples
<a name="API_DescribeAutoScalingNotificationTypes_Examples"></a>

### Example
<a name="API_DescribeAutoScalingNotificationTypes_Example_1"></a>

This example illustrates one usage of DescribeAutoScalingNotificationTypes.

#### Sample Request
<a name="API_DescribeAutoScalingNotificationTypes_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Version=2011-01-01&Action=DescribeAutoScalingNotificationTypes
&Version=2011-01-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeAutoScalingNotificationTypes_Example_1_Response"></a>

```
<DescribeAutoScalingNotificationTypesResponse xmlns="https://autoscaling.amazonaws.com/doc/2011-01-01/">
  <DescribeAutoScalingNotificationTypesResult>
    <AutoScalingNotificationTypes>
      <member>autoscaling:EC2_INSTANCE_LAUNCH</member>
      <member>autoscaling:EC2_INSTANCE_LAUNCH_ERROR</member>
      <member>autoscaling:EC2_INSTANCE_TERMINATE</member>
      <member>autoscaling:EC2_INSTANCE_TERMINATE_ERROR</member>
      <member>autoscaling:TEST_NOTIFICATION</member>
    </AutoScalingNotificationTypes>
  </DescribeAutoScalingNotificationTypesResult>
  <ResponseMetadata>
    <RequestId>7c6e177f-f082-11e1-ac58-3714bEXAMPLE</RequestId>
  </ResponseMetadata>
</DescribeAutoScalingNotificationTypesResponse>
```

## See Also
<a name="API_DescribeAutoScalingNotificationTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/DescribeAutoScalingNotificationTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/DescribeAutoScalingNotificationTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/DescribeAutoScalingNotificationTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/DescribeAutoScalingNotificationTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/DescribeAutoScalingNotificationTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/DescribeAutoScalingNotificationTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/DescribeAutoScalingNotificationTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/DescribeAutoScalingNotificationTypes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/DescribeAutoScalingNotificationTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/DescribeAutoScalingNotificationTypes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
