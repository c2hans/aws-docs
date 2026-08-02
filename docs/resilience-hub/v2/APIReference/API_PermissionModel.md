---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_PermissionModel.html
---

# PermissionModel
<a name="API_PermissionModel"></a>

Defines the permission model for a service.

## Contents
<a name="API_PermissionModel_Contents"></a>

 ** invokerRoleName **   <a name="ngresiliencehub-Type-PermissionModel-invokerRoleName"></a>
IAM role name (supports up to 64 characters per IAM limits).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_+=,.@\-]{1,64}`
Required: Yes

 ** crossAccountRoles **   <a name="ngresiliencehub-Type-PermissionModel-crossAccountRoles"></a>
The list of cross-account IAM role ARNs.
Type: Array of [CrossAccountRole](API_CrossAccountRole.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

## See Also
<a name="API_PermissionModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/PermissionModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/PermissionModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/PermissionModel)
