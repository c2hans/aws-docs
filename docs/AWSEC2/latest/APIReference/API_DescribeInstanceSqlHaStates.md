---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceSqlHaStates.html
---

# DescribeInstanceSqlHaStates
<a name="API_DescribeInstanceSqlHaStates"></a>

Describes the SQL Server High Availability states for Amazon EC2 instances that are enabled for Amazon EC2 High Availability for SQL Server monitoring.

## Request Parameters
<a name="API_DescribeInstanceSqlHaStates_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters to apply to the results. Supported filters include:
+  `tag:<key>` - The tag key and value pair assigned to the instance. For example, to find all instances tagged with `Owner:TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
+  `tag-key` - The tag key assigned to the instance.
+  `haStatus` - The SQL Server High Availability status of the SQL Server High Availability instance (`processing` \| `active` \| `standby` \| `invalid`).
+  `sqlServerLicenseUsage` - The license type for the SQL Server license (`full` \| `waived`).
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **InstanceId.N**
The IDs of the SQL Server High Availability instances to describe. If omitted, the API returns SQL Server High Availability states for all SQL Server High Availability instances.
Type: Array of strings
Required: No

 **MaxResults**
The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 **NextToken**
The token to use to retrieve the next page of results.
Type: String
Required: No

## Response Elements
<a name="API_DescribeInstanceSqlHaStates_ResponseElements"></a>

The following elements are returned by the service.

 **instanceSet**
Information about the SQL Server High Availability instances.
Type: Array of [RegisteredInstance](API_RegisteredInstance.md) objects

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeInstanceSqlHaStates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeInstanceSqlHaStates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeInstanceSqlHaStates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeInstanceSqlHaStates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeInstanceSqlHaStates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeInstanceSqlHaStates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeInstanceSqlHaStates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeInstanceSqlHaStates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeInstanceSqlHaStates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeInstanceSqlHaStates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeInstanceSqlHaStates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeInstanceSqlHaStates)
