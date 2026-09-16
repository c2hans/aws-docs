---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateIamInstanceProfile.html
---

# DisassociateIamInstanceProfile
<a name="API_DisassociateIamInstanceProfile"></a>

Disassociates an IAM instance profile from a running or stopped instance.

Use [DescribeIamInstanceProfileAssociations](API_DescribeIamInstanceProfileAssociations.md) to get the association ID.

## Request Parameters
<a name="API_DisassociateIamInstanceProfile_RequestParameters"></a>

For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AssociationId**
The ID of the IAM instance profile association.
Type: String
Required: Yes

## Response Elements
<a name="API_DisassociateIamInstanceProfile_ResponseElements"></a>

The following elements are returned by the service.

 **iamInstanceProfileAssociation**
Information about the IAM instance profile association.
Type: [IamInstanceProfileAssociation](API_IamInstanceProfileAssociation.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DisassociateIamInstanceProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DisassociateIamInstanceProfile_Examples"></a>

### Example
<a name="API_DisassociateIamInstanceProfile_Example_1"></a>

This example disassociates the specified IAM instance profile association.

#### Sample Request
<a name="API_DisassociateIamInstanceProfile_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DisassociateIamInstanceProfile
&AssociationId=iip-assoc-08049da59357d598c
&AUTHPARAMS
```

#### Sample Response
<a name="API_DisassociateIamInstanceProfile_Example_1_Response"></a>

```
<DisassociateIamInstanceProfileResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>4840f938-fc84-4791-8ae5-example</requestId>
    <iamInstanceProfileAssociation>
        <associationId>iip-assoc-08049da59357d598c</associationId>
        <iamInstanceProfile>
            <arn>arn:aws:iam::123456789012:instance-profile/AdminProfile</arn>
            <id>AIPAI5IVIHMFFYY2DKV5Y</id>
        </iamInstanceProfile>
        <instanceId>i-1234567890abcdef0</instanceId>
        <state>disassociating</state>
    </iamInstanceProfileAssociation>
</DisassociateIamInstanceProfileResponse>
```

## See Also
<a name="API_DisassociateIamInstanceProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DisassociateIamInstanceProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DisassociateIamInstanceProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DisassociateIamInstanceProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DisassociateIamInstanceProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DisassociateIamInstanceProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DisassociateIamInstanceProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DisassociateIamInstanceProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DisassociateIamInstanceProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DisassociateIamInstanceProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DisassociateIamInstanceProfile)
