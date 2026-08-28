---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_InputParallelismUpdate.html
---

# InputParallelismUpdate
<a name="API_InputParallelismUpdate"></a>

For a SQL-based Kinesis Data Analytics application, provides updates to the parallelism count.

## Contents
<a name="API_InputParallelismUpdate_Contents"></a>

 ** CountUpdate **   <a name="APIReference-Type-InputParallelismUpdate-CountUpdate"></a>
The number of in-application streams to create for the specified streaming source.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 64.
Required: Yes

## See Also
<a name="API_InputParallelismUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/InputParallelismUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/InputParallelismUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/InputParallelismUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
