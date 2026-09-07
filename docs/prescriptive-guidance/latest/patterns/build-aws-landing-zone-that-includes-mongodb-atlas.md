---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-aws-landing-zone-that-includes-mongodb-atlas.html
---

# Build an AWS landing zone that includes MongoDB Atlas
<a name="build-aws-landing-zone-that-includes-mongodb-atlas"></a>

*Igor Alekseev, Amazon Web Services*

*Anuj Panchal, MongoDB*

## Summary
<a name="build-aws-landing-zone-that-includes-mongodb-atlas-summary"></a>

This pattern describes how to build an AWS landing zone that’s integrated with a MongoDB Atlas cluster. The infrastructure is automatically deployed by using a Terraform script.

A well-structured, multi-account AWS environment, which is called a [landing zone](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration/aws-landing-zone.html), offers scalability and security, particularly for enterprises. It serves as a foundation for rapid deployment of workloads and applications, and helps ensure confidence in security and infrastructure. Building a landing zone requires careful consideration of technical and business factors, including account structure, networking, security, and access management. These considerations should be aligned with your organization's future growth and business objectives.

The use cases for this pattern include the following.
+ **Enterprise SaaS and PaaS platforms:** Multitenant software as a service (SaaS) applications and platform as a service (PaaS) platforms that run on AWS can use this setup to help provide secure, private access to MongoDB Atlas without exposing data over the public internet.
+ **Highly regulated industries**: Banking, financial services, healthcare, and government workloads that require strict compliance with standards such as Health Insurance Portability and Accountability Act (HIPAA), Payment Card Industry Data Security Standard (PCI DSS), System and Organization Controls 2 (SOC2), and General Data Protection Regulation (GDPR) benefit from:
  + Encrypted, private connectivity through AWS PrivateLink
  + Multi-AZ high availability of MongoDB replica sets
+ **Secure AI/ML workloads**: Training or inference pipelines in Amazon Bedrock, Amazon SageMaker AI, or custom AI models can securely fetch and store data in MongoDB Atlas over PrivateLink.
+ **Disaster recovery and business continuity**: Multi-AZ design ensures that no single Availability Zone failure disrupts workloads. An Atlas replica set across Availability Zones ensures automatic failover. This is critical for always-on services such as financial technology (fintech) apps, digital banking, or healthcare monitoring.

## Prerequisites and limitations
<a name="build-aws-landing-zone-that-includes-mongodb-atlas-prereqs"></a>

**Prerequisites**
+ Organization owner access to MongoDB Atlas so you can create Atlas API keys. For information about this requirement, see [Manage Organization Access](https://www.mongodb.com/docs/atlas/tutorial/manage-organizations/) in the MongoDB documentation.
+ An active [AWS account](https://aws.amazon.com/resources/create-account/).
+ [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli), installed and configured.
+ A MongoDB Atlas cluster, created with MongoDB version 6.0 or later.
+ Familiarity with MongoDB and MongoDB Atlas. For more information, see the [MongoDB Atlas documentation](https://www.mongodb.com/docs/atlas/).

**Limitations**
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

## Architecture
<a name="build-aws-landing-zone-that-includes-mongodb-atlas-architecture"></a>

The following reference architecture diagram illustrates the deployment setup for an AWS landing zone that’s integrated with a MongoDB Atlas private endpoint. This reference architecture demonstrates how to establish a secure, scalable, and highly available AWS landing zone integrated with MongoDB Atlas. By combining AWS best practices such as Multi-AZ deployment, least-privilege security controls, and private connectivity, this design enables organizations to provision a robust environment for modern applications.

![Multi-AZ architecture for AWS landing zone that's integrated with MongoDB Atlas.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/72d335b9-b5b1-4fe2-9972-65edbec60ab1/images/82a8cc98-6f22-4e28-a236-57a809930055.png)

This architecture consists of the following:

**VPC**
+ A single virtual private cloud (VPC) spans three Availability Zones.
+ The VPC is subdivided into subnets that are aligned to each Availability Zone. These subnets distribute workloads for high availability.

**Internet access**
+ An internet gateway provides outbound internet connectivity for resources that need it, such as application or bastion hosts.
+ Public subnets can house NAT gateways, which allow private subnet workloads to download updates, patches, and other required packages without exposing them directly to the public internet.

**Private subnets and route tables**
+ Application components, microservices, or other sensitive resources typically reside in private subnets.
+ Dedicated route tables control traffic flows. Routes direct outbound traffic from private subnets to NAT gateways for secure, egress-only internet access.
+ Inbound requests from the internet flow through elastic load balancers or bastion hosts (if used) in public subnets, and then route appropriately to private subnet resources.

**MongoDB Atlas connectivity through PrivateLink**
+ The architecture uses PrivateLink (through a VPC endpoint) to securely connect to MongoDB Atlas without exposing your data to the public internet.
+ Requests remain on the AWS backbone network. Data in transit benefits from PrivateLink encryption and is never routed over the public internet.
+ The MongoDB Atlas dedicated VPC hosts your primary and secondary nodes, and provides a secure, isolated environment for your managed database cluster.

**Multi-AZ deployment**
+ Critical infrastructure components (such as NAT gateways and application subnets) are distributed across at least three Availability Zones. If an Availability Zone experiences an outage, this architecture ensures that workloads in the remaining Availability Zones remain operational.
+ MongoDB Atlas, by default, offers high availability through replica sets and ensures that your database layer remains fault-tolerant. Critical infrastructure is spread across at least three Availability Zones for resilience.

## Tools
<a name="build-aws-landing-zone-that-includes-mongodb-atlas-tools"></a>

**AWS services**
+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) helps you replace hardcoded credentials in your code, including passwords, with an API call to retrieve the secret programmatically.

**Other products and tools**
+ [MongoDB Atlas](https://www.mongodb.com/atlas) is a fully managed database as a service (DbaaS) for deploying and managing MongoDB databases in the cloud.
+ [Terraform](https://www.terraform.io/) is an infrastructure as code (IaC) tool from HashiCorp that helps you create and manage cloud and on-premises resources. In this pattern, you use Terraform to run a script to facilitate the deployment of required resources on AWS and MongoDB Atlas.

**Code repository**

The code for this pattern is available in the [AWS and MongoDB Atlas Landing Zone](https://github.com/mongodb-partners/AWS-MongoDB-Atlas-Landing-Zone) GitHub repository.

## Epics
<a name="build-aws-landing-zone-that-includes-mongodb-atlas-epics"></a>

### Complete discovery and assessment
<a name="complete-discovery-and-assessment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Identify key stakeholders. | Identify all key stakeholders and team members who are involved in your landing zone project. This could include roles such as:+ Database administrators (DBAs)<br />+ DevOps engineers<br />+ Application developers<br />+ Application architects | Migration lead |
| Create a structural blueprint. | Create a blueprint that outlines the desired structure of your AWS and MongoDB Atlas-enabled landing zone. | Migration lead |
| Create an architecture plan. | Work with your application architects to analyze requirements and design a fault-tolerant, resilient architecture. This pattern provides a starter architecture template for your reference. You can customize this template to meet your organization's security and infrastructure needs. | Cloud architect |
| Plan for setup and deployment. | Determine, with all stakeholders, how the architecture will be deployed, how security measures will be implemented, and any other aspects to ensure alignment with both the organization's and the requesting team's interests. | Migration lead, DevOps engineer, DBA |

### Set up the MongoDB Atlas environment
<a name="set-up-the-mongodb-atlas-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | Clone the code from the [GitHub repository](https://github.com/mongodb-partners/AWS-MongoDB-Atlas-Landing-Zone) by running the command:<pre>git clone https://github.com/mongodb-partners/AWS-MongoDB-Atlas-Landing-Zone</pre> | App developer, DevOps engineer |
| Get your Atlas organization ID. | 1. If you don't have a MongoDB Atlas account, [sign up](https://www.mongodb.com/cloud/atlas/register) for one.<br />2. Follow the [steps](https://www.mongodb.com/docs/atlas/access/orgs-create-view-edit-delete/) in the MongoDB documentation to create an organization.<br />3. Copy the organization ID. | DBA |
| Generate Atlas organization-level API keys. | To generate your organization-level API keys in Atlas, follow the instructions in the [MongoDB documentation](https://www.mongodb.com/docs/atlas/configure-api-access/#grant-programmatic-access-to-an-organization). | DBA |
| Create a secret in AWS Secrets Manager. | Store the MongoDB Atlas API keys generated in the previous step as a key-value secret in Secrets Manager. For instructions, see the [Secrets Manager documentation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html). | DevOps engineer |
| Select the Atlas cluster tier. | To select the correct Atlas cluster tier, follow the instructions in the [MongoDB documentation](https://www.mongodb.com/docs/atlas/sizing-tier-selection/). | DBA |

### Set up the AWS environments
<a name="set-up-the-aws-environments"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Modify the Terraform script. | In your local copy of the GitHub repository, update the secret name in the [modules/mongodb-atlas/main.tf](https://github.com/mongodb-partners/AWS-MongoDB-Atlas-Landing-Zone/blob/3748350730ec2ac7ab64662d536b67b4840c667c/modules/mongodb-atlas/main.tf#L12) file (line 12), so Terraform can retrieve the credentials from Secrets Manager during deployment. | DevOps engineer |
| Create an AWS access key ID and secret key. | To create your AWS access key ID and secret key, follow the instructions in the AWS re:Post article [How do I create an AWS access key?](https://repost.aws/knowledge-center/create-access-key)<br />It is best practice to assign policies with the least privileges necessary, but for this case, select the `AdministratorAccess` policy.<br />After you create your access key, review [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) to learn about best practices for managing access keys. | DevOps engineer |
| Allocate Elastic IP addresses. | Allocate at least two Elastic IP address IDs. For instructions, see the [Amazon Virtual Private Cloud (Amazon VPC) documentation](https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithEIPs.html). | DevOps engineer |
| Create an S3 bucket. | Create an S3 bucket to store the state of your Terraform deployment by following the instructions in the [Amazon Simple Storage Service (Amazon S3) documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html). | DevOps engineer |
| Update the S3 bucket for storage. | Update the S3 bucket information in your local version of [environments/development/main.tf](https://github.com/mongodb-partners/AWS-MongoDB-Atlas-Landing-Zone/blob/83e0b52cc4a8c12b24b54edeecbae496880d3615/environments/development/main.tf#L16) to match the name and Region of the bucket you created in the previous step, and specify a key prefix. For example:<pre>terraform {<br />       ...<br />  backend "s3" {<br />    bucket = "startup-name-product-terraform"<br />    key    = "network/dev"<br />    region = "ap-southeast-1"<br />  }<br />}</pre><br />For this example, you can configure Terraform to use the key prefix `network/dev` to organize the Terraform state file. You can change the value to `prod` or `staging` to match the environment you want to create. For information about using multiple environments, see the last step in this section.<br />For more information about Amazon S3 key prefixes, see [Organizing objects using prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html) in the Amazon S3 documentation. | DevOps engineer |
| Set Terraform variables. | The sample landing zone defines input variable values by using [Terraform variable definition files](https://www.terraform.io/docs/language/values/variables.html#variable-definitions-tfvars-files).<br />The variable file is located at [environments/development/variables.tf](https://github.com/mongodb-partners/AWS-MongoDB-Atlas-Landing-Zone/blob/main/environments/development/variables.tf). You can set the variable values in the [environments/development/terraform.tfvars](https://github.com/mongodb-partners/AWS-MongoDB-Atlas-Landing-Zone/blob/main/environments/development/terraform.tfvars) file. Configure these variables as described in the [Readme file](https://github.com/mongodb-partners/AWS-MongoDB-Atlas-Landing-Zone/blob/main/README.md#terraform-variables) for the GitHub repository. | DevOps engineer |
| Set up environment variables. | If you are planning to run the Terraform script on your local machine, set up the following environment variables:+ `AWS_ACCESS_KEY_ID`: AWS access key ID<br />+ `AWS_SECRET_ACCESS_KEY`: AWS secret access key<br />+ `AWS_DEFAULT_REGION`: AWS Region<br />+ `TF_LOG`: [Terraform log level](https://developer.hashicorp.com/terraform/plugin/log/managing#log-levels) (`DEBUG` or `INFO`)<br />For more information about setting up environment variables, see the [AWS Command Line Interface (AWS CLI) documentation.](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html#envvars-set) | DevOps engineer |
| Check VPC configurations. | To follow the best practices recommended by AWS, configure the settings for VPC and subnet CIDRs, NAT gateways, routes, and route tables in the Terraform script to meet your organization’s needs. For specifics, see the [Readme file](https://github.com/mongodb-partners/AWS-MongoDB-Atlas-Landing-Zone/blob/main/README.md#vpc-configurations) for the GitHub repository. | DevOps engineer |
| Tag resources. | You can tag your AWS resources to monitor them when they’re deployed by the Terraform script. For examples, see the [Readme file](https://github.com/mongodb-partners/AWS-MongoDB-Atlas-Landing-Zone/blob/main/README.md#resource-taggings) for the GitHub repository. For information about monitoring resources through tags for cost, usage, and so on, see [Activating user-defined cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html) in the AWS Billing documentation. | DevOps engineer |
| Use multiple environments. | The GitHub repository provides a `development` environment folder. You can also add your own environments in the environment folder.<br />To add an environment, copy the `development` folder to a new folder (for example, `prod` or `staging`) under `environments`. You can then update the `terraform.tfvars` file with the new value. | DevOps engineer |

### Deploy the landing zone
<a name="deploy-the-landing-zone"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Initialize the Terraform working directory. | To initialize the working directory and download the necessary packages, run the command:<pre>terraform init</pre> | DevOps engineer |
| Create an execution plan. | To create an execution plan and visualize the changes that Terraform will make to your infrastructure, run the command:<pre>terraform plan</pre> | DevOps engineer |
| Deploy the changes. | To implement the changes to your infrastructure as described in the code, run the command:<pre>terraform apply</pre> | DevOps engineer |
| Validate the deployment. | Validate the components that Terraform created or modified in your infrastructure.<br />To test the setup, provision a compute resource (for example, an Amazon EC2 instance or AWS Lambda function) in or attached to the VPC. | DevOps engineer, App developer |

### Remove resources
<a name="remove-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clean up. | When you have finished testing, run the following command to destroy the resources that Terraform deployed in your infrastructure:<pre>terraform destroy</pre> | DevOps engineer |

## Related resources
<a name="build-aws-landing-zone-that-includes-mongodb-atlas-resources"></a>

**Discovery and assessment**
+ [Administrative tips for landing zone setup](https://docs.aws.amazon.com/controltower/latest/userguide/tips-for-admin-setup.html) (AWS Control Tower documentation)
+ [Expectations for landing zone configuration](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-configure.html) (AWS Control Tower documentation)
+ [Best practices for landing zone updates](https://docs.aws.amazon.com/controltower/latest/userguide/lz-update-best-practices.html) (AWS Control Tower documentation)

**Setting up MongoDB Atlas and AWS environments**
+ [Getting MongoDB Atlas](https://aws.amazon.com/marketplace/pp/prodview-pp445qepfdy34) (AWS Marketplace)
+ [Memory](https://docs.atlas.mongodb.com/sizing-tier-selection/#memory) (MongoDB Atlas documentation)
+ [Sizing example with Atlas sample data sets](https://www.mongodb.com/docs/atlas/sizing-tier-selection/#example--the-service-sample-data-sets) (MongoDB Atlas documentation)
+ [Sizing example for mobile applications](https://www.mongodb.com/docs/atlas/sizing-tier-selection/#example--mobile-app) (MongoDB Atlas documentation)
+ [Network traffic](https://docs.atlas.mongodb.com/sizing-tier-selection/#network-traffic) (MongoDB Atlas documentation)
+ [Cluster auto-scaling](https://www.mongodb.com/docs/atlas/sizing-tier-selection/#cluster-auto-scaling) (MongoDB Atlas documentation)
+ [Atlas sizing template](https://www.mongodb.com/docs/atlas/sizing-tier-selection/) (MongoDB Atlas documentation)
+ [Set up a network peering connection](https://docs.atlas.mongodb.com/security-vpc-peering/) (MongoDB Atlas documentation)
+ [Private endpoints in Atlas](https://docs.atlas.mongodb.com/security-private-endpoint/) (MongoDB Atlas documentation)
+ [Client-side field level encryption](https://docs.mongodb.com/manual/core/security-client-side-encryption) (MongoDB database documentation)
+ [Automatic encryption](https://docs.mongodb.com/manual/core/security-automatic-client-side-encryption) (MongoDB database documentation)
+ [Selecting a cluster tier](https://www.mongodb.com/docs/atlas/manage-clusters/#select-cluster-tier) (MongoDB Atlas documentation)

**Deploying the landing zone**
+ [Terraform on AWS](https://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/terraform.html) (*CI/CD for 5G Networks on AWS* whitepaper)
+ [MongoDB Atlas with Terraform](https://www.mongodb.com/developer/products/atlas/mongodb-atlas-with-terraform/) (MongoDB documentation)
