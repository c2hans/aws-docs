---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-with-aws/hybrid-cloud-use-cases.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Hybrid cloud use cases
<a name="hybrid-cloud-use-cases"></a>

 These use cases help you identify and define your business objectives for building a hybrid cloud, such as ongoing migration to the cloud, ensuring business continuity during disasters, extending cloud infrastructure on-premises to support low-latency applications, or expanding your international footprint on AWS.

## Application migration to the cloud
<a name="application-migration-to-the-cloud"></a>

 Large migrations from on-premises datacenters to AWS may involve thousands of applications and can take several years. Customers require a consistent operational environment across their hybrid cloud while they migrate their applications, to ensure business continuity. [Johnson & Johnson](https://aws.amazon.com/solutions/case-studies/johnson-and-johnson/) and [Hess Corporation](https://aws.amazon.com/solutions/case-studies/hess-corporation/) created a hybrid cloud environment to support their migration to AWS.

 You may want to leverage your on-premises investments in VMware while taking advantage of the agility and scalability offered by the AWS Cloud. AWS has partnered with VMware to enable you to migrate and run your VMware vSphere workloads on AWS, and leverage native AWS services for your on-premises environments through [VMware Cloud on AWS](https://aws.amazon.com/vmware/). [Stagecoach Group](https://aws.amazon.com/solutions/case-studies/stagecoach-vmware/) has adopted VMware Cloud on AWS to accelerate their migration to AWS.

## Cloud services on-premises
<a name="cloud-services-on-premises"></a>

 Some applications have data residency, high data transfer costs, local data processing, or low-latency requirements. These applications must be deployed on-premises or close to the end users/systems. Customers want to seamlessly integrate these applications with their cloud deployments in a hybrid cloud environment to ensure operational consistency.

 Similarly, customers who primarily operate on AWS may need to deploy applications on-premises for local data processing or low-latency needs. These customers want to continue leveraging existing cloud skill sets and tools that they have invested in for these on-premises deployments.

 To support these use cases, [AWS Outposts](https://aws.amazon.com/outposts/) provides a consistent hybrid cloud solution that brings the same AWS infrastructure, services, APIs, management tools, support, and operating model that customers are familiar with, in [AWS Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/), to virtually any data center, co-location space, or on-premises facility. [VMware Cloud on AWS](https://aws.amazon.com/vmware/) provides an integrated cloud offering jointly developed by AWS and VMware. Additionally, using [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS) on [VMware](https://aws.amazon.com/rds/vmware/), you can deploy managed databases in on-premises VMware environments using the same Amazon RDS technology they use in the cloud.

## Data center extension
<a name="data-center-extension"></a>

 With [data center extension](https://www.vmware.com/topics/data-center-extension), the AWS Cloud is an extension of your on-premises infrastructure to support applications that need to run on-premises. There are four broad use-cases:

### Cloud bursting
<a name="cloud-bursting"></a>

 Cloud bursting is an application deployment model in which the application primarily runs in an on-premises infrastructure, and when the demand for capacity increases, AWS resources are utilized. Customers like [FuseFX](https://aws.amazon.com/solutions/case-studies/fusefx/), [Pacific Life Insurance](https://aws.amazon.com/solutions/case-studies/pacific-life-insurance/), and Dropbox burst compute and storage resources to AWS from on-premises. There are two main reasons to use cloud bursting:
+  **Bursting for compute resources**: You consume burst compute capacity on AWS through [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2) (Amazon EC2) and [managed container services](https://aws.amazon.com/containers/services/) of the [Amazon Elastic Container Service](https://aws.amazon.com/ecs/) (Amazon ECS), [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (Amazon EKS), and [AWS Fargate](https://aws.amazon.com/fargate/).
+  **Bursting for storage**: In addition to integrating applications with [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) [APIs](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html), [AWS Storage Gateway](https://aws.amazon.com/storagegateway/) enables on-premises workloads to use AWS Cloud storage. Capabilities such as [File Gateway](https://aws.amazon.com/storagegateway/file/), [Tape Gateway](https://aws.amazon.com/storagegateway/vtl/) and [Volume Gateway](https://aws.amazon.com/storagegateway/volume/) help enable cloud bursting capabilities for block and file storage.

### Backup and disaster recovery
<a name="backup-and-disaster-recovery"></a>

 Customers like [Scripps Network Interactive](https://aws.amazon.com/solutions/case-studies/scripps-network-interactive/) implement a hybrid infrastructure with AWS for their application disaster recovery needs for applications that reside on-premises. AWS services like [Amazon S3 APIs](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html), AWS Storage Gateway, [AWS Backup](https://aws.amazon.com/backup/), [AWS DataSync](https://aws.amazon.com/datasync/) and [AWS Transfer for SFTP](https://aws.amazon.com/sftp/) enable you to implement a disaster recovery strategy with AWS for your data hosted on-premises.

### Distributed data processing
<a name="distributed-data-processing"></a>

 Customers often deploy applications across on-premises data centers and AWS, with functionality split between the infrastructures. Most commonly, low-latency or local data processing components reside on-premises and other functionality, including asynchronous processing, archiving, compliance, business analytics processing, or machine learning-based predictions reside on AWS. AWS services like [AWS Storage Gateway](https://aws.amazon.com/storagegateway/), [AWS Backup](https://aws.amazon.com/backup/), [AWS DataSync](https://aws.amazon.com/datasync/), [AWS Transfer Family](https://aws.amazon.com/aws-transfer-family/), [Amazon Data Firehose](https://aws.amazon.com/kinesis/firehose/) and [Amazon Managed Streaming for Apache Kafka](https://aws.amazon.com/msk/) (Amazon MSK) enable you to import data into AWS for data processing needs. When the data is imported, you can leverage AWS services like [AWS Analytics](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/analytics.html), [AWS Machine Learning](https://aws.amazon.com/machine-learning/), [AWS Serverless](https://aws.amazon.com/serverless/), [AWS Containers](https://aws.amazon.com/containers/), and more to process the data. Distributed data processing using AWS Services enables you to leverage AWS innovations in these areas, while meeting the requirements of low-latency or local data processing for the application.

### Geographic expansion
<a name="geographic-expansion"></a>

 You may need to deploy applications closer to your end users for compliance, data sovereignty, low-latency, or local data processing needs. Deploying physical infrastructure in new geographical areas can become prohibitively expensive, or constrained by legal requirements and local laws. Customers like Dropbox leverage [AWS global infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/) as an extension to their existing infrastructure to deploy their applications and make them available globally.

 You can also deploy workloads in AWS Outposts in countries where AWS does not have an AWS Region yet. See the [AWS Outposts](aws-hybrid-cloud-solutions.md#aws-outposts) section of this whitepaper.

## Edge computing
<a name="edge-computing"></a>

 You may have [edge computing](https://en.wikipedia.org/wiki/Edge_computing) needs at facilities like factories, mines, ships and windmills. AWS provides edge computing with [AWS Snowball Edge](https://aws.amazon.com/snowball-edge/), [AWS IoT Greengrass](https://aws.amazon.com/greengrass/), and [AWS Wavelength](https://aws.amazon.com/wavelength/).

 With AWS Snowball Edge edge computing, customers operating in disconnected, harsh, or air-gapped environments can pre-process information before transferring data to the cloud for durable retention and more advanced analysis. They can perform sophisticated analytics, machine learning, and run fully disconnected applications for traditional IT workloads on Amazon EC2 compute resources.

 With [AWS IoT Greengrass](https://aws.amazon.com/greengrass/), you can enable devices and equipment to respond to local events in near real-time by acting locally on the data they generate. [AWS Lambda](https://aws.amazon.com/lambda/) functions deployed on AWS IoT Greengrass Core devices can use local device resources like cameras, serial ports, or GPUs, so device applications can quickly access and process local data. Devices can stay operational and function seamlessly, even with intermittent connectivity to the cloud.

 You can reduce the cost of running edge applications by using AWS IoT Greengrass to filter locally before transmitting to the cloud. [AWS Wavelength](https://aws.amazon.com/wavelength/) is an AWS Infrastructure offering optimized for mobile edge computing applications. Wavelength Zones are AWS infrastructure deployments that embed AWS compute and storage services within communications service provider (CSP) data centers at the edge of the 5G network, so application traffic from 5G devices can reach application servers running in Wavelength Zones without leaving the telecommunications network.

## ISV and software compatibility
<a name="isv-and-software-compatibility"></a>

 If you want run the same independent software vendor (ISV) software that you run on-premises in a hybrid or distributed model, you can use the [AWS Marketplace](https://aws.amazon.com/marketplace), a curated digital catalog, to find, buy, deploy, and manage third-party software on AWS.

 AWS has [built the most complete and proven approach](https://aws.amazon.com/hybrid/use-cases/#Use_case.3A_ISV_and_software_compatibility) for rapidly migrating tens to thousands of applications to the AWS Cloud to help you leverage your existing on-premises ISV software investments.

 Recently, AWS launched the AWS Outpost [Service Ready](https://aws.amazon.com/partners/service-ready/) program, which offers products that integrate with AWS Outposts deployments. You can discover [products on this page](https://aws.amazon.com/outposts/partners) that are tested on AWS Outposts, and follow AWS security and architecture best practices. AWS Competency Partners are ready to help AWS customers migrate and deploy their applications to AWS Outposts. [AWS Partners](https://aws.amazon.com/outposts/partners/) validated through the AWS Service Ready Program offer products tested to integrate with AWS Outposts deployments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
