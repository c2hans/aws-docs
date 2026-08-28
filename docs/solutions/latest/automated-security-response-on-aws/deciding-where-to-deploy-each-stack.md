---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/deciding-where-to-deploy-each-stack.html
---

# Deciding where to deploy each stack
<a name="deciding-where-to-deploy-each-stack"></a>

The three templates will be referred to by the following names and contain the following resources:
+ Admin stack: orchestrator step function, event rules and Security Hub custom action.
+ Member stack: remediation SSM Automation documents.
+ Member roles stack: IAM roles for remediations.

The Admin stack must be deployed once, in a single account and a single Region. It must be deployed into the account and Region that you have configured as the aggregation destination for Security Hub findings for your organization. If you wish to use the Action Log feature to monitor management events, you must deploy the Admin stack in your organization’s management account or a delegated administrator account.

The solution operates on Security Hub findings, so it will not be able to operate on findings from a particular account and Region if that account or Region has not been configured to aggregate findings in the Security Hub administrator account and Region.

**Important**
If you are using [AWS Security Hub (non-CSPM)](https://aws.amazon.com/security-hub/) then you are responsible for ensuring your member accounts onboarded with [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) are also onboarded with AWS Security Hub (non-CSPM). Regions aggregated in AWS Security Hub CSPM should also match regions aggregated in AWS Security Hub (non-CSPM).

For example, an organization has accounts operating in Regions `us-east-1` and `us-west-2`, with account `111111111111` as the Security Hub delegated administrator in Region `us-east-1`. Accounts `222222222222` and `333333333333` must be Security Hub member accounts for the delegated administrator account `111111111111`. All three accounts must be configured to aggregate findings from `us-west-2` to `us-east-1`. The Admin stack must be deployed to account `111111111111` in `us-east-1`.

For more details on finding aggregation, consult the documentation for Security Hub [delegated administrator accounts](https://docs.aws.amazon.com/securityhub/latest/userguide/designate-orgs-admin-account.html) and [cross-Region aggregation](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation.html).

The Admin stack must complete deployment first before deploying the member stacks so that a trust relationship can be created from the member accounts to the hub account.

The member stack must be deployed into every account and Region in which you wish to remediate findings. This can include the Security Hub delegated administrator account in which you previously deployed the ASR Admin stack.The automation documents must execute in the member accounts in order to use the free tier for SSM Automation.

Using the previous example, if you want to remediate findings from all accounts and Regions, the member stack must be deployed to all three accounts (`111111111111`, `222222222222`, and `333333333333`) and both Regions (`us-east-1` and `us-west-2`).

The member roles stack must be deployed to every account, but it contains global resources (IAM roles) that can only be deployed once for each account. It does not matter in which Region you deploy the member roles stack, so for simplicity, deploy the member roles stack to the same Region in which the Admin stack is deployed.

Using the previous example, deploy the member roles stack to all three accounts (`111111111111`, `222222222222`, and `333333333333`) in `us-east-1`.

## Deciding how to deploy each stack
<a name="deciding-how-to-deploy-each-stack"></a>

The options for deploying a stack are
+ CloudFormation StackSet (self-managed permissions)
+ CloudFormation StackSet (service-managed permissions)
+ CloudFormation Stack

StackSets with service-managed permissions are the most convenient because they do not require deploying your own roles and can automatically deploy to new accounts in the organization. Unfortunately, this method does not support nested stacks, used in both the Admin stack and the member stack. The only stack that can be deployed this way is the member roles stack.

Be aware that when deploying to the entire organization, the organization management account is not included, so if you want to remediate findings in the organization management account, you must deploy to this account separately.

The member stack must be deployed to every account and Region but cannot be deployed using StackSets with service-managed permissions because it contains nested stacks. Deploy this stack with StackSets with self-managed permissions.

The Admin stack is only deployed once, so it can be deployed as a plain CloudFormation stack or as a StackSet with self-managed permissions in a single account and Region.

## Consolidated control findings
<a name="consolidated-controls-findings"></a>

The accounts in your organization can be configured with the consolidated control findings feature of Security Hub turned on or off. See [Consolidated control findings](https://docs.aws.amazon.com/securityhub/latest/userguide/controls-findings-create-update.html#consolidated-control-findings) in the *AWS Security Hub User Guide*.

**Important**
When this feature is enabled, you must use solution version 2.0.0 or later and enable the "SC" (Security Control) playbook in both the Admin and Member stacks. These stacks deploy the automation documents needed to work with consolidated control IDs. You do not need to deploy stacks for individual standards (such as AWS FSBP) when using consolidated control findings.

## China deployment
<a name="china-deployment"></a>

The solution does support deployment in China regions, however **you must use the following Launch buttons for one-click deployment in China regions, rather than the Launch buttons provided in other sections of this guide.** Using the "Launch Solution" buttons provided in upcoming sections in this guide will not work if you are deploying in China regions. You can still download the templates from any S3 bucket link and deploy the stacks by uploading the template file.
+  **automated-security-response-admin.template**:

 [![automated-security-response-admin-template launch button](http://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/launch-button.png)](https://cn-north-1.console.amazonaws.cn/cloudformation/home?region=cn-north-1#/stacks/new?stackName=automated-security-response-on-aws-admin&templateURL=https:%2F%2Fs3.cn-north-1.amazonaws.com.cn%2Fsolutions-reference-cn%2Fautomated-security-response-on-aws%2Flatest%2Fautomated-security-response-admin.template&redirectId=ImplementationGuide)
+  **automated-security-response-member-roles.template**:

 [![automated-security-response-member-roles-template launch button](http://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/launch-button.png)](https://cn-north-1.console.amazonaws.cn/cloudformation/home?region=cn-north-1#/stacks/new?stackName=automated-security-response-on-aws-member-roles&templateURL=https:%2F%2Fs3.cn-north-1.amazonaws.com.cn%2Fsolutions-reference-cn%2Fautomated-security-response-on-aws%2Flatest%2Fautomated-security-response-member-roles.template&redirectId=ImplementationGuide)
+  **automated-security-response-member.template**:

 [![automated-security-response-member-template launch button](http://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/launch-button.png)](https://cn-north-1.console.amazonaws.cn/cloudformation/home?region=cn-north-1#/stacks/new?stackName=automated-security-response-on-aws-member&templateURL=https:%2F%2Fs3.cn-north-1.amazonaws.com.cn%2Fsolutions-reference-cn%2Fautomated-security-response-on-aws%2Flatest%2Fautomated-security-response-member.template&redirectId=ImplementationGuide)

## GovCloud (US) deployment
<a name="govcloud-deployment"></a>

The solution does support deployment in GovCloud (US) regions, however **you must use the following Launch buttons for one-click deployment in GovCloud (US) regions, rather than the Launch buttons provided in other sections of this guide.** Using the "Launch Solution" buttons provided in upcoming sections in this guide will not work if you are deploying in GovCloud (US) regions. You can still download the templates from any S3 bucket link and deploy the stacks by uploading the template file.
+  **automated-security-response-admin.template**:

 [![automated-security-response-admin-template launch button](http://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/launch-button.png)](https://console.amazonaws-us-gov.com/cloudformation/home?region=us-gov-west-1#/stacks/new?stackName=automated-security-response-on-aws-admin&templateURL=https:%2F%2Fs3.us-gov-west-1.amazonaws.com%2Fsolutions-reference-us-gov%2Fautomated-security-response-on-aws%2Flatest%2Fautomated-security-response-admin.template&redirectId=ImplementationGuide)
+  **automated-security-response-member-roles.template**:

 [![automated-security-response-member-roles-template launch button](http://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/launch-button.png)](https://console.amazonaws-us-gov.com/cloudformation/home?region=us-gov-west-1#/stacks/new?stackName=automated-security-response-on-aws-member-roles&templateURL=https:%2F%2Fs3.us-gov-west-1.amazonaws.com%2Fsolutions-reference-us-gov%2Fautomated-security-response-on-aws%2Flatest%2Fautomated-security-response-member-roles.template&redirectId=ImplementationGuide)
+  **automated-security-response-member.template**:

 [![automated-security-response-member-template launch button](http://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/launch-button.png)](https://console.amazonaws-us-gov.com/cloudformation/home?region=us-gov-west-1#/stacks/new?stackName=automated-security-response-on-aws-member&templateURL=https:%2F%2Fs3.us-gov-west-1.amazonaws.com%2Fsolutions-reference-us-gov%2Fautomated-security-response-on-aws%2Flatest%2Fautomated-security-response-member.template&redirectId=ImplementationGuide)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Security Response on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
