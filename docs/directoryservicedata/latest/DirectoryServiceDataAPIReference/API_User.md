---
source_url: https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_User.html
---

# User
<a name="API_User"></a>

 A user object that contains identifying information and attributes for a specified user.

## Contents
<a name="API_User_Contents"></a>

 ** SAMAccountName **   <a name="directoryservicedata-Type-User-SAMAccountName"></a>
 The name of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[\w\-.]+`
Required: Yes

 ** DistinguishedName **   <a name="directoryservicedata-Type-User-DistinguishedName"></a>
 The [distinguished name](https://learn.microsoft.com/en-us/windows/win32/ad/object-names-and-identities#distinguished-name) of the object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** EmailAddress **   <a name="directoryservicedata-Type-User-EmailAddress"></a>
 The email address of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Enabled **   <a name="directoryservicedata-Type-User-Enabled"></a>
 Indicates whether the user account is active.
Type: Boolean
Required: No

 ** GivenName **   <a name="directoryservicedata-Type-User-GivenName"></a>
 The first name of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** OtherAttributes **   <a name="directoryservicedata-Type-User-OtherAttributes"></a>
 An expression that includes one or more attributes, data types, and values of a user.
Type: String to [AttributeValue](API_AttributeValue.md) object map
Map Entries: Maximum number of 25 items.
Key Length Constraints: Minimum length of 1. Maximum length of 63.
Key Pattern: `[A-Za-z*][A-Za-z-*]*`
Required: No

 ** SID **   <a name="directoryservicedata-Type-User-SID"></a>
 The unique security identifier (SID) of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Surname **   <a name="directoryservicedata-Type-User-Surname"></a>
 The last name of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** UserPrincipalName **   <a name="directoryservicedata-Type-User-UserPrincipalName"></a>
 The UPN that is an internet-style login name for a user and based on the internet standard [RFC 822](https://datatracker.ietf.org/doc/html/rfc822). The UPN is shorter than the distinguished name and easier to remember.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_User_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directory-service-data-2023-05-31/User)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directory-service-data-2023-05-31/User)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directory-service-data-2023-05-31/User)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Directory Service Data. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directoryservicedata` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
