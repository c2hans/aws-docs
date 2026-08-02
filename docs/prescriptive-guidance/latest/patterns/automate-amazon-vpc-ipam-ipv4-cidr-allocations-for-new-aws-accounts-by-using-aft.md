---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-amazon-vpc-ipam-ipv4-cidr-allocations-for-new-aws-accounts-by-using-aft.html
---

# Automate Amazon VPC IPAM IPv4 CIDR allocations for new AWS accounts by using AFT
<a name="automate-amazon-vpc-ipam-ipv4-cidr-allocations-for-new-aws-accounts-by-using-aft"></a>

*Kien Pham and Alex Pazik, Amazon Web Services*

## Summary
<a name="automate-amazon-vpc-ipam-ipv4-cidr-allocations-for-new-aws-accounts-by-using-aft-summary"></a>

This pattern shows how to automate Amazon VPC IP Address Manager (IPAM) IPv4 CIDR allocations for new AWS accounts by using [AWS Control Tower Account Factory for Terraform (AFT)](https://docs.aws.amazon.com/controltower/latest/userguide/aft-overview.html). This is done using an account-level customization that allocates a IPv4 CIDR block from IPAM to a new virtual private cloud (VPC) using the `aft-account-customizations` module.

With IPAM, you can organize, assign, monitor, and audit IP addresses at scale, allowing you to easily plan, track, and monitor IP addresses for your AWS workloads. You can [create an IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/create-ipam.html) and IPAM pool to use to allocate an IPv4 CIDR block to a new VPC during the account vending process.

## Prerequisites and limitations
<a name="automate-amazon-vpc-ipam-ipv4-cidr-allocations-for-new-aws-accounts-by-using-aft-prereqs"></a>

**Prerequisites**
+ An active AWS account with AWS Control Tower enabled in a supported [AWS Region](https://docs.aws.amazon.com/controltower/latest/userguide/region-how.html) and AFT deployed
+ A supported [version control system (VCS) provider](https://github.com/aws-ia/terraform-aws-control_tower_account_factory?tab=readme-ov-file#input_vcs_provider) such as BitBucket, GitHub, and GitHub Enterprise
+ Terraform Command Line Interface (CLI) [installed](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
+ A runtime environment where you can run the Terraform module that installs AFT
+ AWS Command Line Interface (AWS CLI) [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html)

**Limitations**
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

**Product versions**
+ [AWS Control Tower landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/2022-all.html#version-3.0) version 3.0 or later, earlier than version 4.0
+ [AFT](https://github.com/aws-ia/terraform-aws-control_tower_account_factory) version 1.13.0 or later, earlier than version 2.0.0
+ Terraform OSS version 1.2.0 or later, earlier than version 2.0.0
+ [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs) (`terraform-provider-aws`) version 5.11.0 or later, earlier than version 6.0.0
+ [Terraform module for IPAM](https://github.com/aws-ia/terraform-aws-ipam) (`aws-ia/ipam/aws`) version 2.1.0 or later

## Architecture
<a name="automate-amazon-vpc-ipam-ipv4-cidr-allocations-for-new-aws-accounts-by-using-aft-architecture"></a>

The following diagram shows the workflow and components of this pattern.

![Workflow to create Amazon VPC IPAM IPv4 CIDR allocation.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/986cfc7d-058b-4490-9029-6cd1eadd1dd2/images/f90b84dd-0420-460e-ac0f-9f22b4a9fdc4.png)

The workflow consists of the following main tasks:

1. **Trigger changes** – The changes to Terraform and IPAM customization are committed to the GitHub repository and pushed. This task triggers the AWS CodeBuild pipeline automatically.

1. **Automate build** – Within CodeBuild, multiple build projects trigger AWS Step Functions.

1. **Apply customization** – Step Functions coordinates with CodeBuild to plan and apply Terraform changes. This task uses the AFT Terraform module to coordinate the IPAM pool IP assignment to the AWS vended account.

## Tools
<a name="automate-amazon-vpc-ipam-ipv4-cidr-allocations-for-new-aws-accounts-by-using-aft-tools"></a>

**AWS services**
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) is a fully managed build service that helps you compile source code, run unit tests, and produce artifacts that are ready to deploy.
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) helps you quickly model and configure the different stages of a software release and automate the steps required to release software changes continuously.
+ [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) orchestrates the capabilities of several other [AWS services](https://docs.aws.amazon.com/controltower/latest/userguide/integrated-services.html), including AWS Organizations, AWS Service Catalog, and AWS IAM Identity Center. It can help you set up and govern an AWS multi-account environment, following prescriptive best practices.
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) is a fully managed NoSQL database service that provides fast, predictable, and scalable performance.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) is a software development kit that helps you integrate your Python application, library, or script with AWS services.
+ [AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html) helps you centrally manage catalogs of IT services that are approved for AWS. End users can quickly deploy only the approved IT services they need, following the constraints set by your organization.
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) is a serverless orchestration service that helps you combine AWS Lambda functions and other AWS services to build business-critical applications.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS. Amazon VPC IP Address Manager (IPAM) is a VPC feature that makes it easier for you to plan, track, and monitor IP addresses for your AWS workloads.

**Other tools**
+ [GitHub](https://docs.github.com/) is a developer platform that developers can use to create, store, manage, and share their code.
+ [HashiCorp Terraform](https://www.terraform.io/) is an infrastructure as code (IaC) tool that helps you create and manage cloud and on-premises resources. This includes low-level components such as compute instances, storage, and networking and high-level components such as DNS entries and software a a service (SaaS) features.
+ [Python](https://www.python.org/) is a general-purpose computer programming language. You can use it to build applications, automate tasks, and develop services on the [AWS Cloud](https://aws.amazon.com/developer/language/python/).

**Code repository**
+ The code for this pattern is available in the GitHub [AWS Control Tower Account Factory for Terraform](https://github.com/aws-ia/terraform-aws-control_tower_account_factory) repository.

## Best practices
<a name="automate-amazon-vpc-ipam-ipv4-cidr-allocations-for-new-aws-accounts-by-using-aft-best-practices"></a>

When you deploy AFT, we recommend that you follow best practices to help ensure a secure, efficient, and successful implementation. Key guidelines and recommendations for implementing and operating AFT include the following:
+ **Thorough review of inputs **– Carefully review and understand each [input](https://github.com/aws-ia/terraform-aws-control_tower_account_factory). Correct input configuration is crucial for the setup and functioning of AFT.
+ **Regular template updates **– Keep templates updated with the latest AWS features and Terraform versions. Regular updates help you take advantage of new functionality and maintain security.
+ **Versioning **– Pin your AFT module version and use a separate AFT deployment for testing if possible.
+ **Scope** – Use AFT only to deploy infrastructure guardrails and customizations. Do not use it to deploy your application.
+ **Linting and validation **– The AFT pipeline requires a linted and validated Terraform configuration. Run lint, validate, and test before pushing the configuration to AFT repositories.
+ **Terraform modules** – Build reusable Terraform code as modules, and always specify the Terraform and AWS provider versions to match your organization's requirements.

## Epics
<a name="automate-amazon-vpc-ipam-ipv4-cidr-allocations-for-new-aws-accounts-by-using-aft-epics"></a>

### Set up and configure your AWS environment
<a name="set-up-and-configure-your-aws-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy AWS Control Tower. | Set up and configure AWS Control Tower in your AWS environment to ensure centralized management and governance of your AWS accounts. For more information, see [Getting started with AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html) in the AWS Control Tower documentation. | Cloud administrator |
| Deploy AWS Control Tower Account Factory for Terraform (AFT). | Set up AFT in a new, dedicated AFT management account. For more information, see C[onfigure and launch your AWS Control Tower Account Factory for Terraform](https://docs.aws.amazon.com/controltower/latest/userguide/aft-getting-started.html#aft-configure-and-launch) in the AWS Control Tower documentation. | Cloud administrator |
| Complete AFT post-deployment. | After the AFT infrastructure deployment is complete, complete the steps in [Post-deployment steps](https://docs.aws.amazon.com/controltower/latest/userguide/aft-post-deployment.html) in the AWS Control Tower documentation. | Cloud administrator |

### Create IPAM
<a name="create-ipam"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delegate an IPAM administrator. | To delegate an IPAM administrator account in your AWS organization, use the following steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-amazon-vpc-ipam-ipv4-cidr-allocations-for-new-aws-accounts-by-using-aft.html)<br />Alternatively, you can use the AWS CLI and run the following command:<pre>aws ec2 enable-ipam-organization-admin-account \<br />    --delegated-admin-account-id 012345678901</pre><br />For more information, see [Integrate IPAM with accounts in an AWS organization](https://docs.aws.amazon.com/vpc/latest/ipam/enable-integ-ipam.html) in the Amazon VPC documentation and [enable-ipam-organization-admin-account](https://docs.aws.amazon.com/cli/latest/reference/ec2/enable-ipam-organization-admin-account.html) in the AWS CLI Command Reference. To continue using IPAM, you must sign in to the delegated administrator account. The SSO profile or AWS environment variables specified in the next step must allow you to sign in to that account and grant permissions to create an IPAM top-level and regional pool. | AWS administrator |
| Create an IPAM top-level and regional pool. | This pattern’s GitHub repository contains a Terraform template that you can use to create your IPAM top-level pool and regional pool. Then you can share the pools with an organization, organizational unit (OU), AWS account, or other resource by using AWS Resource Access Manager (AWS RAM).<br />Use the following steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-amazon-vpc-ipam-ipv4-cidr-allocations-for-new-aws-accounts-by-using-aft.html)<br />Make a note of the resource pool ID that’s output after creation. You will need the ID when submitting the account request. If you forget the resource pool ID, you can get it later from the AWS Management Console. Make sure that the created pools’ CIDRs do not overlap with any other pools in your working Region. You can create a pool without a CIDR, but you won’t be able to use the pool for allocations until you’ve provisioned a CIDR for it. You can add CIDRs to a pool at any time by editing the pool. | AWS administrator |

### Integrate IPAM with AFT
<a name="integrate-ipam-with-aft"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Begin to create account customization. | To begin a new account customization, run the following commands from your terminal:<pre># Default name for customization repo<br />cd aft-account-customizations # Replace with your actual repo name if different than the default<br />mkdir -p APG-AFT-IPAM/terraform # Replace APG-AFT-IPAM with your desired customization name<br />cd APG-AFT-IPAM/terraform</pre> | DevOps engineer |
| Create `aft-providers.jinja` file. | Add dynamic code to the `aft-providers.jinja` file that specifies the Terraform backend and provider to use.<br />Use the following steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-amazon-vpc-ipam-ipv4-cidr-allocations-for-new-aws-accounts-by-using-aft.html) | DevOps engineer |
| Create `backend.jinja` file. | Add dynamic code to the `backend.jinja` file that specifies the Terraform backend and provider to use.<br />Use the following steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-amazon-vpc-ipam-ipv4-cidr-allocations-for-new-aws-accounts-by-using-aft.html) | DevOps engineer |
| Create `main.tf` file. | Create a new `main.tf` file and add code that defines two data sources that retrieve two values from AWS Systems Manager (`aws_ssm`) and creates the VPC.<br />Use the following steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-amazon-vpc-ipam-ipv4-cidr-allocations-for-new-aws-accounts-by-using-aft.html) | DevOps engineer |
| Create `variables.tf` file. | Create a `variables.tf` file that declares the variables used by the Terraform module.<br />Use the following steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-amazon-vpc-ipam-ipv4-cidr-allocations-for-new-aws-accounts-by-using-aft.html) | DevOps engineer |
| Create `terraform.tfvars` file. | Create a `terraform.tfvars` file that defines the values of the variables that are passed to the `main.tf` file.<br />Use the following steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-amazon-vpc-ipam-ipv4-cidr-allocations-for-new-aws-accounts-by-using-aft.html) | DevOps engineer |
| Create `outputs.tf` file. | Create a new `outputs.tf` file that exposes some values in CodeBuild.<br />Use the following steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-amazon-vpc-ipam-ipv4-cidr-allocations-for-new-aws-accounts-by-using-aft.html) | DevOps engineer |
| Commit the customization. | To commit the new customization to the account customizations repository, run the following commands:<pre># Assumes you are still in the /terraform directory<br />cd .. # Skip if you are in the account customization root directory (APG-AFT-IPAM)<br />git add .<br />git commit -m "APG customization"<br />git push origin</pre> | DevOps engineer |
| Apply the customization. | Add code to the `account-requests.tf` file that requests a new account with the newly created account customization. The custom fields create Systems Manager parameters in the vended account that are required to create the VPC with the correct IPAM allocated IPv4 CIDR.<br />Use the following steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-amazon-vpc-ipam-ipv4-cidr-allocations-for-new-aws-accounts-by-using-aft.html) | AWS DevOps |
| Validate the customization. | Sign in to the newly vended account and verify that the customization was successfully applied.<br />Use the following steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-amazon-vpc-ipam-ipv4-cidr-allocations-for-new-aws-accounts-by-using-aft.html) | DevOps engineer |

## Troubleshooting
<a name="automate-amazon-vpc-ipam-ipv4-cidr-allocations-for-new-aws-accounts-by-using-aft-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
|  You encounter failures in resource creation or management caused by inadequate permissions. |  Review the AWS Identity and Access Management (IAM) roles and policies that are attached to Step Functions, CodeBuild, and other services involved in the deployment. Confirm that they have the necessary permissions. If there are permission issues, adjust the IAM policies to grant the required access. |
|  You reach AWS service quotas during deployment. |  Before you deploy the pipeline, check AWS service quotas for resources such as Amazon Simple Storage Service (Amazon S3) buckets, IAM roles, and AWS Lambda functions. If necessary, request increases to the quotas. For more information, see [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) in the *AWS General Reference*. |

## Related resources
<a name="automate-amazon-vpc-ipam-ipv4-cidr-allocations-for-new-aws-accounts-by-using-aft-resources"></a>

**AWS service documentation**
+ [AWS Control Tower User Guide](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)
+ [How IPAM works](https://docs.aws.amazon.com/vpc/latest/ipam/how-it-works-ipam.html)
+ [Security best practices in IAM ](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
+ [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)

**Other resources**
+ [Terraform AWS Provider documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
