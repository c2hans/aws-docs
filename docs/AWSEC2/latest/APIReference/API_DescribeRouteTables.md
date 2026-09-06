---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeRouteTables.html
---

# DescribeRouteTables
<a name="API_DescribeRouteTables"></a>

Describes your route tables. The default is to describe all your route tables. Alternatively, you can specify specific route table IDs or filter the results to include only the route tables that match specific criteria.

Each subnet in your VPC must be associated with a route table. If a subnet is not explicitly associated with any route table, it is implicitly associated with the main route table. This command does not return the subnet ID for implicit associations.

For more information, see [Route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_DescribeRouteTables_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `association.gateway-id` - The ID of the gateway involved in the association.
+  `association.route-table-association-id` - The ID of an association ID for the route table.
+  `association.route-table-id` - The ID of the route table involved in the association.
+  `association.subnet-id` - The ID of the subnet involved in the association.
+  `association.main` - Indicates whether the route table is the main route table for the VPC (`true` \| `false`). Route tables that do not have an association ID are not returned in the response.
+  `owner-id` - The ID of the AWS account that owns the route table.
+  `route-table-id` - The ID of the route table.
+  `route.destination-cidr-block` - The IPv4 CIDR range specified in a route in the table.
+  `route.destination-ipv6-cidr-block` - The IPv6 CIDR range specified in a route in the route table.
+  `route.destination-prefix-list-id` - The ID (prefix) of the AWS service specified in a route in the table.
+  `route.egress-only-internet-gateway-id` - The ID of an egress-only Internet gateway specified in a route in the route table.
+  `route.gateway-id` - The ID of a gateway specified in a route in the table.
+  `route.instance-id` - The ID of an instance specified in a route in the table.
+  `route.nat-gateway-id` - The ID of a NAT gateway.
+  `route.transit-gateway-id` - The ID of a transit gateway.
+  `route.origin` - Describes how the route was created. `CreateRouteTable` indicates that the route was automatically created when the route table was created; `CreateRoute` indicates that the route was manually added to the route table; `EnableVgwRoutePropagation` indicates that the route was propagated by route propagation.
+  `route.state` - The state of a route in the route table (`active` \| `blackhole`). The blackhole state indicates that the route's target isn't available (for example, the specified gateway isn't attached to the VPC, the specified NAT instance has been terminated, and so on).
+  `route.vpc-peering-connection-id` - The ID of a VPC peering connection specified in a route in the table.
+  `tag` - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
+  `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
+  `vpc-id` - The ID of the VPC for the route table.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 100.
Required: No

 **NextToken**
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

 **RouteTableId.N**
The IDs of the route tables.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeRouteTables_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **routeTableSet**
Information about the route tables.
Type: Array of [RouteTable](API_RouteTable.md) objects

## Errors
<a name="API_DescribeRouteTables_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeRouteTables_Examples"></a>

### Example
<a name="API_DescribeRouteTables_Example_1"></a>

This example describes all your route tables. The first route table in the returned list is the VPC's main route table. Its association ID represents the association between the table and the VPC.

#### Sample Request
<a name="API_DescribeRouteTables_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeRouteTables
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeRouteTables_Example_1_Response"></a>

```
<DescribeRouteTablesResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>fe876446-c8c0-4f2d-a6df-ed506example</requestId>
    <routeTableSet>
        <item>
            <routeTableId>rtb-1122334455667788a</routeTableId>
            <vpcId>vpc-12345678912345678</vpcId>
            <ownerId>111122223333</ownerId>
            <routeSet>
                <item>
                    <destinationCidrBlock>10.0.1.0/32</destinationCidrBlock>
                    <gatewayId>igw-012345678901abcdef</gatewayId>
                    <state>active</state>
                    <origin>CreateRoute</origin>
                </item>
                <item>
                    <destinationCidrBlock>172.31.0.0/16</destinationCidrBlock>
                    <gatewayId>local</gatewayId>
                    <state>active</state>
                    <origin>CreateRouteTable</origin>
                </item>
                <item>
                    <destinationCidrBlock>0.0.0.0/0</destinationCidrBlock>
                    <gatewayId>igw-012345678901abcdef</gatewayId>
                    <state>active</state>
                    <origin>CreateRoute</origin>
                </item>
            </routeSet>
            <associationSet>
                <item>
                    <routeTableAssociationId>rtbassoc-04ca27a6914a0b4fc</routeTableAssociationId>
                    <routeTableId>rtb-1122334455667788a</routeTableId>
                    <main>true</main>
                </item>
            </associationSet>
            <propagatingVgwSet/>
            <tagSet/>
        </item>
    </routeTableSet>
</DescribeRouteTablesResponse>
```

## See Also
<a name="API_DescribeRouteTables_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeRouteTables)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeRouteTables)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeRouteTables)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeRouteTables)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeRouteTables)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeRouteTables)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeRouteTables)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeRouteTables)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeRouteTables)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeRouteTables)
