---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/handling-write-concurrency.html
---

# Handling write concurrency

Apache Iceberg uses **optimistic concurrency control**: writers don't take a lock before working — they operate against a snapshot they read at the start and defer the concurrency check until they try to commit. At commit time, Iceberg first checks whether any other writer has committed in the meantime. If no one else has, the commit lands and the writer is done. If someone else has, that's where a conflict arises — Iceberg then decides whether the new commit is safe to apply on top of the snapshots that have landed since the writer started.

This section covers what those conflicts are, how Iceberg tries to resolve them automatically, and what your ingestion code needs to do for the cases Iceberg can't resolve on its own. It applies to both **self-managed Iceberg on Amazon S3** and **Amazon S3 Tables** — the concurrency model lives in the Iceberg library, not the hosting option.

## Two types of commit-time conflicts
<a name="two-types-of-commit-time-conflicts"></a>

When a writer commits and finds that the table has moved on from the snapshot it started with, Iceberg classifies the conflict into one of two categories:
+ **Catalog commit conflict (soft).** A newer snapshot exists: the writer started against snapshot X, but at commit time snapshot Y is the latest. Iceberg refreshes the table metadata, re-applies the pending operation on top of snapshot Y, and runs the operation's own validation (none for appends; conflict checks on added, deleted, and delete files for overwrites and rewrites). If validation passes, Iceberg writes a new manifest list and `metadata.json` that reference the writer's existing data files and re-attempts the commit. This is the class of conflict the Iceberg library retries **automatically**.
+ **Data conflict (hard).** The validation in the previous step fails: the two commits touch overlapping data, for example both rewrote the same file, or one deleted rows the other is trying to update. Iceberg cannot safely rebase, the writer **aborts** with a `ValidationException`, and retry logic has to live in your application code.

The likelihood of each conflict type depends on the write operation:

|
|
| **Write operation** | **Catalog commit conflict (automatically retryable)** | **Data conflict (requires application handling)** |
| --- |--- |--- |
| `INSERT` — `AppendFiles` | Possible | Never |
| `UPDATE` / `DELETE` / `MERGE INTO` — `OverwriteFiles` (copy-on-write or merge-on-read) | Possible | Possible |
| Compaction — `RewriteFiles` | Possible | Possible |

`INSERT` writes never produce data conflicts because appends don't overlap with anything already in the table. Update-style writes and compaction can produce either kind, because both can rewrite files that another writer is also touching.

## Handling catalog commit conflicts — table properties
<a name="handling-catalog-commit-conflicts-table-properties"></a>

For catalog commit conflicts, Iceberg's library retries the commit itself — no application code required. You tune the retry behavior with four table properties:

|
|
| **Property** | **Purpose** | **Default** |
| --- |--- |--- |
| `commit.retry.num-retries` | How many times to retry a commit before giving up | 4 |
| `commit.retry.min-wait-ms` | Minimum wait between retries (starts the backoff) | 100 |
| `commit.retry.max-wait-ms` | Upper bound on the backoff between retries | 60000 |
| `commit.retry.total-timeout-ms` | Overall time budget across all retries | 1800000 (30 min) |

The defaults are conservative — appropriate for low-contention workloads. For higher-contention workloads, raise the retry count and adjust the backoff to match the write cadence.

**Frequent concurrent writes** (for example, streaming ingestion into a shared table):

```
tbl_properties = {
    'commit.retry.num-retries':       '10',
    'commit.retry.min-wait-ms':       '100',
    'commit.retry.max-wait-ms':       '10000',
    'commit.retry.total-timeout-ms':  '1800000'
}
```

With these values the backoff sequence is roughly 0.1, 0.2, 0.4, 0.8, 1.6, 3.2, 6.4, 10, 10, 10 seconds, about 45 seconds of waiting in total, so the 30-minute `total-timeout-ms` never binds and is left at its default. Lowering `max-wait-ms` matters more than raising the retry count for streaming writers: with commits arriving every few seconds, waiting up to 60 seconds between retries adds latency long after the conflicting commit has landed. If retries still run out, the writer raises `CommitFailedException`; see the next section for handling it in the application.

Engines that honor these properties on the write path — including **Apache Spark** and **PyIceberg** — automatically rebuild metadata against the latest snapshot and re-attempt the commit up to the configured retry budget. If you're writing from an engine that doesn't consult these properties, you'll need to implement equivalent retry logic in the application.

## Choose the isolation level for row-level writes
<a name="choose-the-isolation-level-for-row-level-writes"></a>

`UPDATE`, `DELETE`, and `MERGE INTO` validate at commit time that concurrent writes did not change their result. The strictness is a table property, set per operation: `write.update.isolation-level`, `write.delete.isolation-level`, and `write.merge.isolation-level`, each `serializable` (default) or `snapshot`.

Under `serializable`, a concurrent append of rows that could match the operation's filter is a data conflict and fails the writer with `ValidationException`, even though the append itself never conflicts. Under `snapshot`, only changes to the files the operation itself rewrites are conflicts; concurrent appends are ignored and their rows are picked up by the next run. For idempotent, key-based upserts, `snapshot` removes most of the conflicts that would otherwise reach the retry logic below:

`ALTER TABLE db.events SET TBLPROPERTIES ('write.merge.isolation-level' = 'snapshot');`

Keep `serializable` when an operation must see every row that exists at commit time, for example a `DELETE` that has to remove all rows matching a predicate. Isolation level does not affect compaction; conflicts between `rewrite_data_files` and ingestion are handled with `where` predicates and partial progress, described below.

## Handling data conflicts — application-level retry
<a name="handling-data-conflicts-application-level-retry"></a>

For data conflicts, Iceberg **aborts** the write and raises a `ValidationException`. The same application-level retry also covers the case where a catalog commit conflict outlives the library's own retry budget and surfaces as `CommitFailedException`. There's no safe generic retry — the table's state has changed, so the correct action depends on the workload (upsert stream? merge? backfill?). The best practice is to wrap the write in application-level retry logic that catches the exception, re-reads the source (so the retry works against the current source state), and re-issues the write, with **exponential backoff plus jitter** — that is, waiting progressively longer before each retry (e.g. 1s, 2s, 4s, 8s) so you don't hammer a contended table, plus a small random offset on each wait so concurrent writers that failed together don't all retry at the same instant and collide again.

Example — Spark Structured Streaming batch that does `MERGE INTO` against an Iceberg table and retries on `ValidationException`:

```
while attempt < max_retries:
    try:
        spark.sql(f"""
            MERGE INTO {DATABASE}.{TABLE} AS t
            USING global_temp.{view_name} AS i
            ON t.value = i.value
            WHEN MATCHED THEN
              UPDATE SET
                t.timestamp = i.timestamp,
                t.value     = i.value
            WHEN NOT MATCHED THEN
              INSERT (timestamp, value)
              VALUES (i.timestamp, i.value)
        """)
        print(f"[SUCCESS] Batch {batchId} processed successfully")
        return
    except Py4JJavaError as e:
        if is_validation_exception(e.java_exception):
            attempt += 1
            if attempt < max_retries:
                delay = backoff(attempt)
                print(f"[RETRY] Batch {batchId} failed with ValidationException. "
                      f"Retrying in {delay} seconds. Attempt {attempt}/{max_retries}")
                time.sleep(delay)
            else:
                print(f"[FAILED] Batch {batchId} failed after {max_retries} attempts")
                raise
        else:
            raise
```

The key details:
+ Catch `ValidationException` (a data conflict) and `CommitFailedException` (a catalog commit conflict that exhausted the `commit.retry.*` budget); in PySpark both surface through `Py4JJavaError`. Both mean the write was not committed and the table is intact, so re-reading the source and re-issuing the write is safe. Do not retry `CommitStateUnknownException` blindly: the commit may have succeeded, so reload the table and check whether your snapshot landed before deciding. Other exceptions should propagate.
+ Use exponential backoff with jitter — for example, base delay doubling each attempt with 0–25% random jitter — to smooth out retry storms between concurrent writers.
+ Bound the retries with a maximum count so the job fails cleanly instead of looping forever.

## Concurrency with compaction
<a name="concurrency-with-compaction"></a>

Compaction is one of the most common sources of concurrent-write conflicts because it rewrites data files that ingestion may also be touching. Where retry logic lives depends on which maintenance execution option runs compaction — but on the ingestion side, retry handling is always the customer's responsibility.

|
|
| **Maintenance execution option** | **Compaction-side retries** | **Ingestion-side retries** |
| --- |--- |--- |
| [**Amazon S3 Tables built-in maintenance**](maintenance-in-amazon-s3-tables.md) | Automatic. S3 Tables retries on conflict — no configuration required. | Customer-owned. Tune `commit.retry.*` on the table for soft conflicts and implement client-side retry (catch `ValidationException`) for data conflicts. |
| [**AWS Glue Data Catalog table optimizer**](maintenance-with-the-aws-glue-data-catalog-table-optimizer.md) | Automatic, with a limit. AWS Glue retries at the next scheduled run, but after four consecutive failed runs it suspends the optimizer; failed runs do not appear in CloudWatch metrics. Check `ListTableOptimizerRuns` or the optimizer history in the console, remove the source of contention, and re-enable the optimizer. | Customer-owned. Tune `commit.retry.*` on the table for soft conflicts and implement client-side retry (catch `ValidationException`) for data conflicts. |
| [**Self-managed maintenance with Apache Spark procedures**](self-managed-maintenance.md) | Customer-owned. Tune `commit.retry.*` on the table for soft conflicts, and implement client-side retry around the `rewrite_data_files` invocation for data conflicts; for long runs that compete with active writers, enable `partial-progress.enabled` so that a data conflict fails one file group, not the whole run (at the cost of one snapshot per file group). | Customer-owned. Tune `commit.retry.*` on the table for soft conflicts and implement client-side retry (catch `ValidationException`) for data conflicts. |

In every case, ingestion pipelines should both **tune **`commit.retry.*` for soft conflicts and **implement application-level retry logic** for data conflicts — client-side retry is required even when the compaction side is fully managed. The managed options do not expose `partial-progress` or `where`; if their compaction keeps conflicting with ingestion, the escalation path below ends in self-managed compaction, where these options are available.

## High-frequency streaming plus compaction — avoiding livelock
<a name="high-frequency-streaming-plus-compaction-avoiding-livelock"></a>

This scenario applies to streams that update or delete rows (upserts, `MERGE INTO`, deletes), because those writes rewrite or attach deletes to the same files compaction is rewriting. Append-only ingestion, however frequent, only causes catalog commit conflicts with compaction, which Iceberg retries on its own; for append-only tables, tune `commit.retry.*` and leave managed compaction enabled. When row-level streaming writes commits at sub-minute intervals, compaction jobs — whether managed (Amazon S3 Tables built-in maintenance or the AWS Glue Data Catalog table optimizer) or self-managed — can end up hitting data conflicts on every attempt and never making forward progress. Follow this escalation path:

1. **Monitor compaction executions.** Track compaction runs where failures are actually recorded: `ListTableOptimizerRuns` or the optimizer history in the AWS Glue console for the AWS Glue Data Catalog table optimizer, `aws s3tables get-table-maintenance-job-status` for Amazon S3 Tables, and job logs plus the procedure's output counts (`rewritten_data_files_count`, `failed_data_files_count`) for self-managed compaction. CloudWatch metrics for the managed options report the throughput of successful runs only and cannot show a failing or suspended optimizer. If compaction is completing on schedule, no action is needed. For the AWS Glue Data Catalog table optimizer, also check whether it has been suspended after repeated failures; a suspended optimizer does not resume on its own and must be re-enabled after you fix the contention.

1. **If compaction is failing, reduce the ingestion commit rate first.** Larger micro-batches or longer trigger intervals on the ingestion side reduce the number of overlapping commits compaction has to contend with — for example, moving from a 30-second Spark Structured Streaming trigger to 2 minutes, or increasing the Amazon Data Firehose buffer interval. Keep monitoring the compaction success rate after the change; this is often enough on its own.

1. **If reducing the ingestion rate isn't enough (or isn't acceptable for the workload), disable managed compaction and take it self-managed.** Turn off the built-in compaction path — see [Turning it off (fall back to Spark procedures)](maintenance-in-amazon-s3-tables.md) for Amazon S3 Tables, or [Turning it off (fall back to Spark procedures)](maintenance-with-the-aws-glue-data-catalog-table-optimizer.md) for the AWS Glue Data Catalog table optimizer — and then run self-managed compaction with these two techniques, applied in order:

   1. **Target non-active partitions.** Configure the self-managed compaction job to process only partitions that ingestion isn't currently modifying — for example, run `rewrite_data_files` with a `where` predicate that excludes the current time window. This reduces conflicts to the soft (catalog commit) class, which Iceberg retries automatically and resolves quickly. See the `where` parameter in [Self-managed maintenance](self-managed-maintenance.md) (**Invocation and parameters** section).

   1. **Enable partial progress.** Set `partial-progress.enabled=true` so that each file group is committed as soon as it is rewritten: a conflict then costs one file group, not the whole run. Lower `max-file-group-size-bytes` (for example, 10-20 GB) to keep each commit's exposure to concurrent writes short. On merge-on-read tables, keep `use-starting-sequence-number=true` (the default) so that delete files written during the compaction still apply to the compacted files.

      The trade-offs: every file group adds a snapshot and a `metadata.json` version (up to `partial-progress.max-commits` per run, default 10), readers can see a partially compacted table between commits, and a run reports success even if some groups failed, so watch `failed_data_files_count` in the procedure output. Use it for long-running compaction that competes with active writers; leave it off for short runs or when the result must appear in a single snapshot. Check for more details in [Self-managed maintenance](self-managed-maintenance.md) (**Invocation and parameters** section).

   1. **Serialize compaction with ingestion.** If targeting non-active partitions still isn't enough (for example, late-arriving data means every partition is "active"), coordinate the two jobs so they don't run concurrently. A common pattern is **stop ingestion → run compaction → restart ingestion** on a scheduled window. This is heavier operationally but eliminates the contention.

## For more detail
<a name="for-more-detail"></a>

For a walk-through of the conflict-detection algorithm and a full end-to-end Python retry example, see the AWS Big Data blog post [Manage concurrent write conflicts in Apache Iceberg on the AWS Glue Data Catalog](https://aws.amazon.com/blogs/big-data/manage-concurrent-write-conflicts-in-apache-iceberg-on-the-aws-glue-data-catalog/).
