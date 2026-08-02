---
source_url: https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html
---

# Group
<a name="API_Group"></a>

A group object that contains the metadata and attributes for a specified group.

## Contents
<a name="API_Group_Contents"></a>

 ** GroupId **   <a name="singlesignon-Type-Group-GroupId"></a>
The identifier for a group in the identity store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 47.
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
Required: Yes

 ** IdentityStoreId **   <a name="singlesignon-Type-Group-IdentityStoreId"></a>
The globally unique identifier for the identity store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `d-[0-9a-f]{10}$|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** CreatedAt **   <a name="singlesignon-Type-Group-CreatedAt"></a>
The date and time the group was created.
Type: Timestamp
Required: No

 ** CreatedBy **   <a name="singlesignon-Type-Group-CreatedBy"></a>
The identifier of the user or system that created the group.
Type: String
Required: No

 ** Description **   <a name="singlesignon-Type-Group-Description"></a>
A string containing a description of the specified group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** DisplayName **   <a name="singlesignon-Type-Group-DisplayName"></a>
The display name value for the group. The length limit is 1,024 characters. This value can consist of letters, accented characters, symbols, numbers, punctuation, tab, new line, carriage return, space, and nonbreaking space in this attribute. This value is specified at the time the group is created and stored as an attribute of the group object in the identity store.
Prefix search supports a maximum of 1,000 characters for the string.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  ]+`
Required: No

 ** ExternalIds **   <a name="singlesignon-Type-Group-ExternalIds"></a>
A list of `ExternalId` objects that contains the identifiers issued to this resource by an external identity provider.
Type: Array of [ExternalId](API_ExternalId.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** UpdatedAt **   <a name="singlesignon-Type-Group-UpdatedAt"></a>
The date and time the group was last updated.
Type: Timestamp
Required: No

 ** UpdatedBy **   <a name="singlesignon-Type-Group-UpdatedBy"></a>
The identifier of the user or system that last updated the group.
Type: String
Required: No

## See Also
<a name="API_Group_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/identitystore-2020-06-15/Group)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/identitystore-2020-06-15/Group)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/identitystore-2020-06-15/Group)
