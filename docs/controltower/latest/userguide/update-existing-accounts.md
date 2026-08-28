---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/update-existing-accounts.html
---

# When to update AWS Control Tower OUs and accounts
<a name="update-existing-accounts"></a>

When you perform a landing zone update, you must update your enrolled accounts to apply new controls to those accounts.
+ You can perform an update to all accounts under an OU using the Re-Register or Reset option.
+ If you have more than one registered OU in your landing zone, re-register or reset all of your OUs to update all of your accounts.
+ To update a single account, you can update from the AWS Control Tower console, or you can select the **Update provisioned product** option in AWS Service Catalog if AWSControlTowerBaseline is enabled on the account. See [Update the account in the console](updating-account-factory-accounts.md#update-account-in-console).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
