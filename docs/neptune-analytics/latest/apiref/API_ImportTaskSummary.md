---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ImportTaskSummary.html
---

# ImportTaskSummary
<a name="API_ImportTaskSummary"></a>

Details about an import task.

## Contents
<a name="API_ImportTaskSummary_Contents"></a>

 ** roleArn **   <a name="neptunegraph-Type-ImportTaskSummary-roleArn"></a>
The ARN of the IAM role that will allow access to the data that is to be imported.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:(role|role/service-role)(/[\w+=,.@-]+)+`
Required: Yes

 ** source **   <a name="neptunegraph-Type-ImportTaskSummary-source"></a>
A URL identifying to the location of the data to be imported. This can be an Amazon S3 path, or can point to a Neptune database endpoint or snapshot
Type: String
Required: Yes

 ** status **   <a name="neptunegraph-Type-ImportTaskSummary-status"></a>
Status of the import task.
Type: String
Valid Values: `INITIALIZING | EXPORTING | ANALYZING_DATA | IMPORTING | REPROVISIONING | ROLLING_BACK | SUCCEEDED | FAILED | CANCELLING | CANCELLED | DELETED`
Required: Yes

 ** taskId **   <a name="neptunegraph-Type-ImportTaskSummary-taskId"></a>
The unique identifier of the import task.
Type: String
Pattern: `t-[a-z0-9]{10}`
Required: Yes

 ** format **   <a name="neptunegraph-Type-ImportTaskSummary-format"></a>
Specifies the format of S3 data to be imported. Valid values are `CSV`, which identifies the [Gremlin CSV format](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html) or `OPENCYPHER`, which identies the [openCypher load format](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-opencypher.html).
Type: String
Valid Values: `CSV | OPEN_CYPHER | PARQUET | NTRIPLES`
Required: No

 ** graphId **   <a name="neptunegraph-Type-ImportTaskSummary-graphId"></a>
The unique identifier of the Neptune Analytics graph.
Type: String
Pattern: `g-[a-z0-9]{10}`
Required: No

 ** parquetType **   <a name="neptunegraph-Type-ImportTaskSummary-parquetType"></a>
The parquet type of the import task.
Type: String
Valid Values: `COLUMNAR`
Required: No

## See Also
<a name="API_ImportTaskSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/ImportTaskSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/ImportTaskSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/ImportTaskSummary)
