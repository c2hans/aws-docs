---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-user-requests-getlanguage.html
---

# Get the language of a user in Connect Customer agent workspace
<a name="3P-apps-user-requests-getlanguage"></a>

Returns the language setting for the current user in the Connect Customer agent workspace.

```
async getLanguage(): Promise<Locale | null>
```

 **Permissions required:**

```
User.Configuration.View
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
