---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/tracking-failed-documents.html
---

# Tracking and remediating failed documents
<a name="tracking-failed-documents"></a>

During a backfill, Reindex-from-Snapshot (RFS) retries most document errors automatically. A document counts as failed only when the error is terminal, either because the error is non-retryable or because RFS exhausted the retry limit. You can list which documents failed, determine why they failed, and remediate them.

## Where failures are recorded
<a name="failed-documents-where-recorded"></a>

Migration Assistant records terminal document failures in two places:
+ The failed document stream is a durable inventory of terminal failures that RFS writes to Amazon S3 as gzip-compressed NDJSON. Each record identifies the document and captures enough detail to diagnose or resubmit it without returning to the source cluster.
+ The RFS worker logs contain lower-level diagnostic detail. The workers log each failed bulk request, including the target index, failed item count, root cause, and the request and response bodies.

**Warning**
The failed document stream is off by default. If you do not enable it before running the backfill, a failed migration leaves no durable inventory of which documents did not reach the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection, and you are limited to the worker logs. Enable it as described in [Enabling the failed document stream](#enable-failed-document-stream) before you start the backfill.

## Enabling the failed document stream
<a name="enable-failed-document-stream"></a>

Setting an Amazon S3 bucket in the migration’s `documentBackfillConfig` enables the stream. There is no separate enable flag, and the stream does not fall back to the deployment’s default bucket, so you must name a bucket explicitly. Complete these steps from a Migration Console shell before you start the backfill.

1. Choose a bucket. Either use the deployment’s default bucket, `migrations-default-<ACCOUNT_ID>-<STAGE>-<REGION>`, which Migration Assistant can already write to. The following command lists the default bucket for every Migration Assistant deployment in the account, so choose the one that matches your stage and Region:

   ```
   aws s3 ls | grep migrations-default
   ```

   Or create a bucket in the same AWS account and Region:

   ```
   aws s3 mb s3://<BUCKET_NAME> --region <REGION>
   ```

1. Open the workflow configuration:

   ```
   workflow configure edit
   ```

1. Add the bucket to each migration’s `documentBackfillConfig`, then save:

   ```
   snapshotMigrationConfigs:
     - ...
       perSnapshotConfig:
         snap1:
           - documentBackfillConfig:
               failedDocumentStreamS3Bucket: <BUCKET_NAME>
   ```

1. Submit the workflow:

   ```
   workflow submit
   ```

1. After the backfill starts, confirm the stream location:

   ```
   console failed-document-stream location
   ```

**Note**
For a bucket in another AWS account or encrypted with an AWS Key Management Service (AWS KMS) customer managed key, also grant the Migration Assistant pod role access in the bucket policy or key policy. By default, uninstalling Migration Assistant empties and deletes the default bucket, so copy any records you want to keep first.

The following table lists the options that configure the failed document stream.

| Option | Default | Description |
| --- | --- | --- |
|  `failedDocumentStreamS3Bucket`  | None | The bucket that stores the records. Setting it enables the stream. |
|  `failedDocumentStreamS3Prefix`  |  `rfs-failed-document-stream/`  | The key prefix. Each run has a session root at `<prefix>session=<uid>/`. Individual objects are nested under that root by target index and worker. |
|  `failedDocumentStreamS3Region`  | Resolved from the configuration | The AWS Region of the bucket. Ignored when no bucket is set. |
|  `failedDocumentStreamS3Endpoint`  | Resolved from the configuration | An endpoint override, for example, LocalStack. Ignored when no bucket is set. |
|  `failedDocumentStreamMaxBufferBytes`  |  `67108864` (64 MiB) | The maximum number of in-memory bytes per index before rotating to a new object. |

In the following paths, replace the values in angle brackets with your own values.

The console reports the session root:

```
s3://<amzn-s3-demo-bucket>/<prefix>session=<migration-uid>/
```

The individual gzip-compressed NDJSON objects are stored beneath that root:

```
s3://<amzn-s3-demo-bucket>/<prefix>session=<migration-uid>/index=<target-index>/worker=<worker-id>/failed-document-stream-<time-stamp>-<sequence>.ndjson.gz
```

## Checking whether any documents failed
<a name="check-failed-documents"></a>

After the backfill finishes, run the following commands from a Migration Console shell:

```
workflow status
```

```
console failed-document-stream count
```

A count greater than `0` means that documents failed. `workflow status` can report the backfill as completed even when documents failed. Check the count instead of relying on the workflow status alone.

**Note**
If the stream is configured but cannot be read, for example, because of missing Amazon S3 permissions, the console command fails rather than reporting no failures.

## Inspecting failed documents
<a name="inspect-failed-documents"></a>

Run the following commands from a Migration Console shell. When more than one migration exists, add `--migration <name>` to select one:

```
# S3 location for the current session
console failed-document-stream location

# Count of distinct failed documents
console failed-document-stream count

# List failures as tab-separated rows without a header
# (columns: timestamp, targetIndex, documentId, failureClass, failureType)
console failed-document-stream list --limit 100

# Full records as JSON, including the captured request item and the OpenSearch response
console --json failed-document-stream list --limit 100
```

The following table lists the fields included in each record.

| Field | Description |
| --- | --- |
|  `targetIndex`  | The index the document was being written to. |
|  `documentId`  | The document’s ID. |
|  `failureClass`  | How the document reached the stream: `NON_RETRYABLE` for errors that are never retried, or `RETRYABLE_EXHAUSTED` when retries were exhausted. |
|  `failureType`  | The OpenSearch error type, for example `mapper_parsing_exception`. |
|  `timestamp`  | When RFS recorded the failure. |
|  `sessionId`  | The session that owns the record. It matches the migration UID in the stream location. |
|  `workerId`  | The RFS worker that produced the failure. |
|  `workItemId`  | The shard work item that produced the failure. |
|  `requestItem`  | The captured bulk request item. When the original source document is available, that source content is stored under `document` so you can diagnose or resubmit without going back to the source cluster. |
|  `responseItem`  | The OpenSearch bulk response item, including the error type and reason. |

A document can appear in the stream more than once, so the console deduplicates records on read by `targetIndex` and `documentId`. Counts therefore reflect the number of distinct failed documents.

## Reading the RFS worker logs
<a name="failed-documents-worker-logs"></a>

For lower-level detail, inspect the RFS worker logs. Each failed bulk request produces an error entry with the target index, failed item count, root cause, and the OpenSearch response body, plus a structured entry under the `FailedRequestsLogger` category containing the request and response bodies.

**Note**
RFS deliberately omits individual failed-item bodies from the general worker log to avoid leaking document data. RFS writes the full request body only to the dedicated `FailedRequestsLogger` category.

## Remediating failures
<a name="remediate-failed-documents"></a>

Use the failed document stream to identify the main cause before retrying any documents.

### Identifying the failure type
<a name="failed-documents-failure-type"></a>

Group the failures returned by `list` by `failureType` to identify the cause, and use `failureClass` to determine whether the error was non-retryable or became terminal only after retries were exhausted. The following table lists common failure types and the recommended remediation for each.

|  `failureType`  | Typical cause | Remediation |
| --- | --- | --- |
|  `mapper_parsing_exception`  | Document doesn’t match the target index mapping. | Fix the target mapping or add or correct a transform, then resubmit. |
|  `version_conflict_engine_exception`  | A newer version of the document already exists at the target. | Usually safe to leave. Resubmit only if the source version should win. |
|  `es_rejected_execution_exception` (often with `failureClass=RETRYABLE_EXHAUSTED`) | Target was overloaded or briefly unavailable. | Address target capacity, then resubmit the affected documents. |

### Resubmitting the failed documents
<a name="resubmit-failed-documents"></a>

The `console --json failed-document-stream list` output contains each failed document’s `requestItem`, so you can correct the root cause, such as a mapping or a transform, and then resubmit those documents to the target. When the original source document was available, `requestItem` holds that source content. However, `requestItem` might not hold the exact transformed payload that RFS sent on the failed write.

## Deleting failed document records
<a name="delete-failed-document-records"></a>

The Migration Console doesn’t provide a command to delete failed document records. To delete the current session’s records, remove the session location that `console failed-document-stream location` reports. Replace the values in angle brackets with your own values:

```
aws s3 rm --recursive \
  s3://<amzn-s3-demo-bucket>/<prefix>session=<migration-uid>/
```

**Warning**
This deletion is irreversible. You can’t recover the failed document records after you remove them.

For additional troubleshooting, see [Troubleshooting](troubleshooting.md).
