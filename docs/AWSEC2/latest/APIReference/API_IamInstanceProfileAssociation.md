---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IamInstanceProfileAssociation.html
---

# IamInstanceProfileAssociation
<a name="API_IamInstanceProfileAssociation"></a>

Describes an association between an IAM instance profile and an instance.

## Contents
<a name="API_IamInstanceProfileAssociation_Contents"></a>

 ** associationId **
The ID of the association.
Type: String
Required: No

 ** iamInstanceProfile **
The IAM instance profile.
Type: [IamInstanceProfile](API_IamInstanceProfile.md) object
Required: No

 ** instanceId **
The ID of the instance.
Type: String
Required: No

 ** state **
The state of the association.
Type: String
Valid Values: `associating | associated | disassociating | disassociated`
Required: No

 ** timestamp **
The time the IAM instance profile was associated with the instance.
Type: Timestamp
Required: No

## See Also
<a name="API_IamInstanceProfileAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IamInstanceProfileAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IamInstanceProfileAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IamInstanceProfileAssociation)
