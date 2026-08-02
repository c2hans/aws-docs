---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/mlops-platform-starter-package.html
---

# MLOps Platform Starter Package
<a name="mlops-platform-starter-package"></a>

The MLOps Platform Starter Package deploys an end-to-end ML lifecycle platform covering training, deployment, and monitoring — governed through MDAA with CDK Nag compliance (AWS Solutions, NIST 800-53, HIPAA, PCI-DSS).

![mlops](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/images/mlops.png)

**MLOps Platform starter kit architecture**
This architecture is particularly effective when:

1. You need automated ML model training pipelines with a versioned model registry.

1. You need multi-stage model deployment (dev → pre-prod → prod) with manual approval gates.

1. You require real-time inference endpoints with model quality monitoring.

1. You need CI/CD for ML with CodePipeline and CodeBuild.

1. You need cross-account model deployment for environment isolation.

## MLOps Components
<a name="mlops-components"></a>
+  **SageMaker MLOps** - Unified training and deployment CI/CD pipelines via `@aws-mdaa/sagemaker-mlops`
+  **SageMaker Pipeline** - preprocess → train → register with automatic execution
+  **SageMaker Endpoint** - With model quality monitoring schedule
+  **Model Package Group** - Versioned model registry
+  **EventBridge** - Triggers deployment pipeline on model approval
+  **KMS-Encrypted S3 Bucket** - For model artifacts
+  **CodeCommit Repositories** - Seeded with ML scripts and MDAA configs

## Deployment Instructions
<a name="deployment-instructions-7"></a>

### Manual CLI Deploy Method
<a name="manual-cli-deploy-method-5"></a>

#### Prerequisites
<a name="prerequisites-10"></a>

Before deploying the MLOps Platform Starter Package using the CLI method, ensure you have:

1. AWS CLI configured with appropriate credentials

1. Node.js 22.x or later and npm/npx 10.x or later installed

1. AWS CDK bootstrapped in your target account and region. For cross-account deployment, also bootstrap the target accounts with cross-account trust.

1. A VPC with at least 2 private subnets and security groups. Subnets must have connectivity to AWS service endpoints via a NAT Gateway or VPC endpoints for `s3`, `sagemaker.api`, `sagemaker.runtime`, `sts`, and `logs`.

1. Sample training data (for example, the Abalone dataset) placed in the starter kit’s `data/` directory.

#### Deployment Steps
<a name="deployment-steps-9"></a>

 **Step 1: Clone the MDAA repository**

```
git clone https://github.com/aws/modern-data-architecture-accelerator.git &&
cd modern-data-architecture-accelerator
```

 **Step 2: Configure your deployment**
+ Copy the starter kit files:

```
cp -r starter_kits/mlops_platform my_mlops
cd my_mlops
```
+ Edit `mdaa.yaml`:

```
organization: <your-unique-org-name>
context:
  sagemaker_project_name: <ml-project-identifier>
  vpc_id: <your vpc id>
  subnet_ids: [<subnet-1>, <subnet-2>]
  security_group_ids: [<sg-1>]
```
+ Optionally configure `preProdEnvironment` and `prodEnvironment` in `mlops/mlops.yaml` for cross-account deployment.

 **Step 3: Deploy the solution**

```
npx @aws-mdaa/cli ls
npx @aws-mdaa/cli synth
npx @aws-mdaa/cli deploy
```

 **Step 4: Verify deployment**
+ Verify the training and deployment CodePipeline pipelines, the SageMaker Pipeline, and the Model Package Group are created in the SageMaker console.

## Usage Instructions
<a name="usage-instructions-7"></a>

1.  **Run the training pipeline** — CodePipeline triggers the seeded SageMaker training pipeline on first deploy. Subsequent runs can be triggered manually or by pushing changes to the seeded CodeCommit repositories.

1.  **Approve the trained model** — Register the model in the Model Package Group with `ModelApprovalStatus: Approved` to trigger the deployment pipeline via EventBridge.

1.  **Invoke the endpoint** — Once deployed, the SageMaker Endpoint is monitored on a scheduled cadence for model quality drift.

1.  **Cross-account promotion** — If configured, the deployment pipeline promotes the approved model through dev → pre-prod → prod with manual approval gates.

For more detailed information, refer to the README.md and USAGE.md files in the starter\_kits/mlops\_platform directory of the MDAA repository.
