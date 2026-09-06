---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_GroupDetail.html
---

# GroupDetail
<a name="API_GroupDetail"></a>

Contains information about an IAM group, including all of the group's policies.

This data type is used as a response element in the [GetAccountAuthorizationDetails](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountAuthorizationDetails.html) operation.

## Contents
<a name="API_GroupDetail_Contents"></a>

 ** Arn **
The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
For more information about ARNs, go to [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** AttachedManagedPolicies.member.N **
A list of the managed policies attached to the group.
Type: Array of [AttachedPolicy](API_AttachedPolicy.md) objects
Required: No

 ** CreateDate **
The date and time, in [ISO 8601 date-time format](http://www.iso.org/iso/iso8601), when the group was created.
Type: Timestamp
Required: No

 ** GroupId **
The stable and unique string identifying the group. For more information about IDs, see [IAM identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 128.
Pattern: `[\w]+`
Required: No

 ** GroupName **
The friendly name that identifies the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: No

 ** GroupPolicyList.member.N **
A list of the inline policies embedded in the group.
Type: Array of [PolicyDetail](API_PolicyDetail.md) objects
Required: No

 ** Path **
The path to the group. For more information about paths, see [IAM identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `(\u002F)|(\u002F[\u0021-\u007E]+\u002F)`
Required: No

## See Also
<a name="API_GroupDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/GroupDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/GroupDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/GroupDetail)
