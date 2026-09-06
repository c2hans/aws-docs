---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UserIdentityInfo.html
---

# UserIdentityInfo
<a name="API_UserIdentityInfo"></a>

Contains information about the identity of a user.

**Note**
For Connect Customer instances that are created with the `EXISTING_DIRECTORY` identity management type, `FirstName`, `LastName`, and `Email` cannot be updated from within Connect Customer because they are managed by the directory.

**Important**
The `FirstName` and `LastName` length constraints below apply only to instances using SAML for identity management. If you are using Connect Customer for identity management, the length constraints are 1-255 for `FirstName`, and 1-256 for `LastName`.

## Contents
<a name="API_UserIdentityInfo_Contents"></a>

 ** Email **   <a name="connect-Type-UserIdentityInfo-Email"></a>
The email address. If you are using SAML for identity management and include this parameter, an error is returned.
Type: String
Required: No

 ** FirstName **   <a name="connect-Type-UserIdentityInfo-FirstName"></a>
The first name. This is required if you are using Connect Customer or SAML for identity management. Inputs must be in Unicode Normalization Form C (NFC). Text containing characters in a non-NFC form (for example, decomposed characters or combining marks) are not accepted.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** LastName **   <a name="connect-Type-UserIdentityInfo-LastName"></a>
The last name. This is required if you are using Connect Customer or SAML for identity management. Inputs must be in Unicode Normalization Form C (NFC). Text containing characters in a non-NFC form (for example, decomposed characters or combining marks) are not accepted.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Required: No

 ** Mobile **   <a name="connect-Type-UserIdentityInfo-Mobile"></a>
The user's mobile number.
Type: String
Pattern: `\\+[1-9]\\d{1,14}$`
Required: No

 ** SecondaryEmail **   <a name="connect-Type-UserIdentityInfo-SecondaryEmail"></a>
The user's secondary email address. If you provide a secondary email, the user receives email notifications - other than password reset notifications - to this email address instead of to their primary email address.
Pattern: `(?=^.{0,265}$)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,63}`
Type: String
Required: No

## See Also
<a name="API_UserIdentityInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UserIdentityInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UserIdentityInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UserIdentityInfo)
