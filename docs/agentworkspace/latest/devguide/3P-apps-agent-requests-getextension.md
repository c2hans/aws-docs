---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-requests-getextension.html
---

# Get the extension of the agent in Connect Customer agent workspace
<a name="3P-apps-agent-requests-getextension"></a>

Returns phone number of the agent currently logged in to the Connect Customer agent workspace. This is the phone number that is dialed by the Connect Customer to connect calls to the agent for incoming and outgoing calls if soft phone is not enabled.

```
async getExtension(): Promise<string | null>
```

 **Permissions required:**

```
User.Configuration.View
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
