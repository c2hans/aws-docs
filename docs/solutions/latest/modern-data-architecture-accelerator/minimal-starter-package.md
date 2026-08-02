---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/minimal-starter-package.html
---

# Minimal Starter Package
<a name="minimal-starter-package"></a>

The Minimal Starter Package deploys the foundational governance layer required by all MDAA architectures: IAM roles, Glue Catalog encryption, and Lake Formation settings. Use this as a starting point when you want to build your own architecture from scratch by adding modules incrementally.

![minimal](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/images/minimal.png)

**Minimal starter kit architecture**
This architecture is particularly effective when:

1. You are starting a new MDAA project from scratch and want to add modules incrementally.

1. You want to establish governance foundations before committing to a specific architecture.

## Shared Governance Components
<a name="shared-governance-components-2"></a>
+  **IAM Roles** - IAM role generation with CDK Nag compliance
+  **Glue Catalog** - KMS encryption at the account level
+  **Lake Formation Settings** - Delegates access control to IAM at the account level
+  **Resource Tagging** - Cost allocation and operational governance tagging

## Deployment Instructions
<a name="deployment-instructions-5"></a>

You can deploy the Minimal Starter Package using the Manual CLI Deploy Method.

### Manual CLI Deploy Method
<a name="manual-cli-deploy-method-3"></a>

#### Prerequisites
<a name="prerequisites-8"></a>

Before deploying the Minimal Starter Package using the CLI method, ensure you have:

1. AWS CLI configured with appropriate credentials

1. Node.js 22.x or later and npm/npx 10.x or later installed

1. AWS CDK bootstrapped in your target account and region

#### Deployment Steps
<a name="deployment-steps-7"></a>

 **Step 1: Clone the MDAA repository**

```
git clone https://github.com/aws/modern-data-architecture-accelerator.git &&
cd modern-data-architecture-accelerator
```

 **Step 2: Configure your deployment**
+ Copy the starter kit files:

```
cp -r starter_kits/minimal my_minimal_config
cd my_minimal_config
```
+ Edit the `mdaa.yaml` file to set your organization name:

```
organization: <your-unique-org-name>
```
+ Review and address CDK Nag suppression TODOs in `govern/roles.yaml`.

 **Step 3: Deploy the solution**

```
npx @aws-mdaa/cli ls
npx @aws-mdaa/cli synth
npx @aws-mdaa/cli deploy
```

 **Step 4: Verify deployment**
+ Verify the IAM roles, Glue Catalog encryption, and Lake Formation settings have been created in the AWS console.

## Usage Instructions
<a name="usage-instructions-5"></a>

Once deployed, extend your architecture by adding modules from the MDAA module catalog. Common next modules include:
+  `@aws-mdaa/datalake` for S3 storage with encryption and access policies
+  `@aws-mdaa/athena-workgroup` for SQL querying
+  `@aws-mdaa/dataops-project` for ETL pipeline infrastructure

For more detailed information, refer to the README.md file in the starter\_kits/minimal directory of the MDAA repository.
