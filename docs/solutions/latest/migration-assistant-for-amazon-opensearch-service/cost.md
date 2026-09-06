---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/cost.html
---

# Cost
<a name="cost"></a>

You are responsible for the cost of the AWS services used while running this solution. As of this revision, the cost for running this solution with the default settings in the US East (N. Virginia) Region is approximately **$2,990 for a zero-downtime migration over 15 days with 100 TB of existing data and 15 MBps of live traffic**. A **backfill-only migration** of the same 100 TB costs approximately **$1,430 over 7 days** because it eliminates the Capture Proxy, Kafka, and Traffic Replayer components entirely. In this model, the initial snapshot and bulk RFS backfill run while the source cluster remains live (no downtime). The maintenance window is limited to the time required to pause ingestion, take a final incremental snapshot of the delta (changes accumulated during backfill), migrate that delta with RFS at higher parallelism, and cut over — typically **1–2 hours** depending on the write volume to the source during the backfill period. These costs are for the resources shown in the sample cost table.

We recommend creating a budget through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs. Prices are subject to change. For full details, refer to the pricing webpage for each AWS service used in this solution.

A migration typically has different duration and data volume for the individual steps described in [Migration phases](plan-your-deployment.md#migration-phases). Customers typically wait to remove infrastructure or delete data until after a migration is complete. It’s crucial to understand the volume and duration of each of the steps to estimate the cost of the solution.

In the following example, we outline the cost of a 15-day migration with the following schedule:

 **Depicts an example 15-day migration schedule from deployment to teardown**

![cost migration schedule](http://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/images/cost-migration-schedule.png)

To understand the costs, we need to map these steps into cost components, including data retention periods as applicable. This yields the following schedule:

 **Depicts an example 15-day migration schedule mapped to this solution’s components**

![cost migration schedule components](http://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/images/cost-migration-schedule-components.png)

+ Core Services - 15 days
+ Capture Proxy - 6 days
+ Capture Proxy Data Retention Period - 4 days
+ Snapshot - 1 day
+ Snapshot Data Retention Period - 9 days
+ Reindex from Snapshot - 3 days
+ Traffic Replayer - 2 days
+ Traffic Replayer Data Retention Period - 4 days

Using this schedule, the following is an example of a customer performing a zero-downtime migration of a cluster with 100 TB of primary shard data with 15 MBps aggregated request-response throughput. The ongoing request throughput over the 6-day capture timeline gives a capture/replay volume of about 7.8 TB.

Assumptions:
+ No data is retained after the teardown step, representing no resources and cost after day 15.
+ Deployment in US East (N. Virginia).
+ The Source Cluster, Target Cluster, and VPC are imported and cost excluded from this calculation, including data transfer cost based on VPC setup. The VPC includes an Amazon S3 Gateway Endpoint (free) and VPC Interface Endpoints for Amazon CloudWatch Logs, Amazon EFS, and Amazon ECR.
+ Amazon EKS Auto Mode pod compute pricing: $0.04048 per vCPU-hour and $0.004445 per GiB-hour (On-Demand, x86\_64, Linux).
+ Apache Kafka is provided by Strimzi on Amazon EKS with Amazon EBS gp3 persistent volumes (replaces Amazon MSK).
+ All pods run on Amazon EKS Auto Mode managed nodes.

This gives us the following cost table:

| AWS service | Dimensions | Cost [USD] |
| --- | --- | --- |
|  **Core services (15 days)**  |  |  |
| Amazon EKS | Cluster fee:<br /> *$0.10 per hour × 24 hours per day × 15 days = $36.00*  | $36.00 |
| Amazon EKS (pod compute) | Migration Console (1.5 vCPU, 2 GiB):<br /> *vCPU: 1.5 × $0.04048 × 24 × 15 = $21.86* <br /> *Memory: 2 × $0.004445 × 24 × 15 = $3.20*  | $25.06 |
| Amazon EKS (pod compute) | Platform pods (Argo Workflows controller and server, Strimzi operator, cert-manager, OTEL Collector, Fluent Bit, Prometheus):<br /> *Total: 3.5 vCPU, 6.4 GiB aggregate resource requests* <br /> *vCPU: 3.5 × $0.04048 × 24 × 15 = $50.93* <br /> *Memory: 6.4 × $0.004445 × 24 × 15 = $10.24* <br />[NOTE] ==== Platform pods provide workflow orchestration (Argo Workflows), Kafka operator (Strimzi), TLS certificate management (cert-manager), metrics and trace collection (OTEL Collector), log forwarding (Fluent Bit), and metrics storage (Prometheus). ==== | $37.71 |
| Amazon EBS | Prometheus persistent volume (50 GiB, gp3):<br /> *(50 × $0.08 per GiB-month × 15 days) / 30 days per month = $2.00*  | $2.00 |
| Amazon Virtual Private Cloud (Amazon VPC) | NAT Gateway (2 Availability Zones):<br /> *2 × $0.045 per hour × 24 hours per day × 15 days = $32.40* <br /> *Data processed: 30 GB × $0.045 per GB = $1.35* <br />VPC Interface Endpoints (CloudWatch Logs, Amazon EFS, Amazon ECR API, Amazon ECR Docker — 2 AZs each):<br /> *4 endpoints × 2 AZs × $0.01 per hour × 24 hours per day × 15 days = $28.80*  Amazon S3 Gateway Endpoint is free. VPC Interface Endpoints reduce data transfer cost for in-VPC traffic.  | $62.55 |
| AWS Secrets Manager |  *($0.40 per secret-month × 10 secrets × 15 days) / 30 days per month = $2.00*  | $2.00 |
| Amazon Elastic Container Registry (Amazon ECR) |  *(3 GiB × $0.10 per GiB-month × 15 days) / 30 days per month = $0.15*  | $0.15 |
|  **Core services total:**  |  |  **$165.47**  |
|  **Miscellaneous services**  |  |  |
| Amazon CloudWatch |  This is a high estimate for aggregated charges over all components for a large migration. Log data ingested (200 GB):<br /> *$0.50 per GB × 200 GB = $100.00* <br />Archived log charges (assume log data compresses to 30 GB):<br /> *($0.03 per GB-month × 30 GB × 15 days) / 30 days per month = $0.45* <br />Metrics (200 metrics):<br /> *(200 metrics × $0.30 per metric-month × 15 days) / 30 days per month = $60.00*  Metrics are metered only while being sent. Actual usage and cost might be lower.  | $160.45 |
| AWS X-Ray |  *1M traces × $5.00 per million traces = $5.00*  | $5.00 |
|  **Miscellaneous services total:**  |  |  **$165.45**  |
|  **Capture proxy and Kafka (7.776 TB captured over 6 days; 4 days data retention)**  |  |  |
| Amazon EKS (pod compute) | Capture Proxy pods (4 pods × 0.5 vCPU, 2 GiB each, 6 days):<br /> *vCPU: 4 × 0.5 × $0.04048 × 24 × 6 = $11.66* <br /> *Memory: 4 × 2 × $0.004445 × 24 × 6 = $5.12*  | $16.78 |
| Elastic Load Balancing | Network Load Balancer (6 days):<br /> *NLB hours: $0.0225 per hour × 24 × 6 = $3.24* <br /> *NLB Capacity Units (processed bytes): 7,776 GB / (6 × 24 hours) = 54 NLCUs average × $0.006 per NLCU-hour × 144 hours = $46.66*  | $49.90 |
| Amazon EKS (pod compute) | Strimzi Kafka broker pods (3 brokers × 1 vCPU, 4 GiB each, 10 days):<br /> *vCPU: 3 × 1 × $0.04048 × 24 × 10 = $29.15* <br /> *Memory: 3 × 4 × $0.004445 × 24 × 10 = $12.80*  | $41.95 |
| Amazon EBS | Kafka persistent volumes (gp3): Storage is sized for peak capture volume with a 20% buffer and the workflow-managed Kafka default of three topic replicas. This default favors durability during migration; reducing topic replicas through `kafkaClusterConfiguration.<cluster>.autoCreate.topicSpecOverrides.replicas` lowers storage cost but also lowers fault tolerance for captured traffic. <br /> *27,994 GiB provisioned × $0.08 per GiB-month × 10 days / 30 days per month = $746.51*  | $746.51 |
|  **Capture proxy and Kafka total:**  |  |  **$855.14**  |
|  **Replay (7.776 TB over 2 days, retention 4 days)**  |  |  |
| Amazon EKS (pod compute) | Traffic Replayer pod (1 pod × 1 vCPU, 4 GiB, 2 days):<br /> *vCPU: 1 × $0.04048 × 24 × 2 = $1.94* <br /> *Memory: 4 × $0.004445 × 24 × 2 = $0.85*  | $2.79 |
| Amazon Elastic File System (Amazon EFS) |  Replay tuples store source and target request/response pairs. Volume = 7.776 TB × 2 = 15.552 TB. Actual cost might differ due to some data spending less than 5 days in EFS Infrequent Access or data inflation. EFS Standard (infrequent after 1 day):<br /> *15,552 GiB × $0.30 per GiB-month × 1 day / 30 days per month = $155.52* <br />EFS Infrequent Access (5 days maximum):<br /> *15,552 GiB × $0.025 per GiB-month × 5 days / 30 days per month = $64.80* <br />EFS Infrequent Access - Tiering:<br /> *15,552 GiB × $0.01 per GiB = $155.52*  | $375.84 |
|  **Replay total:**  |  |  **$378.63**  |
|  **Historical Backfill (100 TB snapshot, 3 days RFS)**  |  |  |
| Amazon EKS (pod compute) | RFS worker pods:<br />Each pod delivers approximately 5 MBps of snapshot data. To deliver 100 TB over 3 days, 77 pods are needed.<br /> *vCPU: 77 pods × 2 vCPU × $0.04048 × 24 × 3 = $448.84* <br /> *Memory: 77 pods × 4 GiB × $0.004445 × 24 × 3 = $98.57* <br /> *Ephemeral storage: 77 pods × (200 GiB − 20 GiB free tier) × $0.000111 per GiB-hour × 24 × 3 = $110.77*  | $658.18 |
| Amazon S3 |  This calculates the cost for all the data residing in the S3 bucket for the entire duration. The actual cost might be less for storage due to partial rate while the snapshot is being taken. Snapshot storage:<br /> *(100 TB × 1,000 GiB per TB × $0.023 per GiB-month × 10 days) / 30 days per month = $766.67*  | $766.67 |
|  **Historical Backfill total:**  |  |  **$1,424.85**  |
|  **Total for all components:**  |  |  **$2,989.54**  |

The Capture and Replay yields an effective cost per TB of $158.66, and the Historic Backfill is $14.25 per TB. For a given cluster, the amount of data in Historic Backfill is largely fixed, while the data for Capture and Replay is based on the time needed to capture. For this reason, it can be cost advantageous to scale up the Amazon OpenSearch Service domain beyond the final intended capacity for the Historic Backfill period to reduce the duration and quantity of data for Capture and Replay.

Taking the table above and dividing out the component costs, we can determine the following calculation method for cost. This is a broad estimation making assumptions on traffic pattern including size per request and number of new connections. We can also subdivide this by migration type applicable.

| Component | Applicable migration type | Cost [USD] |
| --- | --- | --- |
| Core services |  +  Metadata only <br />+  Historical only <br />+  Live only <br />+  Full migration   | $11.03/day |
| Miscellaneous services |  +  Metadata only <br />+  Historical only <br />+  Live only <br />+  Full migration   | $165.45 per large migration |
| Capture runtime |  +  Live only <br />+  Full migration   | $9.31/day \+ $9.60/TB-day (Kafka EBS) \+ $6.00/TB (NLB) |
| Capture data retention period |  +  Live only <br />+  Full migration   | $5.97/day \+ $9.60/TB-day (Kafka EBS) |
| Snapshot |  +  Historical only <br />+  Full migration   | $0.7667/TB-day |
| Snapshot data retention period |  +  Historical only <br />+  Full migration   | $0.7667/TB-day |
| Reindex from snapshot |  +  Historical only <br />+  Full migration   | $6.58/TB |
| Traffic Replayer |  +  Live only <br />+  Full migration   | $1.40/day \+ $40.00/TB (EFS) \+ $1.6667/TB-day (EFS IA) Due to Amazon EFS Intelligent-Tiering, $1.6667/TB-day is not paid for the first day.  |
| Traffic Replayer data retention period |  +  Live only <br />+  Full migration   | $1.6667/TB-day |

We can also identify the cost for full migrations of different sizes that follow the 15-day migration timeline. By applying the durations shown previously, as well as a conversion from TB/day to MBps, we get the following formula for a representative cost estimate:

 *15-day migration ≈ $396 \+ $14.25 × HistoricalTB \+ $77.93 × LiveMBps*

This results in the following cost estimates table:

**Note**
All costs are rounded to the nearest dollar.

| 15-day full migration cost ($ USD/migration) |  | Live traffic throughput |  |
| --- | --- | --- | --- |
| Historical data volume | 5 MBps | 20 MBps | 50 MBps |
| 1 TB | $800 | $1,969 | $4,307 |
| 10 TB | $928 | $2,097 | $4,435 |
| 100 TB | $2,210 | $3,379 | $5,717 |

## Cost optimization tips
<a name="cost-optimization-tips"></a>
+  **Spot Instances for RFS workers**: RFS workers are stateless and checkpoint progress. Configure the Karpenter NodePool’s `karpenter.sh/capacity-type` requirement to include `spot` to use Spot Instances for up to 70% savings on backfill compute.
+  **Scale the target cluster during backfill**: A larger target processes documents faster, reducing the capture window and overall Kafka storage and EFS costs.
+  **Right-size Kafka retention**: If replay catches up quickly, reduce the Kafka log retention to free EBS storage sooner.
+  **Use VPC Interface Endpoints**: Already included in this estimate — these reduce NAT Gateway data processing charges for traffic to AWS services.

## Deprecated: Legacy Amazon ECS deployment cost estimate
<a name="cost-legacy-ecs"></a>

**Note**
The following cost estimate applies to the legacy Amazon ECS deployment of Migration Assistant (version 2.x and earlier). This deployment model uses AWS Fargate tasks on Amazon ECS, Amazon MSK for Kafka, and Application Load Balancers. It is provided for reference only. New deployments should use the Amazon EKS deployment described above.

The legacy ECS deployment of the same 15-day, 100 TB, 15 MBps scenario costs approximately **$3,096** with the following formula:

 *15-day migration = $390.35 \+ $14.24 × HistoricalTB \+ $71.86 × LiveMBps*

| 15-day full migration cost ($ USD/migration) |  | Live traffic throughput |  |
| --- | --- | --- | --- |
| Historical data volume | 5 MBps | 20 MBps | 50 MBps |
| 1 TB | $764 | $1,842 | $4,125 |
| 10 TB | $892 | $1,970 | $3,252 |
| 100 TB | $2,174 | $3,252 | $5,407 |

The primary cost difference between the EKS and legacy ECS deployments comes from replacing Amazon MSK with Strimzi Kafka on Amazon EKS (EBS gp3 storage at $0.08/GiB-month versus MSK storage at $0.10/GiB-month with per-broker duplication) and eliminating intra-region MSK data transfer charges. The EKS deployment adds a fixed cluster fee ($0.10/hr) and VPC Interface Endpoint charges, but these are offset by the Kafka savings at moderate-to-high traffic volumes.
