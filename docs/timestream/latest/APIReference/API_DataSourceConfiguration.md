---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_DataSourceConfiguration.html
---

# DataSourceConfiguration
<a name="API_DataSourceConfiguration"></a>

Defines configuration details about the data source.

## Contents
<a name="API_DataSourceConfiguration_Contents"></a>

 ** DataFormat **   <a name="timestream-Type-DataSourceConfiguration-DataFormat"></a>
This is currently CSV.
Type: String
Valid Values: `CSV`
Required: Yes

 ** DataSourceS3Configuration **   <a name="timestream-Type-DataSourceConfiguration-DataSourceS3Configuration"></a>
Configuration of an S3 location for a file which contains data to load.
Type: [DataSourceS3Configuration](API_DataSourceS3Configuration.md) object
Required: Yes

 ** CsvConfiguration **   <a name="timestream-Type-DataSourceConfiguration-CsvConfiguration"></a>
A delimited data format where the column separator can be a comma and the record separator is a newline character.
Type: [CsvConfiguration](API_CsvConfiguration.md) object
Required: No

## See Also
<a name="API_DataSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-write-2018-11-01/DataSourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-write-2018-11-01/DataSourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-write-2018-11-01/DataSourceConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
