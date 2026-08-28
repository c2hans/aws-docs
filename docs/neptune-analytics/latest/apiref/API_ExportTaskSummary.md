---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ExportTaskSummary.html
---

# ExportTaskSummary
<a name="API_ExportTaskSummary"></a>

Provides details about an export task.

## Contents
<a name="API_ExportTaskSummary_Contents"></a>

 ** destination **   <a name="neptunegraph-Type-ExportTaskSummary-destination"></a>
The Amazon S3 URI of the export task where data will be exported to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** format **   <a name="neptunegraph-Type-ExportTaskSummary-format"></a>
The format of the export task.
Type: String
Valid Values: `PARQUET | CSV`
Required: Yes

 ** graphId **   <a name="neptunegraph-Type-ExportTaskSummary-graphId"></a>
The source graph identifier of the export task.
Type: String
Pattern: `g-[a-z0-9]{10}`
Required: Yes

 ** kmsKeyIdentifier **   <a name="neptunegraph-Type-ExportTaskSummary-kmsKeyIdentifier"></a>
The KMS key identifier of the export task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`
Required: Yes

 ** roleArn **   <a name="neptunegraph-Type-ExportTaskSummary-roleArn"></a>
The ARN of the IAM role that will allow the data to be exported to the destination.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:(role|role/service-role)(/[\w+=,.@-]+)+`
Required: Yes

 ** status **   <a name="neptunegraph-Type-ExportTaskSummary-status"></a>
The current status of the export task.
Type: String
Valid Values: `INITIALIZING | EXPORTING | SUCCEEDED | FAILED | CANCELLING | CANCELLED | DELETED`
Required: Yes

 ** taskId **   <a name="neptunegraph-Type-ExportTaskSummary-taskId"></a>
The unique identifier of the export task.
Type: String
Pattern: `t-[a-z0-9]{10}`
Required: Yes

 ** parquetType **   <a name="neptunegraph-Type-ExportTaskSummary-parquetType"></a>
The parquet type of the export task.
Type: String
Valid Values: `COLUMNAR`
Required: No

 ** statusReason **   <a name="neptunegraph-Type-ExportTaskSummary-statusReason"></a>
The reason that the export task has this status value.
Type: String
Required: No

## See Also
<a name="API_ExportTaskSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/ExportTaskSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/ExportTaskSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/ExportTaskSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for NeptuneAnalyticsAPI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
