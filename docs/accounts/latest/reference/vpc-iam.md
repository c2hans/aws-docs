---
source_url: https://docs.aws.amazon.com/accounts/latest/reference/vpc-iam.html
---

# Amazon Virtual Private Cloud endpoint policies for Account Management
<a name="vpc-iam"></a>

The following information is relevant for all AWS accounts.

You can create a Amazon VPC endpoint policy for Account Management in which you specify the following:
+ The principal that can perform actions.
+ The actions that the principals can perform.
+ The resources on which the actions can be performed.

The following example shows an Amazon VPC endpoint policy that allows one IAM user named Alice in account 123456789012 to both retrieve and change the alternate contact information for any AWS account, but denies all IAM users permission to delete any alternate contact information on any account.

If you want to grant access to accounts that are part of an AWS Organization to a principal that is in one of the organization's member accounts, then the `Resource` element must use the following format:

```
arn:aws:account::{{{ManagementAccountId}}}:account/{{o-{OrganizationId}}}/{{{AccountId}}}
```

For more information about creating endpoint policies, see [Controlling Access to Services with VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *AWS PrivateLink Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Account Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query accounts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
