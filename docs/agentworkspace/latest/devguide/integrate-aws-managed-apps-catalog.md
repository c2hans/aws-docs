---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/integrate-aws-managed-apps-catalog.html
---

# Retrieve available applications
<a name="integrate-aws-managed-apps-catalog"></a>

The `getAppCatalog` method retrieves applications available to the authenticated user. AppManager filters the list based on the user's Security Profile permissions. Use this method to verify if user has permission for the AWS-managed application prior to launching.

```
import { AppConfig } from "@amazon-connect/workspace-types";

// Retrieve applications filtered by Security Profile permissions
const applications: AppConfig[] = await appManager.getAppCatalog();
```

 **Application configuration properties:**

Each `AppConfig` object contains the following properties:
+ `arn` - Amazon Resource Name (ARN) that uniquely identifies the application
+ `name` - Display name for the application

**Note**
This is not required if you know the name of the AWS-managed application that you want to launch and the user is guaranteed to have access.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
