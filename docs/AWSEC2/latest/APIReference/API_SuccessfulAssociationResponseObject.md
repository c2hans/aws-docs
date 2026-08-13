---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SuccessfulAssociationResponseObject.html
---

# SuccessfulAssociationResponseObject
<a name="API_SuccessfulAssociationResponseObject"></a>

Describes a successful application status check association.

## Contents
<a name="API_SuccessfulAssociationResponseObject_Contents"></a>

 ** applicationStatusCheckId **
The ID of the application status check.
Type: String
Required: No

 ** associationType **
The type of association. Valid values: `EC2TAG` and `INSTANCE_ID`.
Type: String
Required: No

 ** associationValue **
The association value. For `EC2TAG`, the value is formatted as `key=value`. For `INSTANCE_ID`, the value is the instance ID.
Type: String
Required: No

## See Also
<a name="API_SuccessfulAssociationResponseObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SuccessfulAssociationResponseObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SuccessfulAssociationResponseObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SuccessfulAssociationResponseObject)
