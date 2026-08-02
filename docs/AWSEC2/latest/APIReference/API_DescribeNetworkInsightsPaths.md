---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInsightsPaths.html
---

# DescribeNetworkInsightsPaths
<a name="API_DescribeNetworkInsightsPaths"></a>

Describes one or more of your paths.

## Request Parameters
<a name="API_DescribeNetworkInsightsPaths_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters. The following are the possible values:
+ destination - The ID of the resource.
+ filter-at-source.source-address - The source IPv4 address at the source.
+ filter-at-source.source-port-range - The source port range at the source.
+ filter-at-source.destination-address - The destination IPv4 address at the source.
+ filter-at-source.destination-port-range - The destination port range at the source.
+ filter-at-destination.source-address - The source IPv4 address at the destination.
+ filter-at-destination.source-port-range - The source port range at the destination.
+ filter-at-destination.destination-address - The destination IPv4 address at the destination.
+ filter-at-destination.destination-port-range - The destination port range at the destination.
+ protocol - The protocol.
+ source - The ID of the resource.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 **NetworkInsightsPathId.N**
The IDs of the paths.
Type: Array of strings
Required: No

 **NextToken**
The token for the next page of results.
Type: String
Required: No

## Response Elements
<a name="API_DescribeNetworkInsightsPaths_ResponseElements"></a>

The following elements are returned by the service.

 **networkInsightsPathSet**
Information about the paths.
Type: Array of [NetworkInsightsPath](API_NetworkInsightsPath.md) objects

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeNetworkInsightsPaths_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeNetworkInsightsPaths_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeNetworkInsightsPaths)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeNetworkInsightsPaths)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeNetworkInsightsPaths)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeNetworkInsightsPaths)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeNetworkInsightsPaths)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeNetworkInsightsPaths)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeNetworkInsightsPaths)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeNetworkInsightsPaths)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeNetworkInsightsPaths)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeNetworkInsightsPaths)
