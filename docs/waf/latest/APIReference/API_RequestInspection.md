---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_RequestInspection.html
---

# RequestInspection
<a name="API_RequestInspection"></a>

The criteria for inspecting login requests, used by the ATP rule group to validate credentials usage.

This is part of the `AWSManagedRulesATPRuleSet` configuration in `ManagedRuleGroupConfig`.

In these settings, you specify how your application accepts login attempts by providing the request payload type and the names of the fields within the request body where the username and password are provided.

## Contents
<a name="API_RequestInspection_Contents"></a>

 ** PasswordField **   <a name="WAF-Type-RequestInspection-PasswordField"></a>
The name of the field in the request payload that contains your customer's password.
How you specify this depends on the request inspection payload type.
+ For JSON payloads, specify the field name in JSON pointer syntax. For information about the JSON Pointer syntax, see the Internet Engineering Task Force (IETF) documentation [JavaScript Object Notation (JSON) Pointer](https://tools.ietf.org/html/rfc6901).

  For example, for the JSON payload `{ "form": { "password": "THE_PASSWORD" } }`, the password field specification is `/form/password`.
+ For form encoded payload types, use the HTML form names.

  For example, for an HTML form with the input element named `password1`, the password field specification is `password1`.
Type: [PasswordField](API_PasswordField.md) object
Required: Yes

 ** PayloadType **   <a name="WAF-Type-RequestInspection-PayloadType"></a>
The payload type for your login endpoint, either JSON or form encoded.
Type: String
Valid Values: `JSON | FORM_ENCODED`
Required: Yes

 ** UsernameField **   <a name="WAF-Type-RequestInspection-UsernameField"></a>
The name of the field in the request payload that contains your customer's username.
How you specify this depends on the request inspection payload type.
+ For JSON payloads, specify the field name in JSON pointer syntax. For information about the JSON Pointer syntax, see the Internet Engineering Task Force (IETF) documentation [JavaScript Object Notation (JSON) Pointer](https://tools.ietf.org/html/rfc6901).

  For example, for the JSON payload `{ "form": { "username": "THE_USERNAME" } }`, the username field specification is `/form/username`.
+ For form encoded payload types, use the HTML form names.

  For example, for an HTML form with the input element named `username1`, the username field specification is `username1`
Type: [UsernameField](API_UsernameField.md) object
Required: Yes

## See Also
<a name="API_RequestInspection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/RequestInspection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/RequestInspection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/RequestInspection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
