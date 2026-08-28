---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/using-traffic-replayer.html
---

# Using Traffic Replayer
<a name="using-traffic-replayer"></a>

**Note**
This section is only relevant if you are using Capture and Replay to avoid downtime during a migration to Amazon OpenSearch Service or Amazon OpenSearch Serverless NextGen. If you are performing backfill only, skip this section.

Traffic Replayer replays captured traffic from the source cluster to the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection. This verifies that the target can handle requests in the same way as the source and catches up to real-time traffic for a smooth migration.

## Replay a captured-traffic archive from Amazon S3
<a name="replay-s3-captured-traffic"></a>

If you already have captured traffic exported from a Migration Assistant Kafka topic, configure it under `traffic.s3Sources`. The workflow loads the `*.proto.gz` archive into Kafka and replays that topic without creating a live capture proxy. Set the replayer’s `fromCapturedTraffic` field to the `s3Sources` key. The same `fromCapturedTraffic` field also references `traffic.proxies` when you replay live captured traffic.

```
{
  "kafkaClusterConfiguration": {
    "default": {
      "autoCreate": {
        "auth": {
          "type": "none"
        }
      }
    }
  },
  "sourceClusters": {},
  "targetClusters": {
    "target": {
      "endpoint": "https://<TARGET_ENDPOINT>"
    }
  },
  "snapshotMigrationConfigs": [],
  "traffic": {
    "s3Sources": {
      "loaded-dump": {
        "s3Uri": "s3://traffic-bucket/captures/one.proto.gz",
        "awsRegion": "us-east-1",
        "sourceLabel": "original-source",
        "kafkaTopic": "loaded-dump"
      }
    },
    "replayers": {
      "replay1": {
        "fromCapturedTraffic": "loaded-dump",
        "toTarget": "target",
        "replayerConfig": {
          "speedupFactor": 2.0
        }
      }
    }
  }
}
```

The `s3Uri` must point to a gzipped captured-traffic export in the form `s3://<BUCKET>/<PATH>/<FILE>.proto.gz`. The loader uses the workflow pod’s AWS identity to read the object, so grant that identity `s3:GetObject` access to the bucket and prefix. The `awsRegion` is the Region of the S3 bucket. The `sourceLabel` is used for workflow resource labels and does not need to match a key in `sourceClusters`. The top-level `sourceClusters` field is still required by the workflow schema; use an empty object when the run only replays an S3 traffic archive and does not access a live source cluster. If you omit `kafka`, the workflow uses the `default` Kafka cluster. If you omit `kafkaTopic`, the workflow uses the `s3Sources` key, such as `loaded-dump`, as the topic name. Use `endpoint` only for a custom S3-compatible endpoint; valid schemes are `http://`, `https://`, `localstack://`, and `localstacks://`.

**Important**
The workflow S3 loader does not mount Kafka SCRAM passwords, Kafka CA certificates, or a custom Kafka client property file. For `traffic.s3Sources`, configure the destination Kafka profile so the loader can write without SCRAM/TLS client material, such as an auto-created Kafka cluster with `auth.type: none` or an existing Kafka cluster with `auth.type: none`. Do not rely on the implicit workflow-managed Kafka default for S3 archive replay; when Kafka auth is omitted, workflow-managed Kafka resolves to SCRAM, and the S3 import step cannot use that SCRAM material. The capture proxy and replayer support SCRAM through `kafkaClusterConfiguration`, but the S3 import step is a separate loader path.

**Important**
An S3 captured-traffic source is loaded into Kafka exactly once. This prevents accidental duplicate replay if a workflow is retried. To replay a different `s3Uri` or reload the same object intentionally, use a new `traffic.s3Sources` key or delete the corresponding `CapturedTraffic` custom resource before rerunning the workflow.

**Note**
Names under `traffic.s3Sources` and `traffic.proxies` share one namespace because replayers resolve both through `fromCapturedTraffic`. Do not reuse the same name in both maps.

**Note**
Each `traffic.proxies` entry and each `traffic.s3Sources` entry owns one captured-traffic topic. Within the same Kafka cluster, two captured-traffic sources cannot resolve to the same effective topic name. The effective topic is the explicit `kafkaTopic`, or the traffic source key when `kafkaTopic` is omitted.

## When to run Traffic Replayer
<a name="when-to-run-replayer"></a>

Run Traffic Replayer only after the backfill work it depends on has completed. In the workflow path, you normally express this by setting `dependsOnSnapshotMigrations` on the replayer, outside `replayerConfig`. The workflow then starts replay automatically after the captured-traffic source is ready and the listed snapshot migrations have completed. Running replay too early can apply operations out of order; for example, a deletion captured after the snapshot was taken could execute before the document is added to the target.

## Starting replay
<a name="start-replayer"></a>

```
workflow submit
workflow manage
```

For workflow-managed migrations, `workflow submit` starts the workflow and the Traffic Replayer starts when its dependencies are ready. Use `workflow manage` for the interactive run view and approval gates.

The legacy `console replay start` command controls a directly configured replayer deployment from older component-style console configurations. It is not the primary workflow path.

## Checking replay status
<a name="replayer-status"></a>

```
workflow status --resource-view
workflow log resource trafficreplay.<NAME> -- --tail=100
```

The resource view groups migration resources by role and shows the `TrafficReplay` resource that owns the replayer pods. Use `workflow log resource --list` if you need the exact resource name.

If you are using a legacy directly configured replayer, `console replay status` reports the number of running, pending, and desired instances for that deployment.

## Stopping or replacing replay
<a name="stop-replayer"></a>

```
workflow submit
```

 `workflow submit` automatically stops and replaces an existing workflow with the same workflow name before submitting the new run. Use `workflow reset` only when you need to delete migration custom resources left from an abandoned or failed run. For legacy directly configured replayers, use `console replay stop`.

## Delivery guarantees
<a name="replay-delivery-guarantees"></a>

Traffic Replayer retrieves traffic from Apache Kafka and updates its commit cursor after sending requests to the target. This provides an "at least once" delivery guarantee. Monitor metrics and validate externally to confirm the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection is functioning as expected.

## Time scaling
<a name="replay-time-scaling"></a>

Traffic Replayer sends requests in the same order they were received on each connection. With a `speedupFactor` greater than 1, requests are sent faster than original timing:
+  **speedupFactor 1** — Same rate and idle periods as the source.
+  **speedupFactor 2** — Twice as fast. GETs sent every 500 ms instead of every second.
+  **speedupFactor 10** — 10x faster, as long as the target responds quickly.

If the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection cannot respond quickly enough, Traffic Replayer waits for the previous request to complete before sending the next one.

## Transformations
<a name="replay-transformations"></a>

Traffic Replayer automatically rewrites host and authentication headers. For more complex transformations, including Elasticsearch content-type header compatibility, see [Transform live traffic (Traffic Replayer)](transform-replayer.md).

## Result logs
<a name="replay-result-logs"></a>

Traffic Replayer can write tuple audit records for HTTP transactions from the source capture and those replayed to the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection. For Amazon EKS workflow runs, configure tuple output to Amazon S3. The following fragment shows only the relevant fields; keep the rest of the replayer configuration unchanged:

```
{
  "traffic": {
    "replayers": {
      "<REPLAYER_NAME>": {
        "replayerConfig": {
          "tupleS3Bucket": "<DEFAULT_MIGRATION_BUCKET>",
          "tupleS3Region": "<REGION>"
        }
      }
    }
  }
}
```

You can use the Migration Assistant-managed default bucket. Retrieve its name and Region from the `migrations-default-s3-config` ConfigMap:

```
kubectl get configmap migrations-default-s3-config -n ma \
  -o jsonpath='{.data.BUCKET_NAME}{"\n"}{.data.AWS_REGION}{"\n"}'
```

S3 tuple objects are gzip-compressed JSON Lines. The default S3 prefix is `tuples/`, and object keys use this structure:

```
<tupleS3Prefix><replayer-pod>/<yyyy/MM/dd/HH>/tuples-<sink-index>-<timestamp>-<sequence>.log.gz
```

The standard Amazon EKS deployment mounts the default bucket read-only on the Migration Console pod at `/s3/artifacts`. Tuple objects written with the default prefix are visible under `/s3/artifacts/tuples/`.

Use `tupleS3Prefix`, `tupleS3Endpoint`, `tupleMaxBufferSeconds`, `tupleMaxFileSizeMb`, and `tupleMaxPerFile` to control the object path and rotation behavior. By default, S3 tuple files rotate after 60 seconds or 256 MB of uncompressed tuple data, with no tuple-count limit. Set `tupleMaxPerFile` only when downstream processing needs smaller objects; `1` creates one S3 object per tuple and can produce many objects.

To view logs in human-readable format:

```
find /s3/artifacts/tuples -name 'tuples-*.log.gz' -print

gzip -dc /s3/artifacts/tuples/<REPLAYER_POD>/<YYYY>/<MM>/<DD>/<HH>/tuples-<SINK>-<TIMESTAMP>-<SEQ>.log.gz \
  | console tuples show > readable-tuples.log
```

If `tupleS3Bucket` is omitted, the replayer falls back to local tuple log files inside the replayer pod; those files are not mounted into the Migration Console in the Amazon EKS workflow deployment.

**Note**
These logs contain the contents of all requests, including authorization headers and HTTP message bodies. Ensure that access to the migration environment is restricted.

## Amazon CloudWatch metrics
<a name="replay-cloudwatch-metrics"></a>

Traffic Replayer emits OpenTelemetry metrics through the configured collector, which the solution exports to Amazon CloudWatch. It can also emit traces when a trace collector endpoint is configured. Key metrics include:

| Metric | Description |
| --- | --- |
|  `sourceStatusCode`  | HTTP status codes for source and target, with dimensions for HTTP verb and status code family. Quickly identifies discrepancies between source and target responses. |
|  `lagBetweenSourceAndTargetRequests`  | Delay between requests hitting the source and target. With a speedup factor greater than 1, this value should decrease as replay progresses. |
|  `bytesWrittenToTarget` / `bytesReadFromTarget`  | Throughput to and from the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection. |
|  `numRetriedRequests`  | Requests retried because of status code mismatches between source and target. |
| Various `(*)Count`  | Event counts for completed operations. |
| Various `(*)Duration`  | Duration of each processing step. |
| Various `(*)ExceptionCount`  | Exceptions encountered during each processing phase. |

**Note**
Metrics pushed to Amazon CloudWatch may experience a visibility lag of approximately 5 minutes. Amazon CloudWatch retains higher-resolution data for a shorter period than lower-resolution data. For more information, see [Amazon CloudWatch concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
