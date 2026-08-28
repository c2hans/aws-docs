---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpointConnections.html
---

# DescribeVpcEndpointConnections
<a name="API_DescribeVpcEndpointConnections"></a>

Describes the VPC endpoint connections to your VPC endpoint services, including any endpoints that are pending your acceptance.

## Request Parameters
<a name="API_DescribeVpcEndpointConnections_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `ip-address-type` - The IP address type (`ipv4` \| `ipv6`).
+  `service-id` - The ID of the service.
+  `vpc-endpoint-owner` - The ID of the AWS account ID that owns the endpoint.
+  `vpc-endpoint-region` - The Region of the endpoint or `cross-region` to find endpoints for other Regions.
+  `vpc-endpoint-state` - The state of the endpoint (`pendingAcceptance` \| `pending` \| `available` \| `deleting` \| `deleted` \| `rejected` \| `failed`).
+  `vpc-endpoint-id` - The ID of the endpoint.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of results to return for the request in a single page. The remaining results of the initial request can be seen by sending another request with the returned `NextToken` value. This value can be between 5 and 1,000; if `MaxResults` is given a value larger than 1,000, only 1,000 results are returned.
Type: Integer
Required: No

 **NextToken**
The token to retrieve the next page of results.
Type: String
Required: No

## Response Elements
<a name="API_DescribeVpcEndpointConnections_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **vpcEndpointConnectionSet**
Information about the VPC endpoint connections.
Type: Array of [VpcEndpointConnection](API_VpcEndpointConnection.md) objects

## Errors
<a name="API_DescribeVpcEndpointConnections_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeVpcEndpointConnections_Examples"></a>

### Example
<a name="API_DescribeVpcEndpointConnections_Example_1"></a>

This example describes all of the VPC endpoint connections for all of your services.

#### Sample Request
<a name="API_DescribeVpcEndpointConnections_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeVpcEndpointConnections
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeVpcEndpointConnections_Example_1_Response"></a>

```
<DescribeVpcEndpointConnectionsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>ed2d237f-426b-4927-981b-980example</requestId>
    <vpcEndpointConnectionSet>
        <item>
            <vpcEndpointOwner>123456789012</vpcEndpointOwner>
            <creationTimestamp>2017-10-19T12:36:10.939Z</creationTimestamp>
            <vpcEndpointState>available</vpcEndpointState>
            <serviceId>vpce-svc-0127881c0d25a3123</serviceId>
            <vpcEndpointId>vpce-09bce00dc3edcc329</vpcEndpointId>
        </item>
        <item>
            <vpcEndpointOwner>112233445566</vpcEndpointOwner>
            <creationTimestamp>2017-10-18T12:14:41.892Z</creationTimestamp>
            <vpcEndpointState>rejected</vpcEndpointState>
            <serviceId>vpce-svc-0435c4480f65e3abc</serviceId>
            <vpcEndpointId>vpce-051a4ba136c8a12d8</vpcEndpointId>
        </item>
        <item>
            <vpcEndpointOwner>123123123123</vpcEndpointOwner>
            <creationTimestamp>2017-10-18T13:25:07.739Z</creationTimestamp>
            <vpcEndpointState>pendingAcceptance</vpcEndpointState>
            <serviceId>vpce-svc-01f406f3e99f8a123</serviceId>
            <vpcEndpointId>vpce-09593ee8e85835659</vpcEndpointId>
        </item>
    </vpcEndpointConnectionSet>
</DescribeVpcEndpointConnectionsResponse>
```

## See Also
<a name="API_DescribeVpcEndpointConnections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeVpcEndpointConnections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeVpcEndpointConnections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeVpcEndpointConnections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeVpcEndpointConnections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeVpcEndpointConnections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeVpcEndpointConnections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeVpcEndpointConnections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeVpcEndpointConnections)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeVpcEndpointConnections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeVpcEndpointConnections)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
