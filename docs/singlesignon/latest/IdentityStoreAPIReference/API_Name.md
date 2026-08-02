---
source_url: https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Name.html
---

# Name
<a name="API_Name"></a>

The full name of the user.

## Contents
<a name="API_Name_Contents"></a>

 ** FamilyName **   <a name="singlesignon-Type-Name-FamilyName"></a>
The family name of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** Formatted **   <a name="singlesignon-Type-Name-Formatted"></a>
A string containing a formatted version of the name for display.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** GivenName **   <a name="singlesignon-Type-Name-GivenName"></a>
The given name of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** HonorificPrefix **   <a name="singlesignon-Type-Name-HonorificPrefix"></a>
The honorific prefix of the user. For example, "Dr."
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** HonorificSuffix **   <a name="singlesignon-Type-Name-HonorificSuffix"></a>
The honorific suffix of the user. For example, "M.D."
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** MiddleName **   <a name="singlesignon-Type-Name-MiddleName"></a>
The middle name of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

## See Also
<a name="API_Name_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/identitystore-2020-06-15/Name)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/identitystore-2020-06-15/Name)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/identitystore-2020-06-15/Name)
