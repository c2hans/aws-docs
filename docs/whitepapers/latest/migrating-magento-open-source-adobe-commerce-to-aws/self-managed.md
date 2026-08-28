---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-magento-open-source-adobe-commerce-to-aws/self-managed.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Self-managed
<a name="self-managed"></a>

 AWS provides three options to quickly get started with a self-managed deployment of Magento. By self-managed we mean that AWS or an AWS partner provides the scripting or Amazon Machine Image (AMI) to deploy Magento and the necessary infrastructure dependencies, such as EC2 instances, in your AWS account. Once deployed, you are responsible for managing the deployment going forward including monitoring, patching, and upgrading.

## Amazon Lightsail
<a name="amazon-lightsail"></a>

 Amazon Lightsail provides virtual servers, storage, databases, and networking that are easy-to-use and designed to allow you to quickly get started with the cloud. Popular application stacks, or blueprints, are available that can be deployed on Lightsail virtual servers. These stacks come preconfigured with all of the necessary components to get started with an application in minutes.

 The Magento application stack is provided by [Bitnami](https://aws.amazon.com/marketplace/pp/Bitnami-Magento-Certified-by-Bitnami/B00NNZTA6Y) and includes Apache, Varnish, Memcached, MySQL, and Magento Open Source bundled in an [AMI](https://aws.amazon.com/marketplace/pp/Bitnami-Magento-Certified-by-Bitnami/B00NNZTA6Y).

 From the Lightsail console in your AWS account, you simply select the AWS Region and availability zone where you want to launch Magento, choose an instance plan, and launch your instance. After a few minutes, your instance is deployed and ready to access. Although Magento and all of its dependencies come preconfigured, you can still securely access the instance using a browser-based SSH interface or your favorite SSH client to make lower level changes. The web-based Magento Administration user interface can also be used to create and customize your stores.

 With the simplicity and cost effectiveness of deploying Magento Open Source through Lightsail also comes some important tradeoffs. These tradeoffs are important to keep in mind when it comes to scalability, availability, and maintenance of your e-commerce site. First, the [Magento opensource AMI](https://aws.amazon.com/marketplace/pp/Bitnami-Magento-Certified-by-Bitnami/B00NNZTA6Y) provided by Bitnami that is used by Lightsail installs Adobe Commerce and all dependencies on a single instance. Although this keeps the deployment simple, it also limits the ability to scale your e-commerce site, creates multiple single points of failure (SPOF), and leaves you with the responsibility to patch and update dependencies such as Memcached and MySQL. Therefore, selecting Lightsail as a deployment option should only be considered for smaller e-commerce sites where you expect a consistently low level of traffic from visitors.

## AWS Marketplace
<a name="aws-marketplace"></a>

 The AWS Marketplace is an e-commerce site where AWS customers can discover, procure, and deploy solutions provided by AWS partners. Thousands of solutions are available across more than 1,000 categories including infrastructure, business applications, machine learning, and many others. Deployment options supported on the Marketplace include applications deployed directly into customer accounts via AMIs or Docker containers, Amazon SageMaker AI, or SaaS solutions. All software purchased through the Marketplace appears on the customer’s AWS invoice along with any other AWS resources consumed.

 Magento deployment options currently available in the AWS Marketplace are AMI-based. These offerings include Magento opensource and all the necessary dependencies such as MySQL, a web-server, and caching components. Therefore, AWS customers can deploy Magento open-source or Adobe Commerce on cloud infrastructure self-service directly into their AWS account and get it up and running within minutes.

 Similar to the Lightsail option, the customer is responsible for patching and upgrading Magento and its dependencies. In addition, the customer is responsible for configuring the networking environment, or Amazon Virtual Private Cloud (Amazon VPC), within which Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service is deployed. Lastly, customers should closely investigate and understand the scalability and high availability characteristics of each option, the Magento Open Source version bundled with each option, and any included customizations such as enhanced caching or multi-store setups. For example, some are all-in-one bundles that are intended to be deployed on a single Amazon EC2 instance. Although this provides a simpler configuration and lower cost, it introduces several single-points-of-failure and lacks the ability to take advantage of the cloud’s elasticity and high availability capabilities.

## AWS Quick Start for Magento Open Source
<a name="aws-quick-start-for-magento-open-source"></a>

 [Magento is an open-source content management system for](https://magento.com/products/magento-open-source) e-commerce websites. AWS enables you to set up the infrastructure to support deployment in a flexible, scalable, and cost-effective manner in the AWS Cloud. This reference deployment will help you rapidly build a Magento Open Source cluster by automating configuration and deployment tasks.

 The automated deployment builds a cluster that runs Magento version 2.4.3 or higher along with optional sample data.

 This guide covers the deployment of [Magento](https://magento.com/products/magento-open-source) Open Source in the AWS Cloud. It doesn’t provide Magento product usage information. For general guidance and best practices for using Magento, see the [Magento User Guide](http://docs.magento.com/m2/ce/user_guide/getting-started.html) on the Adobe website.

## Cost and licenses
<a name="cost-and-licenses"></a>

 This deployment launches Magento Open Source automatically into a configuration of your choice. You are responsible for the cost of the AWS services used while running this Quick Start reference deployment. There is no additional cost for using the Quick Start. The cost will vary depending on the storage and compute configuration of the cluster you deploy. See the pricing pages for each AWS service you will be using for full details.

 This Quick Start uses Magento Open Source (formerly Community Edition), which is open-source software distributed under the Open Software License (OSL 3.0).

## AWS components for Magento Open Source
<a name="aws-components-for-magento-open-source"></a>

Running this Quick Start with default parameters for a new VPC deploys and configures a VPC that spans two Availability Zones. Each Availability Zone is configured with a private and a public subnet. This Quick Start deploys the following AWS components in the AWS Cloud:
+  In a public subnet, a bastion host provides Secure Shell (SSH) access to the Magento web servers. The bastion host is maintained by an Auto Scaling group that spans multiple Availability Zones, and is configured to ensure there is always one bastion host available.
+  AWS-managed network address translation (NAT) gateways deployed into the public subnets and configured with an Elastic IP address for outbound internet connectivity. NAT gateways are used for internet access for all EC2 instances launched within the private network.
+  Auto Scaling is enabled to automatically increase capacity if there is a demand spike, and to reduce capacity during low traffic times. The default installation sets up low and high CPU-based thresholds for scaling the instance capacity up or down. You can modify these thresholds during launch and after deployment.
+  An IAM instance role with fine-grained permissions for access to AWS services necessary for the deployment process.
+  Appropriate security groups for each instance or function to restrict access to only necessary protocols and ports. For example, access to HTTP server ports on Amazon EC2 web servers is limited to Elastic Load Balancing. The security groups also restrict access to Amazon RDS DB instances by web server instances.

 The core AWS components used by this Quick Start include the following AWS services.
+  [Amazon EC2](https://aws.amazon.com/documentation/ec2/) – The Amazon Elastic Compute Cloud (Amazon EC2) service enables you to launch virtual machine instances with a variety of operating systems. You can choose from existing Amazon Machine Images (AMIs) or import your own virtual machine images.
+  [Amazon VPC](https://aws.amazon.com/documentation/vpc/) – The Amazon Virtual Private Cloud (Amazon VPC) service lets you provision a private, isolated section of the AWS Cloud where you can launch AWS services and other resources in a virtual network that you define. You have complete control over your virtual networking environment, including selection of your own IP address range, subnet creation, and configuration of route tables and network gateways.
+  [Terraform modules on AWS](https://aws.amazon.com/quickstart/architecture/terraform-modules-on-aws/) – You can now use Terraform modules on Amazon Web Services (AWS) to deploy native Terraform resources on the AWS Cloud. Terraform modules on AWS are published under an open-source license.

 Terraform modules on AWS are available in the Terraform registry on the [AWS Integration and Automation namespace page](https://registry.terraform.io/namespaces/aws-ia). Use the links provided to access modules in the Terraform registry and source code on GitHub. For module deployment instructions, refer to the `README.md` file in the GitHub repository.
+  [Auto Scaling](https://aws.amazon.com/documentation/autoscaling/) – Auto Scaling helps maintain high availability and manage capacity by automatically increasing or decreasing the EC2 instance fleet. You can use Auto Scaling to run your fleet at optimal utilization by increasing instance capacity during demand spikes and decreasing capacity during down times.
+  [Elastic Load Balancing](https://aws.amazon.com/documentation/elastic-load-balancing/) – Elastic Load Balancing automatically distributes incoming application traffic across multiple EC2 instances.
+  [Amazon CloudFront](https://docs.aws.amazon.com/cloudfront/index.html) - Amazon CloudFront is a web service that speeds up distribution of your static and dynamic web content, such as `.html`, `.css`, `.js`, and image files, to your users. CloudFront delivers your content through a worldwide network of data centers called edge locations.
+  The [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3) – Amazon S3 is an object storage service that offers industry-leading scalability, data availability, security, and performance. This Magento deployment uses Amazon S3 as [Remote Storage Module](https://devdocs.magento.com/guides/v2.4/config-guide/remote-storage/config-remote-storage.html) for Magento to provide the option to store media files and schedule imports/exports in a persistent, remote storage container.

**Note**
[Magento](https://devdocs.magento.com/guides/v2.4/config-guide/remote-storage/config-remote-storage-aws-s3.html) highly discourages the use of public buckets due to high security risks.
+  [Amazon OpenSearch Service](https://aws.amazon.com/what-is/opensearch/) — OpenSearch has quickly become the most popular search engine and is commonly used for log analytics, full-text search, security intelligence, business analytics, and operational intelligence use cases. As of version 2.4, Magento requires OpenSearch to be the catalog search engine. [Magento supports using OpenSearch](https://experienceleague.adobe.com/docs/commerce-operations/installation-guide/prerequisites/search-engine/aws-opensearch.html) provided by Amazon Web Services (AWS).
+  [Amazon ElastiCache](https://aws.amazon.com/documentation/elasticache/) – Amazon ElastiCache service makes it easy to deploy, operate, and scale an in-memory data store or cache in [the cloud](https://aws.amazon.com/what-is-cloud-computing/). The service improves the performance of web applications by allowing you to retrieve information from fast, managed, in-memory data stores, instead of relying entirely on slower disk-based databases.
+  [Amazon MQ](https://docs.aws.amazon.com/amazon-mq/) — Amazon MQ is a managed message broker service that makes it easy to set up and operate message brokers in the cloud. The MQF uses [RabbitMQ](http://www.rabbitmq.com) as the messaging broker, which provides a scalable platform for sending and receiving messages. It also includes a mechanism for storing undelivered messages. RabbitMQ are primarily needed for B2B and async operations like import, export, or Bulk operations.
+  [Amazon RDS](https://aws.amazon.com/documentation/rds/) – Amazon Relational Database Service (Amazon RDS) makes it easy to set up, operate, and scale a growing set of relational databases, including MySQL and Amazon Aurora, both of which are supported by the Magento Quick Start. With Amazon RDS, you can deploy scalable relational databases in minutes with cost-efficient and resizable hardware capacity.
**Note**
The split database feature was [deprecated](https://community.magento.com/t5/Magento-DevBlog/Deprecation-of-Split-Database-in-Magento-Commerce/ba-p/465187?_ga=2.128934671.2024864496.1657558157-1596100530.1657558157) in version 2.4.2 of Magento. See [Revert from a split database to a single database](https://experienceleague.adobe.com/docs/commerce-operations/configuration-guide/storage/split-db/revert-split-database.html?lang=en).
+  [IAM](https://aws.amazon.com/documentation/iam/) – AWS Identity and Access Management (IAM) enables you to securely control access to AWS services and resources for your users. With IAM, you can manage users, security credentials such as access keys, and permissions that control which AWS resources users can access, from a central location.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
