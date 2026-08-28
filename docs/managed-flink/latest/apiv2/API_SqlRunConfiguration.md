---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_SqlRunConfiguration.html
---

# SqlRunConfiguration
<a name="API_SqlRunConfiguration"></a>

Describes the starting parameters for a SQL-based Kinesis Data Analytics application.

## Contents
<a name="API_SqlRunConfiguration_Contents"></a>

 ** InputId **   <a name="APIReference-Type-SqlRunConfiguration-InputId"></a>
The input source ID. You can get this ID by calling the [DescribeApplication](API_DescribeApplication.md) operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** InputStartingPositionConfiguration **   <a name="APIReference-Type-SqlRunConfiguration-InputStartingPositionConfiguration"></a>
The point at which you want the application to start processing records from the streaming source.
Type: [InputStartingPositionConfiguration](API_InputStartingPositionConfiguration.md) object
Required: Yes

## See Also
<a name="API_SqlRunConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/SqlRunConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/SqlRunConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/SqlRunConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
