---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_RegexPatternSetReferenceStatement.html
---

# RegexPatternSetReferenceStatement
<a name="API_RegexPatternSetReferenceStatement"></a>

A rule statement used to search web request components for matches with regular expressions. To use this, create a [RegexPatternSet](API_RegexPatternSet.md) that specifies the expressions that you want to detect, then use the ARN of that set in this statement. A web request matches the pattern set rule statement if the request component matches any of the patterns in the set. To create a regex pattern set, see [CreateRegexPatternSet](API_CreateRegexPatternSet.md).

Each regex pattern set rule statement references a regex pattern set. You create and maintain the set independent of your rules. This allows you to use the single set in multiple rules. When you update the referenced set, AWS WAF automatically updates all rules that reference it.

## Contents
<a name="API_RegexPatternSetReferenceStatement_Contents"></a>

 ** ARN **   <a name="WAF-Type-RegexPatternSetReferenceStatement-ARN"></a>
The Amazon Resource Name (ARN) of the [RegexPatternSet](API_RegexPatternSet.md) that this statement references.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*\S.*`
Required: Yes

 ** FieldToMatch **   <a name="WAF-Type-RegexPatternSetReferenceStatement-FieldToMatch"></a>
The part of the web request that you want AWS WAF to inspect.
Type: [FieldToMatch](API_FieldToMatch.md) object
Required: Yes

 ** TextTransformations **   <a name="WAF-Type-RegexPatternSetReferenceStatement-TextTransformations"></a>
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. Text transformations are used in rule match statements, to transform the `FieldToMatch` request component before inspecting it, and they're used in rate-based rule statements, to transform request components before using them as custom aggregation keys. If you specify one or more transformations to apply, AWS WAF performs all transformations on the specified content, starting from the lowest priority setting, and then uses the transformed component contents.
Type: Array of [TextTransformation](API_TextTransformation.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** PreParseTextTransformations **   <a name="WAF-Type-RegexPatternSetReferenceStatement-PreParseTextTransformations"></a>
Pre-parse text transformations normalize the raw query string before AWS WAF parses it into individual query arguments. They are applied before the standard text transformations. Pre-parse text transformations are only supported when `FieldToMatch` is `SingleQueryArgument` or `AllQueryArguments`. You can specify up to 10 pre-parse text transformations per rule statement.
Type: Array of [PreParseTextTransformation](API_PreParseTextTransformation.md) objects
Required: No

## See Also
<a name="API_RegexPatternSetReferenceStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/RegexPatternSetReferenceStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/RegexPatternSetReferenceStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/RegexPatternSetReferenceStatement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
