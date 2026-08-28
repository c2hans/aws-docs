---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeStoreImageTasks.html
---

# DescribeStoreImageTasks
<a name="API_DescribeStoreImageTasks"></a>

Describes the progress of the AMI store tasks. You can describe the store tasks for specified AMIs. If you don't specify the AMIs, you get a paginated list of store tasks from the last 31 days.

For each AMI task, the response indicates if the task is `InProgress`, `Completed`, or `Failed`. For tasks `InProgress`, the response shows the estimated progress as a percentage.

Tasks are listed in reverse chronological order. Currently, only tasks from the past 31 days can be viewed.

To use this API, you must have the required permissions. For more information, see [Permissions for storing and restoring AMIs using S3](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-ami-store-restore.html#ami-s3-permissions) in the *Amazon EC2 User Guide*.

For more information, see [Store and restore an AMI using S3](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-store-restore.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_DescribeStoreImageTasks_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `task-state` - Returns tasks in a certain state (`InProgress` \| `Completed` \| `Failed`)
+  `bucket` - Returns task information for tasks that targeted a specific bucket. For the filter value, specify the bucket name.
When you specify the `ImageIds` parameter, any filters that you specify are ignored. To use the filters, you must remove the `ImageIds` parameter.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **ImageId.N**
The AMI IDs for which to show progress. Up to 20 AMI IDs can be included in a request.
Type: Array of strings
Required: No

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
You cannot specify this parameter and the `ImageIds` parameter in the same call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 200.
Required: No

 **NextToken**
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

## Response Elements
<a name="API_DescribeStoreImageTasks_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **storeImageTaskResultSet**
The information about the AMI store tasks.
Type: Array of [StoreImageTaskResult](API_StoreImageTaskResult.md) objects

## Errors
<a name="API_DescribeStoreImageTasks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeStoreImageTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeStoreImageTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeStoreImageTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeStoreImageTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeStoreImageTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeStoreImageTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeStoreImageTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeStoreImageTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeStoreImageTasks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeStoreImageTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeStoreImageTasks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
