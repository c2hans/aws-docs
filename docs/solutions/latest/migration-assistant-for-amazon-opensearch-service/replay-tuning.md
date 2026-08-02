---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/replay-tuning.html
---

# Replay tuning
<a name="replay-tuning"></a>

Configure most Traffic Replayer settings under `replayerConfig` in the workflow configuration.

## Throughput and timing
<a name="replay-throughput-timing"></a>
+  `podReplicas` - number of replayer pods. Each pod independently consumes from Kafka and sends traffic to the target.
+  `speedupFactor` - replay speed multiplier. The default is `1.1`; `2.0` means twice the original traffic timeline.
+  `maxConcurrentRequests` - maximum in-flight requests to the target per replayer pod. The default is `10000`.
+  `numClientThreads` - number of client threads used to send replayed requests. The default is `0`, which uses the Netty event loop.
+  `targetServerResponseTimeoutSeconds` - maximum time to wait for a response from the target before timing out a replayed request. The default is `150`.
+  `lookaheadTimeSeconds` - seconds of captured traffic to buffer ahead of the current replay position. The default is `400`; it must be greater than `observedPacketConnectionTimeout`.
+  `observedPacketConnectionTimeout` - seconds of inactivity on a captured connection before the replayer treats the original connection as closed. The default is `360`.
+  `quiescentPeriodMs` - delay before the first request on a resumed connection after Kafka partition reassignment. The default is `5000`.

If the target is saturated, reduce `podReplicas`, `speedupFactor`, or `maxConcurrentRequests`. If the target has spare capacity but replay is not catching up, increase them gradually while watching target latency, rejected requests, and replay lag.

## Authentication, Kafka, and identification
<a name="replay-auth-kafka-and-identification"></a>
+  `removeAuthHeader` - strips the captured `Authorization` header before replaying. Use this when captured credentials are not valid for the target and no replacement `Authorization` header should be applied. Do not set it when the target uses Basic or SigV4 `authConfig`; the workflow applies those target credentials automatically and rejects a replayer that also sets `removeAuthHeader`.
+  `userAgent` - appends a string to the User-Agent header on replayed target requests so you can identify replay traffic in target logs.
+  `kafkaTrafficEnableMSKAuth` - legacy process flag for direct MSK IAM Kafka consumer wiring. The workflow Kafka cluster profile path resolves `auth.type` as `none` or `scram-sha-512`; use this flag only for low-level process configurations that are wired consistently with the capture proxy.
+  `kafkaTrafficPropertyFile` - expert setting for additional Kafka consumer properties. The file must already be mounted into the replayer container.
+  `otelMetricsCollectorEndpoint` - OpenTelemetry metrics collector endpoint. The default is `http://otel-collector:4317`; set it to an empty string to disable metrics export.
+  `otelTraceCollectorEndpoint` - OpenTelemetry trace collector endpoint, such as `http://otel-trace-collector:4317`. Omit it or set it to an empty string to disable trace export.
+  `resources`, `jvmArgs`, and `loggingConfigurationOverrideConfigMap` - Kubernetes resources, JVM arguments, and logging override ConfigMap for replayer pods.

Set `dependsOnSnapshotMigrations` on the replayer, outside `replayerConfig`, when replay must wait for specific snapshot migrations to complete before starting.

## Transforms, tuples, and retries
<a name="replay-transforms-tuples-and-retries"></a>
+  `requestTransforms` - preferred workflow field for request transform pipelines. Use this for workflow-managed JavaScript or Python transforms.
+  `transformerConfig`, `transformerConfigEncoded`, and `transformerConfigFile` - raw request transformer configuration forms for manual or expert use. Do not set these together with `requestTransforms`.
+  `tupleTransforms` - preferred workflow field for tuple transform pipelines. Use this when tuple audit records need additional comparison or normalization logic.
+  `tupleTransformerConfig`, `tupleTransformerConfigBase64`, and `tupleTransformerConfigFile` - raw tuple transformer configuration forms. Do not set these together with `tupleTransforms`.
+  `tupleS3Bucket` and `tupleS3Region` - write tuple logs directly to Amazon S3. `tupleS3Region` is required when `tupleS3Bucket` is set. Recommended for Amazon EKS workflow runs because local replayer tuple logs are not mounted into the Migration Console.
+  `tupleS3Prefix` and `tupleS3Endpoint` - optional S3 key prefix and custom endpoint. The default prefix is `tuples/`.
+  `tupleMaxBufferSeconds`, `tupleMaxFileSizeMb`, and `tupleMaxPerFile` - S3 tuple rotation controls. Defaults are 60 seconds, 256 MB uncompressed, and `0` for no tuple-count limit.
+  `nonRetryableDocExceptionTypes` - document-level bulk error type strings that should not be retried during replay. These errors still count as failures. When omitted, the replayer uses its built-in default set: `version_conflict_engine_exception`, `mapper_parsing_exception`, `strict_dynamic_mapping_exception`, `document_missing_exception`, `action_request_validation_exception`, `invalid_index_name_exception`, `routing_missing_exception`, `illegal_argument_exception`, and `resource_already_exists_exception`. If you set this field, your list replaces the defaults rather than adding to them.

**Warning**
Setting both `replayerConfig.removeAuthHeader: true` and a Basic or SigV4 `authConfig` block on the same target is rejected by the schema. Pick one — either rely on the target’s `authConfig` (the Traffic Replayer applies it for you) or strip the captured header.
