---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/concepts-and-definitions.html
---

# Concepts and definitions
<a name="concepts-and-definitions"></a>

This section describes key concepts and defines terminology specific to this solution:

 **source cluster**

The originating cluster on a specific version of Elasticsearch, OpenSearch, or Apache Solr that the user is attempting to either upgrade or decommission.

 **target cluster**

The destination Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection that the user is migrating to or optimizing.

 **capture proxy**

A pass-through HTTP proxy designed to capture and log all of the request and response traffic to a durable Apache Kafka stream for later reuse.

 **Traffic Replayer**

A tool designed to simulate original traffic workloads by retrieving recorded request traffic and sending it to an Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection. The Traffic Replayer correlates the request and response traffic of the originating request with the request and response traffic to the target, and stores the traffic persistently.

 **Reindex-from-Snapshot (RFS)**

The high-performance backfill engine. RFS reads raw Lucene segment files directly from a snapshot in Amazon S3 and bulk-indexes documents into the target. This approach keeps load off the source cluster and parallelizes work at the shard level.

 **Workflow CLI**

The customer-facing interface for configuring, submitting, approving, and monitoring migrations. The Workflow CLI runs in the Migration Console pod on Amazon EKS and is the day-to-day operator interface for the solution.

 **Migration Console**

A pod on Amazon EKS that runs the Workflow CLI and the `console` command-line tools used to inspect and manually drive individual migration components during validation and troubleshooting.

 **existing data**

Documents that were on the source cluster at the point where a snapshot is taken.

 **live/continuous data**

Data intercepted by the Capture Proxy and subsequently processed through a Traffic Replayer. Initially, this information is transmitted from clients to the source cluster, where it is intercepted by the Capture Proxy. Subsequently, the data is relayed back to the designated target cluster.

**Note**
For a general reference of AWS terms, see the [AWS Glossary](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html).
