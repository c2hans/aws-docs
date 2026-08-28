---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_InputFormatConfiguration.html
---

# InputFormatConfiguration
<a name="API_InputFormatConfiguration"></a>

Specifies the deserializer you want to use to convert the format of the input data. This parameter is required if `Enabled` is set to true.

## Contents
<a name="API_InputFormatConfiguration_Contents"></a>

 ** Deserializer **   <a name="Firehose-Type-InputFormatConfiguration-Deserializer"></a>
Specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or the OpenX JSON SerDe. If both are non-null, the server rejects the request.
Type: [Deserializer](API_Deserializer.md) object
Required: No

## See Also
<a name="API_InputFormatConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/InputFormatConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/InputFormatConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/InputFormatConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
