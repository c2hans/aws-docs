---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/ai-ml-starter-package.html
---

# AI/ML Starter Package
<a name="ai-ml-starter-package"></a>

The AI/ML Starter Package establishes a comprehensive environment for developing, training, and deploying machine learning models at scale.

![datascience](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/images/datascience.png)

**AI/ML (Basic Data Science) starter kit architecture**
This implementation demonstrates AWS best practices for creating an enterprise-grade data science platform. It combines data lake capabilities with SageMaker Studio to provide data scientists with the tools they need while maintaining appropriate governance and security controls.

This architecture is particularly effective when:

1. You need to enable data science teams to rapidly develop and deploy ML models.

1. Your organization requires governed access to data and model resources.

Deploy this package when you need a scalable, secure foundation that supports your organization’s machine learning and AI initiatives.

The AI/ML Starter Package provides a comprehensive environment for developing, training, and deploying machine learning models. This package is organized into three domains that work together to create a complete data science platform:

## Shared Domain Components
<a name="shared-domain-components"></a>
+  **IAM Roles** - Secure access controls for data science teams
+  **Data Lake** - S3 buckets for storing training data and model artifacts
+  **Glue Data Catalog** - KMS-encrypted metadata management
+  **Lake Formation** - Fine-grained access control for data assets
+  **Athena Workgroups** - SQL-based data exploration capabilities
+  **Audit Components** - CloudTrail integration for comprehensive governance

## DataOps Domain Components
<a name="dataops-domain-components"></a>
+  **DataOps Projects** - Shared resources for data engineering workflows
+  **Glue Crawlers** - Automated metadata discovery and schema management

## DataScience Domain Components
<a name="datascience-domain-components"></a>
+  **SageMaker Studio** - Fully managed development environment for ML
+  **Team Workspaces** - Isolated environments for data science teams
+  **Jupyter Notebooks** - Pre-configured templates for common ML tasks
+  **Model Registry** - Version control for ML models
+  **Training Pipelines** - Automated workflows for model development
+  **Deployment Infrastructure** - Endpoints for model serving

This package accelerates your AI/ML initiatives by providing a ready-to-use environment with AWS best practices built in. It’s ideal for organizations looking to establish or enhance their machine learning capabilities with a secure, scalable foundation.

## Deployment Instructions
<a name="deployment-instructions"></a>

Step-by-step guide for deploying the AI/ML Starter Package

You can deploy the AI/ML Starter Package using one of two methods: 1. CloudFormation Installer Method (recommended for most users) 2. Manual CLI Deploy Method (for advanced customization)

### Method 1: CloudFormation Installer Method
<a name="method-1-cloudformation-installer-method"></a>

#### Prerequisites
<a name="prerequisites-2"></a>

Before deploying using the CloudFormation installer, ensure you have:

1. An AWS account with permissions to create the required resources

1. A GitHub CodeConnect connection (if using GitHub as source) or an S3 bucket with the solution code (if using S3 as source)

1. A VPC with at least one subnet (required for SageMaker Studio)

#### Deployment Steps
<a name="deployment-steps"></a>

 **Step 1: Launch the CloudFormation stack**

 **Step 2: Configure the stack**

1. Assign a unique name to your stack (e.g., `mdaa-aiml-<accountname>-<region>`).

1. Under Parameters:
   + Enter your organization name in the `OrgName` field
   + Select `github` as the Source (default)
   + Verify the Repository Owner is `aws` and Repository Name is `modern-data-architecture-accelerator`
   + Enter your GitHub CodeConnect Connection ARN
   + Select `basic_datascience_platform` as the Sample Name
   + Provide Subnet ID and VPC ID (required for SageMaker Studio)

1. Choose Next, review the settings, and acknowledge that the template might create IAM resources

1. Choose Submit to deploy the stack

 **Step 3: Monitor the deployment**

1. Navigate to the AWS CodePipeline console to monitor the deployment progress

1. The pipeline will show a status of either `In Progress` or `Complete`

1. The deployment typically takes about 30-45 minutes for the AI/ML configuration

 **Step 4: Verify deployment**

Check that all CloudFormation stacks have completed successfully and the installer pipeline shows a COMPLETE status

### Method 2: Manual CLI Deploy Method
<a name="method-2-manual-cli-deploy-method"></a>

#### Prerequisites
<a name="prerequisites-3"></a>

Before deploying the AI/ML Starter Package using the CLI method, ensure you have:

1. AWS CLI configured with appropriate credentials

1. Node.js 22.x or later and npm/npx 10.x or later installed

1. AWS CDK installed (`npm install -g aws-cdk`)

1. CDK bootstrapped in your target account and region

1. A VPC with at least one subnet (required for SageMaker Studio)

#### Deployment Steps
<a name="deployment-steps-2"></a>

 **Step 1: Clone the MDAA repository**

```
git clone https://github.com/aws/modern-data-architecture-accelerator.git &&
cd modern-data-architecture-accelerator
```

 **Step 2: Configure your deployment**
+ Copy the sample configuration files:

```
cp -r starter_kits/basic_datascience_platform my_aiml_config
cd my_aiml_config
```
+ Edit the `mdaa.yaml` file to set your organization name, datascience team name and VPC/subnet information:

```
organization: <your-org-name>
context:
  vpc_id: <your vpc id>
  subnet_id: <your subnet id>
  datascience_team_name: <your datascience team name>
```

 **Step 3: Deploy the solution** \* Ensure you are authenticated to your target AWS account.
+ Optionally, run the following command to understand what stacks will be deployed:

```
npx @aws-mdaa/cli ls
```
+ Optionally, run the following command to review the produced templates:

```
npx @aws-mdaa/cli synth
```
+ Run the following command to deploy all modules:

```
npx @aws-mdaa/cli deploy
```

 **Step 4: Verify deployment** \* Check the AWS CloudFormation console to ensure all stacks have been created successfully \* Verify the SageMaker Studio Domain, IAM roles, and other resources have been created

## Usage Instructions
<a name="usage-instructions"></a>

How to effectively use the AI/ML Starter Package after deployment

Once the MDAA deployment is complete, follow these steps to interact with the AI/ML platform:

### Initial Setup and Data Access
<a name="initial-setup-and-data-access"></a>

1.  **Create sample data for testing**
   + Check the `DATASETS.md` file in the starter\_kits/basic\_datascience\_platform directory for instructions on creating a sample\_data folder
   + Alternatively, prepare your own data files for upload

1.  **Assume the shared-roles-data-admin role**
   + This role is configured with AssumeRole trust to the local account by default
   + It has write access to the data lake

1.  **Upload sample data to the transformed bucket**
   + Upload the sample\_data folder and contents to the transformed bucket

1.  **Run the Glue Crawler**
   + In the AWS Glue Console, trigger/run the Glue Crawler
   + Once successful, view the Crawler’s CloudWatch logs to observe that tables were created

### Using SageMaker Studio
<a name="using-sagemaker-studio"></a>

1.  **Assume the data-scientist role**
   + This role is configured with AssumeRole trust to the local account by default
   + Important: The role session name must match the userid specified in the datascience-team.yaml configuration

1.  **Access SageMaker Studio**
   + Navigate to the Amazon SageMaker console
   + Go to the Domain section and find the deployed SageMaker Studio Domain
   + Launch the user profile matching your role session name/userid
   + SageMaker Studio should launch

1.  **Work with data in Athena**
   + In the Athena Query Editor, select the MDAA-deployed Workgroup from the dropdown list
   + The tables created by the crawler should be available for query under the MDAA-created Database
   + Run queries to explore and analyze your data

1.  **Develop ML models**
   + Use the pre-configured Jupyter notebooks in SageMaker Studio
   + Access your data through the Athena integration
   + Train models using SageMaker’s built-in algorithms or custom code
   + Deploy models to SageMaker endpoints for inference

For more detailed information about the configuration files and their purposes, refer to the README.md file in the starter\_kits/basic\_datascience\_platform directory of the MDAA repository.
