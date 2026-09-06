---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RoleGroupAssignment.html
---

# RoleGroupAssignment
<a name="API_RoleGroupAssignment"></a>

Defines the mapping between an in-app role and the AWS IAM Identity Center group patterns that should be assigned to that role within the SageMaker Partner AI App.

## Contents
<a name="API_RoleGroupAssignment_Contents"></a>

 ** GroupPatterns **   <a name="sagemaker-Type-RoleGroupAssignment-GroupPatterns"></a>
A list of AWS IAM Identity Center group patterns that should be assigned to the specified role. Group patterns support wildcard matching using `*`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@*-]+`
Required: Yes

 ** RoleName **   <a name="sagemaker-Type-RoleGroupAssignment-RoleName"></a>
The name of the in-app role within the SageMaker Partner AI App. The specific roles available depend on the app type and version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(?!\s*$).+`
Required: Yes

## See Also
<a name="API_RoleGroupAssignment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/RoleGroupAssignment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/RoleGroupAssignment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/RoleGroupAssignment)
