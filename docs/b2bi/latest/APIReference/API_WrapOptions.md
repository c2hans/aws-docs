---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_WrapOptions.html
---

# WrapOptions
<a name="API_WrapOptions"></a>

Contains options for wrapping (line folding) in X12 EDI files. Wrapping controls how long lines are handled in the EDI output.

## Contents
<a name="API_WrapOptions_Contents"></a>

 ** wrapBy **   <a name="b2bi-Type-WrapOptions-wrapBy"></a>
Specifies the method used for wrapping lines in the EDI output. Valid values:
+  `SEGMENT`: Wraps by segment.
+  `ONE_LINE`: Indicates that the entire content is on a single line.
**Note**
When you specify `ONE_LINE`, do not provide either the line length nor the line terminator value.
+  `LINE_LENGTH`: Wraps by character count, as specified by `lineLength` value.
Type: String
Valid Values: `SEGMENT | ONE_LINE | LINE_LENGTH`
Required: Yes

 ** lineLength **   <a name="b2bi-Type-WrapOptions-lineLength"></a>
Specifies the maximum length of a line before wrapping occurs. This value is used when `wrapBy` is set to `LINE_LENGTH`.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** lineTerminator **   <a name="b2bi-Type-WrapOptions-lineTerminator"></a>
Specifies the character sequence used to terminate lines when wrapping. Valid values:
+  `CRLF`: carriage return and line feed
+  `LF`: line feed)
+  `CR`: carriage return
Type: String
Valid Values: `CRLF | LF | CR`
Required: No

## See Also
<a name="API_WrapOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/WrapOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/WrapOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/WrapOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
