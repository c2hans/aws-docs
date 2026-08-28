---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_RequestInspectionACFP.html
---

# RequestInspectionACFP
<a name="API_RequestInspectionACFP"></a>

The criteria for inspecting account creation requests, used by the ACFP rule group to validate and track account creation attempts.

This is part of the `AWSManagedRulesACFPRuleSet` configuration in `ManagedRuleGroupConfig`.

In these settings, you specify how your application accepts account creation attempts by providing the request payload type and the names of the fields within the request body where the username, password, email, and primary address and phone number fields are provided.

## Contents
<a name="API_RequestInspectionACFP_Contents"></a>

 ** PayloadType **   <a name="WAF-Type-RequestInspectionACFP-PayloadType"></a>
The payload type for your account creation endpoint, either JSON or form encoded.
Type: String
Valid Values: `JSON | FORM_ENCODED`
Required: Yes

 ** AddressFields **   <a name="WAF-Type-RequestInspectionACFP-AddressFields"></a>
The names of the fields in the request payload that contain your customer's primary physical address.
Order the address fields in the array exactly as they are ordered in the request payload.
How you specify the address fields depends on the request inspection payload type.
+ For JSON payloads, specify the field identifiers in JSON pointer syntax. For information about the JSON Pointer syntax, see the Internet Engineering Task Force (IETF) documentation [JavaScript Object Notation (JSON) Pointer](https://tools.ietf.org/html/rfc6901).

  For example, for the JSON payload `{ "form": { "primaryaddressline1": "THE_ADDRESS1", "primaryaddressline2": "THE_ADDRESS2", "primaryaddressline3": "THE_ADDRESS3" } }`, the address field idenfiers are `/form/primaryaddressline1`, `/form/primaryaddressline2`, and `/form/primaryaddressline3`.
+ For form encoded payload types, use the HTML form names.

  For example, for an HTML form with input elements named `primaryaddressline1`, `primaryaddressline2`, and `primaryaddressline3`, the address fields identifiers are `primaryaddressline1`, `primaryaddressline2`, and `primaryaddressline3`.
Type: Array of [AddressField](API_AddressField.md) objects
Required: No

 ** EmailField **   <a name="WAF-Type-RequestInspectionACFP-EmailField"></a>
The name of the field in the request payload that contains your customer's email.
How you specify this depends on the request inspection payload type.
+ For JSON payloads, specify the field name in JSON pointer syntax. For information about the JSON Pointer syntax, see the Internet Engineering Task Force (IETF) documentation [JavaScript Object Notation (JSON) Pointer](https://tools.ietf.org/html/rfc6901).

  For example, for the JSON payload `{ "form": { "email": "THE_EMAIL" } }`, the email field specification is `/form/email`.
+ For form encoded payload types, use the HTML form names.

  For example, for an HTML form with the input element named `email1`, the email field specification is `email1`.
Type: [EmailField](API_EmailField.md) object
Required: No

 ** PasswordField **   <a name="WAF-Type-RequestInspectionACFP-PasswordField"></a>
The name of the field in the request payload that contains your customer's password.
How you specify this depends on the request inspection payload type.
+ For JSON payloads, specify the field name in JSON pointer syntax. For information about the JSON Pointer syntax, see the Internet Engineering Task Force (IETF) documentation [JavaScript Object Notation (JSON) Pointer](https://tools.ietf.org/html/rfc6901).

  For example, for the JSON payload `{ "form": { "password": "THE_PASSWORD" } }`, the password field specification is `/form/password`.
+ For form encoded payload types, use the HTML form names.

  For example, for an HTML form with the input element named `password1`, the password field specification is `password1`.
Type: [PasswordField](API_PasswordField.md) object
Required: No

 ** PhoneNumberFields **   <a name="WAF-Type-RequestInspectionACFP-PhoneNumberFields"></a>
The names of the fields in the request payload that contain your customer's primary phone number.
Order the phone number fields in the array exactly as they are ordered in the request payload.
How you specify the phone number fields depends on the request inspection payload type.
+ For JSON payloads, specify the field identifiers in JSON pointer syntax. For information about the JSON Pointer syntax, see the Internet Engineering Task Force (IETF) documentation [JavaScript Object Notation (JSON) Pointer](https://tools.ietf.org/html/rfc6901).

  For example, for the JSON payload `{ "form": { "primaryphoneline1": "THE_PHONE1", "primaryphoneline2": "THE_PHONE2", "primaryphoneline3": "THE_PHONE3" } }`, the phone number field identifiers are `/form/primaryphoneline1`, `/form/primaryphoneline2`, and `/form/primaryphoneline3`.
+ For form encoded payload types, use the HTML form names.

  For example, for an HTML form with input elements named `primaryphoneline1`, `primaryphoneline2`, and `primaryphoneline3`, the phone number field identifiers are `primaryphoneline1`, `primaryphoneline2`, and `primaryphoneline3`.
Type: Array of [PhoneNumberField](API_PhoneNumberField.md) objects
Required: No

 ** UsernameField **   <a name="WAF-Type-RequestInspectionACFP-UsernameField"></a>
The name of the field in the request payload that contains your customer's username.
How you specify this depends on the request inspection payload type.
+ For JSON payloads, specify the field name in JSON pointer syntax. For information about the JSON Pointer syntax, see the Internet Engineering Task Force (IETF) documentation [JavaScript Object Notation (JSON) Pointer](https://tools.ietf.org/html/rfc6901).

  For example, for the JSON payload `{ "form": { "username": "THE_USERNAME" } }`, the username field specification is `/form/username`.
+ For form encoded payload types, use the HTML form names.

  For example, for an HTML form with the input element named `username1`, the username field specification is `username1`
Type: [UsernameField](API_UsernameField.md) object
Required: No

## See Also
<a name="API_RequestInspectionACFP_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/RequestInspectionACFP)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/RequestInspectionACFP)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/RequestInspectionACFP)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
