---
source_url: https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/shared-security-responsibility-model.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Shared Security Responsibility Model
<a name="shared-security-responsibility-model"></a>

 Security and Compliance is a shared responsibility between AWS and the customer. This shared model can help relieve your operational burden as AWS operates, manages and controls the components from the host operating system and virtualization layer down to the physical security of the facilities in which the service operates. Customers assume responsibility and management of the guest operating system (including updates and security patches), other associated application software as well as the configuration of the AWS provided security group firewall. You should carefully consider the services you choose as your responsibilities vary depending on the services used, the integration of those services into your IT environment, and applicable laws and regulations.

 The following figure provides an overview of the [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/). This differentiation of responsibility is commonly referred to as Security “of” the Cloud versus Security “in” the Cloud, which will be explained in more detail below.

![AWS Shared Responsibility Model](http://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/images/shared-responsibility-model.png)

* AWS Shared Responsibility Model*

 AWS is responsible for the security and compliance ***of*** the Cloud, the infrastructure that runs all of the services offered in the AWS Cloud. Cloud security at AWS is the highest priority. AWS customers benefit from a data center and network architecture that are built to meet the requirements of the most security-sensitive organizations. This infrastructure consists of the hardware, software, networking, and facilities that run AWS Cloud services.

 Customers are responsible for the security and compliance ***in*** the Cloud, which consists of customer-configured systems and services provisioned on AWS. Responsibility within the AWS Cloud is determined by the AWS Cloud services that you select and ultimately the amount of configuration work you must perform as part of your security responsibilities. For example, a service such as Amazon Elastic Compute Cloud (Amazon EC2) is categorized as Infrastructure as a Service (IaaS) and, as such, requires you to perform all of the necessary security configuration and management tasks. Customers that deploy an Amazon EC2 instance are responsible for management of the guest operating system (including updates and security patches), any application software or utilities installed by you on the instances, and the configuration of the AWS-provided firewall (called a security group) on each instance. For abstracted services, such as Amazon S3 and Amazon DynamoDB, AWS operates the infrastructure layer, the operating system, and platforms, and customers access the endpoints to store and retrieve data. You are responsible for managing your data and component configuration (including encryption options), classifying your assets, and using IAM tools to apply the appropriate permissions.

 The AWS Shared Security Responsibility model also extends to IT controls. Just as the responsibility to operate the IT environment is shared between you and AWS, so is the management, operation and verification of IT controls shared. AWS can help relieve your burden of operating controls by managing those controls associated with the physical infrastructure deployed in the AWS environment that may previously have been managed by you. As every customer is deployed differently in AWS, you can take advantage of shifting management of certain IT controls to AWS which results in a (new) distributed control environment. You can then use the AWS control and compliance documentation available to you, as well as techniques discussed later in this whitepaper, to perform your control evaluation and verification procedures as required. Below are examples of controls that are managed by AWS, AWS Customers and/or both.

 **Inherited Controls** – Controls which you fully inherit from AWS.
+  Physical and Environmental controls

 **Shared Controls** – Controls which apply to both the infrastructure layer and customer layers, but in completely separate contexts or perspectives. In a shared control, AWS provides the requirements for the infrastructure and you must provide your own control implementation within your use of AWS services. Examples include:
+  Patch Management – AWS is responsible for patching and fixing flaws within the infrastructure, but you are responsible for patching your guest OS and applications.
+  Configuration Management – AWS maintains the configuration of its infrastructure devices, but you are responsible for configuring your own guest operating systems, databases, and applications.
+  Awareness & Training - AWS trains AWS employees, but you must train your own employees.

 **Customer Specific** – Controls which are ultimately your responsibility based on the application you are deploying within AWS services. Examples include:
+  Data Management – for instance, placement of data on Amazon S3 where you activate encryption.

   While certain controls are customer specific, AWS strives to provide you with the tools and resources to make implementation easier.

 For further information about AWS physical and operational security processes for the network and server infrastructure under the management of AWS see: [AWS Cloud Security site](https://aws.amazon.com/security/).

 For customers who are designing the security infrastructure and configuration for applications running in Amazon Web Services (AWS), see the [Best Practices for Security, Identity, & Compliance](https://aws.amazon.com/architecture/security-identity-compliance/?cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
