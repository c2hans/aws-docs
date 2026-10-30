---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/control-planes-and-data-planes.html
---

# Control planes and data planes
<a name="control-planes-and-data-planes"></a>

 AWS separates most services into control plane and data plane components. These terms originate from the world of networking, specifically routers. The router’s primary function is moving packets around based on rules; this is its data plane. Those rules are created and distributed from the router’s control plane.

 Control planes provide the administrative and configuration APIs used to create, read or describe, update, delete, and list (CRUDL) resources. For example, the following are all control plane actions: launching a new Amazon EC2 instance, creating an [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) bucket, and describing an [Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) (Amazon SQS) queue.

 Control planes tend to be complex workflow orchestration systems that use nuanced business logic with multiple dependencies. For example, when you launch an Amazon EC2 instance, the control plane has to perform multiple tasks like finding a physical host with capacity, allocating the network interfaces, preparing an [Amazon Elastic Block Store](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) (Amazon EBS) volume, generating IAM credentials, adding the security group rules, distributing networking information to other physical hosts, and more. If any one of those steps fails, the overall Amazon EC2 instance provisioning fails.

 The data plane, on the other hand, is what provides the primary function of the service. For example, the following are all parts of the data plane for each of the services involved:
+ For Amazon EC2 – The running instance
+ For Amazon EBS – Reading and writing to a volume
+ For Amazon S3 – Getting and putting objects in a bucket
+ For Route 53 – Answering DNS queries

 Data planes are intentionally simpler than control planes, resulting in fewer dependencies, which makes them more reliable.

 These differences mean that broad failure events are statistically less likely to occur in the data plane than the control plane. It also means that a dependency on the data plane will likely have higher availability than a dependency on the control plane. While both the data plane and control plane contribute to the overall operation and success of the service, AWS considers them to be distinct components. This separation has performance, scalability, and availability benefits. You can use the [Service Authorization Reference](https://docs.aws.amazon.com/service-authorization/latest/reference/service-reference.html) and the `IsDataPlane` property to identify each supported AWS service's data plane actions.
