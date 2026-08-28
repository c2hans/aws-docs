---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CancelInstanceRefresh.html
---

# CancelInstanceRefresh
<a name="API_CancelInstanceRefresh"></a>

Cancels an instance refresh or rollback that is in progress. If an instance refresh or rollback is not in progress, an `ActiveInstanceRefreshNotFound` error occurs.

This operation is part of the [instance refresh feature](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html) in Amazon EC2 Auto Scaling, which helps you update instances in your Auto Scaling group after you make configuration changes.

When you cancel an instance refresh, this does not roll back any changes that it made. Use the [RollbackInstanceRefresh](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_RollbackInstanceRefresh.html) API to roll back instead.

## Request Parameters
<a name="API_CancelInstanceRefresh_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** WaitForTransitioningInstances **
When cancelling an instance refresh, this indicates whether to wait for in-flight launches and terminations to complete. The default is true.
When set to false, Amazon EC2 Auto Scaling cancels the instance refresh without waiting for any pending launches or terminations to complete.
Type: Boolean
Required: No

## Response Elements
<a name="API_CancelInstanceRefresh_ResponseElements"></a>

The following element is returned by the service.

 ** InstanceRefreshId **
The instance refresh ID associated with the request. This is the unique ID assigned to the instance refresh when it was started.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

## Errors
<a name="API_CancelInstanceRefresh_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ActiveInstanceRefreshNotFound **
The request failed because an active instance refresh or rollback for the specified Auto Scaling group was not found.
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
<a name="API_CancelInstanceRefresh_Examples"></a>

### Example
<a name="API_CancelInstanceRefresh_Example_1"></a>

This example illustrates one usage of CancelInstanceRefresh.

#### Sample Request
<a name="API_CancelInstanceRefresh_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=CancelInstanceRefresh
&AutoScalingGroupName=my-asg
&Version=2011-01-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_CancelInstanceRefresh_Example_1_Response"></a>

```
<CancelInstanceRefreshResponse xmlns="https://autoscaling.amazonaws.com/doc/2011-01-01/">
  <CancelInstanceRefreshResult>
    <InstanceRefreshId>08b91cf7-8fa6-48af-b6a6-d227f40f1b9b</InstanceRefreshId>
  </CancelInstanceRefreshResult>
  <ResponseMetadata>
    <RequestId>7c6e177f-f082-11e1-ac58-3714bEXAMPLE</RequestId>
  </ResponseMetadata>
</CancelInstanceRefreshResponse>
```

## See Also
<a name="API_CancelInstanceRefresh_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/CancelInstanceRefresh)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/CancelInstanceRefresh)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/CancelInstanceRefresh)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/CancelInstanceRefresh)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/CancelInstanceRefresh)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/CancelInstanceRefresh)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/CancelInstanceRefresh)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/CancelInstanceRefresh)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/CancelInstanceRefresh)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/CancelInstanceRefresh)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
