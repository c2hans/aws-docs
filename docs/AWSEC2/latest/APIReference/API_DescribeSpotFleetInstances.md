---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSpotFleetInstances.html
---

# DescribeSpotFleetInstances
<a name="API_DescribeSpotFleetInstances"></a>

Describes the running instances for the specified Spot Fleet.

## Request Parameters
<a name="API_DescribeSpotFleetInstances_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 **NextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String
Required: No

 **SpotFleetRequestId**
The ID of the Spot Fleet request.
Type: String
Required: Yes

## Response Elements
<a name="API_DescribeSpotFleetInstances_ResponseElements"></a>

The following elements are returned by the service.

 **activeInstanceSet**
The running instances. This list is refreshed periodically and might be out of date.
Type: Array of [ActiveInstance](API_ActiveInstance.md) objects

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **spotFleetRequestId**
The ID of the Spot Fleet request.
Type: String

## Errors
<a name="API_DescribeSpotFleetInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeSpotFleetInstances_Examples"></a>

### Example
<a name="API_DescribeSpotFleetInstances_Example_1"></a>

This example describes the running instances for Spot Fleet request sfr-123f8fc2-cb31-425e-abcd-example2710.

#### Sample Request
<a name="API_DescribeSpotFleetInstances_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeSpotFleetInstances
&SpotFleetRequestId=sfr-123f8fc2-cb31-425e-abcd-example2710
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeSpotFleetInstances_Example_1_Response"></a>

```
<DescribeSpotFleetInstancesResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>cfb09950-45e2-472d-a6a9-example</requestId>
    <spotFleetRequestId>sfr-123f8fc2-cb31-425e-abcd-example2710</spotFleetRequestId>
    <activeInstanceSet>
        <item>
            <instanceId>i-1234567890abcdef0</instanceId>
            <spotInstanceRequestId>sir-1a1a1a1a</spotInstanceRequestId>
            <instanceType>m3.medium</instanceType>
        </item>
        <item>
            <instanceId>i-1234567890abcdef1</instanceId>
            <spotInstanceRequestId>sir-2b2b2b2b</spotInstanceRequestId>
            <instanceType>m3.medium</instanceType>
        </item>
        <item>
            <instanceId>i-1234567890abcdef2</instanceId>
            <spotInstanceRequestId>sir-3c3c3c3c</spotInstanceRequestId>
            <instanceType>m3.medium</instanceType>
        </item>
        <item>
            <instanceId>i-1234567890abcdef3</instanceId>
            <spotInstanceRequestId>sir-4d4d4d4d</spotInstanceRequestId>
            <instanceType>m3.medium</instanceType>
        </item>
        <item>
            <instanceId>i-1234567890abcdef4</instanceId>
            <spotInstanceRequestId>sir-5e5e5e5e</spotInstanceRequestId>
            <instanceType>m3.medium</instanceType>
        </item>
    </activeInstanceSet>
</DescribeSpotFleetInstancesResponse>
```

## See Also
<a name="API_DescribeSpotFleetInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeSpotFleetInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeSpotFleetInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeSpotFleetInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeSpotFleetInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeSpotFleetInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeSpotFleetInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeSpotFleetInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeSpotFleetInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeSpotFleetInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeSpotFleetInstances)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
