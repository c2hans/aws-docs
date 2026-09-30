---
source_url: https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_GroupMembership.html
---

# GroupMembership
<a name="API_GroupMembership"></a>

Contains the identifiers for a group, a group member, and a `GroupMembership` object in the identity store.

## Contents
<a name="API_GroupMembership_Contents"></a>

 ** IdentityStoreId **   <a name="singlesignon-Type-GroupMembership-IdentityStoreId"></a>
The globally unique identifier for the identity store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 93.
Pattern: `(arn:aws[a-z-]*:identitystore::\d{12}:identitystore/)?(d-[0-9a-f]{10}|[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})`
Required: Yes

 ** MembershipArn **   <a name="singlesignon-Type-GroupMembership-MembershipArn"></a>
The Amazon Resource Name (ARN) of the group membership in the identity store. For example, `arn:aws:identitystore:::membership/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333`.
Type: String
Length Constraints: Minimum length of 60. Maximum length of 100.
Pattern: `arn:aws[a-z-]*:identitystore:::(user|group|membership)/([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
Required: Yes

 ** MembershipId **   <a name="singlesignon-Type-GroupMembership-MembershipId"></a>
The identifier for a `GroupMembership` object in an identity store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(arn:aws[a-z-]*:identitystore:::(user|group|membership)/)?([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
Required: Yes

 ** CreatedAt **   <a name="singlesignon-Type-GroupMembership-CreatedAt"></a>
The date and time the group membership was created.
Type: Timestamp
Required: No

 ** CreatedBy **   <a name="singlesignon-Type-GroupMembership-CreatedBy"></a>
The identifier of the user or system that created the group membership.
Type: String
Required: No

 ** GroupId **   <a name="singlesignon-Type-GroupMembership-GroupId"></a>
The identifier for a group in the identity store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(arn:aws[a-z-]*:identitystore:::(user|group|membership)/)?([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
Required: No

 ** MemberId **   <a name="singlesignon-Type-GroupMembership-MemberId"></a>
An object that contains the identifier of a group member. Setting the `UserId` field to the specific identifier for a user indicates that the user is a member of the group.
Type: [MemberId](API_MemberId.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** UpdatedAt **   <a name="singlesignon-Type-GroupMembership-UpdatedAt"></a>
The date and time the group membership was last updated.
Type: Timestamp
Required: No

 ** UpdatedBy **   <a name="singlesignon-Type-GroupMembership-UpdatedBy"></a>
The identifier of the user or system that last updated the group membership.
Type: String
Required: No

## See Also
<a name="API_GroupMembership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/identitystore-2020-06-15/GroupMembership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/identitystore-2020-06-15/GroupMembership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/identitystore-2020-06-15/GroupMembership)
