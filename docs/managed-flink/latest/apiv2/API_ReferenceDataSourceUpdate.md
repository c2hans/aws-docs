---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ReferenceDataSourceUpdate.html
---

# ReferenceDataSourceUpdate
<a name="API_ReferenceDataSourceUpdate"></a>

When you update a reference data source configuration for a SQL-based Kinesis Data Analytics application, this object provides all the updated values (such as the source bucket name and object key name), the in-application table name that is created, and updated mapping information that maps the data in the Amazon S3 object to the in-application reference table that is created.

## Contents
<a name="API_ReferenceDataSourceUpdate_Contents"></a>

 ** ReferenceId **   <a name="APIReference-Type-ReferenceDataSourceUpdate-ReferenceId"></a>
The ID of the reference data source that is being updated. You can use the [DescribeApplication](API_DescribeApplication.md) operation to get this value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** ReferenceSchemaUpdate **   <a name="APIReference-Type-ReferenceDataSourceUpdate-ReferenceSchemaUpdate"></a>
Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.
Type: [SourceSchema](API_SourceSchema.md) object
Required: No

 ** S3ReferenceDataSourceUpdate **   <a name="APIReference-Type-ReferenceDataSourceUpdate-S3ReferenceDataSourceUpdate"></a>
Describes the S3 bucket name, object key name, and IAM role that Kinesis Data Analytics can assume to read the Amazon S3 object on your behalf and populate the in-application reference table.
Type: [S3ReferenceDataSourceUpdate](API_S3ReferenceDataSourceUpdate.md) object
Required: No

 ** TableNameUpdate **   <a name="APIReference-Type-ReferenceDataSourceUpdate-TableNameUpdate"></a>
The in-application table name that is created by this update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

## See Also
<a name="API_ReferenceDataSourceUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ReferenceDataSourceUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ReferenceDataSourceUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ReferenceDataSourceUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
