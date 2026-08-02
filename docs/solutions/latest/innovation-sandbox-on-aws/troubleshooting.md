---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/troubleshooting.html
---

# Troubleshooting
<a name="troubleshooting"></a>

This section provides information about known issues and instructions to mitigate known errors. If these instructions do not resolve your issue, see the [Contact AWS Support](contact-aws-support.md) section to open an AWS Support case for this solution.

## Application sign in error
<a name="application-sign-in-error"></a>

If you receive an error titled **"Application sign in error"** when accessing the Innovation Sandbox on AWS Web UI, it is likely that the IAM Identity Center application has been misconfigured. Possible root causes include:
+ Incorrect **Attribute mappings** in the IAM Identity Center SAML 2.0 application
+ Incorrect **Application ACS URL** in the IAM Identity Center SAML 2.0 application
+ Incorrect **webAppUrl** in the AWS AppConfig global configuration
+ Incorrect **idpSignInUrl** in the AWS AppConfig global configuration
+ Missing primary email address in IAM Identity Center for the user attempting to login

Refer to the [Post deployment configuration tasks](post-deployment-configuration-tasks.md) section, and validate that the configurations in both IAM Identity Center and AWS AppConfig are correct.

## Incorrect global configuration
<a name="incorrect-global-configuration"></a>

If you receive an error with the message **"Incorrect global configuration"** when accessing the Innovation Sandbox on AWS Web UI, your global configuration in AWS AppConfig has not been updated properly and likely contains invalid fields or values. Review any validation errors included in the error message or logs in the **Compute-ISBLogGroup log group** and make the appropriate corrections to the global configuration. Refer to the [Updating the global configuration](update-auth-config.md#updating-the-global-config) section for information on how to update the global configuration.

## Authentication failed, Invalid document signature
<a name="authentication-failed-invalid-document-signature"></a>

If you receive an error with the message **"Invalid document signature"** when accessing the Innovation Sandbox on AWS Web UI, the IDP Cert secret was either not updated or an incorrect value was provided. Refer back to the [Update values in AWS Secrets Manager](update-values-secrets.md) section to ensure that the value is correct.

## Authentication failed, SAML assertion audience mismatch
<a name="authentication-failed-saml-assertion-audience-mismatch"></a>

If you receive an error with the message **"SAML assertion audience mismatch"** when accessing the Innovation Sandbox on AWS Web UI, the audience value provided in your IAM Identity Center SAML application configuration does not match the one configured in AWS AppConfig. These values must match for the solution authentication to work properly. Refer back to the [Create a SAML 2.0 application](create-saml-app.md) and [Updating the global config](update-auth-config.md#updating-the-global-config) sections for information on how to update these values.

## Investigating accounts in Quarantine state
<a name="investigating-accounts"></a>

**Note**
If the account clean-up mechanism fails to automatically delete resources at the end of an active lease, you might have accounts in a `Quarantine` state. We highly recommend investigating quarantined accounts as quickly as possible, as these accounts can incur costs for resources running inside these accounts.

When the Innovation Sandbox solution is unable to cleanup resources in a sandbox account, the account is moved to a `Quarantine` state and an email is sent to the solution administrators indicating that action should be taken to resolve the account’s quarantine status.

To resolve the quarantined status:

1. Log in to the web UI as an Admin, and from the left, under **Administration**, choose **Accounts**.

1. Verify the accounts in `Quarantine` status, and decide whether to clean up the account and return to the account pool, or to eject the account from the solution.
   + To clean up the account and return it to the account pool, choose the account, and under **Actions**, choose **Retry cleanup**.
   + To eject the account, choose the account, and under **Actions**, choose **Eject account**. This moves the account to the **Exit** OU, from which you can manually move it to your desired OU. For more information, refer to the [Uninstall the solution](uninstall-the-solution.md) section.

If the account is in quarantine because the **retry cleanup failed**, refer to the [Resolving cleanup failures](#resolving-cleanup-failures) section.

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

1. To manually handle any deletion failures in the affected account, navigate back to the **Accounts** page, and log in to the account using the **Login to account** option.

1. After you have manually handled all errors, to restart the cleanup process in the web UI, choose the account and under **Actions**, choose **Retry cleanup**.

## Viewing a specific Lease history
<a name="viewing-lease-history"></a>

1. Log in to the web UI as an Admin, and from the left, under **Administration**, choose **Leases**.

1. Choose the lease name to view lease details.

1. Copy the LeaseID from the Lease Summary page. You will need this to view lease history in the AWS Console.

1. Log in to the AWS Console, and navigate to the **CloudWatch > Logs Insights** page.

1. From the right pane, under Sample queries, choose the ISB group, and from the dropdown, choose `LogQuery` saved query and choose **Apply**.

1. In the query window, choose the time frame to view logs for and paste the LeaseID into the indicated section.

1. Choose **Run query** to view logs related to the LeaseID provided for the selected time frame. The log information is displayed under the *Logs* tab.

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
+ Maintenance mode is enabled and you are signed in using a Manager or User role. You will need to contact your Admin to disable maintenance mode in AWS AppConfig. For more information, refer to the [Maintenance mode](remove-resources.md#enable-maintenance-mode) section.

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

## Unfreezing a lease
<a name="unfreezing-a-lease"></a>

When a lease is frozen due to reaching a budget or duration threshold, simply unfreezing the lease without addressing the underlying threshold condition will result in the lease being automatically refrozen when the monitoring system runs its next check.

To successfully unfreeze a lease that was frozen due to threshold conditions:

1.  **Update the lease parameters first**: Before unfreezing the lease, you must update either the budget limit, duration limit, or both, depending on which threshold caused the freeze.
   + If frozen due to budget threshold: Increase the maximum budget amount for the lease
   + If frozen due to duration threshold: Extend the lease duration
   + You can update both if needed

1.  **Unfreeze the lease**: After updating the appropriate thresholds, you can then unfreeze the lease through the web UI.

1.  **Verify the changes**: Confirm that the updated budget or duration limits are sufficient to prevent immediate refreezing.

## Group Cost reporting issues
<a name="cost-reporting-issues"></a>

If the group cost reporting function fails to generate reports, you can manually re-run the function to resolve the issue.

### Re-running the group cost reporting function
<a name="re-running-the-group-cost-reporting-function"></a>

To manually invoke the group cost reporting function:

1. Log in to the AWS Console using the Hub account.

1. Navigate to the **AWS Lambda** service.

1. Locate and select the group cost reporting Lambda function.

1. Choose **Test** to create a new test event

1. To run the cost reporting for the previous month, use an empty test event `{}`.

1. Choose **Test** to execute the function.

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

1. Choose **Test** to execute the function for the specified month.

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

1. Sign in to the [CloudFormation console](https://console.aws.amazon.com/cloudformation/) in your hub account.

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

1. In the [CloudFormation console](https://console.aws.amazon.com/cloudformation/), navigate to **StackSets** and confirm:

   1. The StackSet status is **ACTIVE**.

   1. The permission model is **SELF\_MANAGED**. Service-managed StackSets are not supported.

1. If the StackSet was created in a different account, recreate it in the hub account. For instructions, refer to [Creating self-managed StackSets](administrator-guide.md#create-stacksets).
