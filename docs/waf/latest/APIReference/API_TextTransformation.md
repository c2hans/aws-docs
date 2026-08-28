---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_TextTransformation.html
---

# TextTransformation
<a name="API_TextTransformation"></a>

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection.

## Contents
<a name="API_TextTransformation_Contents"></a>

 ** Priority **   <a name="WAF-Type-TextTransformation-Priority"></a>
Sets the relative processing order for multiple transformations. AWS WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don't need to be consecutive, but they must all be different.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** Type **   <a name="WAF-Type-TextTransformation-Type"></a>
For detailed descriptions of each of the transformation types, see [Text transformations](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-transformation.html) in the * AWS WAF Developer Guide*.
Type: String
Valid Values: `NONE | COMPRESS_WHITE_SPACE | HTML_ENTITY_DECODE | LOWERCASE | CMD_LINE | URL_DECODE | BASE64_DECODE | HEX_DECODE | MD5 | REPLACE_COMMENTS | ESCAPE_SEQ_DECODE | SQL_HEX_DECODE | CSS_DECODE | JS_DECODE | NORMALIZE_PATH | NORMALIZE_PATH_WIN | REMOVE_NULLS | REPLACE_NULLS | BASE64_DECODE_EXT | URL_DECODE_UNI | UTF8_TO_UNICODE | REMOVE_WHITESPACE | TRIM | TRIM_LEFT | TRIM_RIGHT | REMOVE_COMMENTS_CHAR | UPPERCASE | CMD_LINE_WIN | CMD_LINE_UNIX | JS_DECODE_EXT | SHA256`
Required: Yes

## See Also
<a name="API_TextTransformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/TextTransformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/TextTransformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/TextTransformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
