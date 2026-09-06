---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_JsonMatchPattern.html
---

# JsonMatchPattern
<a name="API_JsonMatchPattern"></a>

The patterns to look for in the JSON body. AWS WAF inspects the results of these pattern matches against the rule inspection criteria. This is used with the [FieldToMatch](API_FieldToMatch.md) option `JsonBody`.

## Contents
<a name="API_JsonMatchPattern_Contents"></a>

 ** All **   <a name="WAF-Type-JsonMatchPattern-All"></a>
Match all of the elements. See also `MatchScope` in [JsonBody](API_JsonBody.md).
You must specify either this setting or the `IncludedPaths` setting, but not both.
Type: [All](API_All.md) object
Required: No

 ** IncludedPaths **   <a name="WAF-Type-JsonMatchPattern-IncludedPaths"></a>
Match only the specified include paths. See also `MatchScope` in [JsonBody](API_JsonBody.md).
Provide the include paths using JSON Pointer syntax. For example, `"IncludedPaths": ["/dogs/0/name", "/dogs/1/name"]`. For information about this syntax, see the Internet Engineering Task Force (IETF) documentation [JavaScript Object Notation (JSON) Pointer](https://tools.ietf.org/html/rfc6901).
You must specify either this setting or the `All` setting, but not both.
Don't use this option to include all paths. Instead, use the `All` setting.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `([/])|([/](([^~])|(~[01]))+)`
Required: No

## See Also
<a name="API_JsonMatchPattern_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/JsonMatchPattern)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/JsonMatchPattern)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/JsonMatchPattern)
