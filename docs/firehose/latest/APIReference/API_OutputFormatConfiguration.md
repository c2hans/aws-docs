---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_OutputFormatConfiguration.html
---

# OutputFormatConfiguration
<a name="API_OutputFormatConfiguration"></a>

Specifies the serializer that you want Firehose to use to convert the format of your data before it writes it to Amazon S3. This parameter is required if `Enabled` is set to true.

## Contents
<a name="API_OutputFormatConfiguration_Contents"></a>

 ** Serializer **   <a name="Firehose-Type-OutputFormatConfiguration-Serializer"></a>
Specifies which serializer to use. You can choose either the ORC SerDe or the Parquet SerDe. If both are non-null, the server rejects the request.
Type: [Serializer](API_Serializer.md) object
Required: No

## See Also
<a name="API_OutputFormatConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/OutputFormatConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/OutputFormatConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/OutputFormatConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
