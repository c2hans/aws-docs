---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFleetInstances.html
---

# DescribeFleetInstances
<a name="API_DescribeFleetInstances"></a>

Describes the running instances for the specified EC2 Fleet.

**Note**
Currently, `DescribeFleetInstances` does not support fleets of type `instant`. Instead, use `DescribeFleets`, specifying the `instant` fleet ID in the request.

For more information, see [Describe your EC2 Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-ec2-fleet.html#monitor-ec2-fleet) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_DescribeFleetInstances_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `instance-type` - The instance type.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **FleetId**
The ID of the EC2 Fleet.
Type: String
Required: Yes

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
Type: Integer
Required: No

 **NextToken**
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

## Response Elements
<a name="API_DescribeFleetInstances_ResponseElements"></a>

The following elements are returned by the service.

 **activeInstanceSet**
The running instances. This list is refreshed periodically and might be out of date.
Type: Array of [ActiveInstance](API_ActiveInstance.md) objects

 **fleetId**
The ID of the EC2 Fleet.
Type: String

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeFleetInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeFleetInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeFleetInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeFleetInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeFleetInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeFleetInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeFleetInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeFleetInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeFleetInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeFleetInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeFleetInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeFleetInstances)
