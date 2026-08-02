---
source_url: https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Email.html
---

# Email
<a name="API_Email"></a>

The email address associated with the user.

## Contents
<a name="API_Email_Contents"></a>

 ** Primary **   <a name="singlesignon-Type-Email-Primary"></a>
A Boolean value representing whether this is the primary email address for the associated resource.
Type: Boolean
Required: No

 ** Type **   <a name="singlesignon-Type-Email-Type"></a>
A string representing the type of address. For example, "Work."
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

 ** Value **   <a name="singlesignon-Type-Email-Value"></a>
A string containing an email address. For example, "johndoe@amazon.com."
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  　]+`
Required: No

## See Also
<a name="API_Email_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/identitystore-2020-06-15/Email)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/identitystore-2020-06-15/Email)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/identitystore-2020-06-15/Email)
