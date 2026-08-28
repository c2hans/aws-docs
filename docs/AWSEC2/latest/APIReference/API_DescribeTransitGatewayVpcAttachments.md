---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayVpcAttachments.html
---

# DescribeTransitGatewayVpcAttachments
<a name="API_DescribeTransitGatewayVpcAttachments"></a>

Describes one or more VPC attachments. By default, all VPC attachments are described. Alternatively, you can filter the results.

## Request Parameters
<a name="API_DescribeTransitGatewayVpcAttachments_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters. The possible values are:
+  `state` - The state of the attachment. Valid values are `available` \| `deleted` \| `deleting` \| `failed` \| `failing` \| `initiatingRequest` \| `modifying` \| `pendingAcceptance` \| `pending` \| `rollingBack` \| `rejected` \| `rejecting`.
+  `transit-gateway-attachment-id` - The ID of the attachment.
+  `transit-gateway-id` - The ID of the transit gateway.
+  `vpc-id` - The ID of the VPC.
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

 **TransitGatewayAttachmentIds.N**
The IDs of the attachments.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeTransitGatewayVpcAttachments_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **transitGatewayVpcAttachments**
Information about the VPC attachments.
Type: Array of [TransitGatewayVpcAttachment](API_TransitGatewayVpcAttachment.md) objects

## Errors
<a name="API_DescribeTransitGatewayVpcAttachments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeTransitGatewayVpcAttachments_Examples"></a>

### Example
<a name="API_DescribeTransitGatewayVpcAttachments_Example_1"></a>

This example describes your transit gateway VPC attachments.

#### Sample Request
<a name="API_DescribeTransitGatewayVpcAttachments_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeTransitGatewayVpcAttachment
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeTransitGatewayVpcAttachments_Example_1_Response"></a>

```
<DescribeTransitGatewayVpcAttachmentsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>5eeb22d7-c1cf-4efd-9725-1e92e8f9a4e7</requestId>
    <transitGatewayVpcAttachments>
        <item>
            <creationTime>2019-07-17T16:04:27.000Z</creationTime>
            <options>
                <dnsSupport>enable</dnsSupport>
                <ipv6Support>disable</ipv6Support>
            </options>
            <state>available</state>
            <subnetIds>
                <item>subnet-0187aff814EXAMPLE</item>
            </subnetIds>
            <tagSet/>
            <transitGatewayAttachmentId>tgw-attach-0d2c54bdb3EXAMPLE</transitGatewayAttachmentId>
            <transitGatewayId>tgw-02f776b1a7EXAMPLE</transitGatewayId>
            <vpcId>vpc-0065acced4EXAMPLE</vpcId>
            <vpcOwnerId>111122223333</vpcOwnerId>
        </item>
    </transitGatewayVpcAttachments>
</DescribeTransitGatewayVpcAttachmentsResponse>
```

## See Also
<a name="API_DescribeTransitGatewayVpcAttachments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeTransitGatewayVpcAttachments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeTransitGatewayVpcAttachments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeTransitGatewayVpcAttachments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeTransitGatewayVpcAttachments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeTransitGatewayVpcAttachments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeTransitGatewayVpcAttachments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeTransitGatewayVpcAttachments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeTransitGatewayVpcAttachments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeTransitGatewayVpcAttachments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeTransitGatewayVpcAttachments)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
