---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/solr-capture-replay.html
---

# Capture and replay live traffic from Solr
<a name="solr-capture-replay"></a>

Migration Assistant supports live traffic capture and replay for Apache Solr sources running in SolrCloud mode. This enables zero-downtime migration by intercepting traffic flowing to your Solr cluster, transforming it to OpenSearch-compatible format, and replaying it against the target in real time.

## How it works
<a name="solr-capture-how-it-works"></a>

The Solr traffic capture and replay pipeline consists of the following components:
+  **Capture Proxy** — A transparent proxy deployed in front of your Solr cluster. It forwards all requests to Solr unchanged and simultaneously records them to Apache Kafka.
+  **Apache Kafka** — A message broker (deployed automatically by Migration Assistant) that durably stores captured traffic.
+  **Traffic Replayer** — Consumes captured traffic from Kafka, applies Solr-to-OpenSearch transformations, and sends the translated requests to the target.
+  **Solr request transform provider** — Converts Solr requests into OpenSearch-compatible API calls using your Solr schema and config set metadata for field-type and request-handler awareness.
+  **Solr tuple transform provider** — Optionally back-translates target responses in tuple audit records into a Solr-shaped response so you can compare captured source behavior with replayed target behavior.

## Prerequisites
<a name="solr-capture-prerequisites"></a>

**Tip**
For a guided, conversational experience that handles configuration generation, schema extraction, and troubleshooting automatically, use Migration Assistant AI agent mode. See [AI-assisted migration](agent-assisted-migration.md).
+  **Source cluster:** Apache Solr running in SolrCloud mode.
+  **Migration Assistant deployed:** The EKS-based Migration Assistant infrastructure must be running. See [Deploy the solution](deploy-the-solution.md).
+  **JSON-format writes:** Your application must send write requests in JSON format. XML-format requests are not supported by the transform layer.
+  **Traffic scope:** The Solr request transform translates `/solr/collection/select` and `/solr/collection/update` traffic. Suppress admin, schema, config, ping, replication, metrics, or other Solr-only endpoints unless you add a custom request transform for them.
+  **Schema files available:** For each Solr collection or config set that you replay, gather the matching schema XML and `solrconfig.xml` files. The schema XML can come from `managed-schema.xml`, `managed-schema`, `schema.xml`, or the Schema API with `wt=schema.xml`. `SolrToOpenSearchTransformProvider` uses these files to map field types and apply request handler defaults. `SolrTupleTransformProvider` is configuration-free.

## Step 1: Extract schema and config files from Solr
<a name="solr-capture-extract-schema"></a>

The Solr request transform provider requires your collection’s schema XML and config set’s `solrconfig.xml` to correctly translate field types and understand request handler defaults. Repeat this step for each collection whose traffic you plan to replay. If multiple collections use the same config set, you can reuse the same `solrconfig.xml` by referencing the same ConfigMap file under each collection prefix, or by making it the unprefixed default if it applies to every replayed collection.

First, map each collection to its SolrCloud config set. The transform configuration uses the collection name as the key prefix, but the ZooKeeper path for `solrconfig.xml` uses the config set name:

```
curl "http://SOLR_ENDPOINT:8983/solr/admin/collections?action=CLUSTERSTATUSwt=json" \
  | jq -r '.cluster.collections | to_entries[] | "\(.key)\t\(.value.configName)"'
```

If `jq` is not available, inspect `cluster.collections.COLLECTION.configName` in the JSON response. Record both values: use `COLLECTION` in transform keys such as `products.solrConfigXml`, and use `CONFIGSET` in ZooKeeper paths such as `zk:/configs/CONFIGSET/solrconfig.xml`.

 **Get schema XML:**

```
curl "http://SOLR_ENDPOINT:8983/solr/COLLECTION/schema?wt=schema.xml"  COLLECTION-managed-schema.xml
```

The output file name is arbitrary. The important part is that the file contains Solr schema XML, not the JSON returned by the default Schema API response.

 **Get solrconfig.xml:**

**Important**
Do not use the `/config` REST endpoint as it returns JSON, which the transform provider cannot parse. Always retrieve `solrconfig.xml` from ZooKeeper.

```
# From a host with access to ZooKeeper
solr zk cp zk:/configs/CONFIGSET/solrconfig.xml /tmp/CONFIGSET-solrconfig.xml -z ZK_HOST:2181 2/dev/null
```

If you are running Solr on Kubernetes within the same cluster as Migration Assistant:

```
# Copy from ZK to a temp file inside the Solr pod
kubectl exec -n NAMESPACE SOLR_POD -- bash -c \
  'solr zk cp zk:/configs/CONFIGSET/solrconfig.xml /tmp/CONFIGSET-solrconfig.xml -z ZK_HOST:2181 2/dev/null'

# Then copy to your local machine
kubectl cp NAMESPACE/SOLR_POD:/tmp/CONFIGSET-solrconfig.xml ./CONFIGSET-solrconfig.xml
```

 **Create a Kubernetes ConfigMap:**

Use one ConfigMap key per file. The ConfigMap key names are arbitrary, but the workflow `path` values in the next step must match them. These file names do not control transform routing; routing comes from the `context.values` key prefix, such as `products.solrSchemaXml` or `reviews.solrConfigXml`.

```
kubectl create configmap solr-config -n ma \
  --from-file=products-managed-schema.xml=./products-managed-schema.xml \
  --from-file=products-solrconfig.xml=./products-solrconfig.xml \
  --from-file=reviews-managed-schema.xml=./reviews-managed-schema.xml \
  --from-file=reviews-solrconfig.xml=./reviews-solrconfig.xml
```

## Step 2: Configure the workflow
<a name="solr-capture-configure-workflow"></a>

Add a `traffic` section to your workflow configuration JSON. The traffic section defines the capture proxy and the replayer with Solr-specific transform providers.

For tuple audit output on Amazon EKS, configure the replayer to write directly to Amazon S3. The standard deployment creates a default bucket and mounts it read-only on the Migration Console pod at `/s3/artifacts`, so tuple objects written under the default `tuples/` prefix are visible from the console at `/s3/artifacts/tuples/`.

```
kubectl get configmap migrations-default-s3-config -n ma \
  -o jsonpath='{.data.BUCKET_NAME}{"\n"}{.data.AWS_REGION}{"\n"}'
```

```
{
  "sourceClusters": {
    "source": {
      "endpoint": "http://SOLR_ENDPOINT:8983",
      "version": "SOLR VERSION",
      "snapshotInfo": {
        "repos": {
          "s3": {
            "awsRegion": "REGION",
            "s3RepoPathUri": "s3://BACKUP_BUCKET"
          }
        },
        "snapshots": {
          "main": {
            "repoName": "s3",
            "config": {
              "createSnapshotConfig": {
                "snapshotPrefix": "solr"
              }
            }
          }
        }
      }
    }
  },
  "targetClusters": {
    "target": {
      "endpoint": "https://TARGET_ENDPOINT",
      "authConfig": {
        "sigv4": {
          "region": "REGION",
          "service": "es"
        }
      }
    }
  },
  "snapshotMigrationConfigs": [
    {
      "fromSource": "source",
      "toTarget": "target",
      "perSnapshotConfig": {
        "main": [
          {
            "metadataMigrationConfig": {},
            "documentBackfillConfig": {
              "podReplicas": 3
            }
          }
        ]
      }
    }
  ],
  "traffic": {
    "proxies": {
      "solr-proxy": {
        "source": "source",
        "proxyConfig": {
          "listenPort": 8983
        }
      }
    },
    "replayers": {
      "solr-replayer": {
        "fromCapturedTraffic": "solr-proxy",
        "toTarget": "target",
        "dependsOnSnapshotMigrations": [
          { "source": "source", "snapshot": "main" }
        ],
        "replayerConfig": {
          "speedupFactor": 1.1,
          "podReplicas": 1,
          "tupleS3Bucket": "DEFAULT_MIGRATION_BUCKET",
          "tupleS3Region": "REGION",
          "requestTransforms": [
            {
              "transformName": "SolrToOpenSearchTransformProvider",
              "context": {
                "values": {
                  "targetType": { "value": "TARGET_TYPE" },
                  "products.solrSchemaXml": {
                    "fromFile": {
                      "configMap": "solr-config",
                      "path": "products-managed-schema.xml"
                    }
                  },
                  "products.solrConfigXml": {
                    "fromFile": {
                      "configMap": "solr-config",
                      "path": "products-solrconfig.xml"
                    }
                  },
                  "reviews.solrSchemaXml": {
                    "fromFile": {
                      "configMap": "solr-config",
                      "path": "reviews-managed-schema.xml"
                    }
                  },
                  "reviews.solrConfigXml": {
                    "fromFile": {
                      "configMap": "solr-config",
                      "path": "reviews-solrconfig.xml"
                    }
                  }
                }
              }
            }
          ],
          "tupleTransforms": [
            {
              "transformName": "SolrTupleTransformProvider"
            }
          ]
        }
      }
    }
  }
}
```

### Solr transform provider configuration
<a name="solr-capture-transform-config"></a>

 `SolrToOpenSearchTransformProvider` supports both a default schema/config pair and collection-specific overrides. Use collection-specific keys when one replay stream contains traffic for multiple Solr collections that use different schemas or config sets.

Collection-specific keys use the collection name exactly as it appears in captured request paths such as `/solr/products/select` or `/solr/reviews/update`. The key prefix is the collection name, not the ZooKeeper config set name. If the provider does not find a collection-specific schema or config for the request’s collection, it falls back to the unprefixed default keys. Schema and config fall back independently, so a collection-specific schema can still use the default config, and a collection-specific config can still use the default schema.

The table lists the provider keys after workflow materialization. In workflow `context.values`, wrap literal strings as `{ "value": "…​" }` and ConfigMap-backed XML as `{ "fromFile": …​ }`, as shown in the example. If you use raw `transformerConfig` outside the workflow pipeline, pass the raw string or file path value directly.

| Key | Value type | Description |
| --- | --- | --- |
|  `targetType`  | String | Optional target type. Valid values are `OpenSearch`, `OpenSearchServerless`, and `NextGenOpenSearchServerless`. If omitted, the provider uses `OpenSearch`. |
|  `solrSchemaXml`  | Inline XML or workflow `fromFile`  | Default `managed-schema.xml` content for collections that do not have a collection-specific schema. The provider reads explicit fields and dynamic field patterns to decide whether plain field queries should become OpenSearch `match` or `term` queries. |
|  `solrConfigXml`  | Inline XML or workflow `fromFile`  | Default `solrconfig.xml` content for collections that do not have a collection-specific config. The provider reads request handler `defaults`, `invariants`, and `appends` for handlers such as `/select`. |
|  `collection.solrSchemaXml`  | Inline XML or workflow `fromFile`  | Collection-specific `managed-schema.xml` content. For example, `products.solrSchemaXml` applies only to requests whose path starts with `/solr/products/`. |
|  `collection.solrConfigXml`  | Inline XML or workflow `fromFile`  | Collection-specific `solrconfig.xml` content. For example, `reviews.solrConfigXml` applies only to requests whose path starts with `/solr/reviews/`. |
|  `solrSchemaXmlFile`, `solrConfigXmlFile`  | Filesystem path | Default file path forms for environments where the replayer can read local files directly. In workflow configurations, prefer `solrSchemaXml` and `solrConfigXml` with `fromFile` so the files are materialized from a ConfigMap. |
|  `collection.solrSchemaXmlFile`, `collection.solrConfigXmlFile`  | Filesystem path | Collection-specific file path forms for direct replayer configuration outside the workflow ConfigMap pattern. |

For each scope and file type, set either the inline/XML key or the `File` key, not both. For example, do not set both `products.solrSchemaXml` and `products.solrSchemaXmlFile`. Blank, missing, or unparsable schema/config XML does not stop the replayer; the provider logs the problem and continues with an empty schema or config for that scope. That keeps replay moving, but fielded queries and request-handler defaults fall back to generic behavior, so verify ConfigMap paths and provider logs before trusting replay results.

The schema and config values are consumed by `SolrToOpenSearchTransformProvider` in `requestTransforms`. If you include `SolrTupleTransformProvider` under `tupleTransforms`, it does not require any `context.values` configuration, does not affect replayed requests, and can be omitted when you do not need Solr-shaped tuple comparison output.

### targetType configuration
<a name="solr-capture-target-type"></a>

The `targetType` value tells the transform provider what type of OpenSearch target you are using. This controls whether certain features (like `?refresh`) are included in the translated requests.

| Value | Target | Behavior |
| --- | --- | --- |
|  `OpenSearch`  | Self-managed OpenSearch or Amazon OpenSearch Service | Full feature set. `?refresh=true` appended when commit semantics are requested. |
|  `OpenSearchServerless`  | Amazon OpenSearch Serverless | Suppresses `?refresh=true` on target-type-gated write translations such as document ingest, bulk add/delete, and delete-by-query. It does not currently suppress `?refresh=true` on standalone delete-by-ID translations when the captured request includes `commit=true` or `commitWithin`. Documents become searchable automatically. |
|  `NextGenOpenSearchServerless`  | Amazon OpenSearch Serverless NextGen | Same as `OpenSearchServerless`: suppresses `?refresh=true` for target-type-gated write translations, with the same standalone delete-by-ID caveat. |

For Amazon OpenSearch Serverless NextGen targets, also set `authConfig.sigv4.service` to `aoss` instead of `es`.

**Important**
 `targetType` does not turn Solr commit-only update commands into no-ops. Requests such as `{"commit":{}}` and empty update arrays still translate to `POST /collection/_refresh`. Also avoid `commit=true` or `commitWithin` on captured delete-by-ID traffic for Serverless targets because the current delete-by-ID translation still appends `?refresh=true`.

### Replayer settings
<a name="solr-capture-replayer-settings"></a>

| Setting | Description | Default |
| --- | --- | --- |
|  `speedupFactor`  | Replay speed multiplier. `1.0` = real-time, `2.0` = double speed. Use higher values to catch up after backfill. | 1.1 |
|  `podReplicas`  | Number of parallel replayer pods. Each independently consumes from Kafka. | 1 |
|  `requestTransforms`  | Array of request transform providers. Required for Solr sources. | None |
|  `tupleTransforms`  | Array of tuple transform providers. Optional; include `SolrTupleTransformProvider` when you want tuple audit records to include Solr-shaped target response comparisons. | None |
|  `removeAuthHeader`  | Strip the captured `Authorization` header before replaying. Do not set this to `true` when the target cluster also has `authConfig`; the workflow applies target authentication automatically and rejects that combination. | false |
|  `maxConcurrentRequests`  | Maximum in-flight requests to the target cluster. | 10000 |
|  `lookaheadTimeSeconds`  | Seconds of traffic to buffer ahead of current replay position. Must be greater than `observedPacketConnectionTimeout`. | 400 |
|  `observedPacketConnectionTimeout`  | Seconds of inactivity on a captured connection before the replayer treats the original connection as closed. | 360 |
|  `targetServerResponseTimeoutSeconds`  | Maximum seconds to wait for a response from the target. | 150 |
|  `numClientThreads`  | Number of client threads used to send replayed requests. `0` uses the replayer’s Netty event loop. | 0 |
|  `quiescentPeriodMs`  | Milliseconds to delay the first request on a resumed connection after a Kafka partition reassignment. | 5000 |
|  `tupleS3Bucket`, `tupleS3Region`  | Optional, and recommended for Amazon EKS workflow runs, S3 destination for tuple audit output. When set, the replayer writes gzip-compressed JSON Lines tuple objects directly to S3. `tupleS3Region` is required when `tupleS3Bucket` is set. | None |
|  `tupleS3Prefix`  | S3 key prefix for tuple objects. |  `tuples/`  |
|  `tupleS3Endpoint`  | Custom S3-compatible endpoint for tuple output, such as LocalStack or another S3-compatible service. | None |
|  `tupleMaxBufferSeconds`  | Maximum age before the current S3 tuple file is rotated and uploaded. | 60 |
|  `tupleMaxFileSizeMb`  | Maximum uncompressed tuple data size before the current S3 tuple file is rotated and uploaded. | 256 |
|  `tupleMaxPerFile`  | Maximum number of tuples per S3 object. `0` means no tuple-count limit. Use `1` only when downstream processing requires one tuple per object. | 0 |
|  `otelMetricsCollectorEndpoint`  | OpenTelemetry metrics collector endpoint. Set to an empty string to disable metrics export. |  `http://otel-collector:4317`  |
|  `otelTraceCollectorEndpoint`  | OpenTelemetry trace collector endpoint. Omit or set to an empty string to disable trace export. | None |
|  `userAgent`  | String appended to the User-Agent header on replayed target requests so replay traffic can be identified in target logs. | None |
|  `nonRetryableDocExceptionTypes`  | Document-level bulk error type strings that should not be retried during replay. If set, your list replaces the replayer’s built-in defaults instead of adding to them. | Built-in list |
|  `resources`, `jvmArgs`, `loggingConfigurationOverrideConfigMap`  | Kubernetes resource requests/limits, JVM arguments, and logging override ConfigMap for replayer pods. | Schema defaults |

**Note**
If `tupleS3Bucket` is omitted, the replayer falls back to local tuple log files inside the replayer pod; those files are not mounted into the Migration Console in the Amazon EKS workflow deployment. For operator-accessible audit output, set `tupleS3Bucket` and `tupleS3Region`. You can use the Migration Assistant-managed default bucket; retrieve its name with `kubectl get configmap migrations-default-s3-config -n ma -o jsonpath='{.data.BUCKET_NAME}'`. You can also set `tupleS3Endpoint` for custom S3-compatible endpoints. For the complete replayer tuning reference, see [Replay tuning](replay-tuning.md).

## Step 3: Submit and start the workflow
<a name="solr-capture-submit"></a>

From the Migration Console pod (`migration-console-0`) in the `ma` namespace:

```
# Load the configuration
workflow configure edit --stdin  /tmp/config.json

# Create target credentials (if using basic auth instead of SigV4)
echo "USERNAME:PASSWORD" | workflow configure credentials create target-creds --stdin

# Submit the workflow
workflow submit
```

## Step 4: Reroute client traffic to the capture proxy
<a name="solr-capture-reroute"></a>

After `workflow status` shows **Create Proxy: Succeeded**, retrieve the proxy endpoint:

```
kubectl get svc solr-proxy -n ma -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'
```

Update your application’s Solr connection URL to point to the capture proxy (for example, `https://PROXY_ENDPOINT:8983`) instead of the source Solr cluster. The proxy is protocol-compatible — your application requires no code changes.

## Step 5: Monitor replay progress
<a name="solr-capture-monitor"></a>

```
# Overall workflow status
workflow status

# Follow replayer logs
workflow log all --follow
```

Key metrics in replayer logs:

| Metric | Description | Expected value |
| --- | --- | --- |
|  `requests`  | Total requests replayed to target | Increasing over time |
|  `targetResponses`  | HTTP status codes from target (grouped) | Mostly `{200=N}` for writes |
|  `exceptions`  | Transform or connection errors | 0 for write operations |
|  `kafkaCommitCount`  | Kafka offsets committed | Increasing (replay progressing) |

## Step 6: Validate and cut over
<a name="solr-capture-validate"></a>

```
# Check document count
console clusters cat-indices --refresh

# Verify a specific document
console clusters curl target /INDEX/_doc/DOCUMENT_ID

# Compare counts
console clusters curl target /INDEX/_count
```

Before switching your application to point directly at OpenSearch:
+  **Confirm replay has reached the live edge** — The replayer should be processing traffic in near-real-time with no growing Kafka lag.
+  **Verify document counts** — Target count should match source count plus any documents added during replay.
+  **Spot-check documents** — Verify that recently ingested and deleted documents are correctly reflected in the target.
+  **Review replayer errors** — Ensure `exceptions=0` for write operations.

## Audit trail
<a name="solr-capture-tuple-audit"></a>

The replayer writes a complete audit trail of every request-response pair (tuples). When `tupleS3Bucket` is configured, inspect the gzip-compressed tuple objects from the Migration Console pod through the mounted default bucket:

```
# List tuple files
find /s3/artifacts/tuples -name 'tuples-*.log.gz' -print

# View tuples in human-readable format
gzip -dc /s3/artifacts/tuples/REPLAYER_POD/YYYY/MM/DD/HH/tuples-SINK-TIMESTAMP-SEQ.log.gz \
  | console tuples show
```

Each tuple contains the original Solr request, the Solr source response, the transformed OpenSearch request, and the OpenSearch response. When `SolrTupleTransformProvider` is enabled, the tuple also includes `targetResponsesTransformed`, which contains the target response back-translated into a Solr-shaped response where possible for translated select and update traffic. If a tuple’s source request path is not recognized by the provider, the corresponding transformed entry is `null`; if back-translation fails, the entry contains an `error` object with the failure message. Do not treat recognized but unsupported Solr endpoints, such as admin, schema, config, ping, and metrics traffic, as Solr-equivalent tuple comparisons; suppress them during capture or add a custom tuple transform if you need to analyze them.

The tuple transform is intentionally configuration-free. It does not read the Solr schema/config values that `SolrToOpenSearchTransformProvider` uses for request translation, so reconstructed `response.docs` use schemaless field-shape defaults: arrays stay arrays, numeric and boolean values stay scalar, and unknown non-array scalar values can appear as single-item arrays. Account for that when comparing tuple output, or add a custom tuple transform if your audit tooling requires exact field cardinality.

**Note**
These logs contain the contents of all requests, including authorization headers and HTTP message bodies. Ensure that access to the migration environment is restricted.

## Supported Solr transformations
<a name="solr-capture-supported-transforms"></a>

For a full reference of supported write operations, search query features, and behavioral differences, see [Transform Solr traffic](transform-solr.md).
