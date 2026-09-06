---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateVpcCidrBlock.html
---

# DisassociateVpcCidrBlock
<a name="API_DisassociateVpcCidrBlock"></a>

Disassociates a CIDR block from a VPC. To disassociate the CIDR block, you must specify its association ID. You can get the association ID by using [DescribeVpcs](API_DescribeVpcs.md). You must detach or delete all gateways and resources that are associated with the CIDR block before you can disassociate it.

You cannot disassociate the CIDR block with which you originally created the VPC (the primary CIDR block).

## Request Parameters
<a name="API_DisassociateVpcCidrBlock_RequestParameters"></a>

For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AssociationId**
The association ID for the CIDR block.
Type: String
Required: Yes

## Response Elements
<a name="API_DisassociateVpcCidrBlock_ResponseElements"></a>

The following elements are returned by the service.

 **cidrBlockAssociation**
Information about the IPv4 CIDR block association.
Type: [VpcCidrBlockAssociation](API_VpcCidrBlockAssociation.md) object

 **ipv6CidrBlockAssociation**
Information about the IPv6 CIDR block association.
Type: [VpcIpv6CidrBlockAssociation](API_VpcIpv6CidrBlockAssociation.md) object

 **requestId**
The ID of the request.
Type: String

 **vpcId**
The ID of the VPC.
Type: String

## Errors
<a name="API_DisassociateVpcCidrBlock_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DisassociateVpcCidrBlock_Examples"></a>

### Example
<a name="API_DisassociateVpcCidrBlock_Example_1"></a>

This example disassociates the IPv6 CIDR block from the VPC.

#### Sample Request
<a name="API_DisassociateVpcCidrBlock_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DisassociateVpcCidrBlock
&AssociationId=vpc-cidr-assoc-e2a5408b
&AUTHPARAMS
```

#### Sample Response
<a name="API_DisassociateVpcCidrBlock_Example_1_Response"></a>

```
<DisassociateVpcCidrBlockResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <ipv6CidrBlockAssociation>
        <ipv6CidrBlock>2001:db8:1234:1a00::/56</ipv6CidrBlock>
        <ipv6CidrBlockState>
            <state>disassociating</state>
        </ipv6CidrBlockState>
        <associationId>vpc-cidr-assoc-e2a5408b</associationId>
    </ipv6CidrBlockAssociation>
    <vpcId>vpc-a034d6c4</vpcId>
</DisassociateVpcCidrBlockResponse>
```

## See Also
<a name="API_DisassociateVpcCidrBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DisassociateVpcCidrBlock)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DisassociateVpcCidrBlock)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DisassociateVpcCidrBlock)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DisassociateVpcCidrBlock)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DisassociateVpcCidrBlock)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DisassociateVpcCidrBlock)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DisassociateVpcCidrBlock)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DisassociateVpcCidrBlock)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DisassociateVpcCidrBlock)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DisassociateVpcCidrBlock)
