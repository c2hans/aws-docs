---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/catalog-federation-for-apache-iceberg-tables.html
---

# Catalog federation for Apache Iceberg tables

Catalog federation lets you register **external Iceberg catalogs** as federated catalogs inside the AWS Glue Data Catalog. Once federated, the tables from the external catalog become visible in the AWS Glue Data Catalog alongside native tables, and access from AWS is governed through AWS Lake Formation. Any AWS analytics service or third-party Iceberg client that talks to the AWS Glue Data Catalog (directly or through the AWS Glue Iceberg REST endpoint) can then read those tables — no data movement, no per-consumer connector.

The primary goal is **interoperability**: one metadata plane, one governance surface, many query engines. Your Iceberg tables can live where they were produced (Snowflake, Databricks, Polaris, and so on) and still be reachable from Amazon Athena, Amazon Redshift, Amazon EMR, AWS Glue, and open-source Iceberg clients on other engines. Federation does not carry over the access policies defined in the source catalog, and support varies by source, engine, and table feature; see [Limitations and restrictions](#limitations-and-restrictions) before you rely on it for governed or production data.

![Architecture diagram showing AWS Glue Data Catalog federating to Databricks Unity Catalog, Snowflake Horizon/Polaris, and an open source Iceberg REST catalog, while consumers query Iceberg tables in Amazon S3 through Glue.](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/988bf6c0-5900-4d43-8158-724b70b25371.png)

## Supported source catalogs
<a name="supported-source-catalogs"></a>

You can federate the AWS Glue Data Catalog to the following external catalogs, provided that the table data they catalog is stored in **Amazon S3**:
+ **Snowflake Horizon Catalog** (Snowflake-managed Iceberg tables), and **Snowflake Open Catalog** (managed Apache Polaris), which has its own endpoint and is federated separately.
+ **Apache Polaris** (self-hosted or managed).
+ **Databricks Unity Catalog** (managed). Only tables that Unity Catalog serves as Iceberg can be read: managed Iceberg tables, and Delta tables with Iceberg reads (UniForm) enabled.
+ **Any Apache Iceberg REST catalog** that implements the standard Iceberg REST specification. The Lake Formation documentation covers the Snowflake and Databricks sources in detail, so validate compatibility for Apache Polaris and other Iceberg REST catalogs before you rely on them.

Once registered, each external catalog appears as a **federated catalog** entry alongside the native Glue databases and tables. Query engines resolve tables through the federated catalog and read the underlying Iceberg data files in place from the Amazon S3 locations where the source catalog stored them. Tables whose data is stored outside Amazon S3, such as in Azure or Google Cloud object storage, cannot be read through federation, because Lake Formation vends credentials only for Amazon S3.

## Access is read-only
<a name="access-is-read-only"></a>

Federated Iceberg tables in the AWS Glue Data Catalog are **read-only**. Consumers can `SELECT`, run time-travel and metadata queries, and read snapshots, but they cannot `INSERT`, `UPDATE`, `DELETE`, `MERGE`, alter, or drop federated tables through AWS Glue. Writes must go through the source catalog (Snowflake, Databricks, Polaris, or the target REST catalog). Write attempts fail, often with errors that mention permissions or credentials rather than the read-only catalog, and Lake Formation grants for write operations on federated tables have no effect. Time travel and snapshot reads are limited to the snapshots that the source catalog commits and retains.

The same applies to Iceberg **maintenance operations** (compaction, snapshot expiration, orphan-file removal). Because these operations mutate table state, they must be scheduled and executed against the source catalog and cannot be run through the AWS Glue Data Catalog federation. Table optimizers and Spark maintenance procedures are rejected or fail on federated tables. This is the correct trade-off for interoperability: the source catalog remains the single writer and single owner of maintenance, and the federation surfaces the current metadata to downstream readers on AWS.

## What federation gives you
<a name="what-federation-gives-you"></a>

Once a catalog is federated:
+ **Unified metadata** — federated tables show up in the AWS Glue Data Catalog under the corresponding federated catalog entry, and are visible to Data Catalog APIs, the console, and any AWS service that browses the catalog, within the visibility limits described in [Limitations and restrictions](#limitations-and-restrictions).
+ **Lake Formation-managed access control** — grant SELECT (and column, row, or cell filters) on federated tables to IAM principals through Lake Formation the same way you grant them on native Iceberg tables. The AWS Glue connection behind each federated catalog is registered with Lake Formation together with an IAM role that can read the table data in Amazon S3, and Lake Formation vends temporary credentials from that role to the analytics engine at query time. Lake Formation grants are the only access control that AWS readers get; policies defined in the source catalog don't apply.
+ **AWS Glue Iceberg REST endpoint exposure** — because the AWS Glue Data Catalog exposes its own Iceberg REST endpoint, federated tables are automatically reachable through that endpoint. Iceberg REST-compliant clients that support SigV4 request signing (open-source Apache Spark, PyIceberg, DuckDB, Flink, and so on) can attach to `https://glue.<region>.amazonaws.com/iceberg` and read federated tables using standard Iceberg SQL.

## Supported clients: any Iceberg REST catalog client
<a name="supported-clients-any-iceberg-rest-catalog-client"></a>

Federated tables in the AWS Glue Data Catalog are reachable from **any client that speaks the Iceberg REST catalog protocol**, since the AWS Glue Data Catalog exposes its own Iceberg REST endpoint. The following table summarizes how the AWS-integrated engines and third-party Iceberg engines typically access federated tables and what governance applies to each.

|
|
| **Consumer** | **How it reads federated tables** | **Governance** |
| --- |--- |--- |
| **Amazon Athena** | Standard Athena SQL with three-part naming: `"<federated_catalog_name>"."<db>"."<table>"`. Browse federated catalogs through `information_schema`, because `SHOW` and `DESCRIBE` statements aren't supported for them | AWS Lake Formation grants, including fine-grained (column, row, cell) filters |
| **Amazon Redshift** | Requires an AWS Lake Formation resource link on the federated database in the AWS Glue Data Catalog, then either automount or an external schema over the resource link (see [Client configuration examples](#client-configuration-examples) below) | AWS Lake Formation grants, including fine-grained (column, row, cell) filters |
| **Amazon EMR** (Spark) | Same Spark catalog configuration used for native Iceberg, with the Spark catalog pointed at the federated catalog (see [Client configuration examples](#client-configuration-examples) below) | AWS Lake Formation grants, including fine-grained (column, row, cell) filters when Lake Formation fine-grained access control is enabled for the EMR runtime |
| **AWS Glue for Spark** | AWS Glue 5.1 or later, with the same Spark catalog configuration used for native Iceberg and the Spark catalog pointed at the federated catalog (see [Client configuration examples](#client-configuration-examples) below) | AWS Lake Formation grants, including fine-grained (column, row, cell) filters when Lake Formation fine-grained access control is enabled for the job |
| **Third-party Iceberg engines** (open-source Spark, PyIceberg, DuckDB, Flink, and so on) | Iceberg REST client pointed at the AWS Glue Iceberg REST endpoint | AWS Lake Formation grants; full-table access only, no FGAC (column, row, and cell filters have to be enforced by the query engine, and plain Iceberg REST clients don't have the Lake Formation integration needed to apply them) |

## Client configuration examples
<a name="client-configuration-examples"></a>

Two patterns are commonly used to read federated catalogs:
+ **AWS Glue Iceberg client** (`org.apache.iceberg.aws.glue.GlueCatalog`) — the same GlueCatalog implementation used for native AWS Glue Data Catalog tables. Available on Spark on Amazon EMR and AWS Glue; relies on the AWS SDK auth chain, so no explicit SigV4 configuration is required. The target catalog is set through `glue.id=<AWS_ACCOUNT_ID>:<FEDERATED_CATALOG_NAME>`. Without a Lake Formation mode enabled, this client reads Amazon S3 with the caller's own IAM permissions, so Lake Formation isn't in the data path.
+ **Iceberg REST catalog** — the standard Iceberg REST protocol pointed at the AWS Glue Iceberg REST endpoint `https://glue.<REGION>.amazonaws.com/iceberg`, with SigV4 signing (`rest.signing-name=glue`). Works for any Iceberg REST-compliant client, including PyIceberg, DuckDB, open-source Spark, and Flink. For jobs on AWS Glue and Amazon EMR, use the GlueCatalog pattern instead.

Both patterns yield read-only access to the same federated tables. Replace `<AWS_ACCOUNT_ID>`, `<REGION>`, and `<FEDERATED_CATALOG_NAME>` (or the equivalent placeholders in the PyIceberg example) with your values.

### Apache Spark on Amazon EMR or AWS Glue (GlueCatalog implementation)
<a name="apache-spark-on-amazon-emr-or-aws-glue-gluecatalog-implementation"></a>

Set the Spark catalog's `glue.id` to `<AWS_ACCOUNT_ID>:<FEDERATED_CATALOG_NAME>`, and set `glue.lakeformation-enabled=true` to enable Lake Formation credential vending, so the job reads federated tables with credentials vended by Lake Formation instead of its own Amazon S3 permissions.

```
spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
spark.sql.catalog.polaris_federated=org.apache.iceberg.spark.SparkCatalog
spark.sql.catalog.polaris_federated.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog
spark.sql.catalog.polaris_federated.glue.id=<AWS_ACCOUNT_ID>:<FEDERATED_CATALOG_NAME>
spark.sql.catalog.polaris_federated.glue.account-id=<AWS_ACCOUNT_ID>
spark.sql.catalog.polaris_federated.client.region=<REGION>
spark.sql.catalog.polaris_federated.glue.lakeformation-enabled=true
spark.sql.catalog.polaris_federated.io-impl=org.apache.iceberg.aws.s3.S3FileIO
```

Reference tables in the federated catalog with the three-part `<catalog>.<db>.<table>` name: `spark.sql("SELECT * FROM polaris_federated.<db>.<table>")`.

With `glue.lakeformation-enabled=true`, Lake Formation provides full-table access only: the job's IAM role needs `SELECT` on the entire table, and tables granted only through column, row, or cell filters fail with a Lake Formation permission error. To enforce fine-grained filters, enable the platform's Lake Formation fine-grained access control instead, and omit `glue.lakeformation-enabled`: use the `--enable-lakeformation-fine-grained-access=true` job parameter on AWS Glue 5.1 or later, or `spark.emr-serverless.lakeformation.enabled=true` on Amazon EMR Serverless. The two modes are mutually exclusive.

### Amazon Redshift (Lake Formation resource link)
<a name="amazon-redshift-lake-formation-resource-link"></a>

Amazon Redshift queries a federated catalog through an AWS Lake Formation resource link on the federated database. Two setup steps:

**Step 1 — Create the resource link in the local AWS Glue Data Catalog.** The link's `TargetDatabase.CatalogId` uses the fully qualified federated catalog identifier (`<AWS_ACCOUNT_ID>:<federated_catalog_name>`). In the following example the federated catalog is `polaris_federated`, its database is `weather_db`, and the local resource link is `weather_db_rl`:

```
aws glue create-database \
    --region <REGION> \
    --catalog-id <AWS_ACCOUNT_ID> \
    --database-input '{
        "Name": "weather_db_rl",
        "TargetDatabase": {
            "CatalogId": "<AWS_ACCOUNT_ID>:polaris_federated",
            "DatabaseName": "weather_db",
            "Region": "<REGION>"
        }
    }'
```

**Step 2 — Grant Lake Formation permissions.** As the data lake admin, grant the IAM principal that Redshift uses:
+ `DESCRIBE` on the resource link database (`weather_db_rl`).
+ `SELECT` on the target federated tables (`polaris_federated.weather_db.<table>`), with column, row, or cell filters as needed.

Once the resource link and grants are in place, Redshift can query the tables through automount — `SELECT ... FROM "awsdatacatalog"."weather_db_rl"."<table>"` — or by mounting the resource link as a Redshift external schema with `CREATE EXTERNAL SCHEMA ... FROM DATA CATALOG DATABASE 'weather_db_rl' IAM_ROLE ...`. The resource link is required, because Redshift cannot query the federated catalog directly. Identities that aren't Redshift superusers also need `GRANT USAGE ON DATABASE awsdatacatalog TO "IAMR:<ROLE_NAME>";` before they can query through automount. See [Querying AWS Glue IRC federated catalogs with Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/glue-irc-federated-catalogs.html) for cross-account variants and the full grant flow.

### PyIceberg (Iceberg REST endpoint)
<a name="pyiceberg-iceberg-rest-endpoint"></a>

PyIceberg attaches to the AWS Glue Iceberg REST endpoint with SigV4 signing:

```
from pyiceberg.catalog import load_catalog

region = "<REGION_ID>"
account_id = "<ACCOUNT_ID>"
catalog_name = "<FEDERATED_CATALOG_NAME>"

#setup access to federated rest catalog
rest_catalog = load_catalog(
    catalog_name,
    **{
        "type": "rest",
        "uri": f"https://glue.{region}.amazonaws.com/iceberg",
        "warehouse": f"{account_id}:{catalog_name}",
        "rest.sigv4-enabled": "true",
        "rest.signing-name": "glue",
        "rest.signing-region": region,
    }
)

#list namespaces
print(rest_catalog.list_namespaces())
...
```

The same shape works for any federated catalog — only the value in `warehouse` (or in `glue.id` for the GlueCatalog pattern) changes to match the target federated catalog name.

**Lake Formation permissions: **because a plain Iceberg REST client cannot enforce Lake Formation FGAC, the IAM principal that PyIceberg authenticates as must be granted** **`SELECT` on the **entire** target table in Lake Formation. Column, row, and cell filters cannot be applied through this path: loading a table that the principal can access only through such grants fails with an explicit Lake Formation permission error (`Insufficient Lake Formation permission(s): FULL SELECT or SUPER privileges required on the table`). To restrict which columns or rows a caller sees, route the query through an engine that integrates with Lake Formation (Amazon Athena, Amazon Redshift, Amazon EMR Spark, or AWS Glue Spark).

### Open-source Apache Spark (Iceberg REST endpoint)
<a name="open-source-apache-spark-iceberg-rest-endpoint"></a>

Open-source Apache Spark reads a federated catalog through the same AWS Glue Iceberg REST endpoint used by PyIceberg. This works from any environment that has network access to AWS — a developer laptop, a self-managed cluster, or a container running on Amazon EKS or Amazon ECS. For jobs on AWS Glue or Amazon EMR, use the GlueCatalog configuration shown earlier instead. Launch `pyspark` with the Iceberg Spark runtime and AWS bundle packages, and point a Spark catalog at the endpoint with SigV4 signing:

```
pyspark \
    --packages org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.10.0,org.apache.iceberg:iceberg-aws-bundle:1.10.0 \
    --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions \
    --conf spark.sql.defaultCatalog=polaris_federated \
    --conf spark.sql.catalog.polaris_federated=org.apache.iceberg.spark.SparkCatalog \
    --conf spark.sql.catalog.polaris_federated.type=rest \
    --conf spark.sql.catalog.polaris_federated.uri=https://glue.<REGION>.amazonaws.com/iceberg \
    --conf spark.sql.catalog.polaris_federated.warehouse=<AWS_ACCOUNT_ID>:<FEDERATED_CATALOG_NAME> \
    --conf spark.sql.catalog.polaris_federated.rest.sigv4-enabled=true \
    --conf spark.sql.catalog.polaris_federated.rest.signing-name=glue \
    --conf spark.sql.catalog.polaris_federated.rest.signing-region=<REGION> \
    --conf spark.sql.catalog.polaris_federated.rest.access-config.aws.region=<REGION> \
    --conf spark.sql.catalog.polaris_federated.io-impl=org.apache.iceberg.aws.s3.S3FileIO \
    --conf spark.sql.catalog.polaris_federated.rest-metrics-reporting-enabled=false
```

With `spark.sql.defaultCatalog=polaris_federated`, unqualified queries resolve against the federated catalog. Three-part references also work: `spark.sql("SELECT * FROM polaris_federated.<db>.<table>").show()`.

**Lake Formation permissions**: same constraint as PyIceberg — open-source Spark using the plain Iceberg REST catalog cannot enforce Lake Formation FGAC, so the IAM principal must be granted `SELECT` on the **entire** target table. Column, row, and cell filters cannot be applied through this path, and tables granted only through them fail with a Lake Formation permission error.

For deployment-specific packaging (job parameters on AWS Glue, cluster configuration on Amazon EMR, PyIceberg installation and AWS authentication), see the parent engine chapters: [Amazon EMR catalog configuration](working-with-iceberg-in-amazon-emr-spark.md), [Catalog configuration for Iceberg on AWS Glue Spark](iceberg-glue.md), and [PyIceberg](iceberg-pyiceberg.md).

## When to use catalog federation
<a name="when-to-use-catalog-federation"></a>
+ **Multi-platform lakehouse** — your organization runs Snowflake, Databricks, and AWS analytics side by side. Federate the Snowflake or Databricks catalogs into the AWS Glue Data Catalog to give downstream consumers — AWS analytics services (Amazon Athena, Amazon Redshift, Amazon EMR Spark, AWS Glue Spark) and third-party Iceberg REST clients (open-source Spark, PyIceberg, DuckDB, ..) — a **unified view across catalogs** and **centralized governance** through AWS Lake Formation, without exporting the underlying data. Lake Formation governs the AWS readers only, so re-create any source-side policies there.
+ **Migration and coexistence** — during a phased migration to or from AWS, keep the source catalog authoritative for writes while all readers unify through the AWS Glue Data Catalog and Lake Formation.
+ **Read-side governance** — enforce Lake Formation row and column filters on tables that were produced elsewhere, without changing the producer. Because source-side policies don't carry over, the Lake Formation policies must re-create any protection that the source applies, and queries must run through an engine that enforces them.
+ **Open-engine access** — expose Iceberg tables to open-source engines (PyIceberg, open-source Spark, DuckDB, and so on) through a single AWS Glue Iceberg REST endpoint, regardless of where each table's authoritative catalog lives. These clients get full-table access only.

## Limitations and restrictions
<a name="limitations-and-restrictions"></a>

Behavior varies by source catalog, engine, and version, and it changes as services and clients evolve. Validate the combination you plan to use before you rely on it for governed or production workloads.
+ **Table data must be stored in Amazon S3** — federation reads Iceberg data files in place, and Lake Formation vends credentials only for Amazon S3. Configure the source storage, such as Snowflake external volumes or Databricks storage locations, to use Amazon S3 buckets; tables stored in other object stores cannot be read through federation. The IAM role registered with Lake Formation must be able to read every bucket that holds federated table data, and to decrypt it if it's encrypted with AWS KMS keys. Buckets in other AWS accounts also need bucket policies that allow that role.
+ **Source-side access policies don't carry over** — row filters, column masks, masking policies, and similar controls defined in the source catalog aren't applied when AWS engines or Iceberg REST clients read federated tables, so protected tables can be read in full. Re-create those protections in Lake Formation as data cells filters or LF-Tag grants (LF-Tag policy grants take the plain account ID as the catalog ID). Limit what the federation identity can access in the source catalog, register the federation with a least-privilege IAM role, and don't give readers direct access to the source Amazon S3 locations.
+ **Fine-grained access needs an engine that enforces it** — Athena and Redshift enforce Lake Formation column, row, and cell filters. Spark on AWS Glue and Amazon EMR enforces them only when the platform's Lake Formation fine-grained access control is enabled, and plain Iceberg REST clients need full-table grants. Grants that an engine can't enforce fail with a permission error instead of returning partial data. When you first use fine-grained access with a federated source, validate query results, including column types.
+ **Not every source object is visible or readable** — only tables that the source serves as Iceberg can be read. Other object types, such as native tables, views, and materialized views, are either hidden or listed without being readable. Objects that the federation identity can't access in the source catalog are absent, without an error. Some source-side policy types can hide a table or prevent its schema from being listed, and table listings can be truncated for some sources; query by exact name when a table doesn't appear. Objects with quoted mixed-case or lowercase names can be hidden by the federation's casing rules, and multi-level namespaces aren't supported.
+ **Iceberg feature and type support varies by engine** — engines and client versions differ in their support for Iceberg format version 3, deletion vectors, newer types such as `VARIANT`, time-of-day types, and some combinations of nested types, binary types, and Parquet encodings. Unsupported features usually cause query errors, but some clients can return incorrect results without an error, for example by not applying deletion vectors. Test each table format and data type with every engine you plan to use.
+ **Snapshot history and metadata tables are limited** — time travel reaches only the snapshots that the source commits and retains, and some sources group several changes into one snapshot. Metadata tables aren't available through every path; for example, Spark and Flink can't query them through the AWS Glue Iceberg REST endpoint, which supports single-level namespaces only. Use Athena or the GlueCatalog client for metadata queries.
+ **Client and network requirements** — the AWS Glue Iceberg REST endpoint requires SigV4 signing, and some clients support SigV4 only with long-term access keys. AWS Glue jobs need AWS Glue 5.1 or later to read federated catalogs. When the source S3 buckets are in a different AWS Region from the engine, enable cross-Region access in GlueCatalog clients (`s3.cross-region-access-enabled=true`), and give Amazon EMR Serverless applications VPC access with a NAT gateway.
+ **Federated catalogs are fixed after creation** — each remote catalog can be federated only once per connection, and a federated catalog can't be modified; to change one, delete and re-create it, and then re-apply its Lake Formation grants. If Iceberg REST clients will use the catalog, create it with Lake Formation data lake access enabled. Table metadata is limited to 5 MB per REST API call.
+ **Token lifecycle depends on the authentication method** — with OAuth2, AWS Glue refreshes access tokens itself. With custom token authentication, you create and refresh the token in AWS Secrets Manager, and the federated catalog stops working if the refresh fails, so monitor and alarm on the refresh process.

## References
<a name="references"></a>
+ [Catalog federation to remote Iceberg catalogs](https://docs.aws.amazon.com/lake-formation/latest/dg/catalog-federation.html)
+ [Using AWS Glue with AWS Lake Formation for fine-grained access control](https://docs.aws.amazon.com/glue/latest/dg/security-lf-enable.html)
+ [Using EMR Serverless with AWS Lake Formation for fine-grained access control](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless-lf-enable.html)
+ AWS blog: [Access Databricks Unity Catalog data using catalog federation in the AWS Glue Data Catalog](https://aws.amazon.com/blogs/big-data/access-databricks-unity-catalog-data-using-catalog-federation-in-the-aws-glue-data-catalog/)
+ AWS blog: [Access Snowflake Horizon Catalog data using catalog federation in the AWS Glue Data Catalog](https://aws.amazon.com/blogs/big-data/access-snowflake-horizon-catalog-data-using-catalog-federation-in-the-aws-glue-data-catalog/)
