---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/smus-data-mesh-starter-package.html
---

# SMUS Data Mesh Starter Package
<a name="smus-data-mesh-starter-package"></a>

The SMUS Data Mesh Starter Package deploys a production-ready, multi-account SageMaker Unified Studio deployment with cross-account data sharing, custom blueprints, and team-based isolation. It is designed for medium to large organizations implementing a data mesh, with multiple business units that need to collaborate on data while maintaining security boundaries and governance controls.

![smus comprehensive](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/images/smus_comprehensive.png)

**SMUS Data Mesh starter kit architecture**
This architecture is particularly effective when:

1. You have multiple business units in separate AWS accounts that need to collaborate on data.

1. You need centralized governance via a single SMUS domain managing data access across accounts.

1. You want cross-account data sharing with teams publishing and consuming data across account boundaries.

1. You need custom blueprints for standardized infrastructure patterns deployed via SMUS projects.

## Enterprise Account Components
<a name="enterprise-account-components"></a>
+  **Data Lake** - Three-zone S3 data lake (raw, transformed, curated), KMS-encrypted
+  **SMUS Domain** - DataZone V2 domain with cross-account associations
+  **Domain Units** - Organizational hierarchy
+  **DataOps Projects** - Glue catalogs, crawlers, and SMUS data sources

## Per-Account Components
<a name="per-account-components"></a>
+  **Glue Catalog** - KMS encryption at the account level (all accounts)
+  **IAM Roles** - `data-admin`, `data-engineer`, `glue-etl`, `ddb-bp-prov` per account
+  **Lake Formation Settings** - DataZone integration
+  **Audit** - Encrypted S3 audit bucket and CloudTrail trail (all accounts)

## Cross-Account Blueprint Components
<a name="cross-account-blueprint-components"></a>
+  **DynamoDB Custom Blueprint** - Deployed across all accounts via project profiles
+  **SMUS Project Profiles** - Standardized deployable environments per team

## Deployment Instructions
<a name="deployment-instructions-10"></a>

### Manual CLI Deploy Method
<a name="manual-cli-deploy-method-8"></a>

#### Prerequisites
<a name="prerequisites-13"></a>

Before deploying the SMUS Data Mesh Starter Package using the CLI method, ensure you have:

1. AWS CLI configured with appropriate credentials for the deployment account

1. Node.js 22.x or later and npm/npx 10.x or later installed

1. AWS CDK bootstrapped in all three accounts (enterprise, team1, team2) with cross-account trust

1. All three accounts must be members of the same AWS Organization, with RAM sharing and automated associations enabled

1. IAM Identity Center enabled in the target region, with SSO groups for enterprise, team1, and team2

1. VPCs with private subnets in each account. Subnets must have connectivity to AWS service endpoints via public routing or VPC Endpoints.

#### Deployment Steps
<a name="deployment-steps-12"></a>

 **Step 1: Clone the MDAA repository**

```
git clone https://github.com/aws/modern-data-architecture-accelerator.git &&
cd modern-data-architecture-accelerator
```

 **Step 2: Configure your deployment**
+ Copy the starter kit files:

```
cp -r starter_kits/smus_data_mesh my_smus_mesh
cd my_smus_mesh
```
+ Edit `mdaa.yaml`:

```
organization: <your-unique-org-name>
context:
  enterprise_account: <account id>
  team1_account: <account id>
  team2_account: <account id>
  admin1_user_sso_id: <admin SSO user id>
  enterprise_group_sso_id: <enterprise SSO group>
  team1_group_sso_id: <team1 SSO group>
  team2_group_sso_id: <team2 SSO group>
  enterprise_vpc_id: <vpc id>
  enterprise_private_subnet_id1: <subnet id>
  enterprise_private_subnet_id2: <subnet id>
  team1_vpc_id: <vpc id>
  team1_private_subnet_id1: <subnet id>
  team1_private_subnet_id2: <subnet id>
  team2_vpc_id: <vpc id>
  team2_private_subnet_id1: <subnet id>
  team2_private_subnet_id2: <subnet id>
```

 **Step 3: Deploy the solution**

```
npx @aws-mdaa/cli ls
npx @aws-mdaa/cli synth
npx @aws-mdaa/cli deploy
```

 **Step 4: Verify deployment**
+ Verify the SMUS domain in the enterprise account associates the team1 and team2 accounts, and that project profiles and the DynamoDB blueprint are visible in the SMUS console.

## Usage Instructions
<a name="usage-instructions-10"></a>

1.  **Access the SMUS portal** — Sign in via IAM Identity Center; users are routed based on their SSO group membership.

1.  **Publish data products** — Team accounts register Glue databases as data sources and publish assets to the enterprise SMUS domain.

1.  **Consume across accounts** — Consumer teams subscribe to data assets via DataZone; Lake Formation enforces fine-grained access across accounts.

1.  **Deploy the DynamoDB blueprint** — The custom blueprint is deployable in team accounts via SMUS project profiles.

For more detailed information, refer to the README.md and USAGE.md files in the starter\_kits/smus\_data\_mesh directory of the MDAA repository.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Modern Data Architecture Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
