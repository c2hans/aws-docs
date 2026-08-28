---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeScheduledInstances.html
---

# DescribeScheduledInstances
<a name="API_DescribeScheduledInstances"></a>

Describes the specified Scheduled Instances or all your Scheduled Instances.

## Request Parameters
<a name="API_DescribeScheduledInstances_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `availability-zone` - The Availability Zone (for example, `us-west-2a`).
+  `instance-type` - The instance type (for example, `c4.large`).
+  `platform` - The platform (`Linux/UNIX` or `Windows`).
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of results to return in a single call. This value can be between 5 and 300. The default value is 100. To retrieve the remaining results, make another call with the returned `NextToken` value.
Type: Integer
Required: No

 **NextToken**
The token for the next set of results.
Type: String
Required: No

 **ScheduledInstanceId.N**
The Scheduled Instance IDs.
Type: Array of strings
Required: No

 **SlotStartTimeRange**
The time period for the first schedule to start.
Type: [SlotStartTimeRangeRequest](API_SlotStartTimeRangeRequest.md) object
Required: No

## Response Elements
<a name="API_DescribeScheduledInstances_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token required to retrieve the next set of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **scheduledInstanceSet**
Information about the Scheduled Instances.
Type: Array of [ScheduledInstance](API_ScheduledInstance.md) objects

## Errors
<a name="API_DescribeScheduledInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeScheduledInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeScheduledInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeScheduledInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeScheduledInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeScheduledInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeScheduledInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeScheduledInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeScheduledInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeScheduledInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeScheduledInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeScheduledInstances)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
