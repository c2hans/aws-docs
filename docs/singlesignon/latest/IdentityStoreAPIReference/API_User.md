---
source_url: https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html
---

# User
<a name="API_User"></a>

A user object that contains the metadata and attributes for a specified user.

## Contents
<a name="API_User_Contents"></a>

 ** IdentityStoreId **   <a name="singlesignon-Type-User-IdentityStoreId"></a>
The globally unique identifier for the identity store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `d-[0-9a-f]{10}$|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** UserId **   <a name="singlesignon-Type-User-UserId"></a>
The identifier for a user in the identity store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 47.
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
Required: Yes

 ** Addresses **   <a name="singlesignon-Type-User-Addresses"></a>
A list of `Address` objects containing addresses associated with the user.
Type: Array of [Address](API_Address.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** Birthdate **   <a name="singlesignon-Type-User-Birthdate"></a>
The user's birthdate in YYYY-MM-DD format. This field stores personal birthdate information for the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** CreatedAt **   <a name="singlesignon-Type-User-CreatedAt"></a>
The date and time the user was created.
Type: Timestamp
Required: No

 ** CreatedBy **   <a name="singlesignon-Type-User-CreatedBy"></a>
The identifier of the user or system that created the user.
Type: String
Required: No

 ** DisplayName **   <a name="singlesignon-Type-User-DisplayName"></a>
A string containing the name of the user that is formatted for display when the user is referenced. For example, "John Doe."
Prefix search supports a maximum of 1,000 characters for the string.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** Emails **   <a name="singlesignon-Type-User-Emails"></a>
A list of `Email` objects containing email addresses associated with the user.
Type: Array of [Email](API_Email.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** Extensions **   <a name="singlesignon-Type-User-Extensions"></a>
A map of explicitly requested attribute extensions associated with the user. Not populated if the user has no requested extensions.
Type: String to JSON value map
Map Entries: Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Key Pattern: `aws:identitystore:[a-z]{1,20}`
Required: No

 ** ExternalIds **   <a name="singlesignon-Type-User-ExternalIds"></a>
A list of `ExternalId` objects that contains the identifiers issued to this resource by an external identity provider.
Type: Array of [ExternalId](API_ExternalId.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** Locale **   <a name="singlesignon-Type-User-Locale"></a>
A string containing the geographical region or location of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** Name **   <a name="singlesignon-Type-User-Name"></a>
An object containing the name of the user.
Type: [Name](API_Name.md) object
Required: No

 ** NickName **   <a name="singlesignon-Type-User-NickName"></a>
A string containing an alternate name for the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** PhoneNumbers **   <a name="singlesignon-Type-User-PhoneNumbers"></a>
A list of `PhoneNumber` objects containing phone numbers associated with the user.
Type: Array of [PhoneNumber](API_PhoneNumber.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** Photos **   <a name="singlesignon-Type-User-Photos"></a>
A list of photos associated with the user. Users can have up to 3 photos with metadata including type, display name, and primary designation.
Type: Array of [Photo](API_Photo.md) objects
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Required: No

 ** PreferredLanguage **   <a name="singlesignon-Type-User-PreferredLanguage"></a>
A string containing the preferred language of the user. For example, "American English" or "en-us."
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** ProfileUrl **   <a name="singlesignon-Type-User-ProfileUrl"></a>
A string containing a URL that might be associated with the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** Roles **   <a name="singlesignon-Type-User-Roles"></a>
A list of `Role` objects containing roles associated with the user.
Type: Array of [Role](API_Role.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** Timezone **   <a name="singlesignon-Type-User-Timezone"></a>
A string containing the time zone of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** Title **   <a name="singlesignon-Type-User-Title"></a>
A string containing the title of the user. Possible values are left unspecified. The value can vary based on your specific use case.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** UpdatedAt **   <a name="singlesignon-Type-User-UpdatedAt"></a>
The date and time the user was last updated.
Type: Timestamp
Required: No

 ** UpdatedBy **   <a name="singlesignon-Type-User-UpdatedBy"></a>
The identifier of the user or system that last updated the user.
Type: String
Required: No

 ** UserName **   <a name="singlesignon-Type-User-UserName"></a>
A unique string used to identify the user. The length limit is 128 characters. This value can consist of letters, accented characters, symbols, numbers, and punctuation. This value is specified at the time the user is created and stored as an attribute of the user object in the identity store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: No

 ** UserStatus **   <a name="singlesignon-Type-User-UserStatus"></a>
The current status of the user account.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** UserType **   <a name="singlesignon-Type-User-UserType"></a>
A string indicating the type of user. Possible values are left unspecified. The value can vary based on your specific use case.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** Website **   <a name="singlesignon-Type-User-Website"></a>
The user's personal website or blog URL. This field stores website information for personal or professional use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

## See Also
<a name="API_User_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/identitystore-2020-06-15/User)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/identitystore-2020-06-15/User)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/identitystore-2020-06-15/User)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Identity Store. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
