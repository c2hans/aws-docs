---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/enabling-and-diabling-parts-of-solution.html
---

# Enabling and disabling parts of the solution
<a name="enabling-and-diabling-parts-of-solution"></a>

As a solution administrator, you have the following controls over which functionalities of the solution are enabled.

 **Where the member and member roles stacks are deployed:**
+ The admin stack will only be able to initiate remediations (through custom action or fully automated) in accounts in which the member and member roles stacks have been deployed with the admin account number given as a parameter value.
+ To exempt accounts or Regions from control of the solution completely, do not deploy the member or member roles stacks to those accounts or Regions.

 **Account and Region finding aggregation configuration in Security Hub:**
+ The admin stack will only be able to initiate remediations (through custom action or fully automated) for findings which arrive in the admin account and Region.
+ To exempt accounts or Regions from control of the solution completely, do not include those accounts or Regions to send findings to the same admin account and Region in which the admin stack is deployed.

 **Which standard nested stacks are deployed:**
+ The admin stack will only be able to initiate remediations (through custom action or fully automated) for controls which have a control runbook deployed in the target member account and Region. These are deployed by the member stack for each standard.
+ The admin stack will only be able to initiate fully automated remediations for controls that are enabled in the Remediation Configuratio DynamoDB table. This table is deployed to the admin account.
+ For simplicity, we recommend deploying standards consistently across your admin and member accounts. If you care about AWS FSBP and CIS v1.2.0, deploy those two nested admin stacks to the admin account, and deploy those two nested member stacks to each member account and Region.

 **Which Control runbooks are deployed in each nested member stack:**
+ The admin stack will only be able to initiate remediations (through custom action or fully automated) for controls which have a control runbook deployed in the target member account and Region by the member stack for each standard.
+ To exercise more fine-grained control over which controls are enabled for a particular standard, each nested stack for a standard has parameters for which control runbooks are deployed. Set the parameter for a control to the value "NOT Available" to undeploy that control runbook.

 **SSM Parameters for enabling and disabling standards:**
+ The admin stack will only be able to initiate remediations (through custom action or fully automated) for standards that are enabled through the SSM Parameter deployed by the standard admin stack.
+ To disable a standard, set the value for the SSM Parameter with the path "/Solutions/SO0111/<standard\_name>/<standard\_version>/status" to "No".

 **Access to the solution’s Web UI:**
+ When the Admin stack is deployed, you will receive an email with temporary credentials to sign in to the Web UI using the email address you provided during deployment.
+ Using the **Invite Users** page, administrators and delegated administrators can invite additional users to access the Web UI and delegate access to the solution.
+ Using the **View Users** page, administrators and delegated administrators can view and manage existing users.
+ To learn more about permissions and how to use the solution’s Web UI, see the [Web UI](webui-developer-guide.md).
