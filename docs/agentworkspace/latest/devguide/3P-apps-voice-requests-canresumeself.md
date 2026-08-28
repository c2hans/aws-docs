---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-canresumeself.html
---

# Check if the current user can be resumed from hold in Connect Customer agent workspace
<a name="3P-apps-voice-requests-canresumeself"></a>

Checks whether the current user's participant can be resumed from hold for a specific contact.

 **Signature**

```
canResumeSelf(contactId: string): Promise<boolean>
```

 **Usage**

```
const canResume = await voiceClient.canResumeSelf("contact-123");
if (canResume) {
  // Resume logic here
}
```

 **Input**

|  **Parameter**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| contactId Required | string | The unique identifier for the contact |

 **Output**

Returns a Promise that resolves to a boolean: true if the current user can be resumed, false otherwise

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
