---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/building-ha-applications-and-infrastructure-solutions-with-aws-outposts.html
---

# Building HA applications and infrastructure solutions with AWS Outposts rack
<a name="building-ha-applications-and-infrastructure-solutions-with-aws-outposts"></a>

 With AWS Outposts rack, you can build, manage, and scale highly available on-premises applications using familiar AWS cloud services and tools. It's important to understand cloud HA architectures and approaches are generally different from traditional on-premises HA architectures you may be running in your datacenter today.

 With traditional on-premises HA application deployments, applications are deployed in virtual machines (VMs). Complex IT systems and infrastructure are deployed and maintained to keep those virtual machines running and healthy. The VMs often have specific identities and each VM may play a critical role in the total application architecture.

 Architectural roles are tightly coupled to VM identities. Systems architects leverage IT infrastructure features to provide highly available VM runtime environments that provide each VM with reliable access to compute capacity, storage volumes, and network services. If a VM fails, automated or manual recovery processes are run to restore the failed VM to a healthy state, often on other infrastructure or in another datacenter entirely.

 Cloud HA architectures take a different approach. AWS cloud services provide reliable compute, storage, and networking capabilities. Application components are deployed to EC2 instances, containers, serverless functions, or other managed services.

 An instance is an instantiation of an application component – perhaps one of many performing that role. Application components are loosely coupled to one another and to the role they play in the total application architecture. The individual identity of an instance is generally not important. Additional instances may be created or destroyed to scale up or scale down in response to demand. Failed instances or unhealthy instances are simply replaced with new healthy instances.

 AWS Outposts rack is a fully managed service that extends AWS compute, storage, networking, database, and other *cloud services* to on-premises locations for a truly consistent hybrid experience. You should not think of the Outposts rack service as a drop-in replacement for IT infrastructure systems with traditional on-premises HA mechanisms. Attempting to use AWS services and Outposts to support a traditional on-premises HA architecture is an anti-pattern.

 Workloads running on AWS Outposts rack *use cloud HA mechanisms* like [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) (to scale horizontally to meet workload demands), [EC2 health checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/healthcheck.html) (to detect and remove unhealthy instances), and [Application Load Balancers](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/) (to redirect incoming workload traffic to scaled or replaced instances). When migrating applications to the cloud, whether to an AWS Region or AWS Outposts rack, you should update your HA application architecture to begin taking advantage of managed cloud services and cloud HA mechanisms.

 The following sections introduce architecture patterns, anti-patterns, and recommended practices for deploying AWS Outposts rack in your on-premises environments to run workloads with high availability requirements. These sections introduce patterns and practices; however, they do not provide configuration and implementation details. You should read and become familiar with the [AWS Outposts rack FAQs](https://aws.amazon.com/outposts/rack/faqs/) and [User Guide](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html) and the FAQs and service documentation for the services that run on Outposts rack as you prepare your environment for Outposts rack and your applications for migration to AWS services.

**Topics**
+ [Networking](networking.md)
+ [Compute](compute.md)
+ [Storage](storage.md)
+ [Databases](databases.md)
+ [Larger failure modes](larger-failure-modes.md)
