---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mes-on-aws/edge.html
---

# Industrial edge computing
<a name="edge"></a>

MES is critical to manufacturing operations. Some microservices or functionalities within MES require low latency and cannot tolerate intermittent connectivity to the cloud. These microservices are better suited to run on premises. [AWS edge services](https://aws.amazon.com/edge/) extend infrastructure, services, APIs, and tools offered in the cloud to an on-premises data center or co-location space. AWS services for the edge are available for infrastructure, storage, content delivery, rugged and disconnected edge, robotics, machine learning, and IoT.

## Architecture
<a name="edge-architecture"></a>

Many MES transactions are latency-sensitive. One of the examples cited later in this guide is the production execution service. One of the functions of the production execution service is to guide the flow of work-in-progress goods. Because this is a sensitive activity, the tolerance for latency could be low, and manufacturers might need an on-premises component of this microservice.

Here is the sample architecture for this use case.

![MES architecture for industrial edge computing use cases](http://docs.aws.amazon.com/prescriptive-guidance/latest/mes-on-aws/images/guide-img/093538ca-c7c9-4311-a0e9-8a876ae66d65/images/3565c1f2-f424-4881-9565-f8cff47c9fc7.png)

1. Amazon Elastic Kubernetes Service (Amazon EKS) for computing and Amazon Relational Database Service (Amazon RDS) for databases are hosted locally in AWS Outposts. You can also use self-managed hardware to host edge components. Some features, such as Amazon EKS Anywhere, can be used for self-managed hardware as well.

1. The edge component of these services can sync with the cloud component through an Amazon API Gateway endpoint between two container instances.

   Another option is to set up a service bus between the two container instances to keep them in sync. You can use Amazon Managed Streaming for Apache Kafka (Amazon MSK) to set up such service buses.

1. Manufacturers can use the cloud components of microservices to process cases that are less sensitive to latency, such as sending updates to a PLM system for process improvement, sending confirmations to an ERP system for production, and exporting data to a data lake for reporting and analytics. Because of the cloud's economics, scale, and disaster recovery benefits, manufacturers can store data for extended periods in cloud instances of the microservice.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
