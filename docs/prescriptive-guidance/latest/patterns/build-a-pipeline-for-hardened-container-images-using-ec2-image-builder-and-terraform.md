---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-a-pipeline-for-hardened-container-images-using-ec2-image-builder-and-terraform.html
---

# Build a pipeline for hardened container images using EC2 Image Builder and Terraform
<a name="build-a-pipeline-for-hardened-container-images-using-ec2-image-builder-and-terraform"></a>

*Mike Saintcross and Andrew Ranes, Amazon Web Services*

## Summary
<a name="build-a-pipeline-for-hardened-container-images-using-ec2-image-builder-and-terraform-summary"></a>

This pattern builds an [EC2 Image Builder pipeline](https://docs.aws.amazon.com/imagebuilder/latest/userguide/start-build-image-pipeline.html) that produces a hardened [Amazon Linux 2](https://aws.amazon.com/amazon-linux-2/) base container image. Terraform is used as an infrastructure as code (IaC) tool to configure and provision the infrastructure that is used to create hardened container images. The recipe helps you deploy a Docker-based Amazon Linux 2 container image that has been hardened according to Red Hat Enterprise Linux (RHEL) 7 STIG Version 3 Release 7 ‒ Medium. (See [STIG-Build-Linux-Medium version 2022.2.1](https://docs.aws.amazon.com/imagebuilder/latest/userguide/toe-stig.html#linux-os-stig) in the *Linux STIG components* section of the EC2 Image Builder documentation.) This is referred to as a *golden *container image.

The build includes two[ Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html). One rule starts the container image pipeline when the [Amazon Inspector finding](https://docs.aws.amazon.com/inspector/latest/user/findings-managing.html) is **High** or **Critical** so that non-secure images are replaced. This rule requires both Amazon Inspector and Amazon Elastic Container Registry (Amazon ECR) [enhanced scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning-enhanced.html) to be enabled. The other rule sends notifications to an Amazon Simple Queue Service (Amazon SQS) [queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-types.html) after a successful image push to the Amazon ECR repository, to help you use the latest container images.

**Note**
Amazon Linux 2 is nearing end of support. For more information, see the [Amazon Linux 2 FAQs](http://aws.amazon.com/amazon-linux-2/faqs/).

## Prerequisites and limitations
<a name="build-a-pipeline-for-hardened-container-images-using-ec2-image-builder-and-terraform-prereqs"></a>

**Prerequisites**
+ An [AWS account](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/) that you can deploy the infrastructure in.
+ [AWS Command Line Interface (AWS CLI) installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) for setting your AWS credentials for local deployment.
+ Terraform [downloaded](https://developer.hashicorp.com/terraform/downloads) and set up by following the [instructions](https://developer.hashicorp.com/terraform/tutorials/aws-get-started) in the Terraform documentation.
+ [Git](https://git-scm.com/) (if you’re provisioning from a local machine).
+ A [role ](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)within the AWS account that you can use to create AWS resources.
+ All variables defined in the [.tfvars](https://developer.hashicorp.com/terraform/tutorials/configuration-language/variables) file.  Or, you can define all variables when you apply the Terraform configuration.

**Limitations**
+ This solution creates an Amazon Virtual Private Cloud (Amazon VPC) infrastructure that includes a [NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) and an [internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) for internet connectivity from its private subnet. You cannot use [VPC endpoints](https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/what-are-vpc-endpoints.html), because the [bootstrap process by AWS Task Orchestrator and Executor (AWSTOE](https://aws.amazon.com/premiumsupport/knowledge-center/image-builder-pipeline-execution-error/)) installs AWS CLI version 2 from the internet.

**Product versions**
+ Amazon Linux 2
+ AWS CLI version 1.1 or later

## Architecture
<a name="build-a-pipeline-for-hardened-container-images-using-ec2-image-builder-and-terraform-architecture"></a>

**Target technology stack**

This pattern creates 43 resources, including:
+ Two Amazon Simple Storage Service (Amazon S3) [buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html): one for the pipeline component files and one for server access and Amazon VPC flow logs
+ An [Amazon ECR repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html)
+ A virtual private cloud (VPC) that contains a public subnet, a private subnet, route tables, a NAT gateway, and an internet gateway
+ An EC2 Image Builder pipeline, recipe, and components
+ A container image
+ An AWS Key Management Service (AWS KMS) [key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms_keys) for image encryption
+ An SQS queue
+ Three roles: one to run the EC2 Image Builder pipeline, one instance profile for EC2 Image Builder, and one for EventBridge rules
+ Two EventBridge rules

**Terraform module structure**

For the source code, see the GitHub repository [Terraform EC2 Image Builder Container Hardening Pipeline](https://github.com/aws-samples/terraform-ec2-image-builder-container-hardening-pipeline).

```
├── components.tf
├── config.tf
├── dist-config.tf
├── files
│   └──assumption-policy.json
├── hardening-pipeline.tfvars
├── image.tf
├── infr-config.tf
├── infra-network-config.tf
├── kms-key.tf
├── main.tf
├── outputs.tf
├── pipeline.tf
├── recipes.tf
├── roles.tf
├── sec-groups.tf
├── trigger-build.tf
└── variables.tf
```

**Module details**
+ `components.tf` contains an Amazon S3 upload resource to upload the contents of the `/files` directory. You can also modularly add custom component YAML files here as well.
+ `/files` contains the `.yml` files that define the components used in `components.tf`.
+ `image.tf` contains the definitions for the base image operating system. This is where you can modify the definitions for a different base image pipeline.
+ `infr-config.tf` and `dist-config.tf` contain the resources for the minimum AWS infrastructure needed to spin up and distribute the image.
+ `infra-network-config.tf` contains the minimum VPC infrastructure to deploy the container image into.
+ `hardening-pipeline.tfvars` contains the Terraform variables to be used at apply time.
+ `pipeline.tf` creates and manages an EC2 Image Builder pipeline in Terraform.
+ `recipes.tf` is where you can specify different mixtures of components to create container recipes.
+ `roles.tf` contains the AWS Identity and Access Management (IAM) policy definitions for the Amazon Elastic Compute Cloud (Amazon EC2) instance profile and pipeline deployment role.
+ `trigger-build.tf` contains the EventBridge rules and SQS queue resources.

**Target architecture**

![Architecture and workflow for building a pipeline for hardened container images](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/4b16bdfa-4f34-41e9-a69a-d023253c8585/images/23443eca-132f-46ac-98bd-32a9e9359a77.png)

The diagram illustrates the following workflow:

1. EC2 Image Builder builds a container image by using the defined recipe, which installs operating system updates and applies the RHEL Medium STIG to the Amazon Linux 2 base image.

1. The hardened image is published to a private Amazon ECR registry, and an EventBridge rule sends a message to an SQS queue when the image has been published successfully.

1. If Amazon Inspector is configured for enhanced scanning, it scans the Amazon ECR registry.

1. If Amazon Inspector generates a **Critical** or **High** severity finding for the image, an EventBridge rule triggers the EC2 Image Builder pipeline to run again and publish a newly hardened image.

**Automation and scale**
+ This pattern describes how to provision the infrastructure and build the pipeline on your computer. However, it is intended to be used at scale. Instead of deploying the Terraform modules locally, you can use them in a multi-account environment, such as an [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) with [Account Factory for Terraform](https://aws.amazon.com/blogs/aws/new-aws-control-tower-account-factory-for-terraform/) environment. In that case, you should use a [backend state S3 bucket](https://developer.hashicorp.com/terraform/language/settings/backends/s3) to manage Terraform state files instead of managing the configuration state locally.
+ For scaled use, deploy the solution to one central account, such as a Shared Services or Common Services account, from a Control Tower or landing zone account model, and grant consumer accounts permission to access the Amazon ECR repository and AWS KMS key. For more information about the setup, see the re:Post article [How can I allow a secondary account to push or pull images in my Amazon ECR image repository?](https://repost.aws/knowledge-center/secondary-account-access-ecr) For example, in an [account vending machine](https://www.hashicorp.com/resources/terraform-landing-zones-for-self-service-multi-aws-at-eventbrite) or Account Factory for Terraform, add permissions to each account baseline or account customization baseline to provide access to that Amazon ECR repository and encryption key.
+ After the container image pipeline is deployed, you can modify it by using EC2 Image Builder features such as [components](https://docs.aws.amazon.com/imagebuilder/latest/userguide/manage-components.html), which help you package more components into the Docker build.
+ The AWS KMS key that is used to encrypt the container image should be shared across the accounts that the image is intended to be used in.
+ You can add support for other images by duplicating the entire Terraform module and modifying the following `recipes.tf` attributes:
  + Modify `parent_image = "amazonlinux:latest"` to another image type.
  + Modify `repository_name` to point to an existing Amazon ECR repository. This creates another pipeline that deploys a different parent image type to your existing Amazon ECR repository.

## Tools
<a name="build-a-pipeline-for-hardened-container-images-using-ec2-image-builder-and-terraform-tools"></a>

**Tools**
+ Terraform (IaC provisioning)
+ Git (if provisioning locally)
+ AWS CLI version 1 or version 2 (if provisioning locally)

**Code **

The code for this pattern is in the GitHub repository [Terraform EC2 Image Builder Container Hardening Pipeline](https://github.com/aws-samples/terraform-ec2-image-builder-container-hardening-pipeline). To use the sample code, follow the instructions in the next section.

## Epics
<a name="build-a-pipeline-for-hardened-container-images-using-ec2-image-builder-and-terraform-epics"></a>

### Provision the infrastructure
<a name="provision-the-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up local credentials. | Set up your AWS temporary credentials.1. See if the AWS CLI is installed:<pre>$ aws --version<br />aws-cli/1.16.249 Python/3.6.8...</pre>AWS CLI version should be 1.1 or later.If the command isn’t found, [install the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).<br />2. Run `aws configure` and provide the following values:<pre>$ aws configure<br />AWS Access Key ID [*************xxxx]: <Your AWS access key ID><br />AWS Secret Access Key [**************xxxx]: <Your AWS secret access key><br />Default region name: [us-east-1]: <Your desired Region for deployment><br />Default output format [None]: <Your desired output format></pre> | AWS DevOps |
| Clone the repository. | 1. Clone the repository that’s provided with this pattern. You can use HTTPS or Secure Shell (SSH).<br />HTTPS:<pre>git clone https://github.com/aws-samples/terraform-ec2-image-builder-container-hardening-pipeline</pre><br />SSH:<pre>git clone git@github.com:aws-samples/terraform-ec2-image-builder-container-hardening-pipeline.git</pre><br />2. Navigate to your local directory that contains this solution:<pre>cd terraform-ec2-image-builder-container-hardening-pipeline</pre> | AWS DevOps |
| Update variables. | Update the variables in the `hardening-pipeline.tfvars` file to match your environment and your desired configuration. You must provide your own `account_id`. However, you should also modify the rest of the variables to fit your desired deployment. All variables are required.<pre>account_id     = "<DEPLOYMENT-ACCOUNT-ID>"<br />aws_region     = "us-east-1"<br />vpc_name       = "example-hardening-pipeline-vpc"<br />kms_key_alias = "image-builder-container-key"<br />ec2_iam_role_name = "example-hardening-instance-role"<br />hardening_pipeline_role_name = "example-hardening-pipeline-role"<br />aws_s3_ami_resources_bucket = "example-hardening-ami-resources-bucket-0123"<br />image_name = "example-hardening-al2-container-image"<br />ecr_name = "example-hardening-container-repo"<br />recipe_version = "1.0.0" <br />ebs_root_vol_size = 10</pre><br />Here’s a description of each variable:+ `account_id` ‒ The AWS account number that you want to deploy the solution into.<br />+ `aws_region` ‒ The AWS Region that you want to deploy the solution into.<br />+ `vpc_name` ‒ The name for your VPC infrastructure.<br />+ `kms_key_alias` ‒ The AWS KMS key name to be used by the EC2 Image Builder infrastructure configuration.<br />+ `ec2_iam_role_name` ‒ The name for the role that will be used as the EC2 instance profile.<br />+ `hardening_pipeline_role_name` ‒ The name for the role that will be used to deploy the hardening pipeline.<br />+ `aws_s3_ami_resources_bucket` ‒ The name for an S3 bucket that will host all files necessary to build the pipeline and container images.<br />+ `image_name` ‒ The container image name. This value must be between 3 and 50 characters and should contain alphanumeric characters and hyphens only.<br />+ `ecr_name` ‒ The name of the Amazon ECR registry to store the container images in.<br />+ `recipe_version` ‒ The version of the image recipe. The default value is 1.0.0.<br />+ `ebs_root_vol_size` ‒ The size (in gigabytes) of the Amazon Elastic Block Store (Amazon EBS) root volume. The default value is 10 gigabytes. | AWS DevOps |
| Initialize Terraform. | After you update your variable values, you can initialize the Terraform configuration directory. Initializing a configuration directory downloads and installs the AWS provider, which is defined in the configuration.<pre>terraform init</pre><br />You should see a message that says Terraform has been successfully initialized and identifies the version of the provider that was installed. | AWS DevOps |
| Deploy the infrastructure and create a container image. | Use the following command to initialize, validate, and apply the Terraform modules to the environment by using the variables defined in your `.tfvars` file:<pre>terraform init && terraform validate && terraform apply -var-file *.tfvars -auto-approve</pre> | AWS DevOps |
| Customize the container. | You can create a new version of a container recipe after EC2 Image Builder deploys the pipeline and initial recipe.<br />You can add any of the 31\+ components available within EC2 Image Builder to customize the container build. For more information, see the *Components* section of [Create a new version of a container recipe](https://docs.aws.amazon.com/imagebuilder/latest/userguide/create-container-recipes.html) in the EC2 Image Builder documentation. | AWS administrator |

### Validate resources
<a name="validate-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate AWS infrastructure provisioning. | After you have successfully completed your first Terraform `apply` command, if you’re provisioning locally, you should see this snippet in your local machine’s terminal:<pre>Apply complete! Resources: 43 added, 0 changed, 0 destroyed.</pre> | AWS DevOps |
| Validate individual AWS infrastructure resources. | To validate the individual resources that were deployed, if you’re provisioning locally, you can run the following command:<pre>terraform state list</pre><br />This command returns a list of 43 resources. | AWS DevOps |

### Remove resources
<a name="remove-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Remove the infrastructure and container image. | When you’ve finished working with your Terraform configuration, you can run the following command to remove resources:<pre>terraform init && terraform validate && terraform destroy -var-file *.tfvars -auto-approve</pre> | AWS DevOps |

## Troubleshooting
<a name="build-a-pipeline-for-hardened-container-images-using-ec2-image-builder-and-terraform-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Error validating provider credentials | When you run the Terraform `apply` or `destroy` command from your local machine, you might encounter an error similar to the following:<pre>Error: configuring Terraform AWS Provider: error validating provider <br />credentials: error calling sts:GetCallerIdentity: operation error STS: <br />GetCallerIdentity, https response error StatusCode: 403, RequestID: <br />123456a9-fbc1-40ed-b8d8-513d0133ba7f, api error InvalidClientTokenId: <br />The security token included in the request is invalid.</pre><br />This error is caused by the expiration of the security token for the credentials used in your local machine’s configuration.<br />To resolve the error, see [Set and view configuration settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-methods) in the AWS CLI documentation. |

## Related resources
<a name="build-a-pipeline-for-hardened-container-images-using-ec2-image-builder-and-terraform-resources"></a>
+ [Terraform EC2 Image Builder Container Hardening Pipeline](https://github.com/aws-samples/terraform-ec2-image-builder-container-hardening-pipeline) (GitHub repository)
+ [EC2 Image Builder documentation](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html)
+ [AWS Control Tower Account Factory for Terraform](https://aws.amazon.com/blogs/aws/new-aws-control-tower-account-factory-for-terraform/) (AWS blog post)
+ [Backend state S3 bucket](https://developer.hashicorp.com/terraform/language/settings/backends/s3) (Terraform documentation)
+ [Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) (AWS CLI documentation)
+ [Download Terraform](https://developer.hashicorp.com/terraform/downloads)
