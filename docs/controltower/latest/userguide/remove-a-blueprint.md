---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/remove-a-blueprint.html
---

# Remove a blueprint from an account
<a name="remove-a-blueprint"></a>

To remove a blueprint from an account, follow the **Update account** workflow to remove the blueprint and return the account to the AWS Control Tower default configurations.

As you enter the **Update account** workflow in the console, you will see that all of the account details are populated, and the customization details are not populated. If you leave these AFC details blank, AWS Control Tower removes the blueprint from the account. You will see a warning message before the action begins.

**Note**
AWS Control Tower adds a blueprint to an account only if you select a blueprint during the **Create account** or **Update account** process.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
