---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/replay-phase.html
---

# Replay captured traffic
<a name="replay-phase"></a>

Replay applies to zero-downtime and capture-and-replay migrations only. After backfill completes, the Traffic Replayer consumes requests from Apache Kafka and sends them to the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection. The Kafka topic can be populated by a live capture proxy or by loading a previously exported captured-traffic archive from Amazon S3. Replay closes the gap between the snapshot point-in-time and the current state of the source, and lets you compare source and target behavior before you switch traffic. If you are running a backfill-only migration, skip this phase. See [Reroute client traffic to the capture proxy](reroute-to-proxy.md) and [Migration scenarios](use-the-solution.md#migration-scenarios).

**Note**
For Apache Solr sources, capture and replay requires Solr-specific transform providers and a different workflow configuration. See [Capture and replay live traffic from Solr](solr-capture-replay.md) in the Solr migration chapter.

Once replay has caught the target up to the live edge and you have validated source and target behavior, proceed to [Switch traffic to the target](switch-traffic.md).
