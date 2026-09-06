---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_SizeConstraint.html
---

# SizeConstraint
<a name="API_waf_SizeConstraint"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Specifies a constraint on the size of a part of the web request. AWS WAF uses the `Size`, `ComparisonOperator`, and `FieldToMatch` to build an expression in the form of "`Size` `ComparisonOperator` size in bytes of `FieldToMatch`". If that expression is true, the `SizeConstraint` is considered to match.

## Contents
<a name="API_waf_SizeConstraint_Contents"></a>

 ** ComparisonOperator **   <a name="WAF-Type-waf_SizeConstraint-ComparisonOperator"></a>
The type of comparison you want AWS WAF to perform. AWS WAF uses this in combination with the provided `Size` and `FieldToMatch` to build an expression in the form of "`Size` `ComparisonOperator` size in bytes of `FieldToMatch`". If that expression is true, the `SizeConstraint` is considered to match.
 **EQ**: Used to test if the `Size` is equal to the size of the `FieldToMatch`
 **NE**: Used to test if the `Size` is not equal to the size of the `FieldToMatch`
 **LE**: Used to test if the `Size` is less than or equal to the size of the `FieldToMatch`
 **LT**: Used to test if the `Size` is strictly less than the size of the `FieldToMatch`
 **GE**: Used to test if the `Size` is greater than or equal to the size of the `FieldToMatch`
 **GT**: Used to test if the `Size` is strictly greater than the size of the `FieldToMatch`
Type: String
Valid Values: `EQ | NE | LE | LT | GE | GT`
Required: Yes

 ** FieldToMatch **   <a name="WAF-Type-waf_SizeConstraint-FieldToMatch"></a>
Specifies where in a web request to look for the size constraint.
Type: [FieldToMatch](API_waf_FieldToMatch.md) object
Required: Yes

 ** Size **   <a name="WAF-Type-waf_SizeConstraint-Size"></a>
The size in bytes that you want AWS WAF to compare against the size of the specified `FieldToMatch`. AWS WAF uses this in combination with `ComparisonOperator` and `FieldToMatch` to build an expression in the form of "`Size` `ComparisonOperator` size in bytes of `FieldToMatch`". If that expression is true, the `SizeConstraint` is considered to match.
Valid values for size are 0 - 21474836480 bytes (0 - 20 GB).
If you specify `URI` for the value of `Type`, the / in the URI path that you specify counts as one character. For example, the URI `/logo.jpg` is nine characters long.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 21474836480.
Required: Yes

 ** TextTransformation **   <a name="WAF-Type-waf_SizeConstraint-TextTransformation"></a>
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on `FieldToMatch` before inspecting it for a match.
You can only specify a single type of TextTransformation.
Note that if you choose `BODY` for the value of `Type`, you must choose `NONE` for `TextTransformation` because Amazon CloudFront forwards only the first 8192 bytes for inspection.
 **NONE**
Specify `NONE` if you don't want to perform any text transformations.
 **CMD\_LINE**
When you're concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:
+ Delete the following characters: \\ " ' ^
+ Delete spaces before the following characters: / (
+ Replace the following characters with a space: , ;
+ Replace multiple spaces with one space
+ Convert uppercase letters (A-Z) to lowercase (a-z)
 **COMPRESS\_WHITE\_SPACE**
Use this option to replace the following characters with a space character (decimal 32):
+ \\f, formfeed, decimal 12
+ \\t, tab, decimal 9
+ \\n, newline, decimal 10
+ \\r, carriage return, decimal 13
+ \\v, vertical tab, decimal 11
+ non-breaking space, decimal 160
 `COMPRESS_WHITE_SPACE` also replaces multiple spaces with one space.
 **HTML\_ENTITY\_DECODE**
Use this option to replace HTML-encoded characters with unencoded characters. `HTML_ENTITY_DECODE` performs the following operations:
+ Replaces `(ampersand)quot;` with `"`
+ Replaces `(ampersand)nbsp;` with a non-breaking space, decimal 160
+ Replaces `(ampersand)lt;` with a "less than" symbol
+ Replaces `(ampersand)gt;` with `>`
+ Replaces characters that are represented in hexadecimal format, `(ampersand)#xhhhh;`, with the corresponding characters
+ Replaces characters that are represented in decimal format, `(ampersand)#nnnn;`, with the corresponding characters
 **LOWERCASE**
Use this option to convert uppercase letters (A-Z) to lowercase (a-z).
 **URL\_DECODE**
Use this option to decode a URL-encoded value.
Type: String
Valid Values: `NONE | COMPRESS_WHITE_SPACE | HTML_ENTITY_DECODE | LOWERCASE | CMD_LINE | URL_DECODE`
Required: Yes

## See Also
<a name="API_waf_SizeConstraint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/SizeConstraint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/SizeConstraint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/SizeConstraint)
