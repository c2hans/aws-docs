---
source_url: https://docs.aws.amazon.com/whitepapers/latest/next-generation-oss/service-fulfillment.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Service Fulfillment
<a name="service-fulfillment"></a>

 This section presents a service fulfillment architecture on AWS that provides flexibility, scalability, reliability, and the integration points to enable the customer journey. As depicted by the following reference architecture, the proposed architecture enables you to seamlessly integrate with order management, service orchestration, service assurance, and domain managers across multiple networks and service domains. Services such as [Amazon API Gateway](https://aws.amazon.com/api-gateway/), [AWS App Mesh](https://aws.amazon.com/app-mesh/), and [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC) provide you with the ability to develop service fulfillment applications that are fully integrated with service orchestration applications and service assurance applications, enabling you to eliminate functional duplication and choose delimitation based on a given technology, network, and service type. For example, [Amazon Aurora](https://aws.amazon.com/rds/aurora/) provides you with a MySQL and PostgreSQL-compatible relational database that can host inventory data used both in service fulfillment and orchestration. While your fulfilment can act as a central location of the inventory data for network services, Amazon Aurora enables you to define read-replicas. This enables you to support low-latency reading of network services for your service orchestration to speed up decision-making while providing APIs to govern provisioning requests at the fulfillment level.

![Diagram showing Service Fulfilment Architecture on AWS](http://docs.aws.amazon.com/whitepapers/latest/next-generation-oss/images/service-fulfilment-architecture.png)

 [Amazon EKS](https://aws.amazon.com/eks/) provides you with the ability to run Kubernetes applications that scale. To achieve high availability and resiliency, the pods are distributed across multiple [AZs](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/). [AWS' purpose-built database services](https://aws.amazon.com/products/databases/) for Graph DB, NoSQL, and RDBMS, can further help you achieve your goals. An ingress gateway fronts the communication to and between your applications and uses the AWS native service [AWS App Mesh](https://aws.amazon.com/app-mesh/) to provide application networking, and offer end-to-end visibility and high availability.

 AWS Step Functions allows you to seamlessly integrate service fulfillment applications with order management applications, allowing you to execute a multitude of events (such as dependency verification, dates, location validation, breaking tasks into sub-tasks, and executing the configuration on an individual network function).

 Dynamic service inventory management is done by using [Amazon Relational Database Service](https://aws.amazon.com/rds/) (RDS) and [graph databases](https://aws.amazon.com/neptune/) to depict the relationship of a service, its status, and the underlying provisioned resources.

 Fulfilment tracking in near real-time is enabled by [Amazon Simple Notification Service](https://aws.amazon.com/sns/?) (Amazon SNS) and [Amazon Simple Queue Service](https://aws.amazon.com/sqs/)(SQS). It provides you with the mechanisms to control how fulfillment operations interact within the service fulfilment stack as well as between other applications in the OSS Stack.
