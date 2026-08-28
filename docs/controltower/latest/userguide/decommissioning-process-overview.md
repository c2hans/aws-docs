---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/decommissioning-process-overview.html
---

# Overview of the decommissioning process
<a name="decommissioning-process-overview"></a>

When you request decommissioning of your landing zone, AWS Control Tower does the following actions.
+ Disables each detective control enabled in the landing zone. AWS Control Tower deletes the CloudFormation resources supporting the control.
+ Disables each preventive control by removing service control policies (SCPs) from AWS Organizations. If a policy is empty (which it should be after removing all SCPs managed by AWS Control Tower), AWS Control Tower detaches and deletes the policy entirely.
+ Deletes all blueprints deployed as CloudFormation StackSets.
+ Deletes all blueprints deployed as CloudFormation Stacks across all Regions.
+ For each provisioned account, AWS Control Tower does the following actions during the decommissioning process.
  + Deletes records of each account factory account.
  + Revokes the AWS Control Tower permissions to the account by removing the IAM role that AWS Control Tower created (unless additional policies have been added to it) and recreates the standard `OrganizationsFullAccessRole` IAM role.
  + Removes records of the account from AWS Service Catalog.
  + Removes the account factory product and portfolio from AWS Service Catalog.
+ Deletes the blueprints for the shared (Audit and Log Archive) accounts.
+ Revokes the AWS Control Tower permissions from the shared accounts by removing the IAM role that AWS Control Tower created (unless additional policies have been added to it) and recreates the `OrganizationsFullAccessRole` IAM role.
+ Deletes records related to the shared accounts.
+ Deletes records related to customer-created OUs.
+ Deletes internal records that identify the home Region.

**Note**
After decommissioning, you may wish to remove the Account Factory VPC blueprint (`BP_ACCOUNT_FACTORY_VPC`) to clean up the routes and NAT gateways, if your VPC was not empty.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
