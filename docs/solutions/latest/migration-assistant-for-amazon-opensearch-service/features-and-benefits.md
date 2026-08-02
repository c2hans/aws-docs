---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/features-and-benefits.html
---

# Features and benefits
<a name="features-and-benefits"></a>

The solution provides the following features:

 **Backfill with reindex-from-snapshot**

This solution guides users through the process of transferring data from a snapshot stored in an [Amazon Simple Storage Service](https://aws.amazon.com/s3) (Amazon S3) bucket to a designated Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection. The Reindex-from-Snapshot (RFS) engine reads Lucene segment files directly from snapshots in Amazon S3, which keeps load off the source cluster and lets backfill scale by running one worker per shard.

 **Live traffic capture and replay**

The solution offers guidance and tools to intercept traffic intended for an original cluster and archive it for future replay on a destination Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection. Typically, the replay occurs at the same rate and concurrency as the original traffic to precisely mimic the workload experienced by the source cluster. Users can choose to replay the recorded traffic subsequently or adjust the replay speed. This flexibility enables users to fine-tune the target cluster, enhancing its performance to suit their requirements.

 **Workflow-driven operations**

Migration Assistant 3.0 is built around a Workflow CLI that runs on Amazon EKS using Argo Workflows. You define the migration in workflow configuration once, submit it from the Migration Console pod, and the solution orchestrates snapshot creation, metadata migration, document backfill, traffic capture and replay, validation, and cutover as Kubernetes-managed steps. Built-in approval gates pause the workflow at meaningful checkpoints so you can validate progress before continuing.

 **Traffic validation**

The solution records requests and responses between the source and destination clusters for comparison. It then forwards the latency metrics and response codes to an analytics platform, enabling users to analyze the data essential for transitioning their traffic from a legacy system to a new Amazon OpenSearch Service destination. The solution stores each request and response for both the source and target for deeper inspection if needed.

 **Integration with AWS Service Catalog AppRegistry and Application Manager, a capability of AWS Systems Manager**

This solution includes a [Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html) resource to register the solution’s CloudFormation template and its underlying resources as an application in both Service Catalog AppRegistry and [Application Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager.html). With this integration, you can centrally manage the solution’s resources and enable application search, reporting, and management actions.
