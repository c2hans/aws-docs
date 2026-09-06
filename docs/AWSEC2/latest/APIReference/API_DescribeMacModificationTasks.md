---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeMacModificationTasks.html
---

# DescribeMacModificationTasks
<a name="API_DescribeMacModificationTasks"></a>

Describes a System Integrity Protection (SIP) modification task or volume ownership delegation task for an Amazon EC2 Mac instance. For more information, see [Configure SIP for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/mac-sip-settings.html#mac-sip-configure) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_DescribeMacModificationTasks_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
Specifies one or more filters for the request:
+  `instance-id` - The ID of the instance for which the task was created.
+  `task-state` - The state of the task (`successful` \| `failed` \| `in-progress` \| `pending`).
+  `mac-system-integrity-protection-configuration.sip-status` - The overall SIP state requested in the task (`enabled` \| `disabled`).
+  `start-time` - The date and time the task was created.
+  `task-type` - The type of task (`sip-modification` \| `volume-ownership-delegation`).
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MacModificationTaskId.N**
The ID of task.
Type: Array of strings
Required: No

 **MaxResults**
The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned `nextToken` value. This value can be between 5 and 500. If `maxResults` is given a larger value than 500, you receive an error.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 **NextToken**
The token to use to retrieve the next page of results.
Type: String
Required: No

## Response Elements
<a name="API_DescribeMacModificationTasks_ResponseElements"></a>

The following elements are returned by the service.

 **macModificationTaskSet**
Information about the tasks.
Type: Array of [MacModificationTask](API_MacModificationTask.md) objects

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeMacModificationTasks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeMacModificationTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeMacModificationTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeMacModificationTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeMacModificationTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeMacModificationTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeMacModificationTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeMacModificationTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeMacModificationTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeMacModificationTasks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeMacModificationTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeMacModificationTasks)
