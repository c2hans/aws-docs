---
source_url: https://docs.aws.amazon.com/accounts/latest/APIReference/API_AlternateContact.html
---

# AlternateContact
<a name="API_AlternateContact"></a>

A structure that contains the details of an alternate contact associated with an AWS account

## Contents
<a name="API_AlternateContact_Contents"></a>

 ** AlternateContactType **   <a name="accounts-Type-AlternateContact-AlternateContactType"></a>
The type of alternate contact.
Type: String
Valid Values: `BILLING | OPERATIONS | SECURITY`
Required: No

 ** EmailAddress **   <a name="accounts-Type-AlternateContact-EmailAddress"></a>
The email address associated with this alternate contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 254.
Pattern: `[\s]*[\w+=.#|!&-]+@[\w.-]+\.[\w]+[\s]*`
Required: No

 ** Name **   <a name="accounts-Type-AlternateContact-Name"></a>
The name associated with this alternate contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** PhoneNumber **   <a name="accounts-Type-AlternateContact-PhoneNumber"></a>
The phone number associated with this alternate contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Pattern: `[\s0-9()+-]+`
Required: No

 ** Title **   <a name="accounts-Type-AlternateContact-Title"></a>
The title associated with this alternate contact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

## See Also
<a name="API_AlternateContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/AlternateContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/AlternateContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/AlternateContact)
