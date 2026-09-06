---
source_url: https://docs.aws.amazon.com/whitepapers/latest/next-generation-oss/service-assurance.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Service Assurance
<a name="service-assurance"></a>

 This section presents a service assurance architecture on AWS that provides you with the scalability, flexibility, reliability, and innovation to enable a fully-automated network that identifies issues and heals itself. The following reference architecture depicts this as well as illustrates key services enabling such automation.

![Diagram showing Service Assurance Architecture on AWS](http://docs.aws.amazon.com/whitepapers/latest/next-generation-oss/images/service-assurance-architecture.png)

 [Kinesis](https://aws.amazon.com/kinesis/) can be leveraged to ingest network events from all DSPs NFx. Kinesis provides you with the scalability to ingest alarms and configuration changes when they occur. It also enables you to integrate with AWS services to perform operations based on the ingested event. For example, a network event from NFx, ingested through Kinesis, can trigger an [AWS Step Functions](https://aws.amazon.com/step-functions/) that orchestrates a workflow; this workflow could correlates three things to trigger a corrective action to the network:
+ KPIs available through a data lake query
+ Network configuration validation using an [AWS Lambda](https://aws.amazon.com/lambda/) function
+ Leveraging a prediction model using [Amazon Sagemaker](https://aws.amazon.com/sagemaker/)

The workflow and the result of the workflow can be achieved using a low-code visual workflow designer, [Workflow Studio for AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/workflow-studio.html). The previously described services and the type of workflow enables you to identify when a network component/service is degraded, provide that status across the OSS stack, and act on that status to correct the situation.

 [Amazon EMR](https://aws.amazon.com/emr) or partner products can be used to store a vast amount of data. EMR simplifies the processing of data and removes the operational complexities associated with provisioning and tuning of big data clusters. The flexibility that EMR provides you with enables you to process trained data at a low cost. Mobility use cases often require 2-5 weeks of network data, and EMR enables you to only spin up the required compute capacity once training data is available.

 By decoupling persistent data layer from the application layer through usage of managed services (e.g., [Amazon Aurora](https://aws.amazon.com/rds/aurora/) and [Amazon Neptune](https://aws.amazon.com/neptune)), data is easily consumed by applications within the OSS stack, enabling closed loop use cases. For example, real-time state of inventory can be used to input service orchestration and fulfillment.

 Finally, [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) is used to scale up or down based on demand, and thus optimal usage of infrastructure is achieved and total cost of ownership is optimized. An OSS solution on AWS scales with the network as network events occur.
