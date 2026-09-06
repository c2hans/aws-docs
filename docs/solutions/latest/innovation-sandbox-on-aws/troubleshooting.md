---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/troubleshooting.html
---

# Troubleshooting
<a name="troubleshooting"></a>

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

## Errors when saving settings
<a name="settings-save-errors"></a>

Admins can modify solution settings on the **Settings** page of the web UI. Each section is validated when you choose **Save**. Two errors need additional action beyond correcting the highlighted field:
+  **"The email provided is not a verified SES identity in this account. Verify the address or its domain in Amazon SES before saving."** This error appears on the **Email from address** field of the **Notification** section. The sender address, or its parent domain, must be a verified identity in Amazon SES in the Hub account. Verify the address or domain in the Amazon SES console, then choose **Save** again.
+  **"These settings were modified by another administrator. Reload to see the latest values."** Another Admin saved the same section after you loaded the page. Choose **Reload** to load the latest values, reapply your changes, and choose **Save** again. Reloading discards your unsaved edits for that section.

For more information, see the [Viewing or modifying Innovation Sandbox settings](administrator-guide.md#manage-settings) section.

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

1. Confirm the account that has failed the cleanup process. You will need this to view log information in the AWS Console.

1. Log in to the AWS Console using the Hub account, and navigate to the **CloudWatch > Logs Insights** page.

1. From the right pane, under Sample queries, choose the ISB group, and from the dropdown, choose the `AccountCleanupLogs` saved query, and choose **Apply**.

1. In the query window, choose a time frame that includes when the account was last cleaned up (for example: last 3 days) and paste the 'Last Cleanup ReferenceID' into the indicated section.

1. Choose **Run query** to see related events. The log information is displayed under the *Logs* tab.

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

1. Log in to the AWS Console, and navigate to the **CloudWatch > Logs Insights** page.

1. From the right pane, under Sample queries, choose the ISB group, and from the dropdown, choose `LogQuery` saved query and choose **Apply**.

1. In the query window, choose the time frame to view logs for and paste the LeaseID into the indicated section.

1. Choose **Run query** to view logs related to the LeaseID provided for the selected time frame. The log information is displayed under the *Logs* tab.

**Note**
Terminated leases distinguish who ended them. When a leaseholder terminates their own lease, the solution records the status as `Terminated by User` (`UserTerminated` in log entries and events). This is distinct from `Lease Manually Terminated`, which indicates an Admin or Manager terminated the lease.

## Viewing a specific User history
<a name="viewing-user-history"></a>

1. Log in to the web UI as an Admin, and from the left, under **Administration**, choose **Accounts**.

1. From the Accounts page, confirm the user email address you want to view history for. You will need this to view user/account history in the AWS Console.

1. Log in to the AWS Console, and navigate to the **CloudWatch > Logs Insights** page.

1. From the right pane, under Sample queries, choose the ISB group, and from the dropdown, choose `LogQuery` saved query and choose **Apply**.

1. In the query window, choose the time frame to view logs for and paste the email address into the indicated section.

1. Choose **Run query** to view logs related to the email address provided for the selected time frame. The log information is displayed under the *Logs* tab.

### 403 Permissions error
<a name="403-permissions-error"></a>

If you find an issue within the Identity Center:
+ Your session might have timed out. Refresh your browser to resolve this.
+ Maintenance mode is enabled and you are signed in using a Manager or User role. New deployments of Innovation Sandbox on AWS start with maintenance mode turned **ON**. Managers and Users cannot access the solution until an Admin turns it off. Contact your Admin: an Admin can turn off maintenance mode on the **Settings** page, under the **General** tab, in the **Maintenance Mode** section. For more information, see the [Managing maintenance mode](administrator-guide.md#maintenance-mode) section.
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

## Lease sharing issues
<a name="lease-sharing-issues"></a>

This section provides troubleshooting guidance for the lease sharing feature. For information about using the feature, refer to [Sharing a lease with additional users and groups](manager-guide.md#lease-sharing).

### Sharing controls do not appear
<a name="sharing-controls-not-visible"></a>

If the **Assignments** tab, the **Allow owner to share lease** setting, or the add and remove controls do not appear, verify the following:
+ The **Assignments** tab is shown to administrators, managers, and the lease owner on leases in the **Active**, **Frozen**, and ended states (such as **Lease Manually Terminated**, **Terminated by User**, and **Account Quarantined**). Users with whom a lease is shared do not see the assignments tab. The tab is not shown on leases in the **Provisioning** state, because the lease has no assignments until provisioning completes.
+ On **Frozen** and **Terminated** leases, the tab is read-only for every role, including administrators and managers. These leases keep their assignment list but hold no live access, so the tab is informational: on a frozen lease it shows the access that unfreezing restores, and on a terminated lease it shows who last had access. To change assignments on a frozen lease, unfreeze it first. The API also rejects assignment edits on a lease that is not active, so this restriction applies to direct API calls as well as the web UI.
+ Lease sharing is enabled globally. Confirm that the **Enable lease sharing** setting is turned on in the **Lease Policies** section of the **Settings** page. It is off by default. When it is off, the **Allow owner to share lease** toggle is disabled (greyed out) and shows an explanatory message, and lease owners cannot add or remove assignments. Administrators and managers can still add or remove assignments while the setting is off. For more information, refer to [Global configuration settings](administrator-guide.md#global-settings).
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
+ Wait for the next scheduled cache sync, or manually invoke the principal cache sync Lambda function from the AWS Lambda console in the hub account to refresh immediately. The sync runs hourly with a five-minute flexible window, so a new principal can take slightly over an hour to appear.
+ For users: confirm the user is a member of one of the solution’s IAM Identity Center groups (Admins, Managers, or Users). Only users who belong to these groups are cached for search. For groups: all groups in the identity store are cached regardless of membership, so a missing group indicates the cache has not yet refreshed.
+ Instead of searching, enter the exact email address of the user or the exact name of the group. This works even when the principal is not yet in the search cache, or when the **Enable principal search** setting is turned off on the **Settings** page, because the exact value is resolved directly from IAM Identity Center.

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

The solution enforces this limit on the server as well, so direct API calls that exceed it are rejected. To share a sandbox environment with more people than this limit allows, share the lease with an IAM Identity Center group instead of adding users individually. A group occupies a single assignment slot regardless of how many members it has. For more information, refer to [Adding or removing users and groups on a lease](manager-guide.md#lease-sharing-add).

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

1. Use the `leaseId` to review related logs. Navigate to **CloudWatch > Logs Insights**, and use the `LogQuery` saved query with the lease ID to identify the underlying error. For more information, refer to [Viewing a specific Lease history](#viewing-lease-history).

1. After resolving the underlying cause (for example, IAM Identity Center throttling subsides, or a deleted principal is removed from the lease), retry the operation by resubmitting the assignments from the **Assignments** tab on the lease details page.

1. After the resubmitted assignments process successfully, delete the corresponding messages from the dead-letter queue to clear the alarm. Don’t redrive them to the source queue; their workflow callback tokens have expired. Always recover by re-submitting the assignments.

**Note**
When a lease is terminated, any access that fails to be revoked is remediated automatically during the account cleanup process before the account returns to the available pool. If remediation fails, the account is moved to the **Quarantine** state for manual review. For more information, refer to [Investigating accounts in Quarantine state](#investigating-accounts).

## Unfreezing a lease
<a name="unfreezing-a-lease"></a>

When a lease is frozen due to reaching a budget or duration threshold, unfreezing the lease without addressing the underlying threshold condition will result in the lease being automatically refrozen when the monitoring system runs its next check.

To successfully unfreeze a lease that was frozen due to threshold conditions:

1.  **Update the lease parameters first**: Before unfreezing the lease, you must update either the budget limit, duration limit, or both, depending on which threshold caused the freeze.
   + If frozen due to budget threshold: Increase the maximum budget amount for the lease
   + If frozen due to duration threshold: Extend the lease duration
   + You can update both if needed

1.  **Unfreeze the lease**: After updating the appropriate thresholds, you can then unfreeze the lease through the web UI.

1.  **Verify the changes**: Confirm that the updated budget or duration limits are sufficient to prevent immediate refreezing.

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
+ The effective window is capped by the lease record retention period (the **Lease record TTL** setting, in days). If the configured **Rate limit window** value exceeds this cap, the solution logs a `LeaseRequestWindowCapped` warning once per Lambda cold start, indicating a configuration mismatch that should be corrected.

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

   ```
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

```
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
