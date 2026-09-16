---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceIamInstanceProfileAssociation.html
---

# ReplaceIamInstanceProfileAssociation
<a name="API_ReplaceIamInstanceProfileAssociation"></a>

Replaces an IAM instance profile for the specified running instance. You can use this action to change the IAM instance profile that's associated with an instance without having to disassociate the existing IAM instance profile first.

Use [DescribeIamInstanceProfileAssociations](API_DescribeIamInstanceProfileAssociations.md) to get the association ID.

## Request Parameters
<a name="API_ReplaceIamInstanceProfileAssociation_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AssociationId**
The ID of the existing IAM instance profile association.
Type: String
Required: Yes

 **IamInstanceProfile**
The IAM instance profile.
Type: [IamInstanceProfileSpecification](API_IamInstanceProfileSpecification.md) object
Required: Yes

## Response Elements
<a name="API_ReplaceIamInstanceProfileAssociation_ResponseElements"></a>

The following elements are returned by the service.

 **iamInstanceProfileAssociation**
Information about the IAM instance profile association.
Type: [IamInstanceProfileAssociation](API_IamInstanceProfileAssociation.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_ReplaceIamInstanceProfileAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ReplaceIamInstanceProfileAssociation_Examples"></a>

### Example
<a name="API_ReplaceIamInstanceProfileAssociation_Example_1"></a>

This example replaces the IAM instance profile represented by the association `iip-assoc-060bae234aac2e7fa` with the IAM instance profile named `AdminProfile`.

#### Sample Request
<a name="API_ReplaceIamInstanceProfileAssociation_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ReplaceIamInstanceProfileAssociation
&AssociationId=iip-assoc-060bae234aac2e7fa
&IamInstanceProfile.Name=AdminProfile
&AUTHPARAMS
```

#### Sample Response
<a name="API_ReplaceIamInstanceProfileAssociation_Example_1_Response"></a>

```
<ReplaceIamInstanceProfileAssociationResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>ba40aa4c-d788-4f24-8a34-example</requestId>
    <iamInstanceProfileAssociation>
        <associationId>iip-assoc-08049da59357d598c</associationId>
        <iamInstanceProfile>
            <arn>arn:aws:iam::123456789012:instance-profile/AdminRole</arn>
            <id>AIPAI5IVIHMFFYY2DKV5Y</id>
        </iamInstanceProfile>
        <instanceId>i-1234567890abcdef0</instanceId>
        <state>associating</state>
    </iamInstanceProfileAssociation>
</ReplaceIamInstanceProfileAssociationResponse>
```

## See Also
<a name="API_ReplaceIamInstanceProfileAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ReplaceIamInstanceProfileAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ReplaceIamInstanceProfileAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ReplaceIamInstanceProfileAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ReplaceIamInstanceProfileAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ReplaceIamInstanceProfileAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ReplaceIamInstanceProfileAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ReplaceIamInstanceProfileAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ReplaceIamInstanceProfileAssociation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ReplaceIamInstanceProfileAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ReplaceIamInstanceProfileAssociation)
