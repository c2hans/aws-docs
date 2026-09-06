---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_PasswordField.html
---

# PasswordField
<a name="API_PasswordField"></a>

The name of the field in the request payload that contains your customer's password.

This data type is used in the `RequestInspection` and `RequestInspectionACFP` data types.

## Contents
<a name="API_PasswordField_Contents"></a>

 ** Identifier **   <a name="WAF-Type-PasswordField-Identifier"></a>
The name of the password field.
How you specify this depends on the request inspection payload type.
+ For JSON payloads, specify the field name in JSON pointer syntax. For information about the JSON Pointer syntax, see the Internet Engineering Task Force (IETF) documentation [JavaScript Object Notation (JSON) Pointer](https://tools.ietf.org/html/rfc6901).

  For example, for the JSON payload `{ "form": { "password": "THE_PASSWORD" } }`, the password field specification is `/form/password`.
+ For form encoded payload types, use the HTML form names.

  For example, for an HTML form with the input element named `password1`, the password field specification is `password1`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_PasswordField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/PasswordField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/PasswordField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/PasswordField)
