---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/deploy-the-solution-in-tutorial.html
---

# Deploy the solution to tutorial accounts
<a name="deploy-the-solution-in-tutorial"></a>

Gather the three Amazon S3 URLs for the admin, member, and member roles stack.

## Deploy the admin stack
<a name="deploy-the-admin-stack"></a>

 [![Automated Security Response on AWS view main template button](http://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/automated-security-response-on-aws/latest/automated-security-response-admin.template) **automated-security-response-admin.template**

In the admin account, navigate to the [CloudFormation console](https://console.aws.amazon.com/cloudformation/) and deploy the admin stack into the Security Hub finding aggregation Region.

Choose `No` for the value of all parameters for loading nested admin stacks except for the "SC" or "Security Control" stack. This stack contains the resources for the consolidated control findings that we have configured in our accounts.

Choose `No` for reusing the orchestrator log group unless you have deployed this solution in this account and Region before.

| Account | Purpose | Action in us-east-1 | Action in us-west-2 |
| --- | --- | --- | --- |
|  `111111111111`  | Admin | Deploy the admin stack | None |
|  `222222222222`  | Member | None | None |

You should receive a `CREATE_COMPLETE` status in the AWS CloudFormation console.

Wait until the admin stack completes deployment before continuing so a trust relationship can be created from the member accounts to the admin account.

## Deploy the member stack
<a name="deploy-the-member-stack"></a>

 [![automated-security-response-member.template button](http://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/automated-security-response-on-aws/latest/automated-security-response-member.template) **automated-security-response-member.template**

In the admin account, navigate to the [CloudFormation StackSets console](https://console.aws.amazon.com/cloudformation/home#/stacksets) and deploy the member stack to each account and Region. Use the StackSets admin and execution roles created in this tutorial.

Enter the name of the log group you created as the value for the parameter for the log group name.

Choose `No` for the value of all parameters for loading nested member stacks except for the "SC" or "security control" stack. This stack contains the resources for the consolidated control findings that we have configured in our accounts.

Enter the ID of the admin account as the value for the parameter for the admin account number. In our example, this is `111111111111`.

| Account | Purpose | Action in us-east-1 | Action in us-west-2 |
| --- | --- | --- | --- |
|  `111111111111`  | Admin | Deploy the member StackSet / Confirm member stack deployed | Confirm member stack deployed |
|  `222222222222`  | Member | Confirm member stack deployed | Confirm member stack deployed |

You should receive a `CREATE_COMPLETE` status for each stack instance in the AWS CloudFormation StackSets console.

## Deploy the member roles stack
<a name="deploy-the-member-roles-stack"></a>

 [automated-security-response-member-roles.template button](https://solutions-reference.s3.amazonaws.com/automated-security-response-on-aws/latest/automated-security-response-member-roles.template) **automated-security-response-member-roles.template**

In the admin account, navigate to the [CloudFormation StackSets console](https://console.aws.amazon.com/cloudformation/home#/stacksets) and deploy the member stack to each account. Use the StackSets admin and execution roles created in this tutorial. Enter the ID of the admin account as the value for the parameter for the admin account number. In our example, this is `111111111111`.

| Account | Purpose | Action in us-east-1 | Action in us-west-2 |
| --- | --- | --- | --- |
|  `111111111111`  | Admin | Deploy the member StackSet / Confirm member stack deployed | None |
|  `222222222222`  | Member | Confirm member stack deployed | None |

You should receive a `CREATE_COMPLETE` status for each stack instance in the AWS CloudFormation StackSets console.

You can proceed, but you will be unable to remediate findings until CloudFormation StackSets finishes deploying.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Security Response on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
