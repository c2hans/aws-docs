---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImportSnapshotTasks.html
---

# DescribeImportSnapshotTasks
<a name="API_DescribeImportSnapshotTasks"></a>

Describes your import snapshot tasks.

## Request Parameters
<a name="API_DescribeImportSnapshotTasks_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filters.N**
The filters.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **ImportTaskId.N**
A list of import snapshot task IDs.
Type: Array of strings
Required: No

 **MaxResults**
The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned `NextToken` value.
Type: Integer
Required: No

 **NextToken**
A token that indicates the next page of results.
Type: String
Required: No

## Response Elements
<a name="API_DescribeImportSnapshotTasks_ResponseElements"></a>

The following elements are returned by the service.

 **importSnapshotTaskSet**
A list of zero or more import snapshot tasks that are currently active or were completed or canceled in the previous 7 days.
Type: Array of [ImportSnapshotTask](API_ImportSnapshotTask.md) objects

 **nextToken**
The token to use to get the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeImportSnapshotTasks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeImportSnapshotTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeImportSnapshotTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeImportSnapshotTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeImportSnapshotTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeImportSnapshotTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeImportSnapshotTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeImportSnapshotTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeImportSnapshotTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeImportSnapshotTasks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeImportSnapshotTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeImportSnapshotTasks)
