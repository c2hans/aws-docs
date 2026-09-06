---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_CsvConfiguration.html
---

# CsvConfiguration
<a name="API_CsvConfiguration"></a>

A delimited data format where the column separator can be a comma and the record separator is a newline character.

## Contents
<a name="API_CsvConfiguration_Contents"></a>

 ** ColumnSeparator **   <a name="timestream-Type-CsvConfiguration-ColumnSeparator"></a>
Column separator can be one of comma (','), pipe ('\|), semicolon (';'), tab('/t'), or blank space (' ').
Type: String
Length Constraints: Fixed length of 1.
Required: No

 ** EscapeChar **   <a name="timestream-Type-CsvConfiguration-EscapeChar"></a>
Escape character can be one of
Type: String
Length Constraints: Fixed length of 1.
Required: No

 ** NullValue **   <a name="timestream-Type-CsvConfiguration-NullValue"></a>
Can be blank space (' ').
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** QuoteChar **   <a name="timestream-Type-CsvConfiguration-QuoteChar"></a>
Can be single quote (') or double quote (").
Type: String
Length Constraints: Fixed length of 1.
Required: No

 ** TrimWhiteSpace **   <a name="timestream-Type-CsvConfiguration-TrimWhiteSpace"></a>
Specifies to trim leading and trailing white space.
Type: Boolean
Required: No

## See Also
<a name="API_CsvConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-write-2018-11-01/CsvConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-write-2018-11-01/CsvConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-write-2018-11-01/CsvConfiguration)
