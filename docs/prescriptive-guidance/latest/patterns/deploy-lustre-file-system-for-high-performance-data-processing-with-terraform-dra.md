---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-lustre-file-system-for-high-performance-data-processing-with-terraform-dra.html
---

# Deploy a Lustre file system for high-performance data processing by using Terraform and DRA
<a name="deploy-lustre-file-system-for-high-performance-data-processing-with-terraform-dra"></a>

*Arun Bagal and Ishwar Chauthaiwale, Amazon Web Services*

## Summary
<a name="deploy-lustre-file-system-for-high-performance-data-processing-with-terraform-dra-summary"></a>

This pattern automatically deploys a Lustre file system on AWS and integrates it with Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Simple Storage Service (Amazon S3).

This solution helps you quickly set up a high performance computing (HPC) environment with integrated storage, compute resources, and Amazon S3 data access. It combines Lustre's storage capabilities with the flexible compute options provided by Amazon EC2 and the scalable object storage in Amazon S3, so you can tackle data-intensive workloads in machine learning, HPC, and big data analytics.

The pattern uses a HashiCorp Terraform module and Amazon FSx for Lustre to streamline the following process:
+ Provisioning a Lustre file system
+ Establishing a data repository association (DRA) between FSx for Lustre and an S3 bucket to link the Lustre file system with Amazon S3 objects
+ Creating an EC2 instance
+ Mounting the Lustre file system with the Amazon S3-linked DRA on the EC2 instance

The benefits of this solution include:
+ Modular design. You can easily maintain and update the individual components of this solution.
+ Scalability. You can quickly deploy consistent environments across AWS accounts or Regions.
+ Flexibility. You can customize the deployment to fit your specific needs.
+ Best practices. This pattern uses preconfigured modules that follow AWS best practices.

For more information about Lustre file systems, see the [Lustre website](https://www.lustre.org/).

## Prerequisites and limitations
<a name="deploy-lustre-file-system-for-high-performance-data-processing-with-terraform-dra-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A least privilege AWS Identity and Access Management (IAM) policy (see [instructions](https://aws.amazon.com/blogs/security/techniques-for-writing-least-privilege-iam-policies/))

**Limitations**

FSx for Lustre limits the Lustre file system to a single Availability Zone, which could be a concern if you have high availability requirements. If the Availability Zone that contains the file system fails, access to the file system is lost until recovery. To achieve high availability, you can use DRA to link the Lustre file system with Amazon S3, and transfer data between Availability Zones.

**Product versions**
+ [Terraform version 1.9.3 or later](https://developer.hashicorp.com/terraform/install?product_intent=terraform)
+ [HashiCorp AWS Provider version 4.0.0 or later](https://registry.terraform.io/providers/hashicorp/aws/latest)

## Architecture
<a name="deploy-lustre-file-system-for-high-performance-data-processing-with-terraform-dra-architecture"></a>

The following diagram shows the architecture for FSx for Lustre and complementary AWS services in the AWS Cloud.

![FSx for Lustre deployment with AWS KMS, Amazon EC2, Amazon CloudWatch Logs, and Amazon S3.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/51d38589-e752-42cd-9f46-59c3c8d0bfd3/images/c1c21952-fd6f-4b1d-9bf8-09b2f4f4459f.png)

The architecture includes the following:
+ An S3 bucket is used as a durable, scalable, and cost-effective storage location for data. The integration between FSx for Lustre and Amazon S3 provides a high-performance file system that is seamlessly linked with Amazon S3.
+ FSx for Lustre runs and manages the Lustre file system.
+ Amazon CloudWatch Logs collects and monitors log data from the file system. These logs provide insights into the performance, health, and activity of your Lustre file system.
+ Amazon EC2 is used to access Lustre file systems by using the open source Lustre client. EC2 instances can access file systems from other Availability Zones within the same virtual private cloud (VPC). The networking configuration allows for access across subnets within the VPC. After the Lustre file system is mounted on the instance, you can work with its files and directories just as you would use a local file system.
+ AWS Key Management Service (AWS KMS)  enhances the security of the file system by providing encryption for data at rest.

**Automation and scale**

Terraform makes it easier to deploy, manage, and scale your Lustre file systems across multiple environments. In FSx for Lustre, a single file system has size limitations, so you might need to horizontally scale by creating multiple file systems. You can use Terraform to provision multiple Lustre file systems based on your workload needs.

## Tools
<a name="deploy-lustre-file-system-for-high-performance-data-processing-with-terraform-dra-tools"></a>

**AWS services**
+ [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) helps you centralize the logs from all your systems, applications, and AWS services so you can monitor them and archive them securely.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [Amazon FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html) makes it easy and cost-effective to launch, run, and scale a high-performance Lustre file system.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Code repository**

The code for this pattern is available in the GitHub [Provision FSx for Lustre Filesystem using Terraform](https://github.com/aws-samples/provision-fsx-lustre-with-terraform) repository.

## Best practices
<a name="deploy-lustre-file-system-for-high-performance-data-processing-with-terraform-dra-best-practices"></a>
+ The following variables define the Lustre file system. Make sure to configure these correctly based on your environment, as instructed in the [Epics](#deploy-lustre-file-system-for-high-performance-data-processing-with-terraform-dra-epics) section.
  + `storage_capacity` – The storage capacity of the Lustre file system, in GiBs. The minimum and default setting is 1200 GiB.
  + `deployment_type` – The deployment type for the Lustre file system. For an explanation of the two options, `PERSISTENT_1` and `PERSISTENT_2` (default), see the [FSx for Lustre documentation](https://docs.aws.amazon.com/fsx/latest/LustreGuide/using-fsx-lustre.html#persistent-file-system).
  + `per_unit_storage_throughput` – The read and write throughput, in MBs per second per TiB.
  + `subnet_id` – The ID of the private subnet where you want to deploy FSx for Lustre.
  + `vpc_id` – The ID of your virtual private cloud on AWS where you want to deploy FSx for Lustre.
  + `data_repository_path` – The path to the S3 bucket that will be linked to the Lustre file system.
  + `iam_instance_profile` – The IAM instance profile to use to launch the EC2 instance.
  + `kms_key_id` – The Amazon Resource Name (ARN) of the AWS KMS key that will be used for data encryption.
+ Ensure proper network access and placement within the VPC by using the `security_group` and `vpc_id` variables.
+ Run the `terraform plan` command as described in the [Epics](#deploy-lustre-file-system-for-high-performance-data-processing-with-terraform-dra-epics) section to preview and verify changes before applying them. This helps catch potential issues and ensures that you are aware of what will be deployed.
+ Use the `terraform validate` command as described in the [Epics](#deploy-lustre-file-system-for-high-performance-data-processing-with-terraform-dra-epics) section to check for syntax errors and to confirm that your configuration is correct.

## Epics
<a name="deploy-lustre-file-system-for-high-performance-data-processing-with-terraform-dra-epics"></a>

### Set up your environment
<a name="set-up-your-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install Terraform. | To install Terraform on your local machine, follow the instructions in the [Terraform documentation](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli). | AWS DevOps, DevOps engineer |
| Set up AWS credentials. | To set up the AWS Command Line Interface (AWS CLI) profile for the account, follow the instructions in the [AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html). | AWS DevOps, DevOps engineer |
| Clone the GitHub repository. | To clone the GitHub repository, run the command:<pre>git clone https://github.com/aws-samples/provision-fsx-lustre-with-terraform.git</pre> | AWS DevOps, DevOps engineer |

### Configure and deploy FSx for Lustre
<a name="configure-and-deploy-fsxlustre"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Update the deployment configuration. | 1. In the cloned repository on your local machine, navigate to the `fsx_deployment` directory:<pre>cd fsx_deployment</pre><br />2. Open the `terraform.tfvars` file, and update the values of the following variables:`vpc_id``subnet_id``data_repository_path``iam_instance_profile``kms_key_id`<br />For descriptions of these variables, see the [Best practices](#deploy-lustre-file-system-for-high-performance-data-processing-with-terraform-dra-best-practices) section.<br />3. In the same directory, open the `locals.tf` file and update the CIDR ranges for the `fsx_inress` and `fsx_egress` security group variables.<br />4. If needed, open the `variables.tf`  file and update the default values of these variables:`storage_capacity``deployment_type``per_unit_storage_throughput`<br />For descriptions of these variables, see the [Best practices](#deploy-lustre-file-system-for-high-performance-data-processing-with-terraform-dra-best-practices) section. | AWS DevOps, DevOps engineer |
| Initialize the Terraform environment. | To initialize your environment to run the Terraform `fsx_deployment` module, run:<pre>terraform init</pre> | AWS DevOps, DevOps engineer |
| Validate the Terraform syntax. | To check for syntax errors and to confirm that your configuration is correct, run:<pre>terraform validate </pre> | AWS DevOps, DevOps engineer |
| Validate the Terraform configuration. | To create a Terraform execution plan and preview the deployment, run:<pre>terraform plan -var-file terraform.tfvars</pre> | AWS DevOps, DevOps engineer |
| Deploy the Terraform module. | To deploy the FSx for Lustre resources, run:<pre>terraform apply -var-file terraform.tfvars</pre> | AWS DevOps, DevOps engineer |

### Clean up AWS resources
<a name="clean-up-aws-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Remove AWS resources. | After you finish using your FSx for Lustre environment, you can remove the AWS resources deployed by Terraform to avoid incurring unnecessary charges. The Terraform module provided in the code repository automates this cleanup.1. In your local repository, navigate to the `fsx_deployment` directory:<pre>cd fsx_deployment</pre><br />2. Run the command: <pre>terraform destroy -var-file terraform.tfvars</pre> | AWS DevOps, DevOps engineer |

## Troubleshooting
<a name="deploy-lustre-file-system-for-high-performance-data-processing-with-terraform-dra-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| FSx for Lustre returns errors. | For help with FSx for Lustre issues, see [Troubleshooting Amazon FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/troubleshooting.html) in the FSx for Lustre documentation. |

## Related resources
<a name="deploy-lustre-file-system-for-high-performance-data-processing-with-terraform-dra-resources"></a>
+ [Building Amazon FSx for Lustre by using Terraform](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/fsx_lustre_file_system) (AWS Provider reference in the Terraform documentation)
+ [Getting started with Amazon FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/getting-started.html) (FSx for Lustre documentation)
+ [AWS blog posts about Amazon FSx for Lustre](https://aws.amazon.com/blogs/storage/tag/amazon-fsx-for-lustre/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
