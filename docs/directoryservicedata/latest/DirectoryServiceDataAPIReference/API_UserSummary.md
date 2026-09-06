---
source_url: https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_UserSummary.html
---

# UserSummary
<a name="API_UserSummary"></a>

A structure containing a subset of the fields of a user object from a directory.

## Contents
<a name="API_UserSummary_Contents"></a>

 ** Enabled **   <a name="directoryservicedata-Type-UserSummary-Enabled"></a>
Indicates whether the user account is active.
Type: Boolean
Required: Yes

 ** SAMAccountName **   <a name="directoryservicedata-Type-UserSummary-SAMAccountName"></a>
The name of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[\w\-.]+`
Required: Yes

 ** SID **   <a name="directoryservicedata-Type-UserSummary-SID"></a>
 The unique security identifier (SID) of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** GivenName **   <a name="directoryservicedata-Type-UserSummary-GivenName"></a>
The first name of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Surname **   <a name="directoryservicedata-Type-UserSummary-Surname"></a>
The last name of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_UserSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directory-service-data-2023-05-31/UserSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directory-service-data-2023-05-31/UserSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directory-service-data-2023-05-31/UserSummary)
