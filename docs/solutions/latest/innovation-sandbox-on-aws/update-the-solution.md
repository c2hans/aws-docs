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

## Update considerations for version 1.3.3
<a name="update-considerations-version-1-3-3"></a>

Version 1.3.3 replaces the solution’s API Gateway REST API and introduces a global setting that controls IAM Identity Center group assignments. Complete the following actions when updating.

### Update machine-to-machine (M2M) clients after the Compute stack
<a name="v1-3-3-m2m-api-update"></a>

The Compute stack update creates a new API Gateway REST API with a new API ID and invoke URL. Existing M2M client roles remain scoped to the previous API until their client stacks are updated. During this interval, M2M requests fail with a `403` authorization response.

After the Compute stack update completes:

1. Update every M2M client stack with the version 1.3.3 `InnovationSandbox-M2mClient.template`.

1. For the new `RestApiIdSsmParam` parameter, use the Compute stack’s `RestApiIdSsmParamName` output. The conventional value is `InnovationSandbox_<Namespace>_Compute_RestApiId`.

1. Verify that the client stack’s `ApiGatewayUrl` output contains the new API URL.

1. Update integrations that store the previous API URL. If you installed the generated `aws isb` CLI model, rerun `install-aws-isb-cli.py` with the same profile and client stack to refresh its endpoint configuration.

Future M2M client stack updates re-read the API ID from the SSM parameter. An SSM value change alone does not update an existing client stack; update the client stack whenever the Compute stack replaces the API.

### Review the group assignment setting
<a name="v1-3-3-group-assignment-mode"></a>

The new **Allow group assignments** setting defaults to **Do not allow groups** when no value has previously been saved. Existing group assignments retain access and can be removed, but new group assignments and group searches are blocked.

To continue assigning IAM Identity Center groups to leases, open the **Lease Policies** section of the **Settings** page and set **Allow group assignments** to **Allow all groups**. A pending lease request that already contains a group cannot be approved while group assignments are disabled; deny the request or re-enable group assignments before approving it.

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

### Preserve AWS Nuke configuration customizations
<a name="v1-3-0-preserve-nuke-config"></a>

When you update from a version earlier than v1.3.0, the Data stack activates a packaged AWS Nuke configuration version. This changes the active configuration even though your customized hosted version remains available in AWS AppConfig.

**Before and after the Data stack update**
If you customized AWS Nuke filters, complete the following procedures. Do not start or retry account cleanup until you confirm that the active version contains your resource exclusions.
Do not delete any AWS AppConfig hosted configuration versions as part of this procedure. To restore your customizations, start a deployment for the recorded version as described in the following procedure. Keeping the existing versions preserves your recovery options.

#### Before the Data stack update
<a name="before-the-data-stack-update"></a>

Record your current AWS Nuke configuration version so you can verify it after the update:

1. In the Hub account, navigate to the [applications page in the AWS AppConfig console](https://console.aws.amazon.com/systems-manager/appconfig/applications).

1. Choose the application whose name starts with **InnovationSandboxData-Config-Application**.

1. Choose the solution environment, and then choose the **Deployments** tab.

1. Find the latest completed deployment for the profile whose name contains **NukeConfigHostedConfiguration**.

1. Record the configuration version number.

1. Return to the application, choose **Configuration profiles**, and then choose the profile whose name contains **NukeConfigHostedConfiguration**.

1. Under **Hosted configuration versions**, open the recorded version and save a copy of its content.

#### After the Data stack update or rollback
<a name="after-the-data-stack-update-or-rollback"></a>

Verify that the recorded AWS Nuke configuration version is active:

1. Return to the applications page in the AWS AppConfig console.

1. Choose the solution application. After a successful update, its name starts with your solution namespace and ends with `-Config-Application`. If the Data stack rolls back, its name starts with `InnovationSandboxData-Config-Application`.

1. Choose the solution environment, and then choose the **Deployments** tab.

1. Find the latest completed deployment for the profile whose name contains **NukeConfigHostedConfiguration**.

1. Confirm that the deployment uses the version you recorded and that the version contains your resource exclusions.

1. If a different version is active, return to the configuration profile and choose **Start deployment**.

1. Choose the recorded version, the solution environment, and the solution’s deployment strategy. On the review page, choose **Start deployment**.

1. Wait until the deployment status is **Complete**.

1. Start or retry account cleanup only after you verify the active configuration.

**Already updated to v1.3.0 or later**
If you already updated to v1.3.0 or later, review the hosted configuration versions and identify the version that contains your intended customizations. Use that version as the recorded version in the after-update procedure before your next account cleanup.

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

If the migration fails, the Data stack update fails and AWS CloudFormation rolls back the update. Your **GlobalConfig** and **ReportingConfig** data is not modified. Review the AWS CloudFormation stack events for the Data stack in the Hub account to identify the cause, resolve it, and update the stack again. After a rollback, verify the active AWS Nuke configuration as described in [Preserve AWS Nuke configuration customizations](#v1-3-0-preserve-nuke-config).

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
   +  [M2M client template](https://solutions-reference.s3.amazonaws.com/innovation-sandbox-on-aws/latest/InnovationSandbox-M2mClient.template) (if you deployed M2M clients)

1. Navigate to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/)

1. The stacks should be updated in the following order: AccountPool, IDC, Data, then Compute

1. Choose **Update stack** from the stack actions

1. Choose **Replace current template** and specify the new template URL or upload the downloaded template

1. On the **Specify stack detail** page, under **Parameters** review the parameters and modify them as necessary

1. On the **Configure stack options** page, under **Stack failure options** section, ensure **Rollback all stack resources** is selected to automatically revert changes if the update fails

1. Complete the stack update process

1. Repeat for each stack that needs to be updated

1. If you deployed M2M clients, update each M2M client stack after the Compute stack. For version 1.3.3 requirements, see [Update M2M clients after the Compute stack](#v1-3-3-m2m-api-update).

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

1. If you deployed M2M clients, update each client stack after deploying the Compute stack. For version 1.3.3 requirements, see [Update M2M clients after the Compute stack](#v1-3-3-m2m-api-update).

1. Verify that the product’s user workflow works as expected after the update
