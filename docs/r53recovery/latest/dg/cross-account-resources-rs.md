---
source_url: https://docs.aws.amazon.com/r53recovery/latest/dg/cross-account-resources-rs.html
---

# Cross-account support in Region switch
<a name="cross-account-resources-rs"></a>

In Region switch, you can add resources from other accounts to your plans. You can also share a Region switch plan with other accounts. For more information, see the following sections.

## Cross-account resources
<a name="cross-account-resources-rs-in-plan"></a>

Region switch allows resources to be hosted in an account that is separate from the account that contains the Region switch plan. When Region switch executes a plan, it assumes the executionRole. If the plan uses resources from an account that is different than the account that hosts the plan, then Region switch uses the executionRole to assume the crossAccountRole to access those resources.

Each resource in the Region switch plan has two optional fields: crossAccountRole and externalId.
+ crossAccountRole: This role allows access to resources in an account that is different than the account that hosts the Region switch plan. The role only needs permissions to act on the resources within its account – it does not need permissions to act on the resources in the account that hosts the Region switch plan.
+ ExternalId: This is the STS external ID from the trust policy of the account that contains the resource that requires action. It is an alphanumeric string that is the shared secret between the two accounts.

## Sharing Region switch plans
<a name="sharing-plans"></a>

Region switch integrates with AWS Resource Access Manager (AWS RAM) to allow you to share plans across AWS accounts. When you share a plan, accounts that you specify can view the plan details, execute the plan, and view the plan's executions, which provides more control and flexibility for recovery capabilities across different teams.

To get started with cross-account sharing in Region switch, you create a resource share in AWS RAM. The resource share specifies participants who are authorized to share the plan that your account owns. Participants can view and execute the shared plan through the console, the CLI, or AWS SDKs.

Important: Your AWS account must own the plans that you want to share. You cannot share a plan that has been shared with you. To share a plan with your organization, or with an organizational unit in AWS Organizations, you must enable sharing with Organizations.

For more information about AWS RAM, see [Support sharing plans across accounts for ARC Region switch](resource-sharing.region-switch.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query r53recovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
