---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ApplicationCodeConfiguration.html
---

# ApplicationCodeConfiguration
<a name="API_ApplicationCodeConfiguration"></a>

Describes code configuration for an application.

## Contents
<a name="API_ApplicationCodeConfiguration_Contents"></a>

 ** CodeContentType **   <a name="APIReference-Type-ApplicationCodeConfiguration-CodeContentType"></a>
Specifies whether the code content is in text or zip format.
Type: String
Valid Values: `PLAINTEXT | ZIPFILE`
Required: Yes

 ** CodeContent **   <a name="APIReference-Type-ApplicationCodeConfiguration-CodeContent"></a>
The location and type of the application code.
Type: [CodeContent](API_CodeContent.md) object
Required: No

## See Also
<a name="API_ApplicationCodeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ApplicationCodeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ApplicationCodeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ApplicationCodeConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
