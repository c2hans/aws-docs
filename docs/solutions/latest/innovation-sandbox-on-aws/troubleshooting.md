---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/troubleshooting.html
---

# Troubleshooting

This section provides information about known issues and instructions to mitigate known errors. If these instructions do not resolve your issue, see the [Contact AWS Support](contact-aws-support.md) section to open an AWS Support case for this solution.

## Application sign in error
<a name="application-sign-in-error"></a>

If you receive an error titled **"Application sign in error"** when accessing the Innovation Sandbox on AWS Web UI, the IAM Identity Center application or its Amazon Cognito integration is likely misconfigured. Possible root causes include:
+ Incorrect **Attribute mappings** in the IAM Identity Center SAML 2.0 application
+ Incorrect **Application ACS URL** in the IAM Identity Center SAML 2.0 application (must match the Data stack `CognitoAcsUrl` output)
+ Incorrect `SamlMetadataUrl` value provided during Data stack deployment
+ The user is not a member of any solution IAM Identity Center group (the Cognito pre-token-generation trigger cannot resolve a role)
+ Missing primary email address in IAM Identity Center for the user attempting to sign in

Refer to the [Post deployment configuration tasks](post-deployment-configuration-tasks.md) section and verify that the SAML application configuration matches the Amazon Cognito values from the Data stack outputs.

## Invalid configuration settings
<a name="invalid-configuration-settings"></a>

Starting with v1.3.0, Innovation Sandbox stores its global configuration in an Amazon DynamoDB table. Every change is validated when an Admin saves it on the **Settings** page of the web UI. Invalid configuration should not occur during normal use. It can occur only if an item in the solution’s **Config** DynamoDB table was edited directly, bypassing this validation.
+ A request for all configuration sections skips a malformed section and falls back to its default values. A request for that individual section fails with an unexpected server error. The individual-section failure is logged to the **Compute-ISBLogGroup log group**; the fallback for the all-sections request is not logged.
+ Saving the affected section again on the **Settings** page does not resolve this error on its own. The malformed item still exists in the DynamoDB table, so the **Settings** page’s save attempt fails with a **Conflict** error instead of succeeding.

To resolve this issue, correct or delete the malformed item for the affected section directly in the solution’s **Config** DynamoDB table. Alternatively, restore the item using point-in-time recovery. Afterward, sign in to the web UI as an Admin, open the **Settings** page, and review the affected section to confirm the values. For more information, see the [Viewing or modifying Innovation Sandbox settings](administrator-guide.md#manage-settings) section.

## Authentication failed, SAML assertion audience mismatch
<a name="authentication-failed-saml-assertion-audience-mismatch"></a>

If you receive an error with the message **"SAML assertion audience mismatch"** when accessing the Innovation Sandbox on AWS Web UI, the **Application SAML audience** value in your IAM Identity Center SAML application does not match the Cognito user pool’s audience. The SAML application audience must equal the Data stack `CognitoAudience` output. Refer back to the [Update the SAML application configuration](update-saml-app-config.md) section to correct it.

## API requests return 403 Forbidden
<a name="api-requests-return-403-forbidden"></a>

If web UI or programmatic API requests fail with **403 Forbidden** from API Gateway, API Gateway rejected the SigV4 signature. Common causes:
+  **Clock skew** — the caller’s system clock is more than five minutes out of sync with AWS. SigV4 rejects requests outside this window. Ensure the client host (for example, an M2M automation host) is synchronized using Network Time Protocol (NTP).
+  **Expired or revoked credentials** — the temporary IAM credentials used to sign the request have expired or the underlying role’s access has been revoked.
+  **M2M client misconfiguration** — an incorrect ExternalId (the `M2MExternalId` stack output) or a trust policy that does not permit the calling principal to assume the client role. Verify the values from the M2M client stack outputs.

## Configuration changes in AWS AppConfig have no effect
<a name="appconfig-changes-no-effect"></a>

If you upgraded to v1.3.0 or later from an earlier version, you might still see configuration profiles in the AWS AppConfig console. Their names contain **GlobalConfigHostedConfiguration** and **ReportingConfigHostedConfiguration**. These profiles are left-over artifacts of the configuration migration. They hold a copy of your pre-upgrade settings, but the solution no longer reads them, so changes you make to them have no effect.

Starting with v1.3.0, Innovation Sandbox stores its global and cost reporting configuration in an Amazon DynamoDB table and no longer reads it from AWS AppConfig. The upgrade removes these profiles from the solution’s AWS CloudFormation template, but AWS AppConfig prevents them from being deleted, so they remain in your account in an orphaned state. You can keep them as a record of your pre-upgrade settings, or delete them manually from the AWS AppConfig console at any time. Deleting them does not affect the solution. To change solution settings, sign in to the web UI as an Admin and use the **Settings** page. For more information, see the [Viewing or modifying Innovation Sandbox settings](administrator-guide.md#manage-settings) section.

**Note**
Only the account cleanup configuration—the AWS Nuke configuration and the cleanup validator exclusion configuration—is still managed in AWS AppConfig.

## Configuration migration fails during solution upgrade
<a name="config-migration-failure"></a>

When you upgrade to v1.3.0, a one-time custom resource in the Data stack migrates your existing global and cost reporting configuration from AWS AppConfig. This configuration moves into the new **Config** DynamoDB table. If this migration fails, the Data stack update fails and AWS CloudFormation rolls back the deployment. Your existing AWS AppConfig configuration is not deleted or modified by a failed update, so no configuration data is lost. You can retry the upgrade after resolving the cause.

To diagnose the failure:

1. In the Hub account, open the AWS CloudFormation console and review the stack events for the Data stack. Identify the failing resource (the configuration migrator custom resource) and its reported error reason.

1. Review the migrator’s logs in the Data stack’s custom resources CloudWatch log group (**Data-ISBLogGroupCustomResources**).

Common causes include invalid or out-of-range values in the existing AWS AppConfig configuration, or malformed configuration content. Correct the issue, then retry the stack update.

**Note**
The migration runs only once. If configuration has already been migrated to the DynamoDB table, retrying the update does not run the migration again. It never overwrites settings that were already saved on the **Settings** page.

## Compute stack deployment or update fails
<a name="observability-deployment-failures"></a>

Open the AWS CloudFormation console in the Hub account and find the failed resource and its error in the stack events. Common causes include the following:
+  **The Hub account already has an observability sink**: `Custom::ObservabilitySinks` fails with an error that contains `already holds a sink that is not InnovationSandbox-Metrics`. Use a Hub account that doesn’t have a sink in any managed Region, or remove that Region from **ISB Managed Regions**. For more information, see [Prerequisites](prerequisites.md).
+  **A managed Region isn’t enabled in the Hub account**: `Custom::ObservabilitySinks` fails if a Region in **ISB Managed Regions** is an opt-in Region that isn’t enabled in the Hub account. Enable the Region in the Hub account, and then deploy the stack again, or update it again with a new **Force configuration update (optional)** value. For more information, see [Managed opt-in Regions](plan-your-deployment.md#managed-opt-in-regions).
+  **The stacks were updated out of order**: When you update from an earlier version, the Compute stack update fails if the AccountPool or Data stack isn’t on version 1.4.0 yet. Update those stacks first, and then update the Compute stack again. For instructions, see [Update via CloudFormation templates](update-the-solution.md#update-via-cloudformation-templates).

## Errors when saving settings
<a name="settings-save-errors"></a>

Admins can modify solution settings on the **Settings** page of the web UI. Each group is validated when you choose **Save changes**. The following errors need additional action beyond correcting the highlighted field:
+  **"The email provided is not a verified SES identity in this account. Verify the address or its domain in Amazon SES before saving."** This error appears on the **Email from address (SES)** field in the **Notifications** group when the solution sends from the Hub account. The sender address, or its parent domain, must be a verified identity in Amazon SES in the Hub account. Verify the address or domain in the Amazon SES console, then choose **Save changes** again.
+  **"The email provided is not covered by the delegated SES identity for this deployment. …​"** This error appears when the Compute stack’s **Delegated SES Identity ARN** parameter is set and the sender address doesn’t match that identity. For an email address identity, use the identity’s address (a `+tag` form of it is also accepted). For a domain identity, use an address in that domain or one of its subdomains. To use a different identity, update the Compute stack. For more information, see [Send email through an SES identity in another account](delegated-ses-sending.md).
+  **"Unable to verify this email against SES. Please try again shortly."** The solution couldn’t check the address with Amazon SES. Wait and choose **Save changes** again. If the error persists, check the logs of the Lambda function that serves the configurations API for an SES access error.
+  **Settings changed by another administrator**: Another Admin saved the same group after you loaded the page. Choose **Reload latest values** to load the latest values, reapply your changes, and choose **Save changes** again. Reloading discards your unsaved edits for that group.

For more information, see the [Viewing or modifying Innovation Sandbox settings](administrator-guide.md#manage-settings) section.

## Notifications are not delivered
<a name="notifications-not-delivered"></a>

If users, managers, or administrators don’t receive notifications, check the following:
+  **Notification channels**: In the notification settings on the **Settings** page, confirm that **Email notifications (SES)**, **SNS integration topic**, or both are on. Email is sent only when **Email from address (SES)** is also set. If no channel is active, the **Settings** page shows an **All notifications are off** warning, and the notification function logs a `Notification No Channel Enabled` warning for each notification it skips.
+  **SES send failures**: The **SES send failure** alarm enters `ALARM` when a notification email can’t be sent. In Amazon CloudWatch Logs, find entries with `notificationMetricType` set to `NotificationDeliveryFailed` and `channel` set to `SES`, and check the error names. When you use a delegated SES identity, an access denied error usually means that the identity’s sending authorization policy doesn’t allow the Hub account, or that the identity isn’t in the Hub account’s Region. For more information, see [Send email through an SES identity in another account](delegated-ses-sending.md). Confirm that the Hub account has SES production access, and, when you send from the Hub account, that the identity is still verified.
+  **SNS publish failures**: The **SNS publish failure** alarm enters `ALARM` when a notification can’t be published to the integration topic. Find log entries with `channel` set to `SNS`. Common causes are changes to the topic’s access policy or to the Compute stack’s KMS key policy. A message that fails to publish is not delivered to subscribers.
+  **Subscriber delivery**: If the topic publishes but your tool doesn’t receive messages, check the subscription’s status and filter policy, and the SNS delivery metrics for the topic. The solution doesn’t manage subscriptions or delivery to subscribers.

## Investigating accounts in Quarantine state
<a name="investigating-accounts"></a>

**Note**
If the account cleanup mechanism fails to automatically delete resources at the end of an active lease, you might have accounts in a `Quarantine` state. We highly recommend investigating quarantined accounts as quickly as possible, as these accounts can incur costs for resources running inside these accounts.

When the Innovation Sandbox solution cannot clean up resources in a sandbox account, it moves the account to a `Quarantine` state and sends an email to the solution administrators to take action on the account’s quarantine status. Accounts also move to a `Quarantine` state when the solution detects drift, or when an Administrator manually quarantines the account (see [Manually quarantining accounts](administrator-guide.md#manually-quarantining-accounts)).

To resolve the quarantined status:

1. Log in to the web UI as an Admin, and from the left, under **Administration**, choose **Accounts**.

1. Verify the accounts in `Quarantine` status, and decide whether to clean up the account and return to the account pool, or to eject the account from the solution.
   + To clean up the account and return it to the account pool, choose the account, and under **Actions**, choose **Retry cleanup**.
   + To eject the account, choose the account, and under **Actions**, choose **Eject account**. This moves the account to the **Exit** OU, from which you can manually move it to your desired OU. For more information, refer to the [Uninstall the solution](uninstall-the-solution.md) section.

If the account is in quarantine because the **retry cleanup failed**, refer to the [Resolving cleanup failures](#resolving-cleanup-failures) section.

### Determining why an account was quarantined
<a name="determining-why-an-account-was-quarantined"></a>

The web UI does not display the reason an account was quarantined. To determine the cause, search Amazon CloudWatch Logs in the Hub account for log entries with `logDetailType` set to `AccountQuarantined` and the relevant account ID. For guidance on querying logs, see [Logs and tracing](monitoring-logs-and-tracing.md). The `reasonForQuarantine` field in the log entry indicates the cause:
+  **MANUAL** — An Administrator quarantined the account from the Accounts page or API.
+  **DRIFT** — Automated drift detection moved the account into quarantine.
+  **CLEANUP\_FAILED** — The account cleanup process exhausted its retries.

## Resolving cleanup failures
<a name="resolving-cleanup-failures"></a>

If the cleanup process fails to completely clean an account at the end of a lease, Innovation Sandbox will move the account into a Quarantine state, and email the Administrators notifying them of the issue.

To resolve an account that has failed cleanup:

1. Log in to the web UI as an Admin, and from the left, under **Administration**, choose **Accounts**.

1. Choose the account ID of the account that failed the cleanup process to open the account details page.

1. Under **Recent cleanups**, choose the failed cleanup report. The **Steps** panel identifies which step failed and shows its error details.

1. If an AWS Nuke phase failed, choose **View build logs** on that step to read the AWS Nuke output in the AWS CodeBuild console. To review only the resource deletion failures, run the `AccountCleanupLogs` saved query against that build. For the full procedure, including how to filter the AWS Nuke configuration for protected resources, see [Resolving Account Cleanup Failures](administrator-guide.md#resolving-account-cleanup-failures).

1. To manually handle any deletion failures in the affected account, navigate back to the **Accounts** page, and log in to the account using the **Login** option.

1. After you have manually handled all errors, to restart the cleanup process in the web UI, choose the account and under **Actions**, choose **Retry cleanup**.

## Manual account quarantine issues
<a name="manual-quarantine-issues"></a>

This section provides troubleshooting guidance for issues related to manually quarantining an account. For instructions on how to manually quarantine an account, refer to the [Manually quarantining accounts](administrator-guide.md#manually-quarantining-accounts) section.

### Quarantine account option is disabled
<a name="quarantine-account-option-is-disabled"></a>

The **Quarantine account** action, under **Actions** on the **Accounts** page, is only enabled when all of the selected accounts are in `Available`, `Active`, or `Frozen` status. If the option is disabled, deselect any selected accounts that are not in one of these statuses, and try again.

### Quarantine request fails
<a name="quarantine-request-fails"></a>

If a request to quarantine an account fails:
+  **The account is already in `Quarantine` status** — no action is needed.
+  **The account is currently in `CleanUp` status** — an account cannot be quarantined while a cleanup operation is in progress. Wait for the cleanup to complete, and then retry the quarantine request.
+  **The account has drifted** — someone moved the account to a different OU directly in AWS Organizations, so its actual OU no longer matches its status in the web UI, and the request fails with an error that retrying does not resolve. Move the account back to the OU that matches its status, or wait for automated drift detection to quarantine the account.
+  **The failure persists** — check the **Compute-ISBLogGroup log group** for error details, and resubmit the request. It is safe to retry a failed quarantine request.

### Recovering a manually quarantined account
<a name="recovering-a-manually-quarantined-account"></a>

A manual quarantine action cannot be undone directly. To recover the account:
+ Choose the account, and under **Actions**, choose **Retry cleanup**. This wipes the resources in the account and returns the account to `Available` status in the account pool.
+ Alternatively, eject the account and re-onboard it. Choose the account, and under **Actions**, choose **Eject account**, which moves the account to the **Exit** OU. From AWS Organizations, move the account to the **Entry** OU, and then follow the steps in [Adding new accounts to the account pool](administrator-guide.md#new-accounts) to re-register the account with the solution.

**Note**
If the account has a lease in `Provisioning` status (a blueprint deployment in progress) when it is quarantined, the lease is terminated, but the in-flight blueprint deployment is not cancelled. The deployment eventually fails or times out on its own.

## Viewing a specific Lease history
<a name="viewing-lease-history"></a>

1. Log in to the web UI as an Admin, and from the left, under **Administration**, choose **Leases**.

1. Choose the lease name to view lease details.

1. Copy the LeaseID from the Lease Summary page. You will need this to view lease history in the AWS Console.

1. Log in to the AWS Console, and navigate to the **CloudWatch > Logs > Log Analytics** page.

1. Choose **Saved queries**, expand the **ISB-<namespace>** folder, and choose the `LogQuery` saved query.

1. In the query window, choose the time frame to view logs for and paste the LeaseID into the indicated section.

1. Choose **Run query** to view logs related to the LeaseID provided for the selected time frame. The log information is displayed under the *Logs* tab.

**Note**
Terminated leases distinguish who ended them. When a leaseholder terminates their own lease, the solution records the status as `Terminated by User` (`UserTerminated` in log entries and events). This is distinct from `Lease Manually Terminated`, which indicates an Admin or Manager terminated the lease.

## Viewing a specific User history
<a name="viewing-user-history"></a>

1. Log in to the web UI as an Admin, and from the left, under **Administration**, choose **Accounts**.

1. From the Accounts page, confirm the user email address you want to view history for. You will need this to view user/account history in the AWS Console.

1. Log in to the AWS Console, and navigate to the **CloudWatch > Logs > Log Analytics** page.

1. Choose **Saved queries**, expand the **ISB-<namespace>** folder, and choose the `LogQuery` saved query.

1. In the query window, choose the time frame to view logs for and paste the email address into the indicated section.

1. Choose **Run query** to view logs related to the email address provided for the selected time frame. The log information is displayed under the *Logs* tab.

### 403 Permissions error
<a name="403-permissions-error"></a>

If you find an issue within the Identity Center:
+ Your session might have timed out. Refresh your browser to resolve this.
+ Maintenance mode is enabled and you are signed in using a Manager or User role. New deployments of Innovation Sandbox on AWS start with maintenance mode turned **ON**. Managers and Users cannot access the solution until an Admin turns it off. Contact your Admin: an Admin can turn off maintenance mode on the **Settings** page, in the **General** group, in the **Maintenance mode** section. For more information, see the [Managing maintenance mode](administrator-guide.md#maintenance-mode) section.
+ The user attempted to terminate a lease they do not own, terminate a lease that is not in `Active` status (for example, `Frozen` or `Provisioning`), or the administrator has disabled self-service lease termination. For more information, refer to the [User lease termination issues](#user-lease-termination-issues) section.
+ A non-Admin user attempted an account management action, such as quarantining an account. Account management actions are available only to Administrators.

### Unexpected server errors
<a name="unexpected-server-errors"></a>

If you find unexpected server errors while using the web UI, you can trace the issue by using AWS X-Ray.

1. Copy the X-Ray trace ID from the error:
   + When an unexpected error occurs in the web UI, a trace ID will be provided.
   + Or, for any error logs found in Amazon CloudWatch, expand the log to find the X-Ray trace ID for the operation.

1. In the AWS Console, navigate to the AWS X-Ray page and paste the trace ID into the search box.

For more information, refer to the [AWS X-Ray Traces](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html#xray-concepts-traces), and [AWS X-Ray Common Errors](https://docs.aws.amazon.com/xray/latest/api/CommonErrors.html) pages.

## Lease assignment issues
<a name="lease-assignment-issues"></a>

This section provides troubleshooting guidance for common issues related to the lease assignment feature.

### User not found error
<a name="user-not-found-error"></a>

If you receive an error stating that the target user cannot be found when attempting to assign a lease:

 **Root causes:**
+ The user does not exist in AWS IAM Identity Center
+ The email address was entered incorrectly
+ The user exists but their email attribute is not properly configured

 **Resolution steps:**

1. Verify the user exists in AWS IAM Identity Center:

   1. Navigate to the AWS IAM Identity Center console in your hub account

   1. Go to **Users** and search for the target user

   1. Confirm the user’s email address matches exactly what you entered

1. If the user doesn’t exist, create the user in IAM Identity Center before attempting lease assignment

1. If the user exists but the email doesn’t match, update either the user’s email in IAM Identity Center or use the correct email address in the lease assignment

## Permission set issues
<a name="permission-set-issues"></a>

### Permission set does not appear in the catalog
<a name="permission-set-not-in-catalog"></a>

1. In IAM Identity Center, confirm that the permission set belongs to the instance configured for this deployment.

1. Check for the exact tag key `ISB:<namespace>:ManagedPermissionSet` and value `true`. Use your deployment’s namespace and match the capitalization. Tag the permission set itself, not its generated IAM role in a sandbox account.

1. Refresh the **Permission Sets** table after synchronization. Event-driven updates normally arrive before the scheduled reconciliation, which runs every hour. Missed events or tagging-index delays can postpone discovery. Refreshing reloads the cached catalog; it does not start synchronization.

1. If the permission set is still missing after reconciliation, investigate [cache synchronization failures](#cache-sync-failure).

The solution excludes its Admin and Manager permission sets from the catalog. The built-in user permission set does not require a registration tag.

### Investigating cache synchronization failures
<a name="cache-sync-failure"></a>

The `CacheSyncFailure` alarm monitors the Principal Cache Sync function’s Lambda `Errors` metric. It enters `ALARM` when errors occur in both of two consecutive one-hour periods. The alarm does not treat missing data as a failure. It covers scheduled and event-driven invocations.

1. In the Hub account’s CloudWatch console, locate the alarm for the Principal Cache Sync function. Its description starts with "Principal or permission-set cache synchronization failed".

1. Open the function’s logs for the failing period. For a scheduled invocation, look for `Starting principal cache sync` and `Starting permission set cache sync` to identify the phase that failed. A principal synchronization failure prevents the permission-set phase from running.

1. For access-denied errors, verify that the AWS IAM Identity Center (IDC) and Compute stack updates completed and that the cross-account roles retain their deployed permissions.

1. For event-driven update failures or missing events, check the EventBridge forwarding rule in the IDC account and the receiving rule in the Hub account. Confirm that the forwarding role can call `events:PutEvents` on the Hub event bus.

1. Resolve the reported error, confirm a successful synchronization in the logs, and refresh the catalog. A scheduled permission-set discovery failure leaves the previous permission-set cache in place, so a populated catalog alone does not prove that synchronization is healthy.

### An assignment uses an unavailable permission set
<a name="unavailable-permission-set"></a>

A custom permission set is unavailable when it is absent from the catalog. This can happen after you remove its registration tag or delete it. New assignments and permission-set replacements require an available permission set. Removing registration does not revoke existing access.

You can approve or unfreeze a lease with an unavailable saved permission set, but the affected grants fail. On an active lease, open **Assignments**, replace the unavailable permission set with an available allowed one or remove the affected assignment, and choose **Save changes**. Administrators and managers can first [update the lease’s access settings](manager-guide.md#lease-access-settings) if a replacement must be allowed.

If you restore registration, wait for synchronization and retry the failed assignment. Restoring the tag does not automatically retry a denied grant. For other processing failures, see [Access not granted after adding a user or group](#shared-access-not-granted).

### AWS access portal shows fewer permission sets than the lease allows
<a name="permission-sets-in-portal"></a>

The allowed list defines your choices for assignments; it does not grant every listed permission set. Check the user’s assigned permission set on the lease’s **Assignments** tab. Separate group memberships or administrative assignments can also provide roles in the portal.

## Lease sharing issues
<a name="lease-sharing-issues"></a>

This section provides troubleshooting guidance for the lease sharing feature. For information about using the feature, refer to [Sharing a lease with additional users and groups](manager-guide.md#lease-sharing).

### Sharing controls do not appear
<a name="sharing-controls-not-visible"></a>

If the **Assignments** tab, the **Allow owner to share lease** setting, or the add and remove controls do not appear, verify the following:
+ The **Assignments** tab is shown to administrators, managers, and the lease owner on leases in the **Active**, **Frozen**, and ended states (such as **Lease Manually Terminated**, **Terminated by User**, and **Account Quarantined**). Users with whom a lease is shared do not see the assignments tab. The tab is not shown on leases in the **Provisioning** state, because the lease has no assignments until provisioning completes.
+ On **Frozen** and **Terminated** leases, the tab is read-only for every role, including administrators and managers. These leases keep their assignment list but hold no live access, so the tab is informational: on a frozen lease it shows the access that unfreezing restores, and on a terminated lease it shows who last had access. To change assignments on a frozen lease, unfreeze it first. The API also rejects assignment edits on a lease that is not active, so this restriction applies to direct API calls as well as the web UI.
+ Lease sharing is enabled globally. Confirm that the **Enable lease sharing** setting is turned on in the **Lease policies** group of the **Settings** page. It is off by default. When it is off, the **Allow owner to share lease** toggle is disabled (greyed out) and shows an explanatory message, and lease owners cannot add or remove assignments. Administrators and managers can still add or remove assignments while the setting is off. For more information, refer to [Global configuration settings](administrator-guide.md#global-settings).
+ For lease owners, the individual lease has **Allow owner to share lease** turned on. This value is inherited from the lease template when the lease is created. Administrators and managers can change it on an individual lease, and can always manage assignments regardless of this setting.

### Access not granted after adding a user or group
<a name="shared-access-not-granted"></a>

Assignment changes are processed asynchronously, so access is typically granted within a few minutes rather than instantly. If a user still cannot access the account after several minutes:
+ On the lease details page, open the **Assignments** tab and check the status of the principal. Each row shows one of the following statuses:
  +  **Pending add** or **Pending remove** — The change is staged but not yet saved. Choose **Save changes** to apply it.
  +  **Granting** or **Revoking** — The solution is processing the change. These statuses are expected for a few minutes. The tab refreshes automatically while an update is in progress, so individual principals update as each one completes.
  +  **Access suspended** or **Access ended** — The lease is frozen or terminated, so access is revoked for everyone listed. Unfreeze the lease to restore access.
  +  **Grant failed** or **Revoke failed** — Processing finished without completing the change, and the operation needs attention.
  +  **Active** — Access is granted and in sync.
+ When any principal shows **Grant failed** or **Revoke failed**, the tab displays a warning titled **Some access changes did not apply**, with a **Retry** button. Choose **Retry** to reapply the access shown in the list. You do not need to change the list first. If you have already staged changes, the warning is hidden because **Save changes** reapplies the same access, so choose **Save changes** instead.
+ If a principal no longer exists in IAM Identity Center, remove it from the assignments instead of retrying.
+ Confirm the user or group still exists in IAM Identity Center.
+ Adding a group to a lease grants access asynchronously, the same as adding a user. Note that when someone joins a group that already has the lease, they get account access immediately, but it can take up to 24 hours to appear in their shared lease views, because group membership is cached for 24 hours.

For persistent failures, investigate the assignment processing dead-letter queue. Refer to [Investigating assignment processing failures](#assignment-processing-failures).

### User or group not appearing in search
<a name="principal-not-in-search"></a>

The search reads from a cache of IAM Identity Center principals that is refreshed hourly. If a recently added user or group does not appear:
+ For groups, confirm that **Allow group assignments** is set to **Allow all groups** in the **Lease policies** group of the **Settings** page. When group assignments are disabled, group search and exact group lookup are unavailable.
+ Wait for the next scheduled cache sync, or manually invoke the principal cache sync Lambda function from the AWS Lambda console in the hub account to refresh immediately. The sync runs hourly with a five-minute flexible window, so a new principal can take slightly over an hour to appear.
+ For users: confirm the user is a member of one of the solution’s IAM Identity Center groups (Admins, Managers, or Users). Only users who belong to these groups are cached for search. For groups: all groups in the identity store are cached regardless of membership, so a missing group indicates the cache has not yet refreshed.
+ Instead of searching, enter the exact email address of the user. When **Allow group assignments** is set to **Allow all groups**, you can also enter the exact name of a group. Exact lookup works when the principal is not yet in the search cache or when **Enable principal search** is turned off, because the value is resolved directly from IAM Identity Center.

### Save changes is unavailable
<a name="assignment-save-paused"></a>

 **Save changes** on the **Assignments** tab is unavailable in the following cases:
+ An earlier assignment update is still in flight, and the tab displays a message stating that an update is being processed. The solution processes one update per lease at a time, so it pauses further saves until the current update completes. Wait for the in-flight principals to leave the **Granting** or **Revoking** status, then save your changes.
+ You have not staged any changes yet.
+ The lease is frozen or terminated, which makes the tab read-only. For more information, refer to [Sharing controls do not appear](#sharing-controls-not-visible).

To discard staged changes without saving, choose **Cancel**. To reverse a single staged change, choose **Undo** on that row.

### Assignment limit reached
<a name="assignment-limit-reached"></a>

A lease supports a maximum of 20 principals in total, including the lease owner, which leaves 19 slots for additional users and groups. When a lease reaches this limit, the **Assignments** tab displays a warning and you cannot add another principal until you remove an existing one.

The solution enforces this limit on the server as well, so direct API calls that exceed it are rejected. When group assignments are enabled, you can share the lease with an IAM Identity Center group instead of adding users individually. A group occupies a single assignment slot regardless of how many members it has. For more information, refer to [Adding or removing users and groups on a lease](manager-guide.md#lease-sharing-add).

### Cannot remove the lease owner
<a name="assignment-owner-removal"></a>

The lease owner always holds an assignment slot and cannot be removed from the lease. The **Remove** action is not shown on the owner’s row. The solution also adds the owner to the assignment list automatically on the server, so a request that omits the owner does not remove their access. To end the owner’s access, terminate the lease instead. For more information, refer to [Managing leases](manager-guide.md#manage-leases).

### Investigating assignment processing failures
<a name="assignment-processing-failures"></a>

The solution processes IAM Identity Center access grants and removals through an SQS queue and an AWS Step Functions workflow. Messages that fail after the maximum number of retries are moved to a dead-letter queue (DLQ). The solution creates a CloudWatch alarm (with a description starting with "Assignment processing dead-letter queue has visible messages") that enters the `ALARM` state when messages are present in the DLQ. To find this alarm in the CloudWatch console, filter alarms by the description text or by the `ApproximateNumberOfMessagesVisible` metric on the DLQ.

**Important**
The solution does not attach a notification action to this alarm. To be notified when assignment processing fails, subscribe the alarm to an Amazon SNS topic after deployment. Otherwise, the alarm changes state without alerting anyone. For more information, refer to [Acting on alarm changes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Acting_Alarm_Changes.html).

Common causes of assignment processing failures include:
+ IAM Identity Center API throttling during periods of high assignment volume
+ A user or group that was deleted from IAM Identity Center after being added to a lease
+ Insufficient IAM permissions for the cross-account roles used to manage account assignments

To investigate messages in the dead-letter queue:

1. Sign in to the AWS Console using the hub account, and navigate to the [Amazon SQS console](https://console.aws.amazon.com/sqs/).

1. Locate the assignment processing dead-letter queue, named `Isb-<namespace>-AssignmentProcessingDLQ` (replace `<namespace>` with your deployment namespace).

1. Choose the queue, then choose **Send and receive messages** and **Poll for messages** to view the failed messages. Each message identifies the affected `leaseId`, `principalId`, `principalType`, and `intent`.

1. Use the `leaseId` to review related logs. Navigate to **CloudWatch > Logs > Log Analytics**, and use the `LogQuery` saved query with the lease ID to identify the underlying error. For more information, refer to [Viewing a specific Lease history](#viewing-lease-history).

1. After resolving the underlying cause (for example, IAM Identity Center throttling subsides, or a deleted principal is removed from the lease), retry the operation by resubmitting the assignments from the **Assignments** tab on the lease details page.

1. After the resubmitted assignments process successfully, delete the corresponding messages from the dead-letter queue to clear the alarm. Don’t redrive them to the source queue; their workflow callback tokens have expired. Always recover by re-submitting the assignments.

**Note**
When a lease is terminated, any access that fails to be revoked is remediated automatically during the account cleanup process before the account returns to the available pool. If remediation fails, the account is moved to the **Quarantine** state for manual review. For more information, refer to [Investigating accounts in Quarantine state](#investigating-accounts).

## Unfreezing a lease
<a name="unfreezing-a-lease"></a>

Unfreezing a lease restores access. It doesn’t change the lease’s budget or duration settings. The threshold that froze the lease freezes it again only if the lease reaches that threshold again.

To unfreeze a lease that a threshold froze:

1. On the lease’s **Cost** tab, in **Breach history**, find the newest row where **Action** is **Freeze account**. Its **Fired on** value shows which kind of threshold froze the lease.

1. (Optional) Change the lease’s **Budget Settings** or **Duration Settings** so that it isn’t frozen again or terminated. For more information, see [Changing a lease’s budget settings](manager-guide.md#edit-lease-budget). Base the change on the **Fired on** value:
   +  **Projected cost** or **Spend rate**: The estimate or rate can drop below the threshold and then reach it again. Raise or remove the threshold.
   +  **Time remaining**: If you set a later **Expiration Date**, the **Freeze Lease** duration threshold fires again when the remaining time reaches it. Change or remove the threshold first.
   + Any value: If current cost is close to the maximum budget, raise it. The solution terminates the lease when current cost reaches it.

1. On the **Leases** page, select the lease, choose **Actions**, and then choose **Unfreeze**.

## Budget and cost tracking issues
<a name="budget-cost-tracking-issues"></a>

Use this section to troubleshoot estimated cost tracking, spend rate thresholds, Amazon Bedrock token monitoring, and the lease **Cost** tab. For information about using these features, see [Reported cost, estimated cost, and current cost](manager-guide.md#threshold-cost-basis) and [Viewing lease costs](manager-guide.md#lease-costs).

### Cost tracking options are unavailable
<a name="cost-tracking-options-unavailable"></a>

If **Estimated cost tracking** or **Amazon Bedrock token monitoring** is unavailable on a lease template or lease budget form, an Admin hasn’t allowed the feature. The info icon next to the toggle shows **"Globally disabled. An administrator can allow this under Lease Policies on the Settings page."** An Admin can allow the features by turning on **Allow estimated cost tracking** or **Allow Bedrock token monitoring** in **Settings** > **Lease policies** > **Cost tracking**. For more information, see [Allowing cost tracking features](administrator-guide.md#cost-tracking-settings).

 **Spend rate thresholds** and the **Estimated cost** cost basis are available only when **Estimated cost tracking** is on for the template or lease.

### Cost tab is missing or shows no data
<a name="cost-tab-missing-data"></a>
+  **The Cost tab doesn’t appear**: Admins, Managers, and the lease owner see the tab on Active, Frozen, and ended leases. Pending Approval, Approval Denied, and Provisioning leases don’t have it.
+  **No cost readings for this lease yet**: AWS Cost Explorer hasn’t reported any cost for the lease yet.
+  **Not enough data yet** for **Predicted spend now**, **Spend rate**, or **Budget exhausted by**: The lease has no spend rate yet, or **Estimated cost tracking** is off for the lease. With **Estimated cost tracking** on, a new lease can take up to 2 days to get a spend rate.
+  **No service breakdown available**: **Enable service cost breakdown** is off, which is the default. For instructions, see [Allowing cost tracking features](administrator-guide.md#cost-tracking-settings).

### Spend figures are delayed or differ from Cost Explorer
<a name="spend-figures-differ"></a>

Billed cost comes from AWS Cost Explorer, so it can lag behind usage. For more information, see [How lease cost figures are calculated and updated](manager-guide.md#lease-cost-figures). On the lease’s **Cost** tab, **Billing data covers** shows the newest billing day included, and **Last checked** shows when the solution last checked the lease. To act before the bill arrives, use **Estimated cost** thresholds or Amazon Bedrock token monitoring.

Figures can also differ for these reasons:
+ The budget bars on the **Leases** page, the lease details page, and the home page show current cost. With Amazon Bedrock token monitoring, current cost includes token cost counted between Cost Explorer reports, so it can be higher than **Billed to date** on the **Cost** tab.
+ Token cost counted between Cost Explorer reports uses public list prices, so it doesn’t reflect discounts, private pricing, or credits.

To compare the figures with Cost Explorer:

1. In Cost Explorer, filter by the `ISB-<namespace>:LeaseId` tag, and use the lease **UUID** from the lease details page as the tag value. For more information, see [Querying sandbox costs by tag](monitoring-cost.md#querying-sandbox-costs-by-tag).

1. Show **Unblended costs**.

1. Exclude the **Credit** and **Refund** charge types.

1. Set the start of the date range to the lease’s start date.

### Thresholds don’t fire, fire early, or repeat
<a name="budget-threshold-issues"></a>

To see which thresholds fired, open **Breach history** on the lease’s **Cost** tab. A threshold doesn’t fire when:
+ The lease’s figure was already past it when you added or lowered it. A threshold fires only when the figure rises past it.
+ It’s an **Estimated cost** or spend rate threshold, and the lease has no spend rate yet.
+ You added it to the lease template after the lease was requested. A lease copies its settings from its template when it’s requested, so later template changes don’t apply. Add the threshold to the lease’s budget settings instead. For instructions, see [Changing a lease’s budget settings](manager-guide.md#edit-lease-budget).

A threshold can fire before billed cost reaches it if it uses **Estimated cost**, or if the lease uses Amazon Bedrock token monitoring. With token monitoring, **Reported cost** thresholds and the maximum budget use current cost.

A spend rate threshold fires again each time the rate drops below it and rises past it, so spending in bursts can cause repeated alerts. To reduce repeats, raise **Rate (USD)** or use **Per day**. For more information about how thresholds fire, see [Reported cost, estimated cost, and current cost](manager-guide.md#threshold-cost-basis) and [Spend rate thresholds](manager-guide.md#spend-rate-thresholds).

### Amazon Bedrock token usage or cost is missing
<a name="token-usage-not-shown"></a>

If a lease’s **Bedrock token usage** panel is missing, or shows no usage or cost, check the following:
+ The lease’s **Budget Settings** show **Amazon Bedrock token monitoring** as **Enabled**. A lease copies this setting from its template when it’s requested.
+ Enough time has passed. The solution reads token usage every 10 minutes.
+ The usage is in a Region in **ISB Managed Regions**. If you added the Region after you deployed the Compute stack, complete [Update managed Regions](step1-deploy-accountpool-stack.md#update-managed-regions) to update the Compute stack with a new **Force configuration update (optional)** value.
+ The lease’s account is linked in that Region, and the solution can read the Region. If the **Observability link missing** or **Observability Region unreadable** alarm is in `ALARM`, follow [Observability link missing in a managed Region](#observability-link-missing) or [Observability Region unreadable](#observability-region-unreadable).

## User lease termination issues
<a name="user-lease-termination-issues"></a>

This section provides troubleshooting guidance for issues related to users terminating their own leases. For instructions, refer to the [Terminating your lease](user-section.md#terminate-your-lease) section.

### Terminate lease button is not visible
<a name="terminate-lease-button-is-not-visible"></a>

The **Terminate lease** button is shown on a user’s own lease card only when all of the following are true:
+ The lease is in `Active` status. The button is not shown for leases in `Frozen` or `Provisioning` status.
+ You are the leaseholder for the lease.
+ Self-service lease termination is enabled by your Administrator. This is controlled by the **Allow user lease termination** global configuration setting. For more information, refer to the [Viewing or modifying Innovation Sandbox settings](administrator-guide.md#manage-settings) section.

### Lease termination request is rejected
<a name="lease-termination-request-is-rejected"></a>

If a request to terminate a lease is rejected with a 403 error, the same conditions listed above are enforced on the server, so they also apply to direct API calls, not just the web UI. Verify that the lease is in `Active` status, that you are the leaseholder, and that self-service lease termination is enabled.

Administrators and Managers are not affected by these restrictions and can terminate any monitored lease regardless of status.

**Note**
Lease termination cannot be undone. Terminating a lease immediately begins the account cleanup process.

## Lease request limit reached
<a name="lease-request-rate-limit"></a>

If you receive an error message stating **"You’ve reached the lease request limit. You can request another lease after …​"** when requesting a new account lease, you have reached the maximum number of lease requests allowed within the configured time window. For more information on requesting a lease, refer to the [Requesting a new account lease](user-section.md#request-new-account-lease) section.

By default, users can request up to 10 leases within a rolling 168-hour (7-day) window. Only leases that consumed an account count toward this limit: leases that reached `Active`, `Frozen`, or `Provisioning` status, or any status where the lease has since ended. Leases in `Pending Approval` or `Approval Denied` status are not counted.
+ Administrators and Managers are exempt from this limit when requesting leases themselves. However, leases they assign to a user still count toward that user’s own request window. If a user is assigned a large number of leases by Admins or Managers, they might be temporarily unable to self-request additional leases until the window slides.
+ The error message includes the time at which you can next request a lease.
+ Administrators can adjust the limit by updating the **Rate limit window** and **Max requests per window** global configuration settings. For more information, refer to the [Viewing or modifying Innovation Sandbox settings](administrator-guide.md#manage-settings) section.
+ The effective window is capped by the lease record retention period (the **Lease record retention (days)** setting). If the configured **Rate limit window** value exceeds this cap, the solution logs a `LeaseRequestWindowCapped` warning once per Lambda cold start, indicating a configuration mismatch that should be corrected.

## Group Cost reporting issues
<a name="cost-reporting-issues"></a>

If the group cost reporting function fails to generate reports, you can manually re-run the function to resolve the issue.

### Re-running the group cost reporting function
<a name="re-running-the-group-cost-reporting-function"></a>

To manually invoke the group cost reporting function:

1. Log in to the AWS Console using the Hub account.

1. Navigate to the **AWS Lambda** service.

1. Locate and choose the group cost reporting Lambda function.

1. Choose **Test** to create a new test event

1. To run the cost reporting for the previous month, use an empty test event `{}`.

1. Choose **Test** to run the function.

### Running cost reporting for a previous month
<a name="running-cost-reporting-for-a-previous-month"></a>

To generate cost reports for a specific previous month:

1. Follow steps 1-4 from the previous section.

1. In the test event configuration, use the following JSON format:

   ```json
   {
     "detail": {
       "reportMonth": "yyyy-MM"
     }
   }
   ```

   Replace `yyyy-MM` with the desired year and month (for example, `2024-03` for March 2024).

1. Choose **Test** to run the function for the specified month.

**Note**
The cost reporting function will process billing data for the specified month and generate reports accordingly. Ensure that billing data is available for the requested month before running the function.

## Observability link missing in a managed Region
<a name="observability-link-missing"></a>

TokenPoll checks for account links after it successfully lists the links attached to a managed Region’s hub sink. The **Observability link missing** alarm enters the `ALARM` state after warnings in two of three ten-minute periods.

The `Isb-<namespace>-ObservabilityLinks` StackSet uses a 100 percent failure tolerance. With this tolerance, the Compute stack update and StackSet operation report success when an affected account and Region stack instance becomes `OUTDATED` with a `FAILED` detailed status. Until the link is restored, the hub cannot read that account’s Bedrock token metrics in the Region.

TokenPoll can report both observability alarms in the same period. It can detect a missing account link after listing attached links and then fail to read the Region’s token metrics. Treat each warning separately. If attached links cannot be listed, TokenPoll cannot determine whether an account link is missing. For Region-wide failures, see [Observability Region unreadable](#observability-region-unreadable).

**Note**
This alarm reports impact to token-monitored leases, not readiness for every account in the pool. Every lease that has a Sandbox Space is token-monitored, so a missing link also affects Sandbox Spaces leases. While the link is missing, token monitoring can’t see that account’s agent spend between Cost Explorer reports, and only the account’s billed cost reaches the lease budget. TokenPoll does not check links when there are no token-monitored leases. The alarm also aggregates every missing account and Region pair, so another missing link keeps it in the `ALARM` state.

### Identify and resolve the cause
<a name="identify-and-resolve-the-cause"></a>

1. Open the [Amazon CloudWatch Logs console](https://console.aws.amazon.com/cloudwatch/home#logsV2:log-groups) in the hub account.

1. Open the **Compute-ISBLogGroup** log group.

1. Search for messages beginning `Observability Link Missing:`. Use the `leaseId`, `awsAccountId`, and `region` fields to identify the affected lease, account, and AWS Region.

1. Open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home#/stacksets) in the hub account.

1. Choose **StackSets**.

1. Choose `Isb-<namespace>-ObservabilityLinks`, inspect the affected stack instance, and resolve the cause reported in its `StatusReason`. If a disabled opt-in Region caused the failure, set that Region’s opt-in status to `ENABLED` in the sandbox account. For more information, see [Managed opt-in Regions](plan-your-deployment.md#managed-opt-in-regions).

**Note**
Use the AWS Organizations management account or an AWS Account Management delegated administrator to change a sandbox account’s Region opt-in status. The solution’s service control policies prevent leased sandbox sessions from changing this status.

Correcting a disabled opt-in Region does not retry an unchanged failed stack instance. If the instance remains `OUTDATED` with a `FAILED` detailed status after you resolve the cause reported in its `StatusReason`, see [Contact AWS Support](contact-aws-support.md). Include the StackSet name, sandbox account ID, AWS Region, and `StatusReason` in the support case.

CloudWatch propagates cross-account metric access asynchronously after the link is restored. Check the next TokenPoll run before investigating a new metric-read warning. The alarm returns to `OK` after two consecutive ten-minute periods without a missing-link warning. If another account and Region pair lacks a link, the alarm remains in `ALARM`.

The alarm treats missing metric data as non-breaching. Confirm that the stack instance is `CURRENT` with a `SUCCEEDED` detailed status. Do not rely on the alarm state alone.

## Observability Region unreadable
<a name="observability-region-unreadable"></a>

TokenPoll skips a managed Region when it cannot list the links attached to the regional OAM sink or cannot read the Region’s Bedrock token metrics. The **Observability Region unreadable** alarm enters the `ALARM` state after warnings in two of three ten-minute periods.

While the Region is skipped, new Bedrock token metrics from that Region are not included in the current TokenPoll budget evaluation. TokenPoll leaves the Region’s stored read position unchanged so a later successful poll can retry the unread window.

**Note**
This alarm reports impact to token-monitored leases, not readiness for every account in the pool. Every lease that has a Sandbox Space is token-monitored, so an unreadable Region also affects Sandbox Spaces leases in that Region. TokenPoll makes no regional calls when there are no token-monitored leases. The alarm aggregates every managed Region and failure cause, so another unreadable Region can keep it in the `ALARM` state.

### Identify and resolve the cause
<a name="identify-and-resolve-the-cause-2"></a>

Follow these steps to identify the affected Region and failed operation.

1. Open the [Amazon CloudWatch Logs console](https://console.aws.amazon.com/cloudwatch/home#logsV2:log-groups) in the hub account.

1. Open the **Compute-ISBLogGroup** log group.

1. Search for messages beginning `Observability Region Unreadable:`. Use the `region`, `leasesAffected`, `errorName`, and `error` fields to identify the affected Region and cause.

1. Use the warning message and `errorName` to select the recovery action:
   +  `linked accounts could not be listed` means TokenPoll could not inspect the regional OAM sink. If `errorName` is `MissingSinkError`, the Account Pool and Compute stacks have different managed Region configurations, either because the Compute refresh did not run or because it failed and rolled back. This is not a failed member link. Complete [Update managed Regions](step1-deploy-accountpool-stack.md#update-managed-regions) to update the Compute stack with a new **Force configuration update (optional)** value. For other errors, verify that the Region is enabled in the hub account and investigate the reported OAM access or service error.
   +  `token metrics could not be read` means TokenPoll inspected the OAM sink but the regional CloudWatch metrics request failed. Investigate the reported CloudWatch permission, throttling, or service error.

1. For throttling or service errors, check the next ten-minute periods before changing infrastructure. TokenPoll retries the Region on its next run.

1. After resolving the cause, confirm that TokenPoll no longer logs the warning.

After two consecutive ten-minute periods without an unreadable-Region warning, the alarm returns to `OK`. An unreadable-Region warning alone does not show that an account link is missing. If the logs also contain `Observability Link Missing`, investigate that warning separately using [Observability link missing in a managed Region](#observability-link-missing).

## Blueprint deployment issues
<a name="blueprint-deployment-issues"></a>

This section covers common issues related to blueprint deployment and resolution steps.

### StackSet not found error
<a name="stackset-not-found-error"></a>

If a lease fails with status **ProvisioningFailed** and logs show `StackSetNotFoundException`, the blueprint’s associated StackSet no longer exists or you cannot access it.

The solution stores the composite StackSet ID (format: `stacksetname:uuid`) at registration time. This ID is unique and immutable, so if the original StackSet is deleted and a new one is created with the same name, the blueprint will not resolve to the new StackSet.

 **Possible root causes:**
+ StackSet was deleted after blueprint registration
+ StackSet permissions changed

 **Impact on existing leases:**

Only new lease deployments are affected. Active leases that already have deployed stack instances continue to function normally. When those leases terminate, the solution attempts stack instance cleanup on a best-effort basis and proceeds with normal account cleanup via AWS Nuke regardless of the cleanup result.

 **To resolve this issue:**

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/) in your hub account.

1. Verify that the StackSet exists and is active.

1. If the StackSet was deleted:

   1. Navigate to the Innovation Sandbox web UI.

   1. From **Administration**, choose **Blueprints**.

   1. Unregister the affected blueprint.

   1. If needed, create a new StackSet and register it as a new blueprint. For instructions, refer to [Creating self-managed StackSets](administrator-guide.md#create-stacksets) and [Registering a new blueprint](administrator-guide.md#registering-blueprint).

1. If the StackSet exists but is inaccessible, verify IAM permissions for the IntermediateRole.

### Blueprint deployment timeout
<a name="deployment-timeout"></a>

A deployment with error type `DeploymentTimeout` means the StackSet deployment took longer than the configured timeout (default: 30 minutes). The lease transitions to **ProvisioningFailed** and the account is automatically cleaned up, including any resources deployed by the blueprint.

 **To resolve this issue:**

1. Review the failed deployment in the blueprint’s **Recent deployments** table to confirm the timeout duration.

1. To prevent future timeouts, increase the deployment timeout in the blueprint’s **Deployment configuration** section. For details, refer to [Updating blueprint metadata](administrator-guide.md#updating-blueprint).

### Concurrent deployment failure (OperationInProgressException)
<a name="concurrent-deployment-failure"></a>

If a blueprint deployment fails with error type `OperationInProgressException` and message "Another operation is in progress on this StackSet", this means multiple leases using the same blueprint were approved at the same time and managed execution is not enabled on the StackSet. Without managed execution, CloudFormation rejects concurrent operations on the same StackSet.

 **Impact:**
+ Innovation Sandbox terminates the affected lease (auto-approved) or resets it to PendingApproval (manual approval) so the manager can re-approve.
+ The failed deployment appears in the blueprint’s deployment history with error type `OperationInProgressException`.

 **To resolve:**

Enable managed execution on your StackSet to allow CloudFormation to queue concurrent operations automatically:

```bash
aws cloudformation update-stack-set \
  --stack-set-name <STACKSET_NAME> \
  --managed-execution Active=true \
  --administration-role-arn <ADMIN_ROLE_ARN> \
  --execution-role-name <EXECUTION_ROLE_NAME> \
  --use-previous-template
```

For more information, refer to [Managed execution](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ManagedExecution.html) in the AWS CloudFormation API Reference.

**Tip**
To avoid this issue when creating new StackSets, include the `--managed-execution Active=true` flag. For instructions, refer to [Creating self-managed StackSets](administrator-guide.md#create-stacksets) in the Administrator Guide.

### Blueprint permission errors
<a name="blueprint-permission-errors"></a>

If blueprint operations fail with permission errors, verify IAM role configuration.

 **To resolve:**

1. Verify the StackSet uses the self-managed permission model. Service-managed StackSets are not supported.

1. Verify the IAM roles have the required CloudFormation permissions:
   +  `cloudformation:CreateStackInstances`
   +  `cloudformation:DescribeStackSetOperation`
   +  `cloudformation:DeleteStackInstances`

1. If you are using custom IAM roles (not the recommended ISB roles), ensure they have equivalent permissions. The recommended roles are:
   + Administration Role: `arn:aws:iam::{ACCOUNT-ID}:role/InnovationSandbox-{NAMESPACE}-IntermediateRole`
   + Execution Role: `InnovationSandbox-{NAMESPACE}-SandboxAccountRole`

**Note**
Custom IAM roles are supported. The solution logs a warning if non-recommended roles are detected but does not block registration or deployment.

### StackSet not appearing in the Innovation Sandbox application
<a name="stackset-not-appearing"></a>

If your StackSet does not appear in the StackSet selection list during blueprint registration, verify the following:

 **Possible root causes:**
+ The StackSet was created in a different AWS account than the Innovation Sandbox hub account
+ The StackSet uses the SERVICE\_MANAGED permission model instead of SELF\_MANAGED
+ The StackSet is in a non-ACTIVE status

 **To resolve:**

1. Verify the StackSet exists in the same AWS account where Innovation Sandbox is deployed (the hub account).

1. In the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/), navigate to **StackSets** and confirm:

   1. The StackSet status is **ACTIVE**.

   1. The permission model is **SELF\_MANAGED**. Service-managed StackSets are not supported.

1. If the StackSet was created in a different account, recreate it in the hub account. For instructions, refer to [Creating self-managed StackSets](administrator-guide.md#create-stacksets).

## Cleanup validation issues
<a name="cleanup-validation-issues"></a>

This section provides guidance for issues related to post-cleanup resource validation. For an overview of the feature, see the [Post-cleanup resource validation](account-cleaner-component.md#post-cleanup-validation) section.

### Validation is quarantining accounts
<a name="validation-quarantining-accounts"></a>

If accounts are being quarantined after cleanup due to validation failures, check the remaining resources from the account details page. Common causes:
+  **Missing exclusion entry**: A resource type or ARN pattern exists in the Nuke configuration’s filter list but not in the validator exclusion configuration. Add the missing entry to the exclusion config in AWS AppConfig. For instructions, see [Keeping exclusion configurations in sync](#validation-exclusion-config-sync).
+  **Resource Explorer indexing delay**: Resource Explorer can take up to 7 days to fully remove deleted resources from its index. We recommend a cooldown period of at least 168 hours (7 days) to avoid false positives in post-cleanup validation. If cooldown is shorter or disabled, validation might flag resources that were successfully deleted but have not yet aged out of the Resource Explorer index.

To temporarily allow accounts through while investigating, set `failureAction` to `Silent` or `Warn` in the **Cleanup** section of the **Settings** page. In `Silent` mode, validation still runs but takes no action. In `Warn` mode, accounts proceed to Available with a warning log and remaining resources are surfaced in the UI.

### Keeping exclusion configurations in sync
<a name="validation-exclusion-config-sync"></a>

The validator exclusion configuration must match the Nuke configuration’s filters. When you add a Nuke filter to protect a resource from deletion:

1. Open the AWS AppConfig console in the hub account.

1. Navigate to the ISB application and choose the configuration profile whose name contains `ValidatorExclusionConfig`.

1. Add the corresponding ARN glob pattern to `validation.excludedArnPatterns`.

1. Deploy the updated configuration.

**Note**
The exclusion config only supports ARN-based patterns (`excludedArnPatterns`). If you need to exclude a resource type, use a wildcard ARN pattern such as `arn:aws:service:*:*:resource-type/*`. Only add exclusion entries for resource types that Resource Explorer indexes. For the list of supported resource types, refer to [Supported resource types](https://docs.aws.amazon.com/resource-explorer/latest/userguide/supported-resource-types.html) in the AWS Resource Explorer User Guide.

## Account cost allocation tag issues
<a name="account-cost-allocation-tag-issues"></a>

This section provides guidance for issues related to the account cost allocation tagging feature. For an overview of the feature, see the [Account cost allocation tagging](account-cost-allocation-tagging.md) section.

### Checking tag activation status
<a name="checking-tag-activation-status"></a>

After you deploy or update the solution, the ISB tag keys can take up to 24 hours to activate in the AWS Billing and Cost Management console. To check their status:

1. Sign in to the AWS Organizations management account and open the [Cost allocation tags](https://console.aws.amazon.com/billing/home#/tags) page in the AWS Billing and Cost Management console.

1. On the **User-defined cost allocation tags** tab, search for the tag keys prefixed with `ISB-<namespace>:`, where `<namespace>` is the namespace of your deployment (for example, `ISB-<namespace>:LeaseId`).

1. Confirm that each ISB tag key shows a status of **Active**.

**Note**
Cost allocation tag keys appear in this list only after they have been applied to at least one account and have propagated to the billing system, which can take several hours. All cost is still attributed correctly during this delay.

### Manually activating cost allocation tags
<a name="manually-activating-cost-allocation-tags"></a>

The solution activates the ISB tag keys automatically through a Step Functions workflow. A CloudWatch alarm fires on any terminal non-success of the workflow that is not operator-initiated. The following conditions trigger the alarm: an unhandled Lambda error; the `TagActivationMaxAttemptsReached` failure, which occurs when the workflow exhausts all 24 retry attempts; or the state machine’s own timeout. The alarm evaluates the sum of the workflow’s `ExecutionsFailed` and `ExecutionsTimedOut` metrics over 1 hour. In this case, you can activate the tag keys manually:

1. Sign in to the AWS Organizations management account and open the [Cost allocation tags](https://console.aws.amazon.com/billing/home#/tags) page in the AWS Billing and Cost Management console.

1. On the **User-defined cost allocation tags** tab, choose each tag key prefixed with `ISB-<namespace>:` (`ISB-<namespace>:LeaseId`, `ISB-<namespace>:CostReportGroup`, `ISB-<namespace>:LeaseTemplate`, `ISB-<namespace>:User`, and `ISB-<namespace>:Status`).

1. Choose **Activate**.

Cost data grouped by the activated tags can take up to 24 hours to appear in AWS Cost Explorer.

### Tag application failures
<a name="tag-application-failures"></a>

If sandbox costs are not appearing under the expected tags, review the Compute stack log group for `TagResourceFailed` log entries. The `reason` field identifies the cause:
+  `TagSpaceExhausted`: The account already holds enough tags that adding the ISB tags would exceed the AWS 50-tag account limit. Remove unused custom tags from the account so that it has 45 or fewer non-ISB tags, then re-run the lease approval or wait for the next lease.
+  `ApiError`: A transient or permissions-related error occurred (for example, throttling or access denied). The lease proceeds using the legacy cost attribution path. Review the log entry for details.

For more information about tagging alarms, see the [Alarms](monitoring-alarms.md) section.
