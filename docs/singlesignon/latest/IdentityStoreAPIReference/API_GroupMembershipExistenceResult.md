---
source_url: https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_GroupMembershipExistenceResult.html
---

# GroupMembershipExistenceResult
<a name="API_GroupMembershipExistenceResult"></a>

Indicates whether a resource is a member of a group in the identity store.

## Contents
<a name="API_GroupMembershipExistenceResult_Contents"></a>

 ** GroupId **   <a name="singlesignon-Type-GroupMembershipExistenceResult-GroupId"></a>
The identifier for a group in the identity store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(arn:aws[a-z-]*:identitystore:::(user|group|membership)/)?([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
Required: No

 ** MemberId **   <a name="singlesignon-Type-GroupMembershipExistenceResult-MemberId"></a>
An object that contains the identifier of a group member. Setting the `UserId` field to the specific identifier for a user indicates that the user is a member of the group.
Type: [MemberId](API_MemberId.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** MembershipExists **   <a name="singlesignon-Type-GroupMembershipExistenceResult-MembershipExists"></a>
Indicates whether a membership relation exists or not.
Type: Boolean
Required: No

## See Also
<a name="API_GroupMembershipExistenceResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/identitystore-2020-06-15/GroupMembershipExistenceResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/identitystore-2020-06-15/GroupMembershipExistenceResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/identitystore-2020-06-15/GroupMembershipExistenceResult)
