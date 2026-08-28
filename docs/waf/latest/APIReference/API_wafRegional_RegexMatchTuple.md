---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_RegexMatchTuple.html
---

# RegexMatchTuple
<a name="API_wafRegional_RegexMatchTuple"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

The regular expression pattern that you want AWS WAF to search for in web requests, the location in requests that you want AWS WAF to search, and other settings. Each `RegexMatchTuple` object contains:
+ The part of a web request that you want AWS WAF to inspect, such as a query string or the value of the `User-Agent` header.
+ The identifier of the pattern (a regular expression) that you want AWS WAF to look for. For more information, see [RegexPatternSet](API_wafRegional_RegexPatternSet.md).
+ Whether to perform any conversions on the request, such as converting it to lowercase, before inspecting it for the specified string.

## Contents
<a name="API_wafRegional_RegexMatchTuple_Contents"></a>

 ** FieldToMatch **   <a name="WAF-Type-wafRegional_RegexMatchTuple-FieldToMatch"></a>
Specifies where in a web request to look for the `RegexPatternSet`.
Type: [FieldToMatch](API_wafRegional_FieldToMatch.md) object
Required: Yes

 ** RegexPatternSetId **   <a name="WAF-Type-wafRegional_RegexMatchTuple-RegexPatternSetId"></a>
The `RegexPatternSetId` for a `RegexPatternSet`. You use `RegexPatternSetId` to get information about a `RegexPatternSet` (see [GetRegexPatternSet](API_wafRegional_GetRegexPatternSet.md)), update a `RegexPatternSet` (see [UpdateRegexPatternSet](API_wafRegional_UpdateRegexPatternSet.md)), insert a `RegexPatternSet` into a `RegexMatchSet` or delete one from a `RegexMatchSet` (see [UpdateRegexMatchSet](API_wafRegional_UpdateRegexMatchSet.md)), and delete an `RegexPatternSet` from AWS WAF (see [DeleteRegexPatternSet](API_wafRegional_DeleteRegexPatternSet.md)).
 `RegexPatternSetId` is returned by [CreateRegexPatternSet](API_wafRegional_CreateRegexPatternSet.md) and by [ListRegexPatternSets](API_wafRegional_ListRegexPatternSets.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** TextTransformation **   <a name="WAF-Type-wafRegional_RegexMatchTuple-TextTransformation"></a>
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on `RegexPatternSet` before inspecting a request for a match.
You can only specify a single type of TextTransformation.
 **CMD\_LINE**
When you're concerned that attackers are injecting an operating system commandline command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:
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
 **NONE**
Specify `NONE` if you don't want to perform any text transformations.
Type: String
Valid Values: `NONE | COMPRESS_WHITE_SPACE | HTML_ENTITY_DECODE | LOWERCASE | CMD_LINE | URL_DECODE`
Required: Yes

## See Also
<a name="API_wafRegional_RegexMatchTuple_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/RegexMatchTuple)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/RegexMatchTuple)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/RegexMatchTuple)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
