---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_CSVInput.html
---

# CSVInput
<a name="API_CSVInput"></a>

Describes how an uncompressed comma-separated values (CSV)-formatted input object is formatted.

## Contents
<a name="API_CSVInput_Contents"></a>

 ** AllowQuotedRecordDelimiter **   <a name="AmazonS3-Type-CSVInput-AllowQuotedRecordDelimiter"></a>
Specifies that CSV field values may contain quoted record delimiters and such records should be allowed. Default value is FALSE. Setting this value to TRUE may lower performance.
Type: Boolean
Required: No

 ** Comments **   <a name="AmazonS3-Type-CSVInput-Comments"></a>
A single character used to indicate that a row should be ignored when the character is present at the start of that row. You can specify any character to indicate a comment line. The default character is `#`.
Default: `#`
Type: String
Required: No

 ** FieldDelimiter **   <a name="AmazonS3-Type-CSVInput-FieldDelimiter"></a>
A single character used to separate individual fields in a record. You can specify an arbitrary delimiter.
Type: String
Required: No

 ** FileHeaderInfo **   <a name="AmazonS3-Type-CSVInput-FileHeaderInfo"></a>
Describes the first line of input. Valid values are:
+  `NONE`: First line is not a header.
+  `IGNORE`: First line is a header, but you can't use the header values to indicate the column in an expression. You can use column position (such as \_1, \_2, …) to indicate the column (`SELECT s._1 FROM OBJECT s`).
+  `Use`: First line is a header, and you can use the header value to identify a column in an expression (`SELECT "name" FROM OBJECT`).
Type: String
Valid Values: `USE | IGNORE | NONE`
Required: No

 ** QuoteCharacter **   <a name="AmazonS3-Type-CSVInput-QuoteCharacter"></a>
A single character used for escaping when the field delimiter is part of the value. For example, if the value is `a, b`, Amazon S3 wraps this field value in quotation marks, as follows: `" a , b "`.
Type: String
Default: `"`
Ancestors: `CSV`
Type: String
Required: No

 ** QuoteEscapeCharacter **   <a name="AmazonS3-Type-CSVInput-QuoteEscapeCharacter"></a>
A single character used for escaping the quotation mark character inside an already escaped value. For example, the value `""" a , b """` is parsed as `" a , b "`.
Type: String
Required: No

 ** RecordDelimiter **   <a name="AmazonS3-Type-CSVInput-RecordDelimiter"></a>
A single character used to separate individual records in the input. Instead of the default value, you can specify an arbitrary delimiter.
Type: String
Required: No

## See Also
<a name="API_CSVInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/CSVInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CSVInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/CSVInput)
