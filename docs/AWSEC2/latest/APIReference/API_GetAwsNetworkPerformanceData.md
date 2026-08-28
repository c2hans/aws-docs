---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetAwsNetworkPerformanceData.html
---

# GetAwsNetworkPerformanceData
<a name="API_GetAwsNetworkPerformanceData"></a>

Gets network performance data.

## Request Parameters
<a name="API_GetAwsNetworkPerformanceData_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DataQuery.N**
A list of network performance data queries.
Type: Array of [DataQuery](API_DataQuery.md) objects
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **EndTime**
The ending time for the performance data request. The end time must be formatted as `yyyy-mm-ddThh:mm:ss`. For example, `2022-06-12T12:00:00.000Z`.
Type: Timestamp
Required: No

 **MaxResults**
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
Type: Integer
Required: No

 **NextToken**
The token for the next page of results.
Type: String
Required: No

 **StartTime**
The starting time for the performance data request. The starting time must be formatted as `yyyy-mm-ddThh:mm:ss`. For example, `2022-06-10T12:00:00.000Z`.
Type: Timestamp
Required: No

## Response Elements
<a name="API_GetAwsNetworkPerformanceData_ResponseElements"></a>

The following elements are returned by the service.

 **dataResponseSet**
The list of data responses.
Type: Array of [DataResponse](API_DataResponse.md) objects

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_GetAwsNetworkPerformanceData_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetAwsNetworkPerformanceData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetAwsNetworkPerformanceData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetAwsNetworkPerformanceData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetAwsNetworkPerformanceData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetAwsNetworkPerformanceData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetAwsNetworkPerformanceData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetAwsNetworkPerformanceData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetAwsNetworkPerformanceData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetAwsNetworkPerformanceData)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetAwsNetworkPerformanceData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetAwsNetworkPerformanceData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
