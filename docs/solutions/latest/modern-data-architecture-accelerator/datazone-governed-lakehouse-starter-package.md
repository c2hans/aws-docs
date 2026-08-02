---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/datazone-governed-lakehouse-starter-package.html
---

# DataZone Governed Lakehouse Starter Package
<a name="datazone-governed-lakehouse-starter-package"></a>

The DataZone Governed Lakehouse Starter Package delivers an enterprise-ready data lakehouse with comprehensive governance capabilities using Amazon DataZone and AWS Lake Formation. This package provides fine-grained access control, data product management, and multi-team collaboration features essential for modern data governance.

![governed lakehouse](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/images/governed_lakehouse.png)

**DataZone Governed Lakehouse starter kit architecture**
Built on AWS best practices, this package combines the flexibility of a data lake with the governance and structure of a data warehouse. It enables organizations to implement data mesh architectures while maintaining centralized governance and compliance controls.

This architecture is particularly effective when:

1. You need fine-grained access control for structured data across multiple teams and projects.

1. Your organization requires comprehensive data governance with data product management capabilities.

Deploy this package when you need a scalable, governed foundation that supports enterprise data governance requirements with DataZone integration and Lake Formation security controls.

The DataZone Governed Lakehouse Starter Package provides a complete environment for enterprise data governance with comprehensive access controls. This package is organized into multiple domains that work together to create a governed data platform:

## Shared Governance Components
<a name="shared-governance-components"></a>
+  **IAM Roles** - Comprehensive roles including data-admin with Lake Formation permissions and data-user roles with fine-grained access controls
+  **Lake Formation Settings** - Configured to disable automatic IAM grants and enable fine-grained access control
+  **Glue Data Catalog** - KMS-encrypted metadata repository with governance controls

## Data Domain Components
<a name="data-domain-components"></a>
+  **S3 Data Lake** - Multi-tier storage architecture with raw, transformed, and curated data buckets
+  **KMS Encryption** - Customer-managed keys for data-at-rest encryption
+  **Bucket Policies** - Fine-grained access controls integrated with Lake Formation

## Governance Domain Components
<a name="governance-domain-components"></a>
+  **DataZone Domain** - Data product management and discovery platform
+  **Environment Blueprints** - Standardized environments for data producers and consumers
+  **Project Templates** - Reusable configurations for different team types

## DataOps Domain Components
<a name="dataops-domain-components-3"></a>
+  **DataOps Projects** - Multiple project configurations for data producers and consumers
+  **Glue Crawlers** - Automated metadata discovery with governance integration
+  **Lake Formation Permissions** - Database and table-level access controls

This package accelerates your data governance initiatives by providing a ready-to-use environment with AWS best practices built in. It’s ideal for organizations looking to establish or enhance their data governance capabilities with enterprise-grade controls, data product management, and multi-team collaboration features.

## Deployment Instructions
<a name="deployment-instructions-4"></a>

Step-by-step guide for deploying the DataZone Governed Lakehouse Starter Package

You can deploy the DataZone Governed Lakehouse Starter Package using Manual CLI Deploy Method

### Manual CLI Deploy Method
<a name="manual-cli-deploy-method-2"></a>

#### Prerequisites
<a name="prerequisites-7"></a>

Before deploying the DataZone Governed Lakehouse Starter Package using the CLI method, ensure you have:

1. AWS CLI configured with appropriate credentials

1. Node.js 22.x or later and npm/npx 10.x or later installed

1. AWS CDK installed (`npm install -g aws-cdk`)

1. CDK bootstrapped in your target account and region

#### Deployment Steps
<a name="deployment-steps-6"></a>

 **Step 1: Clone the MDAA repository**

```
git clone https://github.com/aws/modern-data-architecture-accelerator.git &&
cd modern-data-architecture-accelerator
```

 **Step 2: Configure your deployment**
+ Copy the sample configuration files:

```
cp -r starter_kits/datazone_governed_lakehouse my_governed_lakehouse
cd my_governed_lakehouse
```
+ Edit the `mdaa.yaml` file to set your organization name:

```
organization: <your-unique-org-name>
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

 **Step 4: Verify deployment** \* Check the AWS CloudFormation console to ensure all stacks have been created successfully \* Verify the DataZone domain, Lake Formation settings, S3 buckets, and other resources have been created

## Usage Instructions
<a name="usage-instructions-4"></a>

How to effectively use the DataZone Governed Lakehouse Starter Package after deployment

Once the MDAA deployment is complete, follow these steps to interact with the governed lakehouse:

### Initial Setup and Data Upload
<a name="initial-setup-and-data-upload-2"></a>

1.  **Assume the data-admin role**
   + This role is configured with AssumeRole trust to the local account by default
   + It has comprehensive permissions for Lake Formation and DataZone administration
   + Note: This role is the only role configured with write access to the data lake

1.  **Prepare sample data for testing**
   + Check the `DATASETS.md` file in the starter\_kits/datazone\_governed\_lakehouse directory for instructions on creating sample data
   + Alternatively, prepare your own structured data files for upload

1.  **Upload data to the data lake buckets**
   + Upload data to the appropriate tier based on processing stage:
     + Raw data: `${org}-${env}-data1-datalake-raw`
     + Transformed data: `${org}-${env}-data1-datalake-transformed`
     + Curated data: `${org}-${env}-data1-datalake-curated`
   + Ensure data is uploaded with KMS encryption

### Data Discovery and Governance
<a name="data-discovery-and-governance"></a>

1.  **Run Glue Crawlers**
   + Navigate to the AWS Glue Console
   + Trigger the Glue Crawlers created by the deployment
   + Monitor CloudWatch logs to verify table creation and metadata discovery

1.  **Access DataZone Portal**
   + Navigate to the Amazon DataZone console
   + Launch the DataZone Domain Portal
   + Explore the data governance capabilities including data product creation and discovery

1.  **Configure Lake Formation Permissions**
   + Use Lake Formation to grant fine-grained permissions to different user roles
   + Configure database and table-level access controls as needed
   + Set up data filters for row and column-level security

### Multi-Team Data Access
<a name="multi-team-data-access"></a>

1.  **Assume appropriate user roles**
   + Use data-user roles for read-only access to governed data
   + Each role has specific Lake Formation permissions configured

1.  **Query data using Athena**
   + Access Athena through the configured workgroups
   + Query tables that have been cataloged and for which you have Lake Formation permissions
   + Use DataZone to discover and subscribe to data products

1.  **Manage data products**
   + Create data products in DataZone for different business domains
   + Publish data assets for discovery by other teams
   + Subscribe to data products created by other teams

For more detailed information about the configuration files and their purposes, refer to the README.md file in the starter\_kits/datazone\_governed\_lakehouse directory of the MDAA repository.
