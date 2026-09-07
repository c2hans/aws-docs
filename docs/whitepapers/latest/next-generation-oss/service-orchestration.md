---
source_url: https://docs.aws.amazon.com/whitepapers/latest/next-generation-oss/service-orchestration.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Service Orchestration
<a name="service-orchestration"></a>

 AWS services enable an event-driven Service Orchestration (SO) architecture, which leverages AWS serverless services such as and [AWS Lambda](https://aws.amazon.com/lambda) and [AWS Step Functions](https://aws.amazon.com/step-functions/). The following reference architecture enables you to build SOs that are aligned with European Telecommunications Standards Institute (ETSI) Management and Orchestration (MANO) while enabling cost optimization, security, scalability, and innovation. Similarly, AWS Partners’ ecosystems enable you to leverage ready-to-be-deployed SO solution.

![Diagram showing Service Orchestration Architecture on AWS](https://docs.aws.amazon.com/whitepapers/latest/next-generation-oss/images/service-orchestration-architecture.png)

 This architecture highlights the exposure/integration layer of a service orchestration platform, which leverages [Amazon API Gateway](https://aws.amazon.com/api-gateway) (and integration services such as [AWS Step Functions](https://aws.amazon.com/step-functions/)/[EventBridge](https://aws.amazon.com/eventbridge) as mentioned in a previous section) for both internal API interactions (such as the other OSS modules highlighted, and BSS), as well as external API integrations (e.g., integrating with AWS Partners’ orchestrator or B2B digital platform).

 Core orchestration capabilities highlighted in the application layer are comprised of adapters, workflow engine, catalog services, inventory services, and service management, and can be deployed as containers leveraging Amazon EKS in a shared cluster/namespace. With these functional capabilities implemented as Kubernetes jobs, they can be scheduled and scaled, dynamically leveraging [AWS Fargate](https://aws.amazon.com/fargate) as a serverless compute engine, thus maximizing resource utilization within the cluster.

 Stateful/persistent data (required for drive service orchestration such as inventory, config, and catalog data) are de-coupled from the orchestration process and offloaded to managed database services such as [Amazon RDS](https://aws.amazon.com/rds/), [Amazon Aurora](https://aws.amazon.com/rds/aurora/), [Amazon Neptune](https://aws.amazon.com/neptune), and [Amazon Keyspaces (for Apache Cassandra) (Amazon Keyspaces)](https://aws.amazon.com/keyspaces). As a result, this persistent layer can be scaled independently from the orchestration logic layer, and since it has been de-coupled you can easily enable cross-domain service orchestration use cases.

 To support emerging event-driven/policy-driven architecture patterns, the proposed architecture also enables asynchronous flows to be handled by a serverless, event-driven, layer-utilizing native service such as [Amazon SQS](https://aws.amazon.com/sqs/) for queuing, as well as the following serverless, implementation-leveraging functions: [AWS Step Functions](https://aws.amazon.com/step-functions/), [Amazon EventBridge](https://aws.amazon.com/eventbridge), and [AWS Lambda](https://aws.amazon.com/lambda). Over time, we expect more service-orchestration transactions could be moved towards an event-driven approach, which serves to further reduce the deployment footprint of the service orchestration platform.
