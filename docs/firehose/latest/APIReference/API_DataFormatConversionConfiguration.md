---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_DataFormatConversionConfiguration.html
---

# DataFormatConversionConfiguration
<a name="API_DataFormatConversionConfiguration"></a>

Specifies that you want Firehose to convert data from the JSON format to the Parquet or ORC format before writing it to Amazon S3. Firehose uses the serializer and deserializer that you specify, in addition to the column information from the AWS Glue table, to deserialize your input data from JSON and then serialize it to the Parquet or ORC format. For more information, see [Firehose Record Format Conversion](https://docs.aws.amazon.com/firehose/latest/dev/record-format-conversion.html).

## Contents
<a name="API_DataFormatConversionConfiguration_Contents"></a>

 ** Enabled **   <a name="Firehose-Type-DataFormatConversionConfiguration-Enabled"></a>
Defaults to `true`. Set it to `false` if you want to disable format conversion while preserving the configuration details.
Type: Boolean
Required: No

 ** InputFormatConfiguration **   <a name="Firehose-Type-DataFormatConversionConfiguration-InputFormatConfiguration"></a>
Specifies the deserializer that you want Firehose to use to convert the format of your data from JSON. This parameter is required if `Enabled` is set to true.
Type: [InputFormatConfiguration](API_InputFormatConfiguration.md) object
Required: No

 ** OutputFormatConfiguration **   <a name="Firehose-Type-DataFormatConversionConfiguration-OutputFormatConfiguration"></a>
Specifies the serializer that you want Firehose to use to convert the format of your data to the Parquet or ORC format. This parameter is required if `Enabled` is set to true.
Type: [OutputFormatConfiguration](API_OutputFormatConfiguration.md) object
Required: No

 ** SchemaConfiguration **   <a name="Firehose-Type-DataFormatConversionConfiguration-SchemaConfiguration"></a>
Specifies the AWS Glue Data Catalog table that contains the column information. This parameter is required if `Enabled` is set to true.
Type: [SchemaConfiguration](API_SchemaConfiguration.md) object
Required: No

## See Also
<a name="API_DataFormatConversionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/DataFormatConversionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/DataFormatConversionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/DataFormatConversionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
