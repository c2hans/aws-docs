---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayVpcAttachment.html
---

# CreateTransitGatewayVpcAttachment
<a name="API_CreateTransitGatewayVpcAttachment"></a>

Attaches the specified VPC to the specified transit gateway.

If you attach a VPC with a CIDR range that overlaps the CIDR range of a VPC that is already attached, the new VPC CIDR range is not propagated to the default propagation route table.

To send VPC traffic to an attached transit gateway, add a route to the VPC route table using [CreateRoute](API_CreateRoute.md).

## Request Parameters
<a name="API_CreateTransitGatewayVpcAttachment_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Options**
The VPC attachment options.
Type: [CreateTransitGatewayVpcAttachmentRequestOptions](API_CreateTransitGatewayVpcAttachmentRequestOptions.md) object
Required: No

 **SubnetIds.N**
The IDs of one or more subnets. You can specify only one subnet per Availability Zone. You must specify at least one subnet, but we recommend that you specify two subnets for better availability. The transit gateway uses one IP address from each specified subnet.
Type: Array of strings
Required: Yes

 **TagSpecifications.N**
The tags to apply to the VPC attachment.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **TransitGatewayId**
The ID of the transit gateway.
Type: String
Required: Yes

 **VpcId**
The ID of the VPC.
Type: String
Required: Yes

## Response Elements
<a name="API_CreateTransitGatewayVpcAttachment_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **transitGatewayVpcAttachment**
Information about the VPC attachment.
Type: [TransitGatewayVpcAttachment](API_TransitGatewayVpcAttachment.md) object

## Errors
<a name="API_CreateTransitGatewayVpcAttachment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateTransitGatewayVpcAttachment_Examples"></a>

### Example
<a name="API_CreateTransitGatewayVpcAttachment_Example_1"></a>

This example creates a transit gateway VPC attachment for the specified transit gateway.

#### Sample Request
<a name="API_CreateTransitGatewayVpcAttachment_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateTransitGatewayVpcAttachment
&TransitGatewayId=tgw-02f776b1a7EXAMPLE
&VpcID=vpc-0065acced4EXAMPLE
&SubnetIds.1=subnet-0187aff814EXAMPLE
&Options.DnsSupport=enable
&Options.Ipv6Support=disable
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateTransitGatewayVpcAttachment_Example_1_Response"></a>

```
<CreateTransitGatewayVpcAttachmentResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>374ab4fd-5ccd-4d98-93f5-034c80f67d79</requestId>
    <transitGatewayVpcAttachment>
        <creationTime>2019-07-17T16:04:27.000Z</creationTime>
        <options>
            <dnsSupport>enable</dnsSupport>
            <ipv6Support>disable</ipv6Support>
        </options>
        <state>pending</state>
        <subnetIds>
            <item>subnet-0187aff814EXAMPLE</item>
        </subnetIds>
        <transitGatewayAttachmentId>tgw-attach-0d2c54bdb3EXAMPLE</transitGatewayAttachmentId>
        <transitGatewayId>tgw-02f776b1a7EXAMPLE</transitGatewayId>
        <vpcId>vpc-0065acced4EXAMPLE</vpcId>
        <vpcOwnerId>111122223333</vpcOwnerId>
    </transitGatewayVpcAttachment>
</CreateTransitGatewayVpcAttachmentResponse>
```

## See Also
<a name="API_CreateTransitGatewayVpcAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateTransitGatewayVpcAttachment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateTransitGatewayVpcAttachment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateTransitGatewayVpcAttachment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateTransitGatewayVpcAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateTransitGatewayVpcAttachment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateTransitGatewayVpcAttachment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateTransitGatewayVpcAttachment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateTransitGatewayVpcAttachment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateTransitGatewayVpcAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateTransitGatewayVpcAttachment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
