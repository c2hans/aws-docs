---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-requests-listsecurityprofilepermissions.html
---

# List the contact-handling security profile permissions for the agent in Connect Customer agent workspace
<a name="3P-apps-agent-requests-listsecurityprofilepermissions"></a>

Returns the list of contact-handling security profile permissions granted to the agent currently logged in to the Connect Customer agent workspace. Each permission is returned as a string identifier (for example, `outboundCall`, `outboundEmail`). Apps can use this to gate contact-handling functionality based on what the agent is authorized to do.

```
async listSecurityProfilePermissions(): Promise<string[]>
```

 **Permissions required:**

```
*
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
