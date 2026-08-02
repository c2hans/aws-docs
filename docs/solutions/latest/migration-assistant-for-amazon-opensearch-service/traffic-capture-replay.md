---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/traffic-capture-replay.html
---

# Traffic Capture and Replay
<a name="traffic-capture-replay"></a>

The Capture Proxy relays HTTP requests into a durable, scalable Apache Kafka stream before forwarding them to the source cluster. The Traffic Replayer consumes records from Apache Kafka, reconstructs them into HTTP requests, applies replay-time transformations and authentication behavior, and sends them to the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection. This replication can test the performance of the new target, keep the clusters synchronized, and illustrate differences between a source and target. Users can explore the progress and performance of the replay through Amazon CloudWatch metrics and through the Migration Console by querying results, which are output as rotating JSON files.

Replay duration is mostly a function of how much traffic was captured during backfill, how fast the target can process that traffic, and the `speedupFactor` you configure (default `1.1`; `2.0` means twice the original traffic timeline). Replay duration is not fixed; it depends on backlog and throughput. Tune replay with `podReplicas`, `speedupFactor`, `maxConcurrentRequests`, timeout and lookahead settings, authentication behavior, tuple output settings, and `nonRetryableDocExceptionTypes`. Use `dependsOnSnapshotMigrations` on the replayer when replay must wait for specific backfills to complete.
