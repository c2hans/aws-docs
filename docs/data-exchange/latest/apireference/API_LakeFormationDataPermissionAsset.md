---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_LakeFormationDataPermissionAsset.html
---

# LakeFormationDataPermissionAsset
<a name="API_LakeFormationDataPermissionAsset"></a>

The AWS Lake Formation data permission asset.

## Contents
<a name="API_LakeFormationDataPermissionAsset_Contents"></a>

 ** LakeFormationDataPermissionDetails **   <a name="dataexchange-Type-LakeFormationDataPermissionAsset-LakeFormationDataPermissionDetails"></a>
Details about the AWS Lake Formation data permission.
Type: [LakeFormationDataPermissionDetails](API_LakeFormationDataPermissionDetails.md) object
Required: Yes

 ** LakeFormationDataPermissionType **   <a name="dataexchange-Type-LakeFormationDataPermissionAsset-LakeFormationDataPermissionType"></a>
The data permission type.
Type: String
Valid Values: `LFTagPolicy`
Required: Yes

 ** Permissions **   <a name="dataexchange-Type-LakeFormationDataPermissionAsset-Permissions"></a>
The permissions granted to the subscribers on the resource.
Type: Array of strings
Valid Values: `DESCRIBE | SELECT`
Required: Yes

 ** RoleArn **   <a name="dataexchange-Type-LakeFormationDataPermissionAsset-RoleArn"></a>
The IAM role's ARN that allows AWS Data Exchange to assume the role and grant and revoke permissions to AWS Lake Formation data permissions.
Type: String
Pattern: `arn:aws:iam::(\d{12}):role\/.+`
Required: No

## See Also
<a name="API_LakeFormationDataPermissionAsset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/LakeFormationDataPermissionAsset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/LakeFormationDataPermissionAsset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/LakeFormationDataPermissionAsset)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
