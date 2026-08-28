---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-es68-capture-replay.html
---

# Optional: Add zero-downtime capture and replay
<a name="pb-es68-capture-replay"></a>

If your source takes live writes that you cannot pause, add capture and replay so no writes are lost during the migration. With this pattern, you reroute client traffic through the capture proxy first, then run backfill, then replay the captured traffic to bring the target up to the live edge before cutover.

**Note**
Capture and replay are supported for Elasticsearch 6.8 and for Apache Solr sources running in SolrCloud mode with JSON-format writes. They are not available for standalone Solr or Elasticsearch 1.x-2.x sources, which are backfill-only.

Add a `traffic` section that defines the capture proxy under `traffic.proxies` and the Traffic Replayer under `traffic.replayers`. Set `fromCapturedTraffic` to the proxy name when replaying live captured traffic. The proxy’s listen port and pod count go under `proxyConfig`, and the replayer’s tuning goes under `replayerConfig`. Listing the source snapshot in `dependsOnSnapshotMigrations` (an array of `{source, snapshot}` references, not a boolean) ensures the replayer starts only after that snapshot’s backfill completes:

```
{
  "traffic": {
    "proxies": {
      "capture-proxy": {
        "source": "source",
        "proxyConfig": {
          "listenPort": 9201,
          "podReplicas": 2
        }
      }
    },
    "replayers": {
      "replay1": {
        "fromCapturedTraffic": "capture-proxy",
        "toTarget": "target",
        "dependsOnSnapshotMigrations": [
          {
            "source": "source",
            "snapshot": "migration-snapshot"
          }
        ],
        "replayerConfig": {
          "podReplicas": 2,
          "speedupFactor": 1.5
        }
      }
    }
  }
}
```

The recommended order of operations is:

1. Reroute client traffic to the capture proxy on the configured `listenPort` (9201 in the example) so writes are recorded to Apache Kafka while still reaching the source.

1. Run the snapshot, metadata migration, and backfill as in the previous steps.

1. Let the replayer drain the captured traffic to the target. A `speedupFactor` of `1.5`–`2.0` replays faster than the original timeline so the target catches up to the live edge; raise it only as fast as the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection can keep up.

1. Validate, then switch traffic as in [Cutover and rollback](cutover.md).

**Important**
Auto-generated document IDs are not preserved during replay. If a captured write relied on the source assigning an `_id`, the replayed request can create a differently identified document on the target. Validate identity-sensitive indexes before cutover.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
