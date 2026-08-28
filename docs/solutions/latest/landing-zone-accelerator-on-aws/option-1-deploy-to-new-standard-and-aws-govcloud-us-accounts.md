---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/option-1-deploy-to-new-standard-and-aws-govcloud-us-accounts.html
---

# Option 1: Deploy to new standard and AWS GovCloud (US) accounts
<a name="option-1-deploy-to-new-standard-and-aws-govcloud-us-accounts"></a>

Deploying this solution with the default parameters builds the following environment in the AWS GovCloud (US) Region(s).

 **Architecture diagram depicting AWS GovCloud (US) deployment.**

![image10](http://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/images/image10.png)

The AWS CloudFormation template includes a set of configuration files that have been specifically customized for AWS GovCloud (US) Regions. By following these instructions, you can deploy an environment that includes:

1. Use of AWS Control Tower to manage and govern your [AWS standard accounts](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/getting-started-standard-account-linking.html).
**Note**
In this implementation guide, the terms "AWS standard account" and "AWS standard Region" mean "AWS account that isn’t in an AWS GovCloud (US) Region" and "AWS Region that isn’t an AWS GovCloud (US) Region."

1. A deployment of the solution in your **AWS standard accounts** (refer to the left side of the previous figure), allowing you to activate additional security features and guardrails into your AWS standard accounts and providing you the ability to generate AWS GovCloud (US) accounts.

1. A deployment of the solution in your **AWS GovCloud (US) accounts** (refer to the right side of the previous figure) with the AWS best practices configuration of security services and an AWS best practices-recommended network topology. This configuration is architected to follow the US Department of Defense (DoD) Cloud Computing Security Requirements Guide (CC SRG) for hosting Impact Level (IL)4 and IL5 workloads in the cloud. Using this configuration, you can quickly deploy an architecture baseline that accommodates US federal and DoD requirements to rapidly achieve Authority to Operate (ATO). In addition, this solution is architected to support and accelerate DoD Cybersecurity Maturity Model Certification (CMMC) readiness.

**Important**
Don’t use the AWS standard account paired to AWS GovCloud (US) accounts to host any workloads.

## Step 1. Deploy the solution in your AWS standard Management account and create AWS GovCloud (US) accounts
<a name="step-1.-deploy-the-solution-in-your-aws-standard-management-account-and-create-aws-govcloud-us-accounts"></a>

1. Create an [AWS standard account](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/getting-started-standard-account-linking.html) that is [allowed to access AWS GovCloud (US) Region(s)](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateGovCloudAccount.html) and is the AWS Organizations Management account.

1.  [Set up and verify AWS Organizations through email.](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_create.html) (This step is optional but saves time in AWS Control Tower setup [Step 1.3].)

1.  [Set up Landing Zone Accelerator on AWS](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/automated-deployment.html) in your AWS standard account.

1. After successfully setting up Landing Zone Accelerator on AWS in your AWS standard account, update the `organization-config.yaml` file in the `aws-accelerator-config` CodeCommit repository to make the new OU visible to Landing Zone Accelerator on AWS. [Run](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-rerun-manually.html) the Landing Zone Accelerator on AWS pipeline with this change.

```
enable: true
organizationalUnits:
  - name: Security
  - name: Infrastructure
  - name: GovCloud
serviceControlPolicies: []
taggingPolicies: []
backupPolicies: []
```

1. After the Landing Zone Accelerator on AWS pipeline completes, create new AWS GovCloud (US) accounts using the ` [enableGovCloud](https://awslabs.github.io/landing-zone-accelerator-on-aws/latest/typedocs/latest/classes/_aws_accelerator_config.GovCloudAccountConfig.html#enableGovCloud) ` field in the ` [workloadAccounts](https://awslabs.github.io/landing-zone-accelerator-on-aws/latest/typedocs/latest/classes/_aws_accelerator_config.AccountsConfig.html#workloadAccounts) ` definition. These are AWS GovCloud accounts paired to your AWS standard account. You must specify these under `workloadAccounts:`. The following is a sample account configuration.

```
# commercial accounts-config.yaml
mandatoryAccounts:
  - name: Management
    description: >-
      The management (primary) account. Do not change the name field for this mandatory account.
    email: < landing-zone-management-email@example.com> <----- UPDATE EMAIL ADDRESS
    organizationalUnit: Root
  - name: LogArchive
    description: >-
      The log archive account. Do not change the name field for this mandatory account.
    email: <commercial-log-archive-email@example.com> <----- UPDATE EMAIL ADDRESS
    organizationalUnit: Security
  - name: Audit
    description: >-
      The security audit account (also referred to as the audit account). Do not change the name field for this mandatory account.
    email: <commercial-audit-email@example.com> <----- UPDATE EMAIL ADDRESS
    organizationalUnit: Security
workloadAccounts:
  - name: LogArchiveGC # referred to as LogArchive in the GovCloud account-config.yaml
    description: The log archive account for GovCloud.
    email: <govCloud-log-archive-email@example.com> <----- UPDATE EMAIL ADDRESS
    # this OU has all GovCloud accounts.
    # OU was created from Control Tower
    # in organization-config.yaml this OU was added.
    organizationalUnit: GovCloud
    # enableGovCloud is a one-time non-reversible option
    # which only works with creation of new accounts
    enableGovCloud: true
  - name: AuditGC # referred to as LogArchive in the GovCloud account-config.yaml
    description: The security audit account (also referred to as the audit account) for GovCloud.
    email: <govCloud-audit-email@example.com> <----- UPDATE EMAIL ADDRESS
    organizationalUnit: GovCloud
    enableGovCloud: true
```

1. The solution creates paired accounts which are joined in AWS Organizations in the AWS standard Region. These accounts will have a cross-account assume role in the AWS GovCloud (US) Region(s) but will not be a part of the AWS GovCloud (US) Organization.

1. Add new AWS GovCloud (US) accounts to the `accounts-config.yaml` file in the AWS standard Region and run the solution pipeline.
**Note**
We highly recommend that you vend all AWS GovCloud (US) accounts from the Landing Zone Accelerator on AWS solution.

1. After the pipeline completes, navigate to AWS Organizations console page to retrieve the commercial account IDs of the newly created accounts.

1. Navigate to the AWS GovCloud (US) account mapping table in Amazon DynamoDB. Find the table name from AWS Systems Manager parameter (SSM parameter) `/accelerator/prepare-stack/govCloudAccountMappingTableName`. In that table, look up rows with commercial account IDs from the previous step. The AWS GovCloud (US) account IDs are shown under the **govCloudAccountId** column. You need these AWS GovCloud (US) account IDs to onboard AWS GovCloud (US) accounts.

## Step 2. Deploy the solution in your AWS GovCloud (US) Management account
<a name="step-2.-deploy-the-solution-in-your-aws-govcloud-us-management-account"></a>

1. Log in to the AWS GovCloud (US) Management account.

1.  [Set up and verify AWS Organizations through email.](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_create.html)

1. Invite AWS GovCloud (US) LogArchive and Audit account to your [organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html).

1. Accept the invite by using [switch to the role for the member account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_access.html#orgs_manage_accounts_access-cross-account-role).

**Note**
The role is defined as `managementAccountAccessRole` in the global-config.yaml configuration file for the AWS standard Management account.

1.  [Deploy the solution](deploy-the-solution.md) in the AWS GovCloud (US) Management account. The input into the installer stack for LogArchive and Audit accounts will be the AWS GovCloud (US) accounts vended from the linked AWS standard account. (This implementation guide uses <govCloud-audit- [email@example.com](mailto:email@example.com)> ( [<[email@example.com](mailto:email@example.com)>](mailto:email@example.com)) and <[govCloud-log-archive-email@example.com](mailto:govCloud-log-archive-email@example.com)> ( [<[govCloud-log-archive-email@example.com](mailto:govCloud-log-archive-email@example.com)>](mailto:govCloud-log-archive-email@example.com)) as example accounts.)

## Step 3. Update the configuration file in your AWS standard account to create new AWS GovCloud (US) accounts
<a name="step-3.-update-the-configuration-file-in-your-aws-standard-account-to-create-new-aws-govcloud-us-accounts"></a>

1. Using the AWS standard account, update the `accounts-config.yaml` file to have two new accounts with the `enableGovCloud` option, as shown in the following sample.

   ```
   # commercial accounts-config.yaml
   mandatoryAccounts:
     - name: Management
       description: >-
         The management (primary) account. Do not change the name field for this mandatory account.
       email: <landing-zone-management-email@example.com> <----- UPDATE EMAIL ADDRESS
       organizationalUnit: Root
     - name: LogArchive
       description: >-
         The log archive account. Do not change the name field for this mandatory account.
       email: <commercial-log-archive-email@example.com> <----- UPDATE EMAIL ADDRESS
       organizationalUnit: Security
     - name: Audit
       description: >-
         The security audit account (also referred to as the audit account). Do not change the name field for this mandatory account.
       email: <commercial-audit-email@example.com> <----- UPDATE EMAIL ADDRESS
       organizationalUnit: Security
   workloadAccounts:
     - name: LogArchiveGC # referred to as LogArchive in the GovCloud account-config.yaml
       description: The log archive account for GovCloud.
       email: <govCloud-log-archive-email@example.com> <----- UPDATE EMAIL ADDRESS
       # this OU has all GovCloud accounts.
       # OU was created from Control Tower
       # in organization-config.yaml this OU was added.
       organizationalUnit: GovCloud
       # enableGovCloud is a one-time non-reversible option
       # which only works with creation of new accounts
       enableGovCloud: true
     - name: AuditGC # referred to as Audit in the GovCloud account-config.yaml
       description: The security audit account (also referred to as the audit account) for GovCloud.
       email: <govCloud-audit-email@example.com> <----- UPDATE EMAIL ADDRESS
       organizationalUnit: GovCloud
       enableGovCloud: true
     - name: SharedServicesGC # referred to as SharedServices in the GovCloud account-config.yaml
       description: Shared services account for GovCloud.
       email: <govCloud-shared-services-email@example.com> <----- UPDATE EMAIL ADDRESS
       organizationalUnit: GovCloud
       enableGovCloud: true
     - name: NetworkGC # referred to as Network in the GovCloud account-config.yaml
       description: Network account for GovCloud.
       email: <govCloud-network-email@example.com> <----- UPDATE EMAIL ADDRESS
       organizationalUnit: GovCloud
       enableGovCloud: true
   ```

1. After the commit, confirm that the pipeline runs successfully.

1. From the AWS GovCloud (US) mapping table, retrieve the AWS GovCloud (US) account ID for the **SharedServicesGC** and **NetworkGC** accounts.

## Step 4. Configure solution in AWS GovCloud (US) Region(s) to manage new accounts
<a name="step-4.-configure-solution-in-aws-govcloud-us-regions-to-manage-new-accounts"></a>

1. Log in to the AWS GovCloud (US) Management account.

1. Add the **SharedServices** and **Network** accounts as shown in the following sample.

   ```
   # govCloud accounts-config.yaml
   mandatoryAccounts:
     - name: Management
       description: >-
         The management (primary) account. Do not change the name field for this mandatory account.
       email: <landing-zone-management-email@example.com> <----- UPDATE EMAIL ADDRESS
       organizationalUnit: Root
     - name: LogArchive
       description: >-
         The log archive account. Do not change the name field for this mandatory account.
       email: <govCloud-log-archive-email@example.com> <----- UPDATE EMAIL ADDRESS
       organizationalUnit: Security
     - name: Audit
       description: >-
         The security audit account (also referred to as the audit account). Do not change the name field for this mandatory account.
       email: <govCloud-audit-email@example.com> <----- UPDATE EMAIL ADDRESS
       organizationalUnit: Security
   workloadAccounts:
     - name: SharedServices
       description: Shared services account for GovCloud.
       email: <govCloud-shared-services-email@example.com> <----- UPDATE EMAIL ADDRESS
       organizationalUnit: Infrastructure
     - name: Network
       description: Network account for GovCloud.
       email: <govCloud-network-email@example.com> <----- UPDATE EMAIL ADDRESS
       organizationalUnit: Infrastructure

   accountIds:
     - email: <landing-zone-management-email@example.com> <----- UPDATE EMAIL ADDRESS
       accountId: '000000000000'  <----- UPDATE GOVCLOUD ACCOUNT ID from Commercial GovCloud mapping table
     - email: <govCloud-log-archive-email@example.com> <----- UPDATE EMAIL ADDRESS
       accountId: '111111111111'  <----- UPDATE GOVCLOUD ACCOUNT ID from Commercial GovCloud mapping table
     - email: <govCloud-audit-email@example.com> <----- UPDATE EMAIL ADDRESS
       accountId: '222222222222'  <----- UPDATE GOVCLOUD ACCOUNT ID from Commercial GovCloud mapping table
     - email: <govCloud-shared-services-email@example.com> <----- UPDATE EMAIL ADDRESS
       accountId: '333333333333'
     - email: <govCloud-network-email@example.com> <----- UPDATE EMAIL ADDRESS
       accountId: '444444444444'
   ```

1. After the commit, confirm that the pipeline runs successfully.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
