---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_AddressField.html
---

# AddressField
<a name="API_AddressField"></a>

The name of a field in the request payload that contains part or all of your customer's primary physical address.

This data type is used in the `RequestInspectionACFP` data type.

## Contents
<a name="API_AddressField_Contents"></a>

 ** Identifier **   <a name="WAF-Type-AddressField-Identifier"></a>
The name of a single primary address field.
How you specify the address fields depends on the request inspection payload type.
+ For JSON payloads, specify the field identifiers in JSON pointer syntax. For information about the JSON Pointer syntax, see the Internet Engineering Task Force (IETF) documentation [JavaScript Object Notation (JSON) Pointer](https://tools.ietf.org/html/rfc6901).

  For example, for the JSON payload `{ "form": { "primaryaddressline1": "THE_ADDRESS1", "primaryaddressline2": "THE_ADDRESS2", "primaryaddressline3": "THE_ADDRESS3" } }`, the address field idenfiers are `/form/primaryaddressline1`, `/form/primaryaddressline2`, and `/form/primaryaddressline3`.
+ For form encoded payload types, use the HTML form names.

  For example, for an HTML form with input elements named `primaryaddressline1`, `primaryaddressline2`, and `primaryaddressline3`, the address fields identifiers are `primaryaddressline1`, `primaryaddressline2`, and `primaryaddressline3`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_AddressField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/AddressField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/AddressField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/AddressField)
