---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpoints.html
---

# DescribeVpcEndpoints
<a name="API_DescribeVpcEndpoints"></a>

Describes your VPC endpoints. The default is to describe all your VPC endpoints. Alternatively, you can specify specific VPC endpoint IDs or filter the results to include only the VPC endpoints that match specific criteria.

## Request Parameters
<a name="API_DescribeVpcEndpoints_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `ip-address-type` - The IP address type (`ipv4` \| `ipv6`).
+  `service-name` - The name of the service.
+  `service-region` - The Region of the service.
+  `tag`:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
+  `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
+  `vpc-id` - The ID of the VPC in which the endpoint resides.
+  `vpc-endpoint-id` - The ID of the endpoint.
+  `vpc-endpoint-state` - The state of the endpoint (`pendingAcceptance` \| `pending` \| `available` \| `deleting` \| `deleted` \| `rejected` \| `failed`).
+  `vpc-endpoint-type` - The type of VPC endpoint (`Interface` \| `Gateway` \| `GatewayLoadBalancer` \| `Resource` \| `ServiceNetwork`).
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results.
Constraint: If the value is greater than 1,000, we return only 1,000 items.
Type: Integer
Required: No

 **NextToken**
The token for the next set of items to return. (You received this token from a prior call.)
Type: String
Required: No

 **VpcEndpointId.N**
The IDs of the VPC endpoints.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeVpcEndpoints_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

 **requestId**
The ID of the request.
Type: String

 **vpcEndpointSet**
Information about the VPC endpoints.
Type: Array of [VpcEndpoint](API_VpcEndpoint.md) objects

## Errors
<a name="API_DescribeVpcEndpoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeVpcEndpoints_Examples"></a>

### Example
<a name="API_DescribeVpcEndpoints_Example_1"></a>

This example describes all of your endpoints.

#### Sample Request
<a name="API_DescribeVpcEndpoints_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeVpcEndpoints
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeVpcEndpoints_Example_1_Response"></a>

```
<DescribeVpcEndpointsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>8d3e7656-3328-451d-8c86-7156example</requestId>
    <vpcEndpointSet>
        <item>
            <policyDocument>{"Version":"2008-10-17",		 	 	 "Statement":[{"Effect":"Allow","Principal":"*","Action":"*","Resource":"*"}]}</policyDocument>
            <routeTableIdSet>
                <item>rtb-3d560345</item>
            </routeTableIdSet>
            <dnsEntrySet/>
            <serviceName>com.amazonaws.us-east-1.dynamodb</serviceName>
            <privateDnsEnabled>true</privateDnsEnabled>
            <groupSet/>
            <vpcEndpointId>vpce-032a826a</vpcEndpointId>
            <subnetIdSet/>
            <networkInterfaceIdSet/>
            <vpcEndpointType>Gateway</vpcEndpointType>
            <vpcId>vpc-aabb1122</vpcId>
            <creationTimestamp>2017-09-05T20:41:28Z</creationTimestamp>
            <state>available</state>
            <tagSet>
                <item>
                    <key>Name</key>
                    <value>TeamA</value>
                </item>
            </tagSet>
        </item>
        <item>
            <policyDocument>{"Statement": [{"Action": "*", "Effect": "Allow", "Principal": "*", "Resource": "*"}]}</policyDocument>
            <routeTableIdSet/>
            <dnsEntrySet>
                <item>
                    <hostedZoneId>Z7HUB22UULQXV</hostedZoneId>
                    <dnsName>vpce-0f89a33420c1931d7-bluzidnv.elasticloadbalancing.us-east-1.vpce.amazonaws.com</dnsName>
                </item>
                <item>
                    <hostedZoneId>Z7HUB22UULQXV</hostedZoneId>
                    <dnsName>vpce-0f89a33420c1931d7-bluzidnv-us-east-1b.elasticloadbalancing.us-east-1.vpce.amazonaws.com</dnsName>
                </item>
                <item>
                    <hostedZoneId>Z7HUB22UULQXV</hostedZoneId>
                    <dnsName>vpce-0f89a33420c1931d7-bluzidnv-us-east-1a.elasticloadbalancing.us-east-1.vpce.amazonaws.com</dnsName>
                </item>
            </dnsEntrySet>
            <serviceName>com.amazonaws.us-east-1.elasticloadbalancing</serviceName>
            <privateDnsEnabled>false</privateDnsEnabled>
            <groupSet>
                <item>
                    <groupName>default</groupName>
                    <groupId>sg-54e8bf31</groupId>
                </item>
            </groupSet>
            <vpcEndpointId>vpce-0f89a33420c1931d7</vpcEndpointId>
            <subnetIdSet>
                <item>subnet-d6fcaa8d</item>
                <item>subnet-7b16de0c</item>
            </subnetIdSet>
            <networkInterfaceIdSet>
                <item>eni-2ec2b084</item>
                <item>eni-1b4a65cf</item>
            </networkInterfaceIdSet>
            <vpcEndpointType>Interface</vpcEndpointType>
            <vpcId>vpc-1a2b3c4d</vpcId>
            <creationTimestamp>2017-09-05T17:55:27.583Z</creationTimestamp>
            <state>available</state>
            <tagSet>
                <item>
                    <key>Name</key>
                    <value>TeamA</value>
                </item>
            </tagSet>
        </item>
        <item>
            <creationTimestamp>2020-11-11T08:06:03.522Z</creationTimestamp>
            <networkInterfaceIdSet>
                <item>eni-111111222222333aad</item>
            </networkInterfaceIdSet>
            <ownerId>123456789012</ownerId>
            <requesterManaged>false</requesterManaged>
            <serviceName>com.amazonaws.vpce.us-east-1.vpce-svc-abcd33a1c4321c123</serviceName>
            <state>available</state>
            <subnetIdSet>
                <item>subnet-aaaabbbb333322211</item>
            </subnetIdSet>
            <tagSet/>
            <vpcEndpointId>vpce-22223333bbbbaaaa1</vpcEndpointId>
            <vpcEndpointType>GatewayLoadBalancer</vpcEndpointType>
            <vpcId>vpc-abcabcabc12312312</vpcId>
         </item>
    </vpcEndpointSet>
</DescribeVpcEndpointsResponse>
```

## See Also
<a name="API_DescribeVpcEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeVpcEndpoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeVpcEndpoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeVpcEndpoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeVpcEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeVpcEndpoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeVpcEndpoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeVpcEndpoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeVpcEndpoints)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeVpcEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeVpcEndpoints)
