---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_CsvOptions.html
---

# CsvOptions
<a name="API_CsvOptions"></a>

Represents a set of options that define how DataBrew will read a comma-separated value (CSV) file when creating a dataset from that file.

## Contents
<a name="API_CsvOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Delimiter **   <a name="databrew-Type-CsvOptions-Delimiter"></a>
A single character that specifies the delimiter being used in the CSV file.
Type: String
Length Constraints: Fixed length of 1.
Required: No

 ** HeaderRow **   <a name="databrew-Type-CsvOptions-HeaderRow"></a>
A variable that specifies whether the first row in the file is parsed as the header. If this value is false, column names are auto-generated.
Type: Boolean
Required: No

## See Also
<a name="API_CsvOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/CsvOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/CsvOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/CsvOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
