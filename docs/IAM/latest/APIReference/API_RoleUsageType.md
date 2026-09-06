---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_RoleUsageType.html
---

# RoleUsageType
<a name="API_RoleUsageType"></a>

An object that contains details about how a service-linked role is used, if that information is returned by the service.

This data type is used as a response element in the [GetServiceLinkedRoleDeletionStatus](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetServiceLinkedRoleDeletionStatus.html) operation.

## Contents
<a name="API_RoleUsageType_Contents"></a>

 ** Region **
The name of the Region where the service-linked role is being used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** Resources.member.N **
The name of the resource that is using the service-linked role.
Type: Array of strings
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

## See Also
<a name="API_RoleUsageType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/RoleUsageType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/RoleUsageType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/RoleUsageType)
