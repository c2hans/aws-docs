---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/publishing-indices-s3-tables.html
---

# Publishing indices to Amazon S3 Tables

With Amazon OpenSearch Service catalog publishing, you can keep aged log and trace data in your own data lake. You don't have to build an export pipeline. You publish indices from an Optimized engine domain into Apache Iceberg tables in Amazon S3 Tables, in your AWS account. You can query that aged data with your own engines. Recent data stays searchable on the domain.
+ **No conversion** – The Optimized engine already stores each index as Apache Parquet, so a publish copies files instead of re-encoding documents.
+ **Readable anywhere** – The tables use the Iceberg table format v3. You can query them with DuckDB, Apache Spark on Amazon EMR Serverless, or any Iceberg v3-compatible engine, using your own IAM permissions, with no OpenSearch component involved.
+ **Recent data stays searchable** – Recent data stays on the domain. An Index State Management (ISM) policy publishes each aged generation to the table, deletes it from the domain after the table commit succeeds, and removes it from the table when its retention ends.
+ **The domain doesn't read the tables back** – Searches and queries on the domain cover only the data still on the domain.

## Prerequisites
<a name="publishing-indices-s3-tables-prerequisites"></a>

Catalog publishing has the following prerequisites:
+ **Version** – OpenSearch 3.9 or later.
+ **Engine mode** – The domain must use the Optimized engine.
+ **Encryption at rest** – Must be enabled, as on every Optimized domain.
+ **Domain name** – Must map to a valid S3 Tables namespace. For more information about namespace derivation, see [Namespace and catalog name](#publishing-indices-s3-tables-namespace).
+ **IAM** – The principal that enables catalog publishing needs the required S3 Tables permissions. For more information about these permissions, see [IAM permissions to enable catalog publishing](#publishing-indices-s3-tables-iam-enable).
+ **Fine-grained access control** – If the domain uses fine-grained access control, non-admin users need catalog permissions. For more information about these permissions, see [Fine-grained access control](#publishing-indices-s3-tables-fgac).

**Note**
To encrypt the tables with your own key, use a customer managed AWS KMS key. For more information about the required key policy, see [KMS key policy](#publishing-indices-s3-tables-kms-policy).

## Requirements and considerations
<a name="publishing-indices-s3-tables-considerations"></a>

Review the following requirements and considerations before you enable catalog publishing:
+ **One-way setting** – After you enable catalog publishing, you can't disable it. You also can't change the domain's encryption at rest options or the tables' KMS key.
+ **Append-only data** – You can bind and publish only append-only indices, meaning data stream backing indices and indices with `index.append_only.enabled: true`. Field changes must be compatible additions. The engine refuses type conflicts.
+ **Table bucket** – OpenSearch Service uses one table bucket named `opensearch` per account and Region, created the first time you enable the feature and shared by all your domains. If a table bucket with that name already exists and OpenSearch Service didn't create it, enabling fails.
+ **Table ownership** – OpenSearch Service manages the tables. You can read them and grant read access to others, but you can't write to them directly.
+ **Tables outlive the domain** – Deleting the domain doesn't delete its tables.
+ **Erasure** – Removing an index from a table (the API or `delete_from_catalog`) removes it from the current table snapshot. Older snapshots (time travel) still return it until S3 Tables snapshot expiry runs, 120 hours by default.
+ **Compaction** – OpenSearch Service turns S3 Tables compaction off for these tables. Snapshot expiry and unreferenced-file removal still run.

### Namespace and catalog name
<a name="publishing-indices-s3-tables-namespace"></a>

Each domain publishes into its own namespace in the `opensearch` table bucket.
+ **Derivation** – The namespace is the domain name in lowercase, with hyphens replaced by underscores. If the result starts with `aws` or ends with `_`, it's wrapped in `0`. For example, `my-logs` becomes `my_logs` and `aws-logs` becomes `0aws_logs0`.
+ **Catalog name** – The namespace is also the catalog name used in the `_catalog` APIs.

## Pricing
<a name="publishing-indices-s3-tables-pricing"></a>

There's no additional OpenSearch Service charge for catalog publishing. Amazon S3 Tables charges apply for the tables' storage, requests, and maintenance. Tables keep billing until you drop them, including after you delete the domain. If you use a customer managed key, AWS KMS charges apply. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/).

## Control plane: enabling catalog publishing
<a name="publishing-indices-s3-tables-control-plane"></a>

You can enable catalog publishing when you create a domain, or later on an existing Optimized domain. The `CatalogOptions` status is `Processing` while it's applied, then `Active`.

### IAM permissions to enable catalog publishing
<a name="publishing-indices-s3-tables-iam-enable"></a>

OpenSearch Service creates the table bucket and updates its policy with the credentials of the principal that calls `CreateDomain` or `UpdateDomainConfig`. In addition to `es:CreateDomain` or `es:UpdateDomainConfig`, that principal needs additional S3 Tables permissions.

The following policy grants the required S3 Tables permissions:

```json
{
  "Effect": "Allow",
  "Action": [
    "s3tables:CreateTableBucket",
    "s3tables:TagResource",
    "s3tables:ListTagsForResource",
    "s3tables:GetTableBucketPolicy",
    "s3tables:PutTableBucketPolicy"
  ],
  "Resource": "arn:aws:s3tables:us-east-1:111122223333:bucket/opensearch"
}
```

### Encrypting the tables with a customer managed key
<a name="publishing-indices-s3-tables-cmk"></a>

To encrypt the domain's tables with your own key, set `EncryptionConfiguration` with `Enabled: true` and a `KmsKeyArn` (see the update example in [Enabling catalog publishing (AWS CLI)](#publishing-indices-s3-tables-cli)). The key must be a customer managed key in the domain's Region. You can't change the key after catalog publishing is enabled.

### KMS key policy
<a name="publishing-indices-s3-tables-kms-policy"></a>

Add the following three statements to the key policy, and keep your existing statements, such as key administration. They grant OpenSearch Service and S3 Tables maintenance only what the tables need. The OpenSearch Service grant is scoped to your account, and its data-key actions are scoped to the `opensearch` table bucket:

```json
{
  "Sid": "OpenSearchCatalogDescribeKey",
  "Effect": "Allow",
  "Principal": { "Service": "es.amazonaws.com" },
  "Action": "kms:DescribeKey",
  "Resource": "*",
  "Condition": {
    "StringEquals": { "aws:SourceAccount": "111122223333" }
  }
},
{
  "Sid": "OpenSearchCatalogDataKeys",
  "Effect": "Allow",
  "Principal": { "Service": "es.amazonaws.com" },
  "Action": [ "kms:GenerateDataKey", "kms:Decrypt" ],
  "Resource": "*",
  "Condition": {
    "StringEquals": { "aws:SourceAccount": "111122223333" },
    "StringLike": { "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3tables:us-east-1:111122223333:bucket/opensearch/*" }
  }
},
{
  "Sid": "S3TablesMaintenance",
  "Effect": "Allow",
  "Principal": { "Service": "maintenance.s3tables.amazonaws.com" },
  "Action": [ "kms:GenerateDataKey", "kms:Decrypt" ],
  "Resource": "*",
  "Condition": {
    "StringLike": { "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3tables:us-east-1:111122223333:bucket/opensearch/*" }
  }
}
```

The following table describes the purpose of each statement.

| Statement | Purpose |
| --- | --- |
| OpenSearchCatalogDescribeKey | S3 Tables checks the key when OpenSearch Service creates a table. DescribeKey carries no encryption context, so this statement can't take the bucket condition. |
| OpenSearchCatalogDataKeys | Lets OpenSearch Service write and read the tables' data and metadata files. |
| S3TablesMaintenance | Lets S3 Tables maintenance (snapshot expiry and unreferenced-file removal) use the key for the domain's tables. |

The service principal `es.amazonaws.com` is the OpenSearch Service principal.

Note the following about the key policy:
+ **Limiting the key to specific domains** – Add `"aws:SourceArn": "arn:aws:es:<region>:<account-id>:domain/<domain-name>"` under `StringEquals` in both OpenSearch Service statements.
+ **Using the same key for encryption at rest** – The domain's at-rest statement is separate and still needed.
+ **Not needed** – `kms:Encrypt`, `kms:ReEncrypt*`, and `kms:CreateGrant`.

### Enabling catalog publishing (console)
<a name="publishing-indices-s3-tables-console"></a>

While you create the domain, choose the Optimized engine. Then, under **Catalog publishing**, choose **Enable catalog publishing**, and optionally choose a customer managed KMS key. For an existing domain, choose **Actions**, **Edit cluster configuration**.

### Enabling catalog publishing (AWS CLI)
<a name="publishing-indices-s3-tables-cli"></a>

The following AWS CLI command creates an Optimized domain with catalog publishing enabled:

```bash
aws opensearch create-domain \
  --domain-name my-logs \
  --engine-version OpenSearch_3.9 \
  --engine-mode OPTIMIZED \
  --use-case OBSERVABILITY \
  --cluster-config InstanceType=or2.large.search,InstanceCount=3 \
  --ebs-options EBSEnabled=true,VolumeType=gp3,VolumeSize=100 \
  --node-to-node-encryption-options Enabled=true \
  --encryption-at-rest-options Enabled=true \
  --domain-endpoint-options EnforceHTTPS=true,TLSSecurityPolicy=Policy-Min-TLS-1-2-2019-07 \
  --catalog-options '{"Enabled":true,"Catalog":{"ServiceManagedS3Tables":{}}}' \
  --region us-east-1
```

The following command enables catalog publishing on an existing Optimized domain and encrypts the tables with a customer managed key:

```bash
aws opensearch update-domain-config \
  --domain-name my-logs \
  --catalog-options '{"Enabled":true,"Catalog":{"ServiceManagedS3Tables":{"EncryptionConfiguration":{"Enabled":true,"KmsKeyArn":"arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"}}}}' \
  --region us-east-1
```

To check the setting, run the following command:

```bash
aws opensearch describe-domain --domain-name my-logs --query 'DomainStatus.CatalogOptions'
{ "Enabled": true, "Catalog": { "ServiceManagedS3Tables": {} } }
```

The `CatalogOptions` status (`Processing` or `Active`) appears on the domain config, not the domain status. To see it, run the following command:

```bash
aws opensearch describe-domain-config --domain-name my-logs --query 'DomainConfig.CatalogOptions'
{ "Options": { "Enabled": true, "Catalog": { "ServiceManagedS3Tables": {} } },
  "Status": { "State": "Active" } }
```

The `State` field shows `Processing` while the change is applied, then `Active`.

For more information about these commands, see the [*AWS CLI Command Reference*](https://docs.aws.amazon.com/cli/latest/reference/opensearch/index.html).

### Example – Configuration API request
<a name="publishing-indices-s3-tables-api"></a>

The following request creates an Optimized domain with catalog publishing enabled and the tables encrypted with a customer managed key:

```json
POST https://es.us-east-1.amazonaws.com/2021-01-01/opensearch/domain
{
  "DomainName": "my-logs",
  "EngineVersion": "OpenSearch_3.9",
  "EngineMode": "OPTIMIZED",
  "UseCase": "OBSERVABILITY",
  "ClusterConfig": { "InstanceType": "or2.large.search", "InstanceCount": 3 },
  "EBSOptions": { "EBSEnabled": true, "VolumeType": "gp3", "VolumeSize": 100 },
  "EncryptionAtRestOptions": { "Enabled": true },
  "NodeToNodeEncryptionOptions": { "Enabled": true },
  "DomainEndpointOptions": { "EnforceHTTPS": true, "TLSSecurityPolicy": "Policy-Min-TLS-1-2-2019-07" },
  "CatalogOptions": {
    "Enabled": true,
    "Catalog": {
      "ServiceManagedS3Tables": {
        "EncryptionConfiguration": {
          "Enabled": true,
          "KmsKeyArn": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
        }
      }
    }
  }
}
```

`UpdateDomainConfig` accepts the same `CatalogOptions` block, including with `DryRun`. A dry run only checks that the `opensearch` table bucket name is available.

The `CatalogOptions` request member, its data types, and the errors it can return are described in the [*Amazon OpenSearch Service API Reference*](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/Welcome.html). The member appears on the `CreateDomain`, `UpdateDomainConfig`, `DescribeDomain`, `DescribeDomains`, and `DescribeDomainConfig` pages.

## Security best practices
<a name="publishing-indices-s3-tables-security"></a>

Follow these practices when you enable catalog publishing:
+ **Scope IAM permissions** – Grant only the minimum actions shown in the permissions examples, and scope them to the `opensearch` table bucket.
+ **Limit the KMS key** – Restrict the key to specific domains by adding an `aws:SourceArn` condition to the key policy statements.
+ **Keep encryption at rest enabled** – Encryption at rest is required, and it protects the data the domain publishes to the tables.

## Data plane: binding, publishing, and managing tables
<a name="publishing-indices-s3-tables-data-plane"></a>

These REST APIs run on the domain endpoint. In the following examples, the domain is `my-logs`, so the catalog is `my_logs`.

### Binding indices to a table
<a name="publishing-indices-s3-tables-binding"></a>

Bind indices to a table with index settings, usually in an index template, so that every new backing index of a data stream publishes into the same table. In the following example, replace `web-logs` and `web_logs` with your own index pattern and table name:

```json
PUT _index_template/web-logs
{
  "index_patterns": ["web-logs*"],
  "data_stream": {},
  "template": {
    "settings": {
      "index.append_only.enabled": true,
      "index.catalog.table": "web_logs",
      "index.catalog.strict_mapping": true
    }
  }
}
```

The following table describes the binding settings.

| Setting | Description | Default |
| --- | --- | --- |
| index.catalog.table | The Iceberg table the index publishes to (lowercase letters, digits, and \_). | None |
| index.catalog.name | The catalog to publish to. | The domain's catalog |
| index.catalog.strict\_mapping | Rejects mapping changes that would conflict with the table's schema at mapping time, instead of at publish time. | false |
| index.catalog.time\_field | Root-level date or date\_nanos field used for the time-range partition. Set at index creation. | The data stream's timestamp field, then @timestamp |
| index.catalog.timestamp\_epoch | Groups files into hour, day, month, or year time ranges. Set at index creation. | One range per index |
| index.append\_only.enabled | Makes the index append-only. Required for a binding. | false |

### Publishing indices
<a name="publishing-indices-s3-tables-publishing"></a>

The following request publishes one index and waits for it to finish:

```json
POST _catalog/my_logs/web_logs/.ds-web-logs-000001/_publish?wait_for_completion=true
```

The following is a sample response:

```json
{
  "publish" : {
    "publish_id" : "_FGfjw-JSaW_7GHyWhUffw",
    "catalog" : "my_logs",
    "table" : "web_logs",
    "indices" : [ ".ds-web-logs-000001" ],
    "state" : "SUCCESS",
    "duration_in_millis" : 1002,
    "shards" : { "total" : 1, "successful" : 1, "failed" : 0 },
    "files_added" : 1,
    "files_removed" : 0,
    "files_kept" : 0,
    "table_snapshot_id" : 536706988902634369
  }
}
```
+ **Table creation** – The first publish into a table creates it.
+ **Several indices** – Use a comma-separated list or a pattern, such as `.ds-web-logs-*`. A pattern must start with `.ds-` to match a data stream's hidden backing indices.
+ **Idempotent** – Publishing again is incremental. The engine keeps files that are already published (`files_kept`), adds only new files, and commits no new snapshot for an unchanged index.
+ **Data streams** – The API doesn't accept a data stream name. Name the backing indices, or publish with ISM.

### Checking publish status
<a name="publishing-indices-s3-tables-status"></a>

```json
GET _catalog/my_logs/web_logs/_status
```

The following is a sample response:

```json
{
  "publishes" : [ ],
  "finished" : [ {
      "publish_id" : "_FGfjw-JSaW_7GHyWhUffw", "state" : "SUCCESS", "duration_in_millis" : 1002,
      "shards" : { "total" : 1, "successful" : 1, "failed" : 0 },
      "files_added" : 1, "files_removed" : 0, "files_kept" : 0,
      "table_snapshot_id" : 536706988902634369 } ]
}
```

`publishes` lists running publishes and `finished` lists completed ones. You can scope the request to a catalog (`_catalog/my_logs/_status`) or to indices (`_catalog/my_logs/web_logs/<indices>/_status`).

### Canceling a publish
<a name="publishing-indices-s3-tables-canceling"></a>

To cancel a running publish, use the following request:

```json
DELETE _catalog/my_logs/web_logs/.ds-web-logs-000001/_publish
```

After all of a publish's shards have reported, you can no longer cancel the publish while its table commit is being finalized.

### Listing tables and their indices
<a name="publishing-indices-s3-tables-listing"></a>

```json
GET _catalog/my_logs/tables
{ "tables" : [ { "namespace" : "my_logs", "table" : "web_logs" } ], "total" : 1 }
```

```json
GET _catalog/my_logs/web_logs/indices
{
  "namespace" : "my_logs",
  "table" : "web_logs",
  "indices" : [ {
      "index" : ".ds-web-logs-000001",
      "index_uuid" : "110110lQP6FIhZTgWICp3oTSBWmA",
      "in_cluster" : true,
      "index_created_version" : "3.9.0",
      "index_size_bytes" : 7090244 } ]
}
```

`in_cluster` is `true` while the domain still holds the index, and `false` after ISM deletes the domain copy.

### Getting catalog and table statistics
<a name="publishing-indices-s3-tables-stats"></a>

```json
GET _catalog/my_logs/web_logs/_stats
```

The following is a sample response (trimmed):

```json
{
  "catalog" : "my_logs", "table" : "web_logs", "exists" : true,
  "current" : { "snapshot_id" : 536706988902634369, "data_files" : 1, "delete_files" : 0,
                "records" : 100000, "size_in_bytes" : 2895570 },
  "history" : { "snapshots" : 1 },
  "publishes" : { "total" : 1, "success" : 1, "partial" : 0, "indices" : 1, "records_added" : 100000 }
}
```

`GET _catalog/_stats` returns domain-wide publish counters, and `GET _catalog/my_logs/_stats` returns a catalog's.

### Removing an index from a table
<a name="publishing-indices-s3-tables-removing"></a>

The following request removes one index from a table. The index on the domain isn't affected:

```json
DELETE _catalog/my_logs/web_logs/.ds-web-logs-000002
{
  "indices" : [ {
      "index" : ".ds-web-logs-000002",
      "index_uuid" : "1111002EZgqejrRuursj7nxzWDRA",
      "files_removed" : 1,
      "table_snapshot_id" : 6144041650491398977,
      "already_deleted" : false } ]
}
```
+ **One index per request** – A list, a wildcard, or `_all` returns an error.
+ **Repeating it is safe** – The response then has `"already_deleted": true`.
+ **Erasure** – See the erasure note in [Requirements and considerations](#publishing-indices-s3-tables-considerations).

### Dropping a table
<a name="publishing-indices-s3-tables-dropping"></a>

After you remove every index from a table, you can drop it:

```json
DELETE _catalog/my_logs/web_logs
```

Dropping a table that still holds indices fails. Drop your tables to stop S3 Tables charges.

## ISM: automating publishing as a cold tier
<a name="publishing-indices-s3-tables-ism"></a>

Use Index State Management to publish each generation once it reaches a certain age, delete it from the domain, and later remove it from the table. ISM runs these actions with the permissions of the user who created the policy (see [Fine-grained access control](#publishing-indices-s3-tables-fgac)). `publish_to_catalog` and `delete_from_catalog` are supported ISM operations on Optimized domains with OpenSearch 3.9 or later. For more information about ISM, see [Index State Management](https://opensearch.org/docs/latest/im-plugin/ism/index/) in the OpenSearch documentation.

### publish\_to\_catalog parameters
<a name="publishing-indices-s3-tables-ism-publish"></a>

| Parameter | Required | Description |
| --- | --- | --- |
| table | Yes | The table to publish into. |
| catalog | No | The catalog. Defaults to the domain's catalog. If you provide it, it can't be blank. |
| delete\_index | No (default false) | Deletes the index from the domain after the publish succeeds. |

With `delete_index: true`, the engine deletes the index from the domain only after every shard has published and the table snapshot has committed. The action refuses a generation that is still the data stream's write index. If a publish fails, the index stays on the domain and ISM retries the action.

### delete\_from\_catalog parameters
<a name="publishing-indices-s3-tables-ism-delete"></a>

| Parameter | Required | Description |
| --- | --- | --- |
| catalog, table | No (together) | Normally omitted: OpenSearch Service uses the table the index was published to. Specify both only for an index whose publish location wasn't recorded. |

This action removes the index from the table's current snapshot.

### Sample policy
<a name="publishing-indices-s3-tables-ism-policy"></a>

To set up a cold tier for a data stream, create the index template, then the ISM policy, then the data stream. Create the policy before the data stream: `ism_template` attaches only to indices created after the policy exists, including the first backing index.

**To set up a cold tier with a sample policy**

1. **Create the index template.** Use the template in [Binding indices to a table](#publishing-indices-s3-tables-binding). It creates `web-logs` as a data stream bound to the `web_logs` table.

1. **Create the ISM policy.** The following policy keeps data hot for 7 days and warm until 30 days. At 30 days, it publishes the generation to the `web_logs` table and deletes it from the domain. At 300 days, it removes the generation from the table.

   ```json
   PUT _plugins/_ism/policies/web-logs-lifecycle
   {
     "policy": {
       "description": "Hot 7d, warm to 30d, publish and delete from the domain at 30d, remove from the table at 300d.",
       "default_state": "hot",
       "ism_template": [{ "index_patterns": ["web-logs*"], "priority": 100 }],
       "states": [
         { "name": "hot",
           "actions": [{ "rollover": { "min_index_age": "1d", "min_primary_shard_size": "30gb" } }],
           "transitions": [{ "state_name": "warm", "conditions": { "min_index_age": "7d" } }] },
         { "name": "warm",
           "actions": [{ "warm_migration": {} }],
           "transitions": [{ "state_name": "cold", "conditions": { "min_index_age": "30d" } }] },
         { "name": "cold",
           "actions": [
             { "read_only": {} },
             { "publish_to_catalog": { "table": "web_logs", "delete_index": true },
               "retry": { "count": 3, "backoff": "exponential", "delay": "10m" } } ],
           "transitions": [{ "state_name": "expired", "conditions": { "min_index_age": "300d" } }] },
         { "name": "expired",
           "actions": [{ "delete_from_catalog": {} }],
           "transitions": [] }
       ]
     }
   }
   ```
   + **Data streams** – `ism_template` matches the data stream name (`web-logs*`), so the policy attaches to each new backing index.
   + **No force merge** – You don't need `force_merge` before `publish_to_catalog`.
   + **Parameter names** – The option is `delete_index`. The engine rejects a policy that uses `delete_hot_copy`, or that leaves out `table`.

1. **Create the data stream and ingest.**

   ```json
   PUT _data_stream/web-logs
   POST web-logs/_doc
   { "@timestamp": "2026-11-22T00:00:00.000Z", "service": { "name": "cart" }, "log": { "level": "INFO" },
     "http": { "status_code": 200 }, "latency_ms": 31, "message": "GET /api/cart/items 200 31ms" }
   ```

   Indexing into `web-logs` also creates the data stream if it doesn't exist yet.

1. **Check that the policy is attached.**

   ```json
   GET _plugins/_ism/explain/web-logs
   ```

   Each backing index (`.ds-web-logs-000001`, and so on) is listed with `"policy_id": "web-logs-lifecycle"`.

### Using a rollover alias instead of a data stream
<a name="publishing-indices-s3-tables-ism-rollover"></a>

The steps are the same as the preceding ones, with the following changes.

**To use a rollover alias instead of a data stream**

1. **Create the index template.** As in the preceding step 1, but without `"data_stream": {}`, with `index_patterns` set to `web-logs-*` so that it matches the rollover indices (`web-logs-000001`, and later indices) but not the `web-logs` alias, and with the rollover alias:

   ```json
   PUT _index_template/web-logs
   {
     "index_patterns": ["web-logs-*"],
     "template": {
       "settings": {
         "index.append_only.enabled": true,
         "index.catalog.table": "web_logs",
         "index.catalog.strict_mapping": true,
         "plugins.index_state_management.rollover_alias": "web-logs"
       }
     }
   }
   ```

1. **Create the ISM policy.** Use the same policy as in the preceding step 2, with `"index_patterns": ["web-logs-*"]` in `ism_template`.

1. **Create the first index with the write alias, then ingest through the alias.**

   ```json
   PUT web-logs-000001
   { "aliases": { "web-logs": { "is_write_index": true } } }
   POST web-logs/_doc
   { "@timestamp": "2026-11-22T00:00:00.000Z", "service": { "name": "cart" }, "message": "GET /api/cart/items 200 31ms" }
   ```

1. **Check that the policy is attached.** Use `GET _plugins/_ism/explain/web-logs-*`. Each index is listed with `"policy_id": "web-logs-lifecycle"`.

`publish_to_catalog` with `delete_index: true` refuses an index that still holds the write alias, so it runs only on indices that have rolled over.

### Monitoring the policy
<a name="publishing-indices-s3-tables-ism-monitoring"></a>

While the index is on the domain, use `GET _plugins/_ism/explain/web-logs`. The `publish_to_catalog` action reports the following steps:

| Step | Message |
| --- | --- |
| attempt\_catalog\_publish | Successfully started catalog publish [index=.ds-web-logs-000001] |
| wait\_for\_catalog\_publish | Catalog publish completed [index=.ds-web-logs-000001] (with table\_snapshot\_id) |
| attempt\_delete\_index | Deleted the index; the generation continues as a published index [index=.ds-web-logs-000001] |

ISM runs one step per job run, so allow several job runs between a rollover and the publish.

**Pending delete\_from\_catalog** – After the engine deletes the domain copy, a generation stays in the table until `delete_from_catalog` runs. `GET _plugins/_ism/explain?type=_published` lists these generations with their current state. A generation drops out of the list once the engine removes it from the table. In `GET _catalog/my_logs/web_logs/indices`, these generations show `"in_cluster": false`.

The Explain API documents the `_published` index type.

## Fine-grained access control
<a name="publishing-indices-s3-tables-fgac"></a>

If the domain uses fine-grained access control, the following permissions authorize the catalog APIs and ISM actions, grouped by task.

### Publishing
<a name="publishing-indices-s3-tables-fgac-publishing"></a>

| Permission | Type | Grants | Included in |
| --- | --- | --- | --- |
| cluster:admin/opensearch/catalog/publish | Cluster | Publish indices (\_publish), and the ISM publish\_to\_catalog action. | — |
| indices:data/read/opensearch/catalog/publish | Index | Checked on every index a publish names, so users can publish only indices they can read. | read |
| cluster:admin/opensearch/catalog/publish/status | Cluster | GET \_catalog/.../\_status. Also polled by publish\_to\_catalog. | — |
| cluster:admin/opensearch/catalog/published/get | Cluster | Read published generations. ISM uses it to manage \_published indices. | — |
| cluster:admin/opensearch/catalog/publish/abort | Cluster | Cancel any running publish. | — |

### Table management
<a name="publishing-indices-s3-tables-fgac-table"></a>

| Permission | Type | Grants | Included in |
| --- | --- | --- | --- |
| cluster:admin/opensearch/catalog/table/list | Cluster | GET \_catalog/<catalog>/tables | — |
| cluster:admin/opensearch/catalog/table/get | Cluster | GET \_catalog/<catalog>/<table>/indices | — |
| indices:admin/opensearch/catalog/list | Index | Checked on every index recorded in the table before .../indices responds. The request is denied unless all of them are allowed. | manage, indices:admin/\* |
| indices:admin/opensearch/catalog/delete | Index | Remove an index from a table, and the ISM delete\_from\_catalog action. Checked on the index name, so it also works after the index is deleted from the domain. | manage, indices:admin/\* |
| cluster:admin/opensearch/catalog/table/delete | Cluster | Drop a table. | — |
| cluster:monitor/opensearch/catalog/stats | Cluster | GET \_catalog/\_stats | cluster\_monitor |
| cluster:monitor/opensearch/catalog/stats/table | Cluster | GET \_catalog/<catalog>[/<table>]/\_stats | cluster\_monitor |

### ISM permissions
<a name="publishing-indices-s3-tables-fgac-ism"></a>

ISM runs `publish_to_catalog` and `delete_from_catalog`, including the domain-copy delete, with the permissions of the user who created the policy. In addition to the usual ISM permissions, that user needs the following:
+ **Cluster** – `cluster:admin/opensearch/catalog/publish`, `.../publish/status`, and `.../published/get`.
+ **Index, on the managed index patterns** – `read`, `indices:admin/opensearch/catalog/delete`, and `indices:admin/delete` when the policy uses `delete_index: true`.

## Querying the tables
<a name="publishing-indices-s3-tables-querying"></a>

### Permissions to read the tables
<a name="publishing-indices-s3-tables-query-permissions"></a>

Attach the following policy to the IAM role or user that runs the query, such as an EMR Serverless job execution role or the credentials DuckDB uses. Replace `<region>` and `<account-id>`. Add the `kms:Decrypt` statement only if the tables use a customer managed key, and replace `<key-id>` with your key ID:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ReadOpenSearchTables",
      "Effect": "Allow",
      "Action": [
        "s3tables:GetTableBucket",
        "s3tables:ListNamespaces",
        "s3tables:GetNamespace",
        "s3tables:ListTables",
        "s3tables:GetTable",
        "s3tables:GetTableMetadataLocation",
        "s3tables:GetTableData"
      ],
      "Resource": [
        "arn:aws:s3tables:<region>:<account-id>:bucket/opensearch",
        "arn:aws:s3tables:<region>:<account-id>:bucket/opensearch/table/*"
      ]
    },
    {
      "Sid": "DecryptOpenSearchTables",
      "Effect": "Allow",
      "Action": "kms:Decrypt",
      "Resource": "arn:aws:kms:<region>:<account-id>:key/<key-id>"
    }
  ]
}
```

The S3 Tables statement is what the EMR Serverless execution role used to read the tables on OpenSearch 3.9. It needed no raw Amazon S3 permission on the tables' storage.

### Query engines
<a name="publishing-indices-s3-tables-query-engines"></a>

The tables are standard Iceberg v3. Each table has the index's fields plus the partition columns `index_name`, `_index_uuid`, `_shard_id`, `_start_time`, and `_end_time`. Object fields are Iceberg structs, and date fields are timestamps in UTC.

These tables use Iceberg format version 3 (V3) and store `date_nanos` fields as `timestamp_ns`, so a query engine needs V3 metadata support and nanosecond timestamps. The tables use no deletion vectors, row lineage, variant types, or default values.

The following engines can read Iceberg V3 tables:
+ Apache Spark on Amazon EMR release 7.12 or later
+ AWS Glue ETL 5.1 or later
+ Amazon SageMaker Unified Studio notebooks
+ Amazon Redshift patch 204 or later
+ The S3 Tables Iceberg REST endpoint
+ DuckDB 1.5.1 or later (iceberg extension)

Amazon Athena can't read V3 tables.

For more information, see [Working with Apache Iceberg V3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/working-with-apache-iceberg-v3.html) in the Amazon S3 User Guide.

In the following examples, replace the Region (`us-east-1`) and account ID (`111122223333`) with your own values.

The following example reads the tables with DuckDB 2.0:

```sql
INSTALL iceberg; LOAD iceberg; INSTALL httpfs; LOAD httpfs; INSTALL aws; LOAD aws;
CREATE SECRET (TYPE s3, PROVIDER credential_chain, REGION 'us-east-1');
ATTACH 'arn:aws:s3tables:us-east-1:111122223333:bucket/opensearch' AS s3t (TYPE iceberg, ENDPOINT_TYPE s3_tables);
SELECT service.name, count(*) FROM s3t.my_logs.web_logs
WHERE "@timestamp" >= TIMESTAMP '2026-11-22 06:00:00' GROUP BY 1;
```

For Apache Spark on Amazon EMR Serverless (Amazon EMR release 7.12 or later), configure an Iceberg REST catalog that signs requests with Signature Version 4:

```bash
--conf spark.sql.catalog.s3t=org.apache.iceberg.spark.SparkCatalog
--conf spark.sql.catalog.s3t.type=rest
--conf spark.sql.catalog.s3t.uri=https://s3tables.us-east-1.amazonaws.com/iceberg
--conf spark.sql.catalog.s3t.warehouse=arn:aws:s3tables:us-east-1:111122223333:bucket/opensearch
--conf spark.sql.catalog.s3t.rest.auth.type=sigv4
--conf spark.sql.catalog.s3t.rest.signing-name=s3tables
--conf spark.sql.catalog.s3t.rest.signing-region=us-east-1
```

The EMR Serverless application must run in a virtual private cloud (VPC) with an S3 Tables interface endpoint (`com.amazonaws.<region>.s3tables`) or a NAT gateway.
