---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImageUsageReports.html
---

# DescribeImageUsageReports
<a name="API_DescribeImageUsageReports"></a>

Describes the configuration and status of image usage reports, filtered by report IDs or image IDs.

For more information, see [View your AMI usage](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/your-ec2-ami-usage.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_DescribeImageUsageReports_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `creation-time` - The time when the report was created, in the ISO 8601 format in the UTC time zone (YYYY-MM-DDThh:mm:ss.sssZ), for example, `2025-11-29T11:04:43.305Z`. You can use a wildcard (`*`), for example, `2025-11-29T*`, which matches an entire day.
+  `state` - The state of the report (`available` \| `pending` \| `error`).
+  `tag:<key>` - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
+  `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **ImageId.N**
The IDs of the images for filtering the reports. If specified, only reports containing these images are returned.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 **NextToken**
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

 **ReportId.N**
The IDs of the image usage reports.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Elements
<a name="API_DescribeImageUsageReports_ResponseElements"></a>

The following elements are returned by the service.

 **imageUsageReportSet**
The image usage reports.
Type: Array of [ImageUsageReport](API_ImageUsageReport.md) objects

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeImageUsageReports_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeImageUsageReports_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeImageUsageReports)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeImageUsageReports)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeImageUsageReports)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeImageUsageReports)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeImageUsageReports)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeImageUsageReports)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeImageUsageReports)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeImageUsageReports)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeImageUsageReports)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeImageUsageReports)
