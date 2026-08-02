---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeletionTaskFailureReasonType.html
---

# DeletionTaskFailureReasonType
<a name="API_DeletionTaskFailureReasonType"></a>

The reason that the service-linked role deletion failed.

This data type is used as a response element in the [GetServiceLinkedRoleDeletionStatus](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetServiceLinkedRoleDeletionStatus.html) operation.

## Contents
<a name="API_DeletionTaskFailureReasonType_Contents"></a>

 ** Reason **
A short description of the reason that the service-linked role deletion failed.
Type: String
Length Constraints: Maximum length of 1000.
Required: No

 ** RoleUsageList.member.N **
A list of objects that contains details about the service-linked role deletion failure, if that information is returned by the service. If the service-linked role has active sessions or if any resources that were used by the role have not been deleted from the linked service, the role can't be deleted. This parameter includes a list of the resources that are associated with the role and the Region in which the resources are being used.
Type: Array of [RoleUsageType](API_RoleUsageType.md) objects
Required: No

## See Also
<a name="API_DeletionTaskFailureReasonType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/DeletionTaskFailureReasonType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/DeletionTaskFailureReasonType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/DeletionTaskFailureReasonType)
