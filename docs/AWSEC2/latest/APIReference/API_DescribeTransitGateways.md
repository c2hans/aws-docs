---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGateways.html
---

# DescribeTransitGateways
<a name="API_DescribeTransitGateways"></a>

Describes one or more transit gateways. By default, all transit gateways are described. Alternatively, you can filter the results.

## Request Parameters
<a name="API_DescribeTransitGateways_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters. The possible values are:
+  `options.propagation-default-route-table-id` - The ID of the default propagation route table.
+  `options.amazon-side-asn` - The private ASN for the Amazon side of a BGP session.
+  `options.association-default-route-table-id` - The ID of the default association route table.
+  `options.auto-accept-shared-attachments` - Indicates whether there is automatic acceptance of attachment requests (`enable` \| `disable`).
+  `options.default-route-table-association` - Indicates whether resource attachments are automatically associated with the default association route table (`enable` \| `disable`).
+  `options.default-route-table-propagation` - Indicates whether resource attachments automatically propagate routes to the default propagation route table (`enable` \| `disable`).
+  `options.dns-support` - Indicates whether DNS support is enabled (`enable` \| `disable`).
+  `options.vpn-ecmp-support` - Indicates whether Equal Cost Multipath Protocol support is enabled (`enable` \| `disable`).
+  `owner-id` - The ID of the AWS account that owns the transit gateway.
+  `state` - The state of the transit gateway (`available` \| `deleted` \| `deleting` \| `modifying` \| `pending`).
+  `transit-gateway-id` - The ID of the transit gateway.
+  `tag-key `- The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1000.
Required: No

 **NextToken**
The token for the next page of results.
Type: String
Required: No

 **TransitGatewayIds.N**
The IDs of the transit gateways.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeTransitGateways_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **transitGatewaySet**
Information about the transit gateways.
Type: Array of [TransitGateway](API_TransitGateway.md) objects

## Errors
<a name="API_DescribeTransitGateways_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeTransitGateways_Examples"></a>

### Example
<a name="API_DescribeTransitGateways_Example_1"></a>

This example describes your transit gateways.

#### Sample Request
<a name="API_DescribeTransitGateways_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeTransitGateways
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeTransitGateways_Example_1_Response"></a>

```
<DescribeTransitGatewaysResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>151283df-f7dc-4317-89b4-01c9888b1d45</requestId>
    <transitGatewaySet>
        <item>
            <creationTime>2019-05-08T13:21:33.000Z</creationTime>
            <description>example tgw</description>
            <options>
                <amazonSideAsn>64512</amazonSideAsn>
                <associationDefaultRouteTableId>tgw-rtb-002573ed1eEXAMPLE</associationDefaultRouteTableId>
                <autoAcceptSharedAttachments>disable</autoAcceptSharedAttachments>
                <defaultRouteTableAssociation>enable</defaultRouteTableAssociation>
                <defaultRouteTablePropagation>enable</defaultRouteTablePropagation>
                <dnsSupport>enable</dnsSupport>
                <propagationDefaultRouteTableId>tgw-rtb-002573ed1eEXAMPLE</propagationDefaultRouteTableId>
                <vpnEcmpSupport>enable</vpnEcmpSupport>
            </options>
            <ownerId>111122223333</ownerId>
            <state>available</state>
            <tagSet/>
            <transitGatewayArn>arn:aws:ec2:us-east-1:111122223333:transit-gateway/tgw-02f776b1a7EXAMPLE</transitGatewayArn>
            <transitGatewayId>tgw-02f776b1a7EXAMPLE</transitGatewayId>
        </item>
    </transitGatewaySet>
</DescribeTransitGatewaysResponse>
```

## See Also
<a name="API_DescribeTransitGateways_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeTransitGateways)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeTransitGateways)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeTransitGateways)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeTransitGateways)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeTransitGateways)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeTransitGateways)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeTransitGateways)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeTransitGateways)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeTransitGateways)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeTransitGateways)
