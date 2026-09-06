---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceEventWindows.html
---

# DescribeInstanceEventWindows
<a name="API_DescribeInstanceEventWindows"></a>

Describes the specified event windows or all event windows.

If you specify event window IDs, the output includes information for only the specified event windows. If you specify filters, the output includes information for only those event windows that meet the filter criteria. If you do not specify event windows IDs or filters, the output includes information for all event windows, which can affect performance. We recommend that you use pagination to ensure that the operation returns quickly and successfully.

For more information, see [Define event windows for scheduled events](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_DescribeInstanceEventWindows_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters.
+  `dedicated-host-id` - The event windows associated with the specified Dedicated Host ID.
+  `event-window-name` - The event windows associated with the specified names.
+  `instance-id` - The event windows associated with the specified instance ID.
+  `instance-tag` - The event windows associated with the specified tag and value.
+  `instance-tag-key` - The event windows associated with the specified tag key, regardless of the value.
+  `instance-tag-value` - The event windows associated with the specified tag value, regardless of the key.
+  `tag:<key>` - The key/value combination of a tag assigned to the event window. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `CMX`, specify `tag:Owner` for the filter name and `CMX` for the filter value.
+  `tag-key` - The key of a tag assigned to the event window. Use this filter to find all event windows that have a tag with a specific key, regardless of the tag value.
+  `tag-value` - The value of a tag assigned to the event window. Use this filter to find all event windows that have a tag with a specific value, regardless of the tag key.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **InstanceEventWindowId.N**
The IDs of the event windows.
Type: Array of strings
Required: No

 **MaxResults**
The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned `NextToken` value. This value can be between 20 and 500. You cannot specify this parameter and the event window IDs parameter in the same call.
Type: Integer
Valid Range: Minimum value of 20. Maximum value of 500.
Required: No

 **NextToken**
The token to request the next page of results.
Type: String
Required: No

## Response Elements
<a name="API_DescribeInstanceEventWindows_ResponseElements"></a>

The following elements are returned by the service.

 **instanceEventWindowSet**
Information about the event windows.
Type: Array of [InstanceEventWindow](API_InstanceEventWindow.md) objects

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeInstanceEventWindows_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeInstanceEventWindows_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeInstanceEventWindows)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeInstanceEventWindows)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeInstanceEventWindows)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeInstanceEventWindows)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeInstanceEventWindows)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeInstanceEventWindows)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeInstanceEventWindows)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeInstanceEventWindows)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeInstanceEventWindows)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeInstanceEventWindows)
