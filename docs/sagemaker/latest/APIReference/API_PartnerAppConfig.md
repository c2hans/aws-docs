---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PartnerAppConfig.html
---

# PartnerAppConfig
<a name="API_PartnerAppConfig"></a>

Configuration settings for the SageMaker Partner AI App.

## Contents
<a name="API_PartnerAppConfig_Contents"></a>

 ** AdminUsers **   <a name="sagemaker-Type-PartnerAppConfig-AdminUsers"></a>
The list of users that are given admin access to the SageMaker Partner AI App.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(?!\s*$).+`
Required: No

 ** Arguments **   <a name="sagemaker-Type-PartnerAppConfig-Arguments"></a>
This is a map of required inputs for a SageMaker Partner AI App. Based on the application type, the map is populated with a key and value pair that is specific to the user and application.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 5 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: `(?!\s*$).+`
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** AssignedGroupPatterns **   <a name="sagemaker-Type-PartnerAppConfig-AssignedGroupPatterns"></a>
A list of AWS IAM Identity Center group patterns that can access the SageMaker Partner AI App. Group names support wildcard matching using `*`. An empty list indicates the app will not use Identity Center group features. All groups specified in `RoleGroupAssignments` must match patterns in this list.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@*-]+`
Required: No

 ** RoleGroupAssignments **   <a name="sagemaker-Type-PartnerAppConfig-RoleGroupAssignments"></a>
A map of in-app roles to AWS IAM Identity Center group patterns. Groups assigned to specific roles receive those permissions, while groups in `AssignedGroupPatterns` but not in this map receive default in-app role depending on app type. Group patterns support wildcard matching using `*`. Currently supported by Fiddler version 1.3 and later with roles: `ORG_MEMBER` (default) and `ORG_ADMIN`.
Type: Array of [RoleGroupAssignment](API_RoleGroupAssignment.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_PartnerAppConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/PartnerAppConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/PartnerAppConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/PartnerAppConfig)
