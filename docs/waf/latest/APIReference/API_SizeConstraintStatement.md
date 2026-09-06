---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_SizeConstraintStatement.html
---

# SizeConstraintStatement
<a name="API_SizeConstraintStatement"></a>

A rule statement that compares a number of bytes against the size of a request component, using a comparison operator, such as greater than (>) or less than (<). For example, you can use a size constraint statement to look for query strings that are longer than 100 bytes.

If you configure AWS WAF to inspect the request body, AWS WAF inspects only the number of bytes in the body up to the limit for the web ACL and protected resource type. If you know that the request body for your web requests should never exceed the inspection limit, you can use a size constraint statement to block requests that have a larger request body size. For more information about the inspection limits, see `Body` and `JsonBody` settings for the `FieldToMatch` data type.

If you choose URI for the value of Part of the request to filter on, the slash (/) in the URI counts as one character. For example, the URI `/logo.jpg` is nine characters long.

## Contents
<a name="API_SizeConstraintStatement_Contents"></a>

 ** ComparisonOperator **   <a name="WAF-Type-SizeConstraintStatement-ComparisonOperator"></a>
The operator to use to compare the request part to the size setting.
Type: String
Valid Values: `EQ | NE | LE | LT | GE | GT`
Required: Yes

 ** FieldToMatch **   <a name="WAF-Type-SizeConstraintStatement-FieldToMatch"></a>
The part of the web request that you want AWS WAF to inspect.
Type: [FieldToMatch](API_FieldToMatch.md) object
Required: Yes

 ** Size **   <a name="WAF-Type-SizeConstraintStatement-Size"></a>
The size, in byte, to compare to the request part, after any transformations.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 21474836480.
Required: Yes

 ** TextTransformations **   <a name="WAF-Type-SizeConstraintStatement-TextTransformations"></a>
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. Text transformations are used in rule match statements, to transform the `FieldToMatch` request component before inspecting it, and they're used in rate-based rule statements, to transform request components before using them as custom aggregation keys. If you specify one or more transformations to apply, AWS WAF performs all transformations on the specified content, starting from the lowest priority setting, and then uses the transformed component contents.
Type: Array of [TextTransformation](API_TextTransformation.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** PreParseTextTransformations **   <a name="WAF-Type-SizeConstraintStatement-PreParseTextTransformations"></a>
Pre-parse text transformations normalize the raw query string before AWS WAF parses it into individual query arguments. They are applied before the standard text transformations. Pre-parse text transformations are only supported when `FieldToMatch` is `SingleQueryArgument` or `AllQueryArguments`. You can specify up to 10 pre-parse text transformations per rule statement.
Type: Array of [PreParseTextTransformation](API_PreParseTextTransformation.md) objects
Required: No

## See Also
<a name="API_SizeConstraintStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/SizeConstraintStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/SizeConstraintStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/SizeConstraintStatement)
