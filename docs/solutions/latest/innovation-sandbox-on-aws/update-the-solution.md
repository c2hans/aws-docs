---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/update-the-solution.html
---

# Update the solution
<a name="update-the-solution"></a>

**Important**
Always review the solution release notes before updating to understand any changes, new features, or configuration requirements that may affect your deployment.

## Overview
<a name="update-overview"></a>

The Innovation Sandbox on AWS solution can be updated to newer versions via two methods:
+ Via **CloudFormation templates**, update your existing stacks through the AWS CloudFormation console
+ Via **source code (Git)**, pull the latest changes from the Git repository and redeploy

**Note**
During the update process, you should turn on maintenance mode to prevent managers and users from making API requests while the update is in progress. For more information, see [Managing maintenance mode](administrator-guide.md#maintenance-mode).

## Update considerations for version 1.3.0
<a name="update-considerations-version-1-3-0"></a>

Version 1.3.0 introduces several new features and architectural changes. Review the following considerations before or immediately after updating to this version.

### Reconfiguring the SAML application
<a name="v1-3-0-saml-app-reconfiguration"></a>

Version 1.3.0 moves web application authentication to an Amazon Cognito user pool that federates to AWS IAM Identity Center as the SAML service provider.

**Before and after the Data stack update**
Before you update the **Data** stack, copy the **IAM Identity Center SAML metadata URL** from your existing SAML 2.0 application. You supply this as the required `SamlMetadataUrl` parameter during the update. After the Data stack update completes, update that same application with the new Amazon Cognito values. Until you complete this step, you cannot sign in to the web application, and neither can anyone else, including administrators. For the procedure, see [Update the SAML application configuration](update-saml-app-config.md).

### Behavioral changes that take effect immediately
<a name="v1-3-0-behavioral-changes"></a>
+ After updating, the solution enables user self-service lease termination by default. The new **Allow user lease termination** setting defaults to enabled, so leaseholders immediately see a **Terminate lease** button on their active leases (see [Terminating your lease](user-section.md#terminate-your-lease)). If you do not want this behavior (for example, in top-down environments where leases are assigned to users), disable this setting after updating. For instructions on modifying global configuration values, see [Viewing or modifying Innovation Sandbox settings](administrator-guide.md#manage-settings).
+ Lease request rate limiting takes effect immediately with default values. By default, users can create at most 10 leases (the **Max requests per window** setting) within a rolling 168-hour window (the **Rate limit window** setting) when [requesting a new account lease](user-section.md#request-new-account-lease). This count includes leases created before the update, so users who already created several leases recently might be rate limited immediately after updating. Both values are adjustable in the global configuration; see [Viewing or modifying Innovation Sandbox settings](administrator-guide.md#manage-settings).

### Event and API changes
<a name="v1-3-0-event-and-api-changes"></a>
+ If you have custom integrations that consume this solution’s events or APIs, note that the lease status values and `LeaseTerminated` event reason types gain a new value, `UserTerminated`, emitted when a user terminates their own lease. Update any integrations that enumerate lease statuses or termination reasons to handle this new value. Additionally, `AccountQuarantined` events can now result from manual Administrator action (see [Manually quarantining accounts](administrator-guide.md#manually-quarantining-accounts)), not only from automated processes such as cleanup failures or drift detection.

### Migrating existing SCP customizations
<a name="v1-3-0-scp-migration"></a>

If you have previously customized the solution’s Service Control Policies (SCPs) directly in the AWS Organizations console, you must migrate those customizations before updating. Transfer your existing changes to the new AWS CloudFormation parameters described in this section. The AccountPool stack update overwrites any direct SCP edits made in the AWS Organizations console.

Starting in v1.3.0, you can manage SCP customizations through CloudFormation using three new AccountPool stack parameters: **Additional Allowed Services**, **Additional Principal Exceptions**, and **Bedrock Inference Profile Patterns**. These values persist automatically across upgrades.

**Important**
When you update the AccountPool stack, it overwrites any SCP modifications you made directly in the AWS Organizations console. Use the CloudFormation parameters described below to preserve your customizations across upgrades.

#### Step 1: Identify your existing customizations
<a name="step-1-identify-your-existing-customizations"></a>

Before updating, compare the live SCPs in your AWS Organizations console against the solution’s previous baseline to identify any manual additions.

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/) in the management account.

1. Navigate to **Policies** > **Service control policies**.

1. Locate the Innovation Sandbox SCPs attached to your account pool OU (prefixed with your namespace).

1. For each SCP, compare the current policy content against the solution’s previous version to identify any manually added entries:
   +  **Additional service actions** you added to the NotAction list in the Allowed Services SCP
   +  **Additional IAM role ARN patterns** you added to the ArnNotLike conditions
   +  **Bedrock inference profile patterns** you added for cross-region inference

#### Step 2: Transfer customizations to CloudFormation parameters
<a name="step-2-transfer-customizations-to-cloudformation-parameters"></a>

During the stack update, provide your customizations as CloudFormation parameter values:

| Customization type | Parameter name | Example value |
| --- | --- | --- |
| Additional service actions added to NotAction list |  **Additional Allowed Services**  |  `sts:*,support:*,tag:*`  |
| Additional IAM role ARNs added to ArnNotLike conditions |  **Additional Principal Exceptions**  |  `arn:aws:iam::*:role/CustomGovernanceRole*`  |
| Bedrock inference profile ARN patterns |  **Bedrock Inference Profile Patterns**  |  `arn:aws:bedrock:*:*:inference-profile/us.*`  |

#### Step 3: Update the AccountPool stack
<a name="step-3-update-the-accountpool-stack"></a>

1. Follow the update procedures described below ([Update via CloudFormation templates](#update-via-cloudformation-templates) or [Update via source code](#update-via-source-code)).

1. On the **Parameters** page, enter your customizations in the appropriate parameter fields.

1. Complete the stack update.

#### After the update
<a name="after-the-update"></a>
+ CloudFormation now manages your customizations and persists them automatically across future upgrades.
+ You no longer need to re-apply manual SCP edits after each update.
+ To modify your customizations in the future, update the AccountPool stack and change the parameter values.

**Note**
Future solution upgrades will preserve your parameter values automatically. You only need to perform this migration once.

### Configuration migration
<a name="v1-3-0-configuration-migration"></a>

When you update a deployment from a version earlier than v1.3.0, the Data stack update automatically migrates your existing AWS AppConfig configuration. The configuration moves into the solution’s new Amazon DynamoDB configuration store. This one-time migration:
+ Runs automatically during the Data stack update. No manual action is required.
+ Preserves your existing customized values for the migrated sections.
+ Never overwrites configuration that has already been saved through the **Settings** page, so re-running an update cannot revert configuration that an Administrator has already saved.
+ Does not migrate authentication configuration. Authentication is handled by the Amazon Cognito based sign-in introduced in the same release.

On the **Settings** page, each section that was migrated shows "Last edited by system:migration" until an Administrator saves that section again.

**Important**
AWS AppConfig deletion protection prevents CloudFormation from deleting the previous **GlobalConfig** and **ReportingConfig** configuration profiles, so they remain in your account after the upgrade. Editing these orphaned profiles has no effect. After upgrading, make all configuration changes on the **Settings** page in the web UI. For more information, see [Viewing or modifying Innovation Sandbox settings](administrator-guide.md#manage-settings).

If the migration fails, the Data stack update fails and AWS CloudFormation rolls back the update. Your AWS AppConfig configuration is not modified and no configuration data is lost. Review the AWS CloudFormation stack events for the Data stack in the Hub account to identify the cause, resolve it, and update the stack again.

**Note**
When updating from a version earlier than v1.3.0, there is a brief window between the Data stack update and the Compute stack update. During this window, API requests to the solution might fail intermittently. Normal operation resumes after the Compute stack update completes.

## Update via CloudFormation templates
<a name="update-via-cloudformation-templates"></a>

If you originally deployed the solution using CloudFormation templates, follow these steps to update to a newer version:

1. Download the latest CloudFormation templates:
   +  [AccountPool template](https://solutions-reference.s3.amazonaws.com/innovation-sandbox-on-aws/latest/InnovationSandbox-AccountPool.template)
   +  [IDC template](https://solutions-reference.s3.amazonaws.com/innovation-sandbox-on-aws/latest/InnovationSandbox-IDC.template)
   +  [Data template](https://solutions-reference.s3.amazonaws.com/innovation-sandbox-on-aws/latest/InnovationSandbox-Data.template)
   +  [Compute template](https://solutions-reference.s3.amazonaws.com/innovation-sandbox-on-aws/latest/InnovationSandbox-Compute.template)

1. Navigate to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/)

1. The stacks should be updated in the following order: AccountPool, IDC, Data, then Compute

1. Choose **Update stack** from the stack actions

1. Choose **Replace current template** and specify the new template URL or upload the downloaded template

1. On the **Specify stack detail** page, under **Parameters** review the parameters and modify them as necessary

1. On the **Configure stack options** page, under **Stack failure options** section, ensure **Rollback all stack resources** is selected to automatically revert changes if the update fails

1. Complete the stack update process

1. Repeat for each stack that needs to be updated

**Note**
If you turned on maintenance mode during the update process, turn it off after all updates are complete to restore normal user access. For more information, see [Managing maintenance mode](administrator-guide.md#maintenance-mode).
If you enabled maintenance mode in AWS AppConfig before upgrading to v1.3.0, you must turn it off from the **Settings** page after the upgrade completes. The migrated value carries over into the new configuration store, but the old AWS AppConfig profile no longer has any effect.

**Note**
When you update to a version that includes account cost allocation tagging, the solution automatically activates the ISB tag keys after the Compute stack update completes. Activation can take up to 24 hours and requires no manual action. If a stack update rolls back, any in-progress activation is stopped and the temporary seed tags are removed; tags that were already activated remain active. For more information, see the [Account cost allocation tagging](account-cost-allocation-tagging.md) section.

**Note**
When you update to v1.3.0, the account cleanup event payloads (`AccountCleanupSucceeded` and `AccountCleanupFailed`) rename `cleanupExecutionContext.stateMachineExecutionArn` to `cleanupExecutionContext.executionArn` and `cleanupExecutionContext.stateMachineExecutionStartTime` to `cleanupExecutionContext.executionStartTime`. If you have custom EventBridge rules or Lambda consumers that process these events, update them to use the new field names.
 **Before (v1.2.x):**

```
"cleanupExecutionContext": {
  "stateMachineExecutionArn": "arn:aws:states:...",
  "stateMachineExecutionStartTime": "2024-01-15T14:30:25Z"
}
```
 **After (v1.3.0):**

```
"cleanupExecutionContext": {
  "executionArn": "arn:aws:lambda:...",
  "executionStartTime": "2024-01-15T14:30:25Z"
}
```

## Update via source code (Git)
<a name="update-via-source-code"></a>

If you originally deployed the solution from the Git repository source code, follow these steps to update to a newer version:

**Note**
Before updating from source code, ensure your development environment is properly configured by referring to the [README](https://github.com/aws-solutions/innovation-sandbox-on-aws) for setup instructions.

1. Navigate to your local copy of the [Innovation Sandbox on AWS repository](https://github.com/aws-solutions/innovation-sandbox-on-aws)

1. Pull the latest changes from the remote repository:

   ```
   git pull origin main
   ```

1. Review the updated code and configuration files for any changes that may affect your deployment

1. If you made custom modifications, resolve any merge conflicts that may arise

1. Redeploy the solution using npm commands:
   + To deploy all stacks:

     ```
     npm run deploy:all
     ```
   + Alternatively, stacks can be deployed individually in the following order:

     ```
     npm run deploy:account-pool
     npm run deploy:idc
     npm run deploy:data
     npm run deploy:compute
     ```

1. Verify that the product’s user workflow works as expected after the update

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
