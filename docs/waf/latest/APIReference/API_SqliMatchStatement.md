---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_SqliMatchStatement.html
---

# SqliMatchStatement
<a name="API_SqliMatchStatement"></a>

A rule statement that inspects for malicious SQL code. Attackers insert malicious SQL code into web requests to do things like modify your database or extract data from it.

## Contents
<a name="API_SqliMatchStatement_Contents"></a>

 ** FieldToMatch **   <a name="WAF-Type-SqliMatchStatement-FieldToMatch"></a>
The part of the web request that you want AWS WAF to inspect.
Type: [FieldToMatch](API_FieldToMatch.md) object
Required: Yes

 ** TextTransformations **   <a name="WAF-Type-SqliMatchStatement-TextTransformations"></a>
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. Text transformations are used in rule match statements, to transform the `FieldToMatch` request component before inspecting it, and they're used in rate-based rule statements, to transform request components before using them as custom aggregation keys. If you specify one or more transformations to apply, AWS WAF performs all transformations on the specified content, starting from the lowest priority setting, and then uses the transformed component contents.
Type: Array of [TextTransformation](API_TextTransformation.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** PreParseTextTransformations **   <a name="WAF-Type-SqliMatchStatement-PreParseTextTransformations"></a>
Pre-parse text transformations normalize the raw query string before AWS WAF parses it into individual query arguments. They are applied before the standard text transformations. Pre-parse text transformations are only supported when `FieldToMatch` is `SingleQueryArgument` or `AllQueryArguments`. You can specify up to 10 pre-parse text transformations per rule statement.
Type: Array of [PreParseTextTransformation](API_PreParseTextTransformation.md) objects
Required: No

 ** SensitivityLevel **   <a name="WAF-Type-SqliMatchStatement-SensitivityLevel"></a>
The sensitivity that you want AWS WAF to use to inspect for SQL injection attacks.
 `HIGH` detects more attacks, but might generate more false positives, especially if your web requests frequently contain unusual strings. For information about identifying and mitigating false positives, see [Testing and tuning](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-testing.html) in the * AWS WAF Developer Guide*.
 `LOW` is generally a better choice for resources that already have other protections against SQL injection attacks or that have a low tolerance for false positives.
Default: `LOW`
Type: String
Valid Values: `LOW | HIGH`
Required: No

## See Also
<a name="API_SqliMatchStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/SqliMatchStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/SqliMatchStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/SqliMatchStatement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
