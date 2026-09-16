---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotFleetRequests.html
---

# DescribeSpotFleetRequests
<a name="API_DescribeSpotFleetRequests"></a>

Describes your Spot Fleet requests.

Spot Fleet requests are deleted 48 hours after they are canceled and their instances are terminated.

## Request Parameters
<a name="API_DescribeSpotFleetRequests_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
Type: Integer
Required: No

 **NextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String
Required: No

 **SpotFleetRequestId.N**
The IDs of the Spot Fleet requests.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeSpotFleetRequests_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **spotFleetRequestConfigSet**
Information about the configuration of your Spot Fleet.
Type: Array of [SpotFleetRequestConfig](API_SpotFleetRequestConfig.md) objects

## Errors
<a name="API_DescribeSpotFleetRequests_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeSpotFleetRequests_Examples"></a>

### Example
<a name="API_DescribeSpotFleetRequests_Example_1"></a>

This example describes all of your Spot Fleet requests.

#### Sample Request
<a name="API_DescribeSpotFleetRequests_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeSpotFleetRequests
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeSpotFleetRequests_Example_1_Response"></a>

```
<DescribeSpotFleetRequestsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>4d68a6cc-8f2e-4be1-b425-example</requestId>
    <spotFleetRequestConfigSet>
        <item>
            <spotFleetRequestId>sfr-12345678-cb31-425e-8c23-example2710</spotFleetRequestId>
            <spotFleetRequestState>cancelled</spotFleetRequestState>
            <spotFleetRequestConfig>
                <spotPrice>0.0153</spotPrice>
                <targetCapacity>20</targetCapacity>
                <iamFleetRole>arn:aws:iam::123456789011:role/spot-fleet-role</iamFleetRole>
                <launchSpecifications>
                    <item>
                        <subnetId>subnet-1a2b3c4d</subnetId>
                        <ebsOptimized>false</ebsOptimized>
                        <imageId>ami-1ecae776</imageId>
                        <instanceType>m4.xlarge</instanceType>
                    </item>
                    <item>
                        <subnetId>subnet-1a2b3c4d</subnetId>
                        <ebsOptimized>false</ebsOptimized>
                        <imageId>ami-1ecae776</imageId>
                        <instanceType>m3.medium</instanceType>
                    </item>
                </launchSpecifications>
            </spotFleetRequestConfig>
        </item>
        <item>
            <spotFleetRequestId>sfr-abcdefgh-e71f-450d-880d-examplec127</spotFleetRequestId>
            <spotFleetRequestState>active</spotFleetRequestState>
            <spotFleetRequestConfig>
                <spotPrice>0.0153</spotPrice>
                <targetCapacity>5</targetCapacity>
                <iamFleetRole>arn:aws:iam::123456789011:role/spot-fleet-role</iamFleetRole>
                <launchSpecifications>
                    <item>
                        <subnetId>subnet-abc123ab</subnetId>
                        <ebsOptimized>false</ebsOptimized>
                        <imageId>ami-1ecae776</imageId>
                        <instanceType>m4.large</instanceType>
                    </item>
                    <item>
                        <subnetId>subnet-abc123ab</subnetId>
                        <ebsOptimized>false</ebsOptimized>
                        <imageId>ami-1ecae776</imageId>
                        <instanceType>m3.medium</instanceType>
                    </item>
                </launchSpecifications>
            </spotFleetRequestConfig>
        </item>
    </spotFleetRequestConfigSet>
</DescribeSpotFleetRequestsResponse>
```

## See Also
<a name="API_DescribeSpotFleetRequests_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeSpotFleetRequests)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeSpotFleetRequests)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeSpotFleetRequests)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeSpotFleetRequests)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeSpotFleetRequests)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeSpotFleetRequests)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeSpotFleetRequests)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeSpotFleetRequests)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeSpotFleetRequests)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeSpotFleetRequests)
