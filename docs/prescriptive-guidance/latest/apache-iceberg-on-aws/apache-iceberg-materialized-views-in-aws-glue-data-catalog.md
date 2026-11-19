---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/apache-iceberg-materialized-views-in-aws-glue-data-catalog.html
---

# Apache Iceberg materialized views in AWS Glue Data Catalog

An **Iceberg materialized view (MV)** is a managed Iceberg table in the AWS Glue Data Catalog that stores the pre-computed result of a SQL query. Unlike a standard Data Catalog view (which is evaluated on every read), a materialized view physically stores the results and is refreshed either on a schedule or on demand — incrementally when the source tables and the view definition support it. Queries that match (or partially match) the MV definition are automatically rewritten by supported engines to read from the MV instead of the base tables.

Because the MV result is persisted as a **regular Iceberg table**, it can be consumed by **any Iceberg-compatible client **— AWS analytics services (Amazon Athena, Amazon Redshift, Amazon EMR for Spark, AWS Glue for Spark) as well as third-party Iceberg engines (open-source Apache Spark, PyIceberg, DuckDB, Apache Flink) — through the AWS Glue Data Catalog or the AWS Glue Iceberg REST endpoint. The MV's underlying Iceberg table can live in either of the two hosting options:
+ **Self-managed Iceberg on Amazon S3** — the MV is a regular Iceberg table in your S3 bucket, registered in the AWS Glue Data Catalog. You control its S3 location and schedule its maintenance (compaction, snapshot expiration, orphan-file cleanup).
+ **Amazon S3 Tables **— the MV is created inside your S3 table bucket and inherits Amazon S3 Tables automatic table maintenance.

## Typical use cases
<a name="typical-use-cases"></a>
+ **Medallion gold layer** — pre-aggregate a silver-layer Iceberg table into a business-facing gold-layer MV. Managed refresh handles change detection and incremental updates for you, so anyone who knows SQL can maintain a gold layer without a team building an orchestration pipeline around it.
+ **Dashboard and BI acceleration **— back your BI dashboards (Amazon Quick Sight, Tableau, Looker, and so on — through whichever Iceberg query engine your BI tool connects to) with a MV so each dashboard load reads pre-computed results instead of scanning the full source tables.
+ **Repeated queries** — compute a heavy aggregation once and let many downstream consumers reuse it via the MV.

## Managed refresh vs building your own pipeline
<a name="managed-refresh-vs-building-your-own-pipeline"></a>

Producing and maintaining a gold-layer Iceberg table without a materialized view typically means owning an orchestrator (such as Apache Airflow), custom change-detection logic to find what's new in the sources, a MERGE job that applies those changes to the gold table, and state / retry / backfill logic for when things go wrong. With an Iceberg MV, that shape collapses to a single SQL statement — AWS Glue runs the change detection, the incremental refresh, and the recovery on your behalf.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/20e6c7a0-d504-462e-8b9f-9a658830a949.png)

## Engine and version requirements
<a name="engine-and-version-requirements"></a>

**Creating and manually refreshing** materialized views is an AWS-specific capability. The `CREATE MATERIALIZED VIEW` and client-side `REFRESH MATERIALIZED VIEW` statements require the AWS Glue Data Catalog integration and Iceberg extensions that ship with AWS-managed Spark — open-source Apache Spark (including OSS clusters that talk to the AWS Glue Iceberg REST endpoint) does not include these extensions and cannot create or refresh Iceberg MVs. The AWS-managed Spark environments that provide the required version (3.5.6 or later) to create/refresh Glue Iceberg Materialized Views are:

|
|
| **Engine** | **Minimum version** |
| --- |--- |
| AWS Glue for Spark | 5.1\+ |
| Amazon EMR for Spark | 7.12.0\+ |
| Amazon Athena for Apache Spark | Spark 3.5.6\+ |

**Server-side on-demand or scheduled refresh** (`SCHEDULE REFRESH` on the MV, or `start-materialized-view-refresh-task-run`) is another AWS-managed capability — AWS Glue executes the refresh on your behalf, and you don't need to bring your own compatible Spark. See [Refreshing a materialized view](#refreshing-a-materialized-view) below for the full server-side / client-side breakdown.

**Consuming (querying) materialized views** works everywhere. Because a MV is a regular Iceberg table underneath, Amazon Athena SQL (Trino) and any other Iceberg-compatible reader — including third-party engines and open-source Apache Spark — can query it directly by name. What Athena SQL and third-party engines cannot do is **create** or **refresh** MVs; those statements require the AWS-managed Spark environments listed above.

**Automatic query rewrite** — silently redirecting a query issued against the base tables to a matching MV, controlled via settings like `spark.sql.optimizer.answerQueriesWithMVs.enabled` — is also an AWS-specific optimization that requires the AWS-managed Spark environments and versions listed above. Consumers on other engines still benefit from a MV, but only when they explicitly reference it in the `FROM` clause of the query.

## Iceberg format version
<a name="iceberg-format-version"></a>

Materialized views are created in Iceberg format version 2 (V2) in both hosting options (self-managed Iceberg on Amazon S3 and Amazon S3 Tables).

## Creating a materialized view
<a name="creating-a-materialized-view"></a>

Use `CREATE MATERIALIZED VIEW <catalog>.<db>.<mv_name> AS <SELECT ...>` from any of the supported Spark engines. You must use three-part naming (`<catalog>.<db>.<table>`**) **for both the MV target and every table referenced inside the** **`SELECT` — including the catalog qualifier, even when a default catalog is set on the Spark session. Iceberg MV creation resolves every source table to a specific AWS Glue Data Catalog entry at creation time, so unqualified or two-part references are rejected.

The three subsections below show the DDL for the two same-target patterns and for a cross-catalog case (MV target in one hosting option, source table in the other).

### Spark syntax for self-managed Iceberg on Amazon S3
<a name="spark-syntax-for-self-managed-iceberg-on-amazon-s3"></a>

Using an Iceberg catalog named `iceberg_catalog` registered against the AWS Glue Data Catalog (see [Catalog configuration on Amazon EMR](working-with-iceberg-in-amazon-emr-spark.md) or [on AWS Glue](iceberg-glue.md)):

```
spark.sql("""
    CREATE MATERIALIZED VIEW iceberg_catalog.evs.charging_sessions_customers_summary
    AS
    SELECT
        customer_id,
        sum(duration_minutes) AS overall_duration_charging_sessions_minutes
    FROM iceberg_catalog.evs.charging_sessions
    GROUP BY customer_id
""")
```

### Spark syntax for Amazon S3 Tables
<a name="spark-syntax-for-amazon-s3-tables"></a>

Using an S3 Tables catalog named `s3_tables_catalog` (see [Catalog configuration on Amazon EMR](working-with-iceberg-in-amazon-emr-spark.md) or [on AWS Glue](iceberg-glue.md)):

```
spark.sql("""
    CREATE MATERIALIZED VIEW s3_tables_catalog.evs.charging_sessions_customers_summary
    AS
    SELECT
        customer_id,
        sum(duration_minutes) AS overall_duration_charging_sessions_minutes
    FROM s3_tables_catalog.evs.charging_sessions
    GROUP BY customer_id
""")
```

### Spark syntax for a cross-catalog MV (S3 Tables target reading from self-managed Iceberg)
<a name="spark-syntax-for-a-cross-catalog-mv-s3-tables-target-reading-from-self-managed-iceberg"></a>

The three-part naming rule makes cross-catalog MVs straightforward: the MV target and the source tables can live in different Spark catalogs, as long as each table is referenced with its own catalog qualifier. The following example creates the MV inside the S3 Tables catalog (`s3_tables_catalog.evs.charging_sessions_customers_summary`) and reads the source data from the self-managed Iceberg catalog (`iceberg_catalog.evs.charging_sessions`):

```
spark.sql("""
    CREATE MATERIALIZED VIEW s3_tables_catalog.evs.charging_sessions_customers_summary
    AS
    SELECT
        customer_id,
        sum(duration_minutes) AS overall_duration_charging_sessions_minutes
    FROM iceberg_catalog.evs.charging_sessions
    GROUP BY customer_id
""")
```

Both catalogs must be configured in the same Spark session — see [Catalog configuration on Amazon EMR](working-with-iceberg-in-amazon-emr-spark.md) or [on AWS Glue](iceberg-glue.md) for the Spark properties. The rule applies in both directions: you can equally create the MV in `iceberg_catalog` and read from `s3_tables_catalog`.

## Refreshing a materialized view
<a name="refreshing-a-materialized-view"></a>

There are two ways to refresh an MV, and they differ by **who runs the compute**.

### Server-side compute (Data Catalog runs the refresh)
<a name="server-side-compute-data-catalog-runs-the-refresh"></a>

The AWS Glue Data Catalog can run the refresh for you on Data Catalog-managed compute — no cluster or job on your side. Two options:
+ **Automatic** — attach a schedule directly in the DDL at create time:

  ```
  spark.sql("""
      CREATE MATERIALIZED VIEW s3_tables_catalog.evs.charging_sessions_customers_summary
      SCHEDULE REFRESH EVERY 1 HOUR
      AS
      SELECT ...
  """)
  ```

  Or attach one later with `ALTER MATERIALIZED VIEW`:

  ```
  spark.sql("""
      ALTER MATERIALIZED VIEW s3_tables_catalog.evs.charging_sessions_customers_summary
      ADD SCHEDULE REFRESH EVERY 1 HOUR
  """)
  ```

  The **minimum automatic refresh interval is one hour**. For use cases that need more frequent updates, drive refreshes from your orchestration through client-side `REFRESH MATERIALIZED VIEW` or server-side on-demand `start-materialized-view-refresh-task-run` instead.
+ **On demand** — call the AWS CLI (or the equivalent Glue API) to trigger a one-off refresh:

  ```
  aws glue start-materialized-view-refresh-task-run \
      --catalog-id <aws_account_id> \
      --database-name evs \
      --table-name charging_sessions_customers_summary
  ```

  For an MV in an S3 Tables catalog, use the S3 Tables catalog ID form instead: `--catalog-id <aws_account_id>:s3tablescatalog/<table-bucket-name>`.

### Client-side compute (Spark runs the refresh)
<a name="client-side-compute-spark-runs-the-refresh"></a>

Run the refresh from your own Spark session on Amazon EMR, AWS Glue, or Athena for Spark:

```
spark.sql("REFRESH MATERIALIZED VIEW iceberg_catalog.evs.charging_sessions_customers_summary")
```

Use this when you want the refresh to run on your existing cluster (for example, right after upstream ETL steps in the same job, or on Spark configuration your team already owns and monitors).

AWS Glue applies incremental refresh when the MV's SQL and the source tables satisfy the incremental eligibility rules; otherwise the refresh falls back to a full recompute. The eligible shape is a single `SELECT`-`FROM`-`WHERE`-`GROUP BY`-`HAVING` block with only `INNER JOIN`s, and it cannot use set operations, subqueries, window functions, or the `DISTINCT` keyword in the `SELECT` or in an aggregate. See the [Data Catalog materialized view considerations and limitations](https://docs.aws.amazon.com/glue/latest/dg/materialized-views.html#materialized-views-considerations-limitations) for the exact SQL clauses that support incremental refresh.

## Automatic query rewrite
<a name="automatic-query-rewrite"></a>

When a supported Spark engine (AWS Glue 5.1\+, Amazon EMR 7.12.0\+, or Athena for Spark) encounters a query whose logical plan can be satisfied by an existing MV, the engine rewrites the plan to read from the MV instead of scanning the base tables. This is transparent — application SQL doesn't change, and the engine falls back to the base tables when no matching MV exists.

Because the rewrite is plan-based, MVs benefit workloads that repeat similar aggregations (dashboards, reports, gold-layer transforms). See [Introducing Apache Iceberg materialized views in AWS Glue Data Catalog](https://aws.amazon.com/blogs/big-data/introducing-apache-iceberg-materialized-views-in-aws-glue-data-catalog/) for a walkthrough that uses `EXPLAIN` to show how the optimizer rewrites a query plan to leverage a matching MV.

## Monitoring MV refresh operations
<a name="monitoring-mv-refresh-operations"></a>

Server-side refresh activity is observable through standard AWS operational tooling:
+ **List refresh job runs through the AWS APIs** — enumerate historical refresh task runs and inspect their status, duration, and outcome from your own tooling.
+ **Amazon CloudWatch metrics** — MV refresh jobs emit metrics that you can graph, alarm on, or aggregate across MVs.
+ **Amazon CloudWatch Logs **— AWS Glue writes refresh job execution logs to CloudWatch Logs, so you can inspect the actual output of each run to debug failures or slow refreshes.
+ **Amazon EventBridge** — configure EventBridge rules on MV refresh events to trigger downstream automation, such as sending notifications, invoking an AWS Lambda function, or kicking off a dependent job.

For the exact API names, metric names, log group formats, and EventBridge event patterns, see [Materialized views (AWS Lake Formation)](https://docs.aws.amazon.com/lake-formation/latest/dg/materialized-views.html).

## System-managed materialized views
<a name="system-managed-materialized-views"></a>

Starting with **AWS Glue 6.0**, you can create a **system-managed** MV, where only AWS Glue can write the MV's data and definition — no other engine or principal can modify it (not another query engine, not a direct `UpdateTable` call, and not a direct write to the underlying Iceberg table). AWS Glue stores system-managed MVs **only in Amazon S3 Tables** (general purpose S3 buckets are not supported).

Enable the capability with the Spark session property `spark.sql.mv.managed.enabled=true` (defaults to `false` in AWS Glue 6.0), then create the MV with the `MANAGED` keyword:

```
spark.sql("""
    CREATE MANAGED MATERIALIZED VIEW s3_tables_catalog.analytics.customer_summary
    AS
    SELECT ...
""")
```

AWS Glue performs the materialization itself, so the `CREATE MANAGED MATERIALIZED VIEW` statement blocks until the managed create completes. You can still run `REFRESH` (compute is delegated to AWS Glue), change the refresh schedule and table properties, and drop the MV — but **schema evolution is not supported**; to change the SQL definition, drop and recreate the MV.

## Considerations and limitations
<a name="considerations-and-limitations"></a>

For the full list of considerations — including which SQL constructs support incremental refresh, restrictions on nested MVs, permission and Lake Formation requirements, and pricing details — see [Data Catalog materialized view considerations and limitations](https://docs.aws.amazon.com/glue/latest/dg/materialized-views.html#materialized-views-considerations-limitations) and [Materialized views (AWS Lake Formation)](https://docs.aws.amazon.com/lake-formation/latest/dg/materialized-views.html).

Additional notes specific to hosting options:
+ **Self-managed Iceberg on Amazon S3 **— You must maintain MV files using your usual table maintenance. Run compaction and snapshot expiration on the MV table the same way you would on any other self-managed Iceberg table — either through Spark procedures or the [AWS Glue Data Catalog table optimizer](maintenance-with-the-aws-glue-data-catalog-table-optimizer.md).
+ **Amazon S3 Tables** — MV maintenance is included in the automatic S3 Tables maintenance (compaction, snapshot expiration, orphan-file removal). No extra action is required.
