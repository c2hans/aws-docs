---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/basic-datalake-starter-package.html
---

# Basic Data Lake Starter Package
<a name="basic-datalake-starter-package"></a>

The Basic Data Lake Starter Package establishes a robust foundation for storing and managing large volumes of data in its native format.

 **Basic Data Lake starter kit architecture**

![Basic Data Lake starter kit — secure S3 data lake with Glue Data Catalog and Athena querying.](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/images/basic_datalake.png)

This S3 Data Lake implementation demonstrates best practices for creating an enterprise data lake on AWS. Access to the data lake can be granted to IAM and federated principals, with comprehensive access controls.

This architecture is particularly effective when:

1. You need to store both structured and unstructured data in a centralized repository.

1. Your organization requires governed access to data lake resources.

Deploy this package when you need a scalable, secure foundation that supports your organization’s data storage and analytics requirements.

The Data Lake Starter Package provides a complete foundation for enterprise data management with a secure, scalable architecture organized into multiple domains:

## Shared Domain Components
<a name="shared-domain-components-2"></a>
+  **IAM Roles** - Predefined roles for data administrators, users, and ETL processes with least-privilege permissions
+  **S3 Data Lake** - Multi-zone storage architecture with raw and transformed data buckets
+  **Access Policies** - Granular bucket policies with prefix-based access controls
+  **Glue Data Catalog** - KMS-encrypted metadata repository for data assets
+  **Lake Formation** - Configured for IAM-based access control to data resources
+  **Athena Workgroups** - Query environment with predefined settings for data analysis
+  **Audit Components** - CloudTrail integration with secure S3 buckets for comprehensive audit trails

## DataOps Domain Components
<a name="dataops-domain-components-2"></a>
+  **DataOps Projects** - Shared resources for data engineering workflows
+  **Glue Crawlers** - Automated metadata discovery for data assets

This architecture provides a robust foundation for organizations that need to:

1. Centralize data storage with appropriate security controls

1. Implement governance and compliance requirements

1. Enable self-service data access for various user roles

1. Support both batch and interactive data processing

The Data Lake Starter Package follows AWS best practices for security, scalability, and operational excellence, making it an ideal starting point for organizations building their modern data architecture.

## Deployment Instructions
<a name="deployment-instructions-2"></a>

Step-by-step guide for deploying the Data Lake Starter Package

You can deploy the Basic Data Lake Starter Package using one of two methods: 1. CloudFormation Installer Method (recommended for most users) 2. Manual CLI Deploy Method (for advanced customization)

### Method 1: CloudFormation Installer Method
<a name="method-1-cloudformation-installer-method-2"></a>

#### Prerequisites
<a name="prerequisites-4"></a>

Before deploying using the CloudFormation installer, verify you have:

1. An AWS account with permissions to create the required resources

1. A GitHub CodeConnect connection (if using GitHub as source) or an S3 bucket with the solution code (if using S3 as source)

### Deployment Steps
<a name="deployment-steps-3"></a>

 **Step 1: Launch the CloudFormation stack**

 **Step 2: Configure the stack**

1. Assign a unique name to your stack (e.g., `mdaa-basicdatalake-<accountname>-<region>`)

1. Under Parameters:
   + Enter your organization name in the `OrgName` field
   + Select `github` as the Source (default)
   + Verify the Repository Owner is `aws` and Repository Name is `modern-data-architecture-accelerator`
   + Enter your GitHub CodeConnect Connection ARN
   + Select `basic_datalake` as the Sample Name

1. Choose Next, review the settings, and acknowledge that the template might create IAM resources

1. Choose Submit to deploy the stack

 **Step 3: Monitor the deployment**

1. Navigate to the AWS CodePipeline console to monitor the deployment progress

1. The pipeline will show a status of either `In Progress` or `Complete`

1. The deployment typically takes about 15-20 minutes for the basic datalake configuration

 **Step 4: Verify deployment**

Check that all CloudFormation stacks have completed successfully and the installer pipeline shows a COMPLETE status

### Method 2: Manual CLI Deploy Method
<a name="method-2-manual-cli-deploy-method-2"></a>

#### Prerequisites
<a name="prerequisites-5"></a>

Before deploying the Basic Data Lake Starter Package using the CLI method, verify you have:

1. AWS CLI configured with appropriate credentials

1. Node.js 22.x or later and npm/npx 10.x or later installed

1. AWS CDK installed (`npm install -g aws-cdk`)

1. CDK bootstrapped in your target account and region

#### Deployment Steps
<a name="deployment-steps-4"></a>

 **Step 1: Clone the MDAA repository**

```
git clone https://github.com/aws/modern-data-architecture-accelerator.git &&
cd modern-data-architecture-accelerator
```

 **Step 2: Configure your deployment**
+ Copy the sample configuration files:

```
cp -r starter_kits/basic_datalake my_datalake_config
cd my_datalake_config
```
+ Edit the `mdaa.yaml` file to set your organization name:

```
organization: <your-org-name>
```

 **Step 3: Deploy the solution** \* Verify you are authenticated to your target AWS account.
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

 **Step 4: Verify deployment** \* Check the AWS CloudFormation console to verify all stacks have been created successfully \* Verify the S3 buckets, Glue Crawler, IAM roles, and other resources have been created

## Usage Instructions
<a name="usage-instructions-2"></a>

How to effectively use the Basic Data Lake Starter Package after deployment

Once the MDAA deployment is complete, follow these steps to interact with the data lake:

### Initial Setup and Data Upload
<a name="initial-setup-and-data-upload"></a>

1.  **Create sample data for testing**
   + Check the `DATASETS.md` file in the starter\_kits/basic\_datalake directory for instructions on creating a sample\_data folder
   + Alternatively, prepare your own data files for upload

1.  **Assume the data-admin role**
   + This role is configured with AssumeRole trust to the local account by default
   + Note that this role is the only role configured with write access to the data lake
   + All other roles (including existing administrator roles in the account) will be denied write access

1.  **Upload sample data to the transformed bucket**
   + Upload the sample\_data folder and contents to the transformed bucket.

### Data Discovery and Querying
<a name="data-discovery-and-querying"></a>

1.  **Run the Glue Crawler**
   + In the AWS Glue Console, locate the crawler created by the deployment
   + Trigger/run the Glue Crawler
   + Once successful, view the Crawler’s CloudWatch logs to observe that tables were created

1.  **Assume the data-user role**
   + This role is configured with AssumeRole trust to the local account by default
   + It has read-only access to the data lake

1.  **Query data using Athena**
   + In the Athena Query Editor, select the MDAA-deployed Workgroup from the dropdown list
   + The tables created by the crawler should be available for query under the MDAA-created Database

For more detailed information about the configuration files and their purposes, refer to the README.md file in the starter\_kits/basic\_datalake directory of the MDAA repository.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Modern Data Architecture Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
