---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_FieldToProtect.html
---

# FieldToProtect
<a name="API_FieldToProtect"></a>

Specifies a field type and keys to protect in stored web request data. This is part of the data protection configuration for a web ACL.

## Contents
<a name="API_FieldToProtect_Contents"></a>

 ** FieldType **   <a name="WAF-Type-FieldToProtect-FieldType"></a>
Specifies the web request component type to protect.
Type: String
Valid Values: `SINGLE_HEADER | SINGLE_COOKIE | SINGLE_QUERY_ARGUMENT | QUERY_STRING | BODY`
Required: Yes

 ** FieldKeys **   <a name="WAF-Type-FieldToProtect-FieldKeys"></a>
Specifies the keys to protect for the specified field type.
Required for `SINGLE_HEADER`, `SINGLE_COOKIE`, and `SINGLE_QUERY_ARGUMENT`: provide a non-empty array naming the specific headers, cookies, or query arguments to protect. There is no option to protect all keys of these field types, so enumerate each key you intend to protect.
Must be omitted for `QUERY_STRING` and `BODY`: the entire component is protected and these field types take no keys. Supplying `FieldKeys` for them is rejected.
Type: Array of strings
Array Members: Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_FieldToProtect_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/FieldToProtect)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/FieldToProtect)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/FieldToProtect)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
