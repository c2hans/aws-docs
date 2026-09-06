---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_CopyCommand.html
---

# CopyCommand
<a name="API_CopyCommand"></a>

Describes a `COPY` command for Amazon Redshift.

## Contents
<a name="API_CopyCommand_Contents"></a>

 ** DataTableName **   <a name="Firehose-Type-CopyCommand-DataTableName"></a>
The name of the target table. The table must already exist in the database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*`
Required: Yes

 ** CopyOptions **   <a name="Firehose-Type-CopyCommand-CopyOptions"></a>
Optional parameters to use with the Amazon Redshift `COPY` command. For more information, see the "Optional Parameters" section of [Amazon Redshift COPY command](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html). Some possible examples that would apply to Firehose are as follows:
 `delimiter '\t' lzop;` - fields are delimited with "\\t" (TAB character) and compressed using lzop.
 `delimiter '|'` - fields are delimited with "\|" (this is the default delimiter).
 `delimiter '|' escape` - the delimiter should be escaped.
 `fixedwidth 'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6'` - fields are fixed width in the source, with each width specified after every column in the table.
 `JSON 's3://mybucket/jsonpaths.txt'` - data is in JSON format, and the path specified is the format of the data.
For more examples, see [Amazon Redshift COPY command examples](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY_command_examples.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.
Pattern: `.*`
Required: No

 ** DataTableColumns **   <a name="Firehose-Type-CopyCommand-DataTableColumns"></a>
A comma-separated list of column names.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.
Pattern: `.*`
Required: No

## See Also
<a name="API_CopyCommand_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/CopyCommand)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/CopyCommand)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/CopyCommand)
