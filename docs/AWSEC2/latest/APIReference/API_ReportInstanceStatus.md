---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReportInstanceStatus.html
---

# ReportInstanceStatus
<a name="API_ReportInstanceStatus"></a>

Submits feedback about the status of an instance. The instance must be in the `running` state. If your experience with the instance differs from the instance status returned by [DescribeInstanceStatus](API_DescribeInstanceStatus.md), use [ReportInstanceStatus](#API_ReportInstanceStatus) to report your experience with the instance. Amazon EC2 collects this information to improve the accuracy of status checks.

Use of this action does not change the value returned by [DescribeInstanceStatus](API_DescribeInstanceStatus.md).

## Request Parameters
<a name="API_ReportInstanceStatus_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Description**
 *This parameter has been deprecated.*
Descriptive text about the health state of your instance.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **EndTime**
The time at which the reported instance health state ended.
Type: Timestamp
Required: No

 **InstanceId.N**
The instances.
Type: Array of strings
Required: Yes

 **ReasonCode.N**
The reason codes that describe the health state of your instance.
+  `instance-stuck-in-state`: My instance is stuck in a state.
+  `unresponsive`: My instance is unresponsive.
+  `not-accepting-credentials`: My instance is not accepting my credentials.
+  `password-not-available`: A password is not available for my instance.
+  `performance-network`: My instance is experiencing performance problems that I believe are network related.
+  `performance-instance-store`: My instance is experiencing performance problems that I believe are related to the instance stores.
+  `performance-ebs-volume`: My instance is experiencing performance problems that I believe are related to an EBS volume.
+  `performance-other`: My instance is experiencing performance problems.
+  `other`: [explain using the description parameter]
Type: Array of strings
Valid Values: `instance-stuck-in-state | unresponsive | not-accepting-credentials | password-not-available | performance-network | performance-instance-store | performance-ebs-volume | performance-other | other`
Required: Yes

 **StartTime**
The time at which the reported instance health state began.
Type: Timestamp
Required: No

 **Status**
The status of all instances listed.
Type: String
Valid Values: `ok | impaired`
Required: Yes

## Response Elements
<a name="API_ReportInstanceStatus_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_ReportInstanceStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ReportInstanceStatus_Examples"></a>

### Example 1
<a name="API_ReportInstanceStatus_Example_1"></a>

This example reports instance health state for two instances.

#### Sample Request
<a name="API_ReportInstanceStatus_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ReportInstanceStatus
&Status=impaired
&InstanceId.1=i-1234567890abcdef0
&InstanceId.2=i-0598c7d356eba48d7
&AUTHPARAMS
```

### Example 2
<a name="API_ReportInstanceStatus_Example_2"></a>

This example reports instance health state for two instances with reason codes.

#### Sample Request
<a name="API_ReportInstanceStatus_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=ReportInstanceStatus
&Description=Description+of+my+issue.
&Status=impaired
&InstanceId.1=i-1234567890abcdef0
&InstanceId.2=i-0598c7d356eba48d7
&ReasonCode.1=instance-performance-network
&ReasonCode.2=instance-performance-disk
&AUTHPARAMS
```

## See Also
<a name="API_ReportInstanceStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ReportInstanceStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ReportInstanceStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ReportInstanceStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ReportInstanceStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ReportInstanceStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ReportInstanceStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ReportInstanceStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ReportInstanceStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ReportInstanceStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ReportInstanceStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
