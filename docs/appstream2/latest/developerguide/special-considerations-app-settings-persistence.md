---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/special-considerations-app-settings-persistence.html
---

# Special Considerations for Application Settings Persistence
<a name="special-considerations-app-settings-persistence"></a>

When you create a stack in the WorkSpaces Applications console, in **Step 3: User Settings**, if you use the same settings group under **Application settings persistence** as another stack that uses different regional settings, only one set of regional settings is used for both stacks. For each user, the default regional settings for the stack that the user logs into first automatically override the default regional settings of any other stacks in the same application settings group. To avoid this problem, do not use the same application settings group for two different stacks that have different regional settings.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
