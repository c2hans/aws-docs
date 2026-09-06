---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateSubnetCidrBlock.html
---

# DisassociateSubnetCidrBlock
<a name="API_DisassociateSubnetCidrBlock"></a>

Disassociates a CIDR block from a subnet. Currently, you can disassociate an IPv6 CIDR block only. You must detach or delete all gateways and resources that are associated with the CIDR block before you can disassociate it.

## Request Parameters
<a name="API_DisassociateSubnetCidrBlock_RequestParameters"></a>

For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AssociationId**
The association ID for the CIDR block.
Type: String
Required: Yes

## Response Elements
<a name="API_DisassociateSubnetCidrBlock_ResponseElements"></a>

The following elements are returned by the service.

 **ipv6CidrBlockAssociation**
Information about the IPv6 CIDR block association.
Type: [SubnetIpv6CidrBlockAssociation](API_SubnetIpv6CidrBlockAssociation.md) object

 **requestId**
The ID of the request.
Type: String

 **subnetId**
The ID of the subnet.
Type: String

## Errors
<a name="API_DisassociateSubnetCidrBlock_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DisassociateSubnetCidrBlock_Examples"></a>

### Example
<a name="API_DisassociateSubnetCidrBlock_Example_1"></a>

This example disassociates the IPv6 CIDR block from the subnet.

#### Sample Request
<a name="API_DisassociateSubnetCidrBlock_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DisassociateSubnetCidrBlock
&AssociationId=subnet-cidr-assoc-3aa54053
&AUTHPARAMS
```

#### Sample Response
<a name="API_DisassociateSubnetCidrBlock_Example_1_Response"></a>

```
<DisassociateSubnetCidrBlockResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <subnetId>subnet-5f46ec3b</subnetId>
    <ipv6CidrBlockAssociation>
        <ipv6CidrBlock>2001:db8:1234:1a00::/64</ipv6CidrBlock>
        <ipv6CidrBlockState>
            <state>disassociating</state>
        </ipv6CidrBlockState>
        <associationId>subnet-cidr-assoc-3aa54053</associationId>
    </ipv6CidrBlockAssociation>
</DisassociateSubnetCidrBlockResponse>
```

## See Also
<a name="API_DisassociateSubnetCidrBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DisassociateSubnetCidrBlock)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DisassociateSubnetCidrBlock)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DisassociateSubnetCidrBlock)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DisassociateSubnetCidrBlock)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DisassociateSubnetCidrBlock)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DisassociateSubnetCidrBlock)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DisassociateSubnetCidrBlock)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DisassociateSubnetCidrBlock)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DisassociateSubnetCidrBlock)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DisassociateSubnetCidrBlock)
