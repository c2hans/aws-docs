---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeCapacityManagerDataExports.html
---

# DescribeCapacityManagerDataExports
<a name="API_DescribeCapacityManagerDataExports"></a>

 Describes one or more Capacity Manager data export configurations. Returns information about export settings, delivery status, and recent export activity.

## Request Parameters
<a name="API_DescribeCapacityManagerDataExports_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **CapacityManagerDataExportId.N**
 The IDs of the data export configurations to describe. If not specified, all export configurations are returned.
Type: Array of strings
Required: No

 **DryRun**
 Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
 One or more filters to narrow the results. Supported filters include export status, creation date, and S3 bucket name.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
 The maximum number of results to return in a single call. If not specified, up to 1000 results are returned.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 **NextToken**
 The token for the next page of results. Use this value in a subsequent call to retrieve additional results.
Type: String
Required: No

## Response Elements
<a name="API_DescribeCapacityManagerDataExports_ResponseElements"></a>

The following elements are returned by the service.

 **capacityManagerDataExportSet**
 Information about the data export configurations, including export settings, delivery status, and recent activity.
Type: Array of [CapacityManagerDataExportResponse](API_CapacityManagerDataExportResponse.md) objects

 **nextToken**
 The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeCapacityManagerDataExports_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeCapacityManagerDataExports_Examples"></a>

### Example
<a name="API_DescribeCapacityManagerDataExports_Example_1"></a>

This example describes a specific data export configuration.

#### Sample Request
<a name="API_DescribeCapacityManagerDataExports_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeCapacityManagerDataExports
&CapacityManagerDataExportId.1=cmde-0abcd1234EXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeCapacityManagerDataExports_Example_1_Response"></a>

```
<DescribeCapacityManagerDataExportsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>d4904fd9-82c2-4ea5-adfe-a9cc3EXAMPLE</requestId>
    <capacityManagerDataExportSet>
        <item>
            <capacityManagerDataExportId>cmde-0abcd1234EXAMPLE</capacityManagerDataExportId>
            <s3BucketName>my-capacity-exports-bucket</s3BucketName>
            <s3BucketPrefix>capacity-data/</s3BucketPrefix>
            <schedule>hourly</schedule>
            <outputFormat>parquet</outputFormat>
            <createTime>2024-01-15T10:30:00.000Z</createTime>
            <latestDeliveryStatus>delivered</latestDeliveryStatus>
            <latestDeliveryTime>2024-01-16T02:00:00.000Z</latestDeliveryTime>
            <latestDeliveryS3LocationUri>s3://my-capacity-exports-bucket/capacity-data/20240116.parquet</latestDeliveryS3LocationUri>
        </item>
    </capacityManagerDataExportSet>
</DescribeCapacityManagerDataExportsResponse>
```

## See Also
<a name="API_DescribeCapacityManagerDataExports_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeCapacityManagerDataExports)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeCapacityManagerDataExports)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeCapacityManagerDataExports)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeCapacityManagerDataExports)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeCapacityManagerDataExports)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeCapacityManagerDataExports)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeCapacityManagerDataExports)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeCapacityManagerDataExports)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeCapacityManagerDataExports)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeCapacityManagerDataExports)
