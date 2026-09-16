---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateIamInstanceProfile.html
---

# AssociateIamInstanceProfile
<a name="API_AssociateIamInstanceProfile"></a>

Associates an IAM instance profile with a running or stopped instance. You cannot associate more than one IAM instance profile with an instance.

## Request Parameters
<a name="API_AssociateIamInstanceProfile_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **IamInstanceProfile**
The IAM instance profile.
Type: [IamInstanceProfileSpecification](API_IamInstanceProfileSpecification.md) object
Required: Yes

 **InstanceId**
The ID of the instance.
Type: String
Required: Yes

## Response Elements
<a name="API_AssociateIamInstanceProfile_ResponseElements"></a>

The following elements are returned by the service.

 **iamInstanceProfileAssociation**
Information about the IAM instance profile association.
Type: [IamInstanceProfileAssociation](API_IamInstanceProfileAssociation.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_AssociateIamInstanceProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_AssociateIamInstanceProfile_Examples"></a>

### Example
<a name="API_AssociateIamInstanceProfile_Example_1"></a>

This example associates the IAM instance profile with the specified instance.

#### Sample Request
<a name="API_AssociateIamInstanceProfile_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=AssociateIamInstanceProfile
&InstanceId=i-1234567890abcdef0
&IamInstanceProfile.Name=AdminProfile
&AUTHPARAMS
```

#### Sample Response
<a name="API_AssociateIamInstanceProfile_Example_1_Response"></a>

```
<AssociateIamInstanceProfileResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>e10deeaf-7cda-48e7-950b-example</requestId>
    <iamInstanceProfileAssociation>
        <associationId>iip-assoc-0750e3af14e2b40ad</associationId>
        <iamInstanceProfile>
            <arn>arn:aws:iam::123456789012:instance-profile/AdminProfile</arn>
            <id>AIPAJEDNCAA64SSD265D6</id>
        </iamInstanceProfile>
        <instanceId>i-1234567890abcdef0</instanceId>
        <state>associating</state>
    </iamInstanceProfileAssociation>
</AssociateIamInstanceProfileResponse>
```

## See Also
<a name="API_AssociateIamInstanceProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/AssociateIamInstanceProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/AssociateIamInstanceProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AssociateIamInstanceProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/AssociateIamInstanceProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AssociateIamInstanceProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/AssociateIamInstanceProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/AssociateIamInstanceProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/AssociateIamInstanceProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/AssociateIamInstanceProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AssociateIamInstanceProfile)
