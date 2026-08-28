---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-activity-sendactivity.html
---

# Inform Connect Customer that the agent is active
<a name="3P-apps-activity-sendactivity"></a>

Sends a signal to the Connect Customer indicating that the agent is active and should not be logged out. It takes a provider as a parameter.

 **Signature**

```
sendActivity(provider): void
```

 **Usage**

```
import { sendActivity } from '@amazon-connect/activity';

const handleActivity = () => {
   sendActivity(sampleProvider);
};

window.addEventListener("click", handleActivity);
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
