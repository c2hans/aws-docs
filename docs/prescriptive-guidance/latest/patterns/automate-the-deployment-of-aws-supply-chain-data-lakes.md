---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-the-deployment-of-aws-supply-chain-data-lakes.html
---

# Automate Supply Chain data lakes deployment in a multi-repository setup
<a name="automate-the-deployment-of-aws-supply-chain-data-lakes"></a>

*Keshav Ganesh, Amazon Web Services*

## Summary
<a name="automate-the-deployment-of-aws-supply-chain-data-lakes-summary"></a>

This pattern provides an automated approach for deploying and managing AWS Supply Chain data lakes using a multi-repository continuous integration and continuous deployment (CI/CD) pipeline. It demonstrates two deployment methods: automated deployment using GitHub Actions workflows, or manual deployment using Terraform directly. Both approaches use Terraform for infrastructure as code (IaC), with the automated method adding GitHub Actions and JFrog Artifactory for enhanced CI/CD capabilities.

The solution leverages Supply Chain, AWS Lambda, and Amazon Simple Storage Service (Amazon S3) to establish the data lake infrastructure, while using either deployment method to automate configuration and resource creation. This automation eliminates manual configuration steps and ensures consistent deployments across environments. In addition, Supply Chain eliminates the need for deep expertise in extract, transform, and load (ETL) and can provide insights and analytics powered by Amazon Quick Sight.

By implementing this pattern, organizations can reduce deployment time, maintain infrastructure as code, and manage supply chain data lakes through a version-controlled, automated process. The multi-repository approach provides fine-grained access control and supports independent deployment of different components. Teams can choose the deployment method that best fits their existing tools and processes.

## Prerequisites and limitations
<a name="automate-the-deployment-of-aws-supply-chain-data-lakes-prereqs"></a>

**Prerequisites**

Ensure the following are installed on your local machine:
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) version 2
+ [GitHub CLI](https://docs.github.com/en/get-started/git-basics/set-up-git)
+ [Python](https://www.python.org/downloads/) v3.13
+ [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) v1.12 or later

Ensure the following are in place before deployment:
+ An active AWS account.
+ A [virtual private cloud (VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html) with two [private subnets](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-example-private-subnets-nat.html) in your AWS account in the AWS Region of your choice.
+ Sufficient permissions for the AWS Identity and Access Management (IAM) role used for deployment to the following services:
  + Supply Chain – Full Access preferred for deploying its components like datasets and integration flows, along with accessing it from the AWS Management Console.
  + Amazon CloudWatch Logs – For creating and managing CloudWatch log groups.
  + Amazon Elastic Compute Cloud (Amazon EC2) – For Amazon EC2 security groups and Amazon Virtual Private Cloud (Amazon VPC) endpoints.
  + Amazon EventBridge – For use by Supply Chain.
  + IAM – For creating AWS Lambda service roles.
  + AWS Key Management Service (AWS KMS) – For access to the AWS KMS keys used for the Amazon S3 artifacts bucket and the Amazon S3 Supply Chain staging bucket.
  + AWS Lambda – For creating the Lambda functions that deploy the Supply Chain components.
  + Amazon S3 – For access to the Amazon S3 artifacts bucket, server access logging bucket, and Supply Chain staging bucket. If you’re using manual deployment, permissions for the Amazon S3 Terraform artifacts bucket are also required.
  + Amazon VPC – For creating and managing a VPC.

If you prefer to use GitHub Actions workflows for deployment, do the following:
+ Set up [OpenID Connect (OIDC)](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-aws#configuring-the-role-and-trust-policy) for the IAM role with the permissions mentioned earlier.
+ Create an IAM role with similar permissions to access the AWS Management Console. For more information, see [Create a role to give permissions to an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the IAM documentation.

If you prefer to do a manual deployment, do the following:
+ Create an IAM user to assume the IAM role with the permissions mentioned earlier. For more information, see [Create a role to give permissions to an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the IAM documentation.
+ [Assume the role](https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-role.html) in your local terminal.

If you prefer to use GitHub Actions workflows for deployment, set up the following:
+ A [JFrog Artifactory account](https://jfrog.com/artifactory/?utm_source=google&utm_medium=cpc_search&utm_campaign=SearchDSKBrandAPACIN202506&utm_term=jfrog%20cloud&gads_network=g&utm_content=u-bin&gads_campaign_id=22674833884&gads_adgroup_id=184501797241&gads_extension_id=233003714635&gads_target_id=aud-312135645780:kwd-1598615735032&gads_matchtype=b&gad_source=1&gad_campaignid=22674833884&gbraid=0AAAAADqV85U5B37iapTR9IIFHBvydF5AQ&gclid=CjwKCAjwiY_GBhBEEiwAFaghvqdNV-odNLZXPHjT7NAwf8lA-QuMtg666hgvDW1oCJ4nn7wvf869_xoCW4IQAvD_BwE) to get the host name, login username, and login access token.
+ A [JFrog project key and repository](https://docs.jfrog.com/projects/docs/create-a-project) for storing artifacts.

**Limitations**
+ The Supply Chain instance doesn’t support complex data transformation techniques.
+ Supply Chain is most suited for supply chain domains because it provides built-in analytics and insights. For any other domain, Supply Chain can be used as a data store as part of the data lake architecture.
+ Lambda functions used in this solution might need to be enhanced to handle API retries and memory management in a production scale deployment.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

## Architecture
<a name="automate-the-deployment-of-aws-supply-chain-data-lakes-architecture"></a>

You can deploy this solution either by using automated GitHub Actions workflows or manually using Terraform.

**Automated deployment with GitHub Actions**

The following diagram shows the automated deployment option that uses GitHub Actions workflows. JFrog Artifactory is used for artifacts management. It stores resource information and outputs for use in a multi-repository deployment.

![Automated deployment option that uses GitHub Actions workflows and JFrog.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/2f0b78b0-a174-4703-b533-d66b3fb005e0/images/d454a5c5-ed51-421c-a87f-ff74cfcb30be.png)

**Manual deployment with Terraform**

The following diagram shows the manual deployment option through Terraform. Instead of JFrog Artifactory, Amazon S3 is used for artifacts management.

![Manual deployment option using Terraform and Amazon S3.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/2f0b78b0-a174-4703-b533-d66b3fb005e0/images/1130e728-44d5-4ae7-9586-1e497f54352a.png)

**Deployment workflow**

The diagrams show the following workflow:

1. Deploy Supply Chain service datasets infrastructure and databases using one of the following deployment methods:
   + **Automated deployment** – Uses GitHub Actions workflows to orchestrate all deployment steps and uses JFrog Artifactory for artifacts management.
   + **Manual deployment** – Executes Terraform commands directly for each deployment step and uses Amazon S3 for artifacts management.

1. Create the supporting AWS resources that are required for Supply Chain service operation:
   + Amazon VPC endpoints and security groups
   + AWS KMS keys
   + CloudWatch Logs log groups

1. Create and deploy the following infrastructure resources:
   + Lambda functions that manage (create, update, and delete) the Supply Chain service instance, namespaces, and datasets.
   + Supply Chain staging Amazon S3 bucket for data ingestion

1. Deploy the Lambda function that manages integration flows between the staging bucket and Supply Chain datasets. After deployment is complete, the remaining workflow steps manage data ingestion and analysis.

1. Configure source data ingestion to the Supply Chain staging Amazon S3 bucket.

1. After data is added to the Supply Chain staging Amazon S3 bucket, the service automatically triggers the integration flow to the Supply Chain datasets.

1. Supply Chain integrates with Quick Sight Analytics to produce dashboards based on the ingested data.

## Tools
<a name="automate-the-deployment-of-aws-supply-chain-data-lakes-tools"></a>

**AWS services**
+ [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) helps you centralize the logs from all your systems, applications, and AWS services so you can monitor them and archive them securely.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open source tool that helps you interact with AWS services through commands in your command-line shell.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that helps you connect your applications with real-time data from a variety of sources. For example, AWS Lambda functions, HTTP invocation endpoints using API destinations, or event buses in other AWS accounts.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) helps you centrally manage single sign-on (SSO) access to all of your AWS accounts and cloud applications.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Q](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/qinasc.html) in Supply Chain is an interactive generative AI assistant that helps you operate your supply chain more efficiently by analyzing the data in your Supply Chain data lake.
+ [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) is a cloud-scale business intelligence (BI) service that helps you visualize, analyze, and report your data in a single dashboard.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [Supply Chain](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/getting-started.html) is a cloud-based managed application that can be used as a data store in organizations for supply chain domains, which can be used to generate insights and perform analysis on the ingested data.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS. An [Amazon VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) is a virtual device that helps you privately connect your VPC to supported AWS services without requiring an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection.

**Other tools**
+ [GitHub Actions](https://docs.github.com/en/actions) is a continuous integration and continuous delivery (CI/CD) platform that’s tightly integrated with GitHub repositories. You can use GitHub Actions to automate your build, test, and deployment pipeline.
+ [HashiCorp Terraform](https://www.terraform.io/) is an infrastructure as code (IaC) tool that helps you create and manage cloud and on-premises resources.
+ [JFrog Artifactory](https://jfrog.com/help/r/jfrog-artifactory-documentation/jfrog-artifactory) provides end-to-end automation and management of binaries and artifacts through the application delivery process.
+ [Python](https://www.python.org/) is a general-purpose computer programming language. This pattern uses Python for the AWS function’s code to interact with Supply Chain

  .

## Best practices
<a name="automate-the-deployment-of-aws-supply-chain-data-lakes-best-practices"></a>
+ Maintain the highest possible security when implementing this pattern. As stated in [Prerequisites](#automate-the-deployment-of-aws-supply-chain-data-lakes-prereqs), make sure a [virtual private cloud (VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html) with two [private subnets](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-example-private-subnets-nat.html) is in your AWS account in the AWS Region of your choice.
+ Use AWS KMS [customer managed keys](https://docs.aws.amazon.com/kms/latest/cryptographic-details/basic-concepts.html) wherever possible, and grant limited access permissions to them.
+ To set up IAM roles with the least access required for ingesting data for this pattern, see [Secure Data Ingestion from Source Systems to Amazon S3](https://github.com/aws-samples/sample-automate-aws-supply-chain-deployment/tree/main?tab=readme-ov-file#secure-data-ingestion-from-source-systems-to-amazon-s3) in this pattern’s repository.

## Epics
<a name="automate-the-deployment-of-aws-supply-chain-data-lakes-epics"></a>

### (Both options) Set up local workstation
<a name="both-options-set-up-local-workstation"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | To clone this pattern’s repository, run the following command in your local workstation:<pre>git clone https://github.com/aws-samples/sample-automate-aws-supply-chain-deployment.git<br />cd ASC-Deployment</pre> | AWS DevOps |
| (Automated option) Verify prerequisites for deployment. | Make sure that the [Prerequisites](#automate-the-deployment-of-aws-supply-chain-data-lakes-prereqs) are complete for the automated deployment. | App owner |
| (Manual option) Prepare for deployment of Supply Chain datasets. | To go to the `terraform-deployment` directory of `ASC-Datasets`, run the following command:<pre>cd ASC-Datasets/terraform-deployment</pre><br />To assume the role ARN that was created in the [Prerequisites](#automate-the-deployment-of-aws-supply-chain-data-lakes-prereqs), run the following command:<pre>aws sts assume-role --role-arn <enter AWS user role ARN> --role-session-name <your-session-name></pre><br />To configure and export the environment variables, run the following commands:<pre># Export Environment variables<br />export REGION=<Enter deployment region><br />export REPO_NAME=<Enter Current ASC Datasets dir name><br />export PROJECT_NAME="asc-deployment-poc"<br />export ACCOUNT_ID=<Enter deployment Account ID><br />export ENVIRONMENT="dev"<br />export LAMBDA_LAYER_TEMP_DIR_TERRAFORM="layerOutput"<br />export LAMBDA_FUNCTION_TEMP_DIR_TERRAFORM="lambdaOutput"<br />export AWS_USER_ROLE=<Enter user role ARN for AWS Console access and deployment><br />export S3_TERRAFORM_ARTIFACTS_BUCKET_NAME="$PROJECT_NAME-$ACCOUNT_ID-$REGION-terraform-artifacts-$ENVIRONMENT"</pre> | AWS DevOps |
| (Manual option) Prepare for managing Supply Chain integration flows in deployment. | To go to the `terraform-deployment` directory of `ASC-Integration-Flows`, run the following command:<pre>cd ASC-Integration-Flows/terraform-deployment</pre><br />To assume the role ARN that was created earlier, run the following command:<pre>aws sts assume-role --role-arn <enter AWS user role ARN> --role-session-name <your-session-name></pre><br />To configure and export the environment variables, run the following commands:<pre># Export Environment variables<br />export REGION=<Enter deployment region><br />export REPO_NAME=<Enter Current ASC Integration Flows dir name><br />export ASC_DATASET_VARS_REPO=<Enter Current ASC Datasets dir name>  #Must be the same directory name used for ASC Datasets deployment<br />export PROJECT_NAME="asc-deployment-poc"<br />export ACCOUNT_ID=<Enter deployment Account ID><br />export ENVIRONMENT="dev"<br />export LAMBDA_LAYER_TEMP_DIR_TERRAFORM="layerOutput"<br />export LAMBDA_FUNCTION_TEMP_DIR_TERRAFORM="lambdaOutput"<br />export S3_TERRAFORM_ARTIFACTS_BUCKET_NAME="$PROJECT_NAME-$ACCOUNT_ID-$REGION-terraform-artifacts-$ENVIRONMENT"</pre> | App owner |

### (Automated option) Deploy Supply Chain datasets using GitHub Actions workflows
<a name="automated-option-deploy-supplychain-datasets-using-github-actions-workflows"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Copy the `ASC-Datasets` directory. | To copy the `ASC-Datasets` directory to a new location, use the following steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-the-deployment-of-aws-supply-chain-data-lakes.html) | AWS DevOps |
| Set up the `ASC-Datasets` directory. | To set up `ASC-Datasets` as a standalone repository in your organization, run the following commands:<pre>git init<br />git add .<br />git commit -m "Initial commit: ASC-Datasets standalone repository"<br />git remote add origin <INSERT_ASC_DATASETS_GITHUB_URL><br />git branch -M dev</pre> | AWS DevOps |
| Configure the branch name in the .github workflow file. | Set up the branch name in the [deployment](https://github.com/aws-samples/sample-automate-aws-supply-chain-deployment/blob/main/ASC-Datasets/.github/workflows/asc-datasets.yml) workflow file as shown in the following example:<pre>   on:<br />     workflow_dispatch:<br />     push:<br />       branches:<br />         - dev     #Change to any other branch preferred for deployment</pre> | App owner |
| Set up GitHub environments and configure environment values. | To set up GitHub environments in your GitHub organization, use the instructions in [Setup GitHub environments](https://github.com/aws-samples/sample-automate-aws-supply-chain-deployment/tree/main/ASC-Datasets#setup-github-environments) in this pattern’s repository.<br />To configure [environment values](https://github.com/aws-samples/sample-automate-aws-supply-chain-deployment/tree/main/ASC-Datasets#setup-environment-values-in-the-workflow-files) in the workflow files, use the instructions in [Setup environment values in the workflow files](https://github.com/aws-samples/sample-automate-aws-supply-chain-deployment/tree/main/ASC-Datasets#setup-environment-values-in-the-workflow-files) in this pattern’s repository. | App owner |
| Trigger the workflow. | To push your changes to your GitHub organization and trigger the deployment workflow, run the following command:<pre>git push -u origin dev</pre> | AWS DevOps |

### (Automated option) Deploy Supply Chain integration flows using GitHub Actions workflows
<a name="automated-option-deploy-supplychain-integration-flows-using-github-actions-workflows"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Copy the `ASC-Integration-Flows` directory. | To copy the `ASC-Integration-Flows` directory to a new location, use the following steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-the-deployment-of-aws-supply-chain-data-lakes.html) | AWS DevOps |
| Set up the `ASC-Integration-Flows` directory. | To set up the `ASC-Integration-Flows` directory as a standalone repository in your organization, run the following commands:<pre>git init<br />git add .<br />git commit -m "Initial commit: ASC-Integration-Flows standalone repository"<br />git remote add origin <INSERT_ASC_Integration_Flows_GITHUB_URL><br />git branch -M dev</pre> | AWS DevOps |
| Configure the branch name in the .github workflow file. | Set up the branch name in the [deployment](https://github.com/aws-samples/sample-automate-aws-supply-chain-deployment/blob/main/ASC-Integration-Flows/.github/workflows/asc-integration-flows.yml) workflow file as shown in the following example:<pre>   on:<br />     workflow_dispatch:<br />     push:<br />       branches:<br />         - dev     #Change to any other branch preferred for deployment</pre> | App owner |
| Set up GitHub environments and configure environment values. | To set up GitHub environments in your GitHub organization, use the instructions in [Setup GitHub environments](https://github.com/aws-samples/sample-automate-aws-supply-chain-deployment/tree/main/ASC-Integration-Flows#setup-github-environments) in this pattern’s repository.<br />To configure [environment values](https://github.com/aws-samples/sample-automate-aws-supply-chain-deployment/tree/main/ASC-Integration-Flows#setup-github-environments) in the workflow files, use the instructions in [Setup environment values in the workflow files](https://github.com/aws-samples/sample-automate-aws-supply-chain-deployment/tree/main/ASC-Integration-Flows#setup-environment-values-in-the-workflow-files) in this pattern’s repository. | App owner |
| Trigger the workflow. | To push your changes to your GitHub organization and trigger the deployment workflow, run the following command:<pre>git push -u origin dev</pre> | AWS DevOps |

### (Manual option) Deploy Supply Chain datasets using Terraform
<a name="manual-option-deploy-supplychain-datasets-using-terraform"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Navigate to the `terraform-deployment `directory. | To go to the `terraform-deployment` directory of `ASC-Datasets`, run the following command:<pre>cd ASC-Datasets/terraform-deployment</pre> | AWS DevOps |
| Set up the Terraform state Amazon S3 bucket. | To set up the Terraform state Amazon S3 bucket, use the following script:<pre># Setup terraform bucket<br />chmod +x ../scripts/setup-terraform.sh<br />../scripts/setup-terraform.sh</pre> | AWS DevOps |
| Set up the Terraform artifacts Amazon S3 bucket. | To set up the Terraform artifacts Amazon S3 bucket, use the following script:<pre># Setup terraform artifacts bucket<br />chmod +x ../scripts/setup-terraform-artifacts-bucket.sh<br />../scripts/setup-terraform-artifacts-bucket.sh</pre> | AWS DevOps |
| Set up the Terraform backend and providers configuration. | To set up the Terraform backend and providers configuration, use the following script:<pre># Setup terraform backend and providers config if they don't exist<br />chmod +x ../scripts/generate-terraform-config.sh<br />../scripts/generate-terraform-config.sh</pre> | AWS DevOps |
| Generate a deployment plan. | To generate a deployment plan, run the following commands:<pre># Run terraform init and validate<br />terraform init<br />terraform validate<br /><br /># Run terraform plan<br />terraform plan \<br />-var-file="tfInputs/$ENVIRONMENT.tfvars" \<br />-var="project_name=$PROJECT_NAME" \<br />-var="environment=$ENVIRONMENT" \<br />-var="user_role=$AWS_USER_ROLE" \<br />-var="lambda_temp_dir=$LAMBDA_FUNCTION_TEMP_DIR_TERRAFORM" \<br />-var="layer_temp_dir=$LAMBDA_LAYER_TEMP_DIR_TERRAFORM" \<br />-parallelism=40 \<br />-out='tfplan.out'</pre> | AWS DevOps |
| Deploy the configurations. | To deploy the configurations, run the following command:<pre># Run terraform apply<br />terraform apply tfplan.out</pre> | AWS DevOps |
| Update other configurations and store outputs. | To update AWS KMS key policies and store the applied configurations outputs in the Terraform artifacts Amazon S3 bucket, run the following commands:<pre># Update AWS Supply Chain KMS Key policy with the service's requirements<br />chmod +x ../scripts/update-asc-kms-policy.sh<br />../scripts/update-asc-kms-policy.sh<br /></pre><pre># Update AWS KMS Keys' policy with IAM roles<br />chmod +x ../scripts/update-kms-policy.sh<br />../scripts/update-kms-policy.sh<br /></pre><pre># Create terraform outputs file to be used as input variables<br />terraform output -json > raw_output.json<br />jq -r 'to_entries | map(<br />  if .value.type == "string" then<br />      "\(.key) = \"\(.value.value)\""<br />  else<br />      "\(.key) = \(.value.value | tojson)"<br />  end<br />) | .[]' raw_output.json > $REPO_NAME-outputs.tfvars<br /></pre><pre># Upload reformed outputs file to Amazon S3 terraform artifacts bucket (For retrieval from other repositories)<br />aws s3 cp $REPO_NAME-outputs.tfvars s3://$S3_TERRAFORM_ARTIFACTS_BUCKET_NAME/$REPO_NAME-outputs.tfvars<br />rm -f raw_output.json<br />rm -f $REPO_NAME-outputs.tfvars<br /></pre> | AWS DevOps |

### (Manual option) Deploy Supply Chain service integration flows using Terraform
<a name="manual-option-deploy-supplychain-service-integration-flows-using-terraform"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Navigate to the `terraform-deployment` directory. | To go to the `terraform-deployment` directory of `ASC-Integration-Flows`, run the following command:<pre>cd ASC-Integration-Flows/terraform-deployment</pre> | AWS DevOps |
| Set up the Terraform backend and providers configuration. | To set up the Terraform backend and provider configurations, use the following script:<pre># Setup terraform backend and providers config if they don't exist<br />chmod +x ../scripts/generate-terraform-config.sh<br />../scripts/generate-terraform-config.sh</pre> | AWS DevOps |
| Generate a deployment plan. | To generate a deployment plan, run the following commands. These commands initialize your Terraform environment, merge configuration variables from `ASC-Datasets` with your existing Terraform configurations, and generate a deployment plan.<pre># Run terraform init and validate<br />terraform init<br />terraform validate<br /></pre><pre># Download and merge ASC DATASET tfvars<br />chmod +x ../scripts/download-vars-through-s3.sh<br />../scripts/download-vars-through-s3.sh $ASC_DATASET_VARS_REPO<br /></pre><pre># Run terraform plan<br />terraform plan \<br />-var-file="tfInputs/$ENVIRONMENT.tfvars" \<br />-var="project_name=$PROJECT_NAME" \<br />-var="environment=$ENVIRONMENT" \<br />-var="lambda_temp_dir=$LAMBDA_FUNCTION_TEMP_DIR_TERRAFORM" \<br />-var="layer_temp_dir=$LAMBDA_LAYER_TEMP_DIR_TERRAFORM" \<br />-parallelism=40 \<br />-out='tfplan.out'</pre> | AWS DevOps |
| Deploy the configurations. | To deploy the configurations, run the following command:<pre># Run terraform apply<br />terraform apply tfplan.out</pre> | AWS DevOps |
| Update other configurations. | To update AWS KMS key policies and store the applied configurations outputs in the Terraform artifacts Amazon S3 bucket, run the following commands:<pre># Update AWS KMS Keys' policy with IAM roles<br />chmod +x ../scripts/update-kms-policy-through-s3.sh<br />../scripts/update-kms-policy-through-s3.sh $ASC_DATASET_VARS_REPO<br /></pre><pre># Create terraform outputs file to be used as input variables<br />terraform output -json > raw_output.json<br />jq -r 'to_entries | map(<br />  if .value.type == "string" then<br />      "\(.key) = \"\(.value.value)\""<br />  else<br />      "\(.key) = \(.value.value | tojson)"<br />  end<br />) | .[]' raw_output.json > $REPO_NAME-outputs.tfvars<br /></pre><pre># Upload reformed outputs file to Amazon S3 terraform artifacts bucket (For retrieval from other repositories)<br />aws s3 cp $REPO_NAME-outputs.tfvars s3://$S3_TERRAFORM_ARTIFACTS_BUCKET_NAME/$REPO_NAME-outputs.tfvars<br />rm -f raw_output.json<br />rm -f $REPO_NAME-outputs.tfvars<br /></pre> | AWS DevOps |

### (Both options) Ingest data
<a name="both-options-ingest-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Upload sample CSV files. | To upload sample CSV files for the datasets, use the following steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-the-deployment-of-aws-supply-chain-data-lakes.html) | Data engineer |

### (Both options) Set up Supply Chain access
<a name="both-options-set-up-supplychain-access"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up Supply Chain access. | To set up Supply Chain access from the AWS Management Console, use the following steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-the-deployment-of-aws-supply-chain-data-lakes.html) | App owner |

### (Automated option) Clean up all resources using GitHub Actions workflows
<a name="automated-option-clean-up-all-resources-using-github-actions-workflows"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Trigger the destroy workflow for integration flows resources. | Trigger the [destroy workflow](https://github.com/aws-samples/sample-automate-aws-supply-chain-deployment/blob/main/ASC-Integration-Flows/.github/workflows/destroy-workflow.yml) of `ASC-Integration-Flows` from your deployment branch in your GitHub organization. | AWS DevOps |
| Trigger the destroy workflow for datasets resources. | Trigger the [destroy workflow](https://github.com/aws-samples/sample-automate-aws-supply-chain-deployment/blob/main/ASC-Datasets/.github/workflows/destroy-workflow.yml) of `ASC-Datasets` from your deployment branch in your GitHub organization. | AWS DevOps |

### (Manual option) Clean up resources of Supply Chain integration flows using Terraform
<a name="manual-option-clean-up-resources-of-supplychain-integration-flows-using-terraform"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Navigate to the `terraform-deployment` directory. | To go to the `terraform-deployment` directory of `ASC-Integration-Flows`, run the following command:<pre>cd ASC-Integration-Flows/terraform-deployment</pre> | AWS DevOps |
| Set up the Terraform backend and providers configuration. | To set up the Terraform backend and providers configuration, use the following script:<pre># Setup terraform backend and providers config if they don't exist<br />chmod +x ../scripts/generate-terraform-config.sh<br />../scripts/generate-terraform-config.sh</pre> | AWS DevOps |
| Generate infrastructure destruction plan. | To prepare for the controlled destruction of your AWS infrastructure by generating a detailed teardown plan, run the following commands. The process initializes Terraform, incorporates Supply Chain dataset configurations, and creates a destruction plan that you can review before executing.<pre># Run terraform init and validate<br />terraform init<br />terraform validate<br /></pre><pre># Download and merge ASC DATASET tfvars<br />chmod +x ../scripts/download-vars-through-s3.sh<br />../scripts/download-vars-through-s3.sh $ASC_DATASET_VARS_REPO<br /></pre><pre># Run terraform plan<br />terraform plan -destroy\<br />-var-file="tfInputs/$ENVIRONMENT.tfvars" \<br />-var="project_name=$PROJECT_NAME" \<br />-var="environment=$ENVIRONMENT" \<br />-var="lambda_temp_dir=$LAMBDA_FUNCTION_TEMP_DIR_TERRAFORM" \<br />-var="layer_temp_dir=$LAMBDA_LAYER_TEMP_DIR_TERRAFORM" \<br />-parallelism=40 \<br />-out='tfplan.out'</pre> | AWS DevOps |
| Execute infrastructure destruction plan. | To execute the planned destruction of your infrastructure, run the following command:<pre># Run terraform apply<br />terraform apply tfplan.out</pre> | AWS DevOps |
| Remove Terraform outputs from Amazon S3 bucket. | To remove the outputs file that was uploaded during the deployment of `ASC-Integration-Flows`, run the following command:<pre># Delete the outputs file<br />aws s3 rm s3://$S3_TERRAFORM_ARTIFACTS_BUCKET_NAME/$REPO_NAME-outputs.tfvars</pre> | AWS DevOps |

### (Manual option) Clean up resources of Supply Chain service datasets using Terraform
<a name="manual-option-clean-up-resources-of-supplychain-service-datasets-using-terraform"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Navigate to the `terraform-deployment` directory. | To go to the `terraform-deployment` directory of `ASC-Datasets`, run the following command:<pre>cd ASC-Datasets/terraform-deployment</pre> | AWS DevOps |
| Set up the Terraform backend and providers configuration. | To set up the Terraform backend and providers configuration, use the following script:<pre># Setup terraform backend and providers config if they don't exist<br />chmod +x ../scripts/generate-terraform-config.sh<br />../scripts/generate-terraform-config.sh</pre> | AWS DevOps |
| Generate infrastructure destruction plan. | To create a plan for destroying Supply Chain dataset resources, run the following commands:<pre># Run terraform init and validate<br />terraform init<br />terraform validate<br /><br /># Run terraform plan<br />terraform plan -destroy\<br />-var-file="tfInputs/$ENVIRONMENT.tfvars" \<br />-var="project_name=$PROJECT_NAME" \<br />-var="environment=$ENVIRONMENT" \<br />-var="user_role=$AWS_USER_ROLE" \<br />-var="lambda_temp_dir=$LAMBDA_FUNCTION_TEMP_DIR_TERRAFORM" \<br />-var="layer_temp_dir=$LAMBDA_LAYER_TEMP_DIR_TERRAFORM" \<br />-parallelism=40 \<br />-out='tfplan.out'</pre> | AWS DevOps |
| Empty Amazon S3 buckets. | To empty all Amazon S3 buckets (except the server access logging bucket, which is configured for `force-destroy`), use the following script:<pre># Delete S3 buckets excluding server access logging bucket<br />chmod +x ../scripts/empty-s3-buckets.sh<br />../scripts/empty-s3-buckets.sh tfplan.out</pre> | AWS DevOps |
| Execute infrastructure destruction plan. | To execute the planned destruction of your Supply Chain dataset infrastructure using the generated plan, run the following command:<pre># Run terraform apply<br />terraform apply tfplan.out</pre> | AWS DevOps |
| Remove Terraform outputs from the Amazon S3 Terraform artifacts bucket. | To complete the cleanup process, remove the outputs file that was uploaded during the deployment of `ASC-Datasets` by running the following command:<pre># Delete the outputs file<br />aws s3 rm s3://$S3_TERRAFORM_ARTIFACTS_BUCKET_NAME/$REPO_NAME-outputs.tfvars</pre> | AWS DevOps |

## Troubleshooting
<a name="automate-the-deployment-of-aws-supply-chain-data-lakes-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| An Supply Chain dataset or integration flow did not deploy correctly because of Supply Chain internal errors or insufficient IAM permissions for the service role. | First, clean up all resources. Then, redeploy the Supply Chain [dataset resources](https://github.com/aws-samples/sample-automate-aws-supply-chain-deployment/blob/main/ASC-Datasets/README.md) and then redeploy the Supply Chain [integration flow resources](https://github.com/aws-samples/sample-automate-aws-supply-chain-deployment/blob/main/ASC-Integration-Flows/README.md). |
| The Supply Chain integration flow doesn’t fetch the new data files uploaded for the Supply Chain datasets. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-the-deployment-of-aws-supply-chain-data-lakes.html) |

## Related resources
<a name="automate-the-deployment-of-aws-supply-chain-data-lakes-resources"></a>

**AWS documentation**
+ [Supply Chain](https://docs.aws.amazon.com/aws-supply-chain/latest/adminguide/getting-started.html)

**Other resources**
+ [Understanding GitHub Actions workflows](https://docs.github.com/en/actions/get-started/understand-github-actions) (GitHub documentation)

## Additional information
<a name="automate-the-deployment-of-aws-supply-chain-data-lakes-additional"></a>

This solution can be replicated for more datasets and can be queried for further analysis, through prebuilt dashboards provided with Supply Chain or custom integration with Amazon Quick Sight. In addition, you can use Amazon Q to ask questions related to your Supply Chain instance.

**Analyze data with Supply Chain Analytics**

For instructions to set up Supply Chain Analytics, see [Setting Supply Chain Analytics](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/setting_analytics.html) in the Supply Chain documentation.

This pattern demonstrated the creation of **Calendar** and **Outbound\_Order\_Line** datasets. To create an analysis that uses these datasets, use the following steps:

1. To analyze the datasets, use the **Seasonality Analysis** dashboard. To add the dashboard, follow the steps in [Prebuilt dashboards](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/prebuilt_dashboards.html) in the Supply Chain documentation.

1. Choose the dashboard to see its analysis that is based on sample CSV files for Calendar data and Outbound Order Line data.

The dashboard provides insights on demand over the years based on the ingested data for the datasets. You can further specify the ProductID, CustomerID, years, and other parameters for analysis.

**Use Amazon Q to ask questions related to your Supply Chain instance**

[Amazon Q in Supply Chain](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/qinasc.html) is an interactive generative AI assistant that helps you operate your supply chain more efficiently. Amazon Q can do the following:
+ Analyze the data in your Supply Chain data lake.
+ Provide operational and financial insights.
+ Answer your immediate supply chain questions.

For more information about using Amazon Q, see [Enabling Amazon Q in Supply Chain](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/enabling_QinASC.html) and [Using Amazon Q in Supply Chain](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/using_QinASC.html) in the Supply Chain documentation.
