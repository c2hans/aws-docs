---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRdsDbInstanceAssociatedRole.html
---

# AwsRdsDbInstanceAssociatedRole
<a name="API_AwsRdsDbInstanceAssociatedRole"></a>

An IAM role associated with the DB instance.

## Contents
<a name="API_AwsRdsDbInstanceAssociatedRole_Contents"></a>

 ** FeatureName **   <a name="securityhub-Type-AwsRdsDbInstanceAssociatedRole-FeatureName"></a>
The name of the feature associated with the IAM role.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RoleArn **   <a name="securityhub-Type-AwsRdsDbInstanceAssociatedRole-RoleArn"></a>
The ARN of the IAM role that is associated with the DB instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="securityhub-Type-AwsRdsDbInstanceAssociatedRole-Status"></a>
Describes the state of the association between the IAM role and the DB instance. The `Status` property returns one of the following values:
+  `ACTIVE` - The IAM role ARN is associated with the DB instance and can be used to access other AWS services on your behalf.
+  `PENDING` - The IAM role ARN is being associated with the DB instance.
+  `INVALID` - The IAM role ARN is associated with the DB instance. But the DB instance is unable to assume the IAM role in order to access other AWS services on your behalf.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsRdsDbInstanceAssociatedRole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRdsDbInstanceAssociatedRole)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRdsDbInstanceAssociatedRole)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRdsDbInstanceAssociatedRole)
