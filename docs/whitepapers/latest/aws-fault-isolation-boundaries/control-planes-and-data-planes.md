---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/control-planes-and-data-planes.html
---

# Control planes and data planes
<a name="control-planes-and-data-planes"></a>

 AWS separates most services into the concepts of *control plane* and *data plane*. These terms come from the world of networking, specifically routers. The router’s data plane, which is its main functionality, is moving packets around based on rules. But the routing policies have to be created and distributed from somewhere, and that’s where the control plane comes in.

 Control planes provide the administrative APIs used to create, read/describe, update, delete, and list (CRUDL) resources. For example, the following are all control plane actions: launching a new [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2) instance, creating an [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) bucket, and describing an [Amazon Simple Queue Service](https://aws.amazon.com/sqs/) (Amazon SQS) queue. When you launch an EC2 instance, the control plane has to perform multiple tasks like finding a physical host with capacity, allocating the network interface(s), preparing an [Amazon Elastic Block Store](https://aws.amazon.com/ebs/) (Amazon EBS) volume, generating IAM credentials, adding the Security Group rules, and more. Control planes tend to be complicated orchestration and aggregation systems.

 The data plane is what provides the primary function of the service. For example, the following are all parts of the data plane for each of the services involved: the running EC2 instance itself, reading and writing to an EBS volume, getting and putting objects in an S3 bucket, and Route 53 answering DNS queries and performing health checks.

 Data planes are intentionally less complicated, with fewer moving parts compared to control planes, which usually implement a complex system of workflows, business logic, and databases. This makes failure events statistically less likely to occur in the data plane versus the control plane. While both the data and control plane contribute to the overall operation and success of the service, AWS considers them to be distinct components. This separation has both performance and availability benefits.
