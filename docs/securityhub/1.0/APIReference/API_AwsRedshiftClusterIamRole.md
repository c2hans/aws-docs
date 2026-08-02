---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRedshiftClusterIamRole.html
---

# AwsRedshiftClusterIamRole
<a name="API_AwsRedshiftClusterIamRole"></a>

An IAM role that the cluster can use to access other AWS services.

## Contents
<a name="API_AwsRedshiftClusterIamRole_Contents"></a>

 ** ApplyStatus **   <a name="securityhub-Type-AwsRedshiftClusterIamRole-ApplyStatus"></a>
The status of the IAM role's association with the cluster.
Valid values: `in-sync` \| `adding` \| `removing`
Type: String
Pattern: `.*\S.*`
Required: No

 ** IamRoleArn **   <a name="securityhub-Type-AwsRedshiftClusterIamRole-IamRoleArn"></a>
The ARN of the IAM role.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsRedshiftClusterIamRole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRedshiftClusterIamRole)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRedshiftClusterIamRole)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRedshiftClusterIamRole)
