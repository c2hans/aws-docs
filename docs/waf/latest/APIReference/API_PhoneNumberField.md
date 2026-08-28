---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_PhoneNumberField.html
---

# PhoneNumberField
<a name="API_PhoneNumberField"></a>

The name of a field in the request payload that contains part or all of your customer's primary phone number.

This data type is used in the `RequestInspectionACFP` data type.

## Contents
<a name="API_PhoneNumberField_Contents"></a>

 ** Identifier **   <a name="WAF-Type-PhoneNumberField-Identifier"></a>
The name of a single primary phone number field.
How you specify the phone number fields depends on the request inspection payload type.
+ For JSON payloads, specify the field identifiers in JSON pointer syntax. For information about the JSON Pointer syntax, see the Internet Engineering Task Force (IETF) documentation [JavaScript Object Notation (JSON) Pointer](https://tools.ietf.org/html/rfc6901).

  For example, for the JSON payload `{ "form": { "primaryphoneline1": "THE_PHONE1", "primaryphoneline2": "THE_PHONE2", "primaryphoneline3": "THE_PHONE3" } }`, the phone number field identifiers are `/form/primaryphoneline1`, `/form/primaryphoneline2`, and `/form/primaryphoneline3`.
+ For form encoded payload types, use the HTML form names.

  For example, for an HTML form with input elements named `primaryphoneline1`, `primaryphoneline2`, and `primaryphoneline3`, the phone number field identifiers are `primaryphoneline1`, `primaryphoneline2`, and `primaryphoneline3`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_PhoneNumberField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/PhoneNumberField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/PhoneNumberField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/PhoneNumberField)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
