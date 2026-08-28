---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/smus-research-environment-starter-package.html
---

# SMUS Research Environment Starter Package
<a name="smus-research-environment-starter-package"></a>

The SMUS Research Environment Starter Package deploys a SageMaker Unified Studio (SMUS) environment for organizations with multiple research teams operating within a single AWS account. It provides a governed ML platform where teams collaborate on data and ML projects through the SMUS portal, with centralized identity management via IAM Identity Center.

![smus research environment](http://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/images/smus_research_environment.png)

**SMUS Research Environment starter kit architecture**
This architecture is particularly effective when:

1. You have multiple research teams operating in a single account under shared governance.

1. You want self-service ML platform access via the SMUS portal.

1. You need team-based project isolation with SSO group membership.

## Governance Components
<a name="governance-components"></a>
+  **Glue Catalog** - KMS encryption at the account level
+  **IAM Roles** - Domain and data administration roles
+  **Lake Formation Settings** - Account-level governance for fine-grained data access
+  **Audit** - Encrypted S3 audit bucket and CloudTrail trail for S3 data events

## SMUS Components
<a name="smus-components"></a>
+  **SMUS Domain** - DataZone V2 domain with IAM Identity Center SSO integration
+  **Project Profiles** - Standardized team environments
+  **Team Projects** - Team1 and team2 projects with SSO group membership

## Deployment Instructions
<a name="deployment-instructions-9"></a>

### Manual CLI Deploy Method
<a name="manual-cli-deploy-method-7"></a>

#### Prerequisites
<a name="prerequisites-12"></a>

Before deploying the SMUS Research Environment Starter Package using the CLI method, ensure you have:

1. AWS CLI configured with appropriate credentials

1. Node.js 22.x or later and npm/npx 10.x or later installed

1. AWS CDK bootstrapped in your target account and region. The account should be part of an AWS Organization for full Identity Center support.

1. IAM Identity Center enabled in the deployment region, with SSO groups created for team1 and team2.
**Note**
If deploying to an account not part of an AWS Organization, you must deploy in the same region where IAM Identity Center is enabled, or deployment will fail with `IDC not enabled (Service: DataZone, Status Code: 400)`.

1. A VPC with at least 2 private subnets. Subnets must have connectivity to AWS service endpoints via a NAT Gateway or VPC endpoints for SageMaker API, DataZone, STS, S3, and CloudWatch Logs.

#### Deployment Steps
<a name="deployment-steps-11"></a>

 **Step 1: Clone the MDAA repository**

```
git clone https://github.com/aws/modern-data-architecture-accelerator.git &&
cd modern-data-architecture-accelerator
```

 **Step 2: Configure your deployment**
+ Copy the starter kit files:

```
cp -r starter_kits/smus_research_environment my_smus_research
cd my_smus_research
```
+ Edit `mdaa.yaml`:

```
organization: <your-unique-org-name>
context:
  team1-group-sso-id: <SSO group name for team1>
  team2-group-sso-id: <SSO group name for team2>
  vpc_id: <your vpc id>
  private_subnet_id1: <private subnet id>
  private_subnet_id2: <private subnet id>
```

 **Step 3: Deploy the solution**

```
npx @aws-mdaa/cli ls
npx @aws-mdaa/cli synth
npx @aws-mdaa/cli deploy
```

 **Step 4: Verify deployment**
+ Verify the SMUS domain, project profiles, and team projects are visible in the SageMaker Unified Studio console.

## Usage Instructions
<a name="usage-instructions-9"></a>

1.  **Access the SMUS portal** — Sign in via IAM Identity Center; users are routed based on their SSO group membership.

1.  **Team projects** — Team1 and team2 each have an isolated project. Members can access shared data via Lake Formation governance.

1.  **Add data sources** — Register Glue databases as data sources in your team’s SMUS project for analytics and ML workflows.

For more detailed information, refer to the README.md and USAGE.md files in the starter\_kits/smus\_research\_environment directory of the MDAA repository.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Modern Data Architecture Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
