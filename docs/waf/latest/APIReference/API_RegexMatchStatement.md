---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_RegexMatchStatement.html
---

# RegexMatchStatement
<a name="API_RegexMatchStatement"></a>

A rule statement used to search web request components for a match against a single regular expression.

## Contents
<a name="API_RegexMatchStatement_Contents"></a>

 ** FieldToMatch **   <a name="WAF-Type-RegexMatchStatement-FieldToMatch"></a>
The part of the web request that you want AWS WAF to inspect.
Type: [FieldToMatch](API_FieldToMatch.md) object
Required: Yes

 ** RegexString **   <a name="WAF-Type-RegexMatchStatement-RegexString"></a>
The string representing the regular expression. AWS WAF enforces a quota on the maximum number of characters in a regex pattern. For the current limit, see [AWS WAF quotas](https://docs.aws.amazon.com/waf/latest/developerguide/limits.html) in the * AWS WAF Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*`
Required: Yes

 ** TextTransformations **   <a name="WAF-Type-RegexMatchStatement-TextTransformations"></a>
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. Text transformations are used in rule match statements, to transform the `FieldToMatch` request component before inspecting it, and they're used in rate-based rule statements, to transform request components before using them as custom aggregation keys. If you specify one or more transformations to apply, AWS WAF performs all transformations on the specified content, starting from the lowest priority setting, and then uses the transformed component contents.
Type: Array of [TextTransformation](API_TextTransformation.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** PreParseTextTransformations **   <a name="WAF-Type-RegexMatchStatement-PreParseTextTransformations"></a>
Pre-parse text transformations normalize the raw query string before AWS WAF parses it into individual query arguments. They are applied before the standard text transformations. Pre-parse text transformations are only supported when `FieldToMatch` is `SingleQueryArgument` or `AllQueryArguments`. You can specify up to 10 pre-parse text transformations per rule statement.
Type: Array of [PreParseTextTransformation](API_PreParseTextTransformation.md) objects
Required: No

## See Also
<a name="API_RegexMatchStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/RegexMatchStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/RegexMatchStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/RegexMatchStatement)
