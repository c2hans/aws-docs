---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/known-issue-resolution.html
---

# Known issue resolution
<a name="known-issue-resolution"></a>
+  **Issue:** A finding that I suppressed in AWS Security Hub CSPM changed to `NOTIFIED` (**In progress** in AWS Security Hub) and was then automatically remediated.

   **Cause:** This affects versions earlier than v4.1.0. A suppression set in AWS Security Hub CSPM is not reflected in the finding’s status in AWS Security Hub. Those versions based their remediation decision only on the status included in each incoming event. The solution therefore treated an AWS Security Hub event that still showed the finding’s previous status as actionable. The solution then changed the AWS Security Hub CSPM workflow status from `SUPPRESSED` to `NOTIFIED`. A later event could then start a remediation. The finding history shows the change as made by the `SO0111-ASR-sendNotifications` Lambda function’s role, with a note such as `Finding Workflow State is not NEW (NOTIFIED)`.

   **Resolution:** Update the solution to v4.1.0 or later. Starting in v4.1.0, the solution reads the finding’s current status in both AWS Security Hub CSPM and AWS Security Hub before an automatic or deadline-enforced remediation. It no longer changes the workflow status of a finding that was not `NEW`. Until you update, keep the affected resources out of fully automated remediation with an exclude-mode resource filter. The filter should match the resources by account ID, organizational unit, or ARN pattern (see [Create and apply resource filters](manage-automated-remediation.md#manage-resource-filters)). Resource filters require the Web UI or the MCP server. Alternatively, disable automated remediation for the control.
+  **Issue:** The solution deployment fails with an error stating that the resources are already available in Amazon CloudWatch.

   **Resolution:** Check for an error message in the CloudFormation resources/events section indicating log groups already exist. The ASR deployment templates allow reuse of existing log groups. Verify that you have selected reuse.
+  **Issue:** Solution fails to deploy with an error in a playbook nested stack where an EventBridge Rule fails to create

   **Resolution:** You have likely hit the [quota for EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-quota.html) with the number of playbooks deployed. You can avoid this by using [Consolidated control findings](deciding-where-to-deploy-each-stack.md#consolidated-controls-findings) in Security Hub paired with the SC playbook in this solution, deploy only the playbooks for the standards used, or requesting an increase to the EventBridge rules quota.
+  **Issue:** I run Security Hub in multiple Regions in the same account. I want to deploy this solution in multiple Regions.

   **Resolution:** Deploy the admin stack in the same account and Region as your Security Hub admin. Install the member template into each account and Region where you have a Security Hub member configured. Enable aggregation in the Security Hub.
+  **Issue:** Immediately after deploying, the **SO0111-ASR-Orchestrator** is failing in the Get Automation Document State with a 502 error: *"`Lambda was unable to decrypt the environment variables because KMS access was denied. Please check the function’s KMS key settings. KMS Exception: UnrecognizedClientExceptionKMS Message: The security token included in the request is invalid. (Service: AWSLambda; Status Code: 502; Error Code: KMSAccessDeniedException; Request ID: …​`"*

   **Resolution:** Allow the solution about 10 minutes to stabilize before running remediations. If the problem continues, open a support ticket or GitHub issue.
+  **Issue**: I attempted to remediate a finding but nothing happened.

   **Resolution:** Check the notes of the finding for reasons why it was not remediated. A common cause is that the finding has no automated remediation. At this time there is no way to provide direct feedback to the user when no remediation exists other than via the notes. Review the solution logs. Open CloudWatch Logs in the console. Find the SO0111-ASR CloudWatch Logs Group. Sort the list so the most-recently updated streams appear first. Select the log stream for the finding you attempted to run. You should find any errors there. Some reasons for the failure could be: mismatch between finding control and remediation control, the member stacks are not deployed in the finding’s account and Region, or that the finding has already been remediated. If unable to determine the reason for the failure, collect the logs and open a support ticket.
+  **Issue:** After starting a remediation, the status in the Security Hub console has not updated.

   **Resolution:** The Security Hub console does not update automatically. Refresh the current view. The status of the finding should update. It might take several hours for the finding to transition from **Failed** to **Passed**. Findings are created from event data sent by other services, such as AWS Config, to AWS Security Hub. The time before a rule is reevaluated depends on the underlying service. If this does not resolve the issue, refer to the preceding resolution for *"`I attempted to remediate a finding but nothing happened.`"*
+  **Issue**: Orchestrator step function fails in **Get Automation Document State**: *An error occurred (AccessDenied) when calling the AssumeRole operation*.

   **Resolution**: The member template has not been installed in the member account where ASR is attempting to remediate a finding. Follow instructions for deployment of the member template.
+  **Issue**: Config.1 runbook fails because Recorder or Delivery Channel already exists.

   **Resolution**: Inspect your AWS Config settings carefully to ensure Config is properly set up. The automated remediation is not able to fix existing AWS Config settings in some cases.
+  **Issue**: Remediation is successful but returns the message `"No output available yet because the step is not successfully executed."`

   **Resolution**: This is a known issue in this release where certain remediation runbooks do not return a response. The remediation runbooks will properly fail and signal the solution if they do not work.
+  **Issue**: The resolution failed and sent a stack trace.

   **Resolution**: Occasionally, we miss the opportunity to handle an error condition that results in a stack trace rather than an error message. Attempt to troubleshoot the problem from the trace data. Open a support ticket if you need assistance.
+  **Issue**: Removal of the v1.3.0 stack failed on the Custom Action resource.

   **Resolution**: Removal of the admin template may fail on the Custom Action removal. This is a known issue that will be fixed in the next release. If this occurs:

  1. Sign in to [AWS Security Hub management console](https://console.aws.amazon.com/securityhub/home).

  1. In the admin account, go to **Settings**.

  1. Select the **Custom actions** tab

  1. Manually delete the entry **Remediate with ASR**.

  1. Delete the stack again.
+  **Issue**: After redeploying the admin stack the step function is failing on `AssumeRole`.

   **Resolution**: Redeploying the admin stack breaks the trust connection between the admin role in the admin account and the member role in the member accounts. You must redeploy the member roles stack in all member accounts.
+  **Issue**: CIS 3.x remediations are not showing `PASSED` after more than 24 hours.

   **Resolution**: This is a common occurrence if you have no subscriptions to the `SO0111-ASR_LocalAlarmNotification` SNS topic in the member account.
