---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/enabling-and-disabling-parts-of-solution.html
---

# Enabling and disabling parts of the solution
<a name="enabling-and-disabling-parts-of-solution"></a>

As a solution administrator, you have the following controls over which functionalities of the solution are enabled.

 **Where the member and member roles stacks are deployed:**
+ The admin stack will only be able to initiate remediations (through custom action or fully automated) in accounts in which the member and member roles stacks have been deployed with the admin account number given as a parameter value.
+ To exempt accounts or Regions from control of the solution completely, do not deploy the member or member roles stacks to those accounts or Regions.

 **Account and Region finding aggregation configuration in Security Hub:**
+ The admin stack will only be able to initiate remediations (through custom action or fully automated) for findings which arrive in the admin account and Region.
+ To exempt accounts or Regions from control of the solution completely, do not include those accounts or Regions to send findings to the same admin account and Region in which the admin stack is deployed.

 **Which standard nested stacks are deployed:**
+ The admin stack will only be able to initiate remediations (through custom action or fully automated) for controls which have a control runbook deployed in the target member account and Region. These are deployed by the member stack for each standard.
+ The admin stack can initiate fully automated remediations only for controls that are enabled in the Remediation Configuration Amazon DynamoDB table. This table is deployed to the admin account.
+ For simplicity, deploy standards consistently across your admin and member accounts. If you care about AWS FSBP and CIS v1.2.0, deploy those two nested admin stacks to the admin account, and deploy those two nested member stacks to each member account and Region.

 **Which Control runbooks are deployed in each nested member stack:**
+ The admin stack will only be able to initiate remediations (through custom action or fully automated) for controls which have a control runbook deployed in the target member account and Region by the member stack for each standard.
+ To exercise more fine-grained control over which controls are enabled for a particular standard, each nested stack for a standard has parameters for which control runbooks are deployed. Set the parameter for a control to the value "NOT Available" to undeploy that control runbook.

 **SSM Parameters for enabling and disabling standards:**
+ The admin stack will only be able to initiate remediations (through custom action or fully automated) for standards that are enabled through the SSM Parameter deployed by the standard admin stack.
+ To disable a standard, set the value for the SSM Parameter with the path "/Solutions/SO0111/<standard\_name>/<standard\_version>/status" to "No".

 **Which controls have fully-automated remediation enabled:**

The solution offers two ways to enable or disable fully-automated remediation. Both write to the same Remediation Configuration Amazon DynamoDB table in the admin account, so they stay in sync.
+  **Web UI (recommended when deployed).** Manage fully-automated remediation from the **Controls** page. Admins and delegated admins can enable or disable automated remediation per control, and apply reusable resource filters to scope which findings are acted on. To turn off automated remediation for all controls at once — for example, during an incident, choose **Disable All Automated Remediations**. This button is unavailable to account operators (read-only) and when automated remediation is already off for all controls. For details, see [Manage automated remediation](manage-automated-remediation.md).
+  **Legacy configuration (no Web UI).** If you did not deploy the Web UI, enable or disable fully-automated remediation by editing the items in the Remediation Configuration DynamoDB table directly, and scope which findings are remediated with the AWS Systems Manager filter parameters. For the steps, see [Enable fully-automated remediations](enable-fully-automated-remediations.md). To quickly disable automated remediation during an incident without the Web UI, see the disable scenarios in [Troubleshooting](troubleshooting.md).

 **Access to the solution’s Web UI:**
+ When the Admin stack is deployed, you receive an email with temporary credentials to sign in to the Web UI using the email address you provided during deployment.
+ Using the **Invite Users** page, administrators and delegated administrators can invite additional users to access the Web UI and delegate access to the solution.
+ Using the **View Users** page, administrators and delegated administrators can view and manage existing users.
+ To learn more about permissions and how to use the solution’s Web UI, see the [Web UI](webui-developer-guide.md).
