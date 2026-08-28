---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-user-requests-getinstanceid.html
---

# Get the instance ID of the current Connect Customer instance in Connect Customer agent workspace
<a name="3P-apps-user-requests-getinstanceid"></a>

Returns the Connect Customer instance ID associated with the user that's currently logged in to the Connect Customer agent workspace.

```
async getInstanceId(): Promise<string>
```

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
