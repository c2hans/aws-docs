---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/userguide/cancel-export-task.html
---

# cancel-export-task
<a name="cancel-export-task"></a>

 The `cancel-export-task` command allows you to cancel an ongoing export task that was started using the `start-export-task` command.

## cancel-export-task syntax
<a name="cancel-export-task-syntax"></a>

```
aws neptune-graph cancel-export-task \
  --task-identifier <taskId> \
  --region <region>
```

## cancel-export-task inputs
<a name="cancel-export-task-inputs"></a>
+  `--task-identifier <taskId>` - The unique identifier of the export task you want to cancel.
+  `--region <region>` - The AWS region where the Neptune Analytics graph is located.

## cancel-export-task output
<a name="cancel-export-task-output"></a>

```
{
    // The unique identifier of the Neptune Analytics graph that was exported
    "graphId": "$GRAPH_ID",

    // The ARN of the IAM role that was used to grant Neptune Analytics the necessary permissions to access the Amazon S3 bucket for the export
    "roleArn": "$arn",

    // The unique identifier of the export task
    "taskId": "$taskId",

    // The current status of the export task,
    // which is one of "SUCCEEDED"/"FAILED" etc.
    "status": "SUCCEEDED",

    // The output format of the exported data, which is "PARQUET"/"CSV".
    "format": "PARQUET",

    // The Amazon S3 location where the exported data was written
    "destination": "$s3-url",

    // The AWS KMS key used for server-side encryption of the exported data in Amazon S3
    "kmsKeyIdentifier": "$kms_key",

    // The type of Parquet file generated, which is "COLUMNAR".
    "parquetType": "COLUMNAR",

    // If there is an error, a reason will be provided.
    "statusReason"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
