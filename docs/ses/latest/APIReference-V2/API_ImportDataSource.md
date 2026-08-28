---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ImportDataSource.html
---

# ImportDataSource
<a name="API_ImportDataSource"></a>

An object that contains details about the data source of the import job.

## Contents
<a name="API_ImportDataSource_Contents"></a>

 ** DataFormat **   <a name="SES-Type-ImportDataSource-DataFormat"></a>
The data format of the import job's data source.
Type: String
Valid Values: `CSV | JSON`
Required: Yes

 ** S3Url **   <a name="SES-Type-ImportDataSource-S3Url"></a>
An Amazon S3 URL in the format s3://*<bucket\_name>*/*<object>*.
Type: String
Pattern: `^s3:\/\/([^\/]+)\/(.*?([^\/]+)\/?)$`
Required: Yes

## See Also
<a name="API_ImportDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ImportDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ImportDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ImportDataSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
