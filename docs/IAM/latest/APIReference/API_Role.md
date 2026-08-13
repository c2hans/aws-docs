---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_Role.html
---

# Role
<a name="API_Role"></a>

Contains information about an IAM role. This structure is returned as a response element in several API operations that interact with roles.

## Contents
<a name="API_Role_Contents"></a>

 ** Arn **
 The Amazon Resource Name (ARN) specifying the role. For more information about ARNs and how to use them in policies, see [IAM identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) in the *IAM User Guide* guide.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** CreateDate **
The date and time, in [ISO 8601 date-time format](http://www.iso.org/iso/iso8601), when the role was created.
Type: Timestamp
Required: Yes

 ** Path **
 The path to the role. For more information about paths, see [IAM identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `(\u002F)|(\u002F[\u0021-\u007E]+\u002F)`
Required: Yes

 ** RoleId **
 The stable and unique string identifying the role. For more information about IDs, see [IAM identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 128.
Pattern: `[\w]+`
Required: Yes

 ** RoleName **
The friendly name that identifies the role.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@-]+`
Required: Yes

 ** AssumeRolePolicyDocument **
The policy that grants an entity permission to assume the role.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: No

 ** Description **
A description of the role that you provide.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]*`
Required: No

 ** MaxSessionDuration **
The maximum session duration (in seconds) for the specified role. Anyone who uses the AWS CLI, or API to assume the role can specify the duration using the optional `DurationSeconds` API parameter or `duration-seconds` CLI parameter.
Type: Integer
Valid Range: Minimum value of 3600. Maximum value of 43200.
Required: No

 ** PermissionsBoundary **
The ARN of the policy used to set the permissions boundary for the role.
For more information about permissions boundaries, see [Permissions boundaries for IAM identities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) in the *IAM User Guide*.
Type: [AttachedPermissionsBoundary](API_AttachedPermissionsBoundary.md) object
Required: No

 ** RoleLastUsed **
Contains information about the last time that an IAM role was used. This includes the date and time and the Region in which the role was last used. Activity is only reported for the trailing 400 days. This period can be shorter if your Region began supporting these features within the last year. The role might have been used more than 400 days ago. For more information, see [Regions where data is tracked](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period) in the *IAM user Guide*.
Type: [RoleLastUsed](API_RoleLastUsed.md) object
Required: No

 ** SourceRoleTemplate **
Contains information about the role template that this role was created from. This member is present only for roles created with [AcquireRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_AcquireRole.html).
Type: [SourceRoleTemplate](API_SourceRoleTemplate.md) object
Required: No

 ** Tags.member.N **
A list of tags that are attached to the role. For more information about tagging, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 50 items.
Required: No

## See Also
<a name="API_Role_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/Role)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/Role)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/Role)
