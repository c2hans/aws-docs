---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-magento-open-source-adobe-commerce-to-aws/aws-architecture-components.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS architecture components
<a name="aws-architecture-components"></a>

 As you plan your migration from an on-premises environment to AWS, you might find yourself introduced to new concepts. The first of those is the concept of managed services, which, simply defined, is a specific capability delivered as a service. For example, Amazon Elastic File System (Amazon EFS) provides network file system (NFS) based storage, eliminating the need to otherwise manage a fleet of EC2 instances to accomplish the same.

 Another might be the scaling of shared services – so whereas before your on-premises environment may have consisted of a cluster of load balancing appliances, AWS offers (in a similar fashion as Amazon EFS described above) Elastic Load Balancing as a service, allowing you to manage the components used to deliver Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service in an end-to-end fashion.

 Yet another concept might be the physical architecture of AWS – where a singular AWS Region comprises numerous groups of physically isolated datacenters (each group of data centers is referred to as an Availability Zone), providing native support for not just N\+1 or active/passive or active/active resiliency, but doing so in physically distributed manner without implementing complex solutions.

 In line with these previously described services, where an on-premises implementation of Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service might look like shared domain, networking, and load balancing services with an external content delivery network, all running on one or more servers (physical or virtual), in AWS, you may find yourself using any number of services to accomplish the same outcome from a service delivery perspective, while reducing cost and providing increased automation capabilities and increased scalability and resiliency capabilities.

## Types of services
<a name="types-of-services"></a>

 Continuing the concepts previously described, a typical collection of AWS services supporting your Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service environment, assuming no external or on-premises services are leveraged, might look like this:
+  [Amazon Route 53](https://aws.amazon.com/route53) for DNS
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront) for content delivery network
+  [Amazon S3](https://aws.amazon.com/s3) as remote storage for web server instances to store shared media files.
+  [Elastic Loading Balancing](https://aws.amazon.com/elasticloadbalancing/) through an Application Load Balancer for load balancing
+  [AWS Auto Scaling](https://aws.amazon.com/autoscaling) Groups of Amazon EC2 (virtual machine) instances for the Magento open-source or Adobe Commerce on cloud infrastructure self-service execution environment
+  [Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds) for the Magento open-source or Adobe Commerce on cloud infrastructure self-service database environment
+  [Amazon ElastiCache (Redis OSS)](https://aws.amazon.com/elasticache/redis) for session and configuration caching
+  [Amazon Simple Email Service (Amazon SES)](https://aws.amazon.com/ses) as your mail gateway
+  [Amazon MQ](https://aws.amazon.com/amazon-mq/?amazon-mq.sort-by=item.additionalFields.postDateTime&amazon-mq.sort-order=desc&trk=023e579b-fefa-4cea-8fe9-eca10449ac3a&sc_channel=ps&sc_campaign=acquisition&sc_medium=ACQ-P|PS-GO|Non-Brand|Desktop|SU|Application%20Integration|Solution|US|EN|DSA&ef_id=Cj0KCQjwyMiTBhDKARIsAAJ-9Vunw36OB9aDpHFdsHYXkliTVqLtbadyS3mjh0jNNHh6-DyuqguNkboaArI_EALw_wcB:G:s&s_kwcid=AL!4422!3!579408093299!!!g!!) (optional) is a message broker that offers a reliable, highly available, scalable, and portable messaging system.

 The above list, while detailed with regard to the Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service environment itself, excludes numerous services providing supporting infrastructure of your platform (such as [Amazon Virtual Private Cloud [Amazon VPC]](https://aws.amazon.com/vpc)) and as such this list should not be treated as a definitive list of services or requirements. Its intention is to illustrate the baseline AWS services you can use to host your Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service and eliminate unnecessary care and feeding of servers.

### Monitoring
<a name="monitoring"></a>

 An additional benefit to leveraging managed services is that each service provides observability via metrics ([CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)), logs ([CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)) and events ([CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html)) providing the often-sought single pane of glass around each of your Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service environments. This data can include performance, exceptions (both technical measures) as well as business measures such as cost per transaction (via the [CloudWatch API](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/Welcome.html)). This robust set of data, in addition to being available historically for reporting and near real time for dashboarding is also available for alerting – of both individuals in your organization and automations for self-healing processes.

 From an organizational operations perspective, each of the preceding services also support the application of arbitrary metadata (referred to as *tags*), which can be used to allocate costs (cost per environment, as an example), in conjunction with AWS configuration management service, [AWS Config](https://aws.amazon.com/config), as well as an AWS robust audit trail solution, [AWS CloudTrail](https://aws.amazon.com/cloudtrail), which provides insight into user or service access and change to AWS services.

 Finally, services such as Application Load Balancer integrate into [AWS X-Ray](https://aws.amazon.com/xray/), which is the AWS distributed application tracing solution which provides for additional instrumentation into the runtime environment of Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service and associated code.

### DevOps
<a name="devops-1"></a>

 Access to on-demand compute and managed services, along with a common set of operational capabilities (authentication, authorization and auditing via [AWS Identity and Access Management](https://aws.amazon.com/iam) and CloudTrail APIs, and SDKs available on a variety of platforms and common metric, log, and event ingestion services) support’s an organization’s goal towards automation.

 AWS provides numerous services that abstract procedural level automation of resource lifecycle management including [AWS CloudFormation](https://aws.amazon.com/cloudformation), [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/), [AWS OpsWorks](https://aws.amazon.com/opsworks/), [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/), and [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/), in addition to a rich ecosystem of third-party services such as [Terraform](https://aws.amazon.com/partners/find/partnerdetails/?n=HashiCorp&id=001E000001BxMyKIAV), [Ansible](https://aws.amazon.com/partners/find/partnerdetails/?n=Ansible&id=001E000000iLvuJIAS) and others.

 There are multiple approaches with regards to managing a code base running in a compute environment. One such approach is using [Amazon Machine Images (AMIs)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) where a machine image is programmatically configured at launch and cycled through with each code revision. Another approach is to statically maintain and configure managed machines leveraging agent or agent-based code deployment solutions. Lastly, container-based code deployments where a container is moved through different environments instead of code.

 Each of these have their own strengths and weaknesses, however, container-based code deployments are becoming more common and support additional compute services such as [AWS Fargate](https://aws.amazon.com/fargate/), a serverless container solution.

 Regardless of the approach, the primary objective should be to maintain the compute environments in a hands-off approach with best security practices and monitoring solutions that provide good operational support.

 For Magento, the management of the application lifecycle involves many of the same concepts, considered best practices and leveraged by other development platforms such as the use of a code repository and versioning (Git), separate build environments (for code compilation) and separate runtime environments (for example, development, and production). In addition, Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service supports the management of stores, cron entries, and so on, via the command line. This management logic can be built into the deployment pipeline. Also the configuration files can be versioned similar to code. Magento recommends management of assets via the same code repository as the application and configuration files, but this may create additional complexity, depending on the size of your application’s assets. As an alternative approach, you can use one-way synchronization between environment specific [Amazon Elastic File System (Amazon EFS)](https://aws.amazon.com/efs/) volumes.

![Reference architecture diagram for DevOps using containers](http://docs.aws.amazon.com/whitepapers/latest/migrating-magento-open-source-adobe-commerce-to-aws/images/reference-architecture-magento-containers.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
