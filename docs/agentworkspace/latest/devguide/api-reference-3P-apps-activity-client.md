---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/api-reference-3P-apps-activity-client.html
---

# Connect Customer agent workspace Activity API
<a name="api-reference-3P-apps-activity-client"></a>

The Amazon Connect SDK provides a `SessionExpirationWarningClient` which serves as an interface that your app in the Connect Customer agent workspace can use to subscribe to events related to session expiration due to inactivity and to signal the Connect Customer that the agent is active.

The `SessionExpirationWarningClient` accepts an optional constructor argument, ` ConnectClientConfig` which itself is defined as:

```
export type ConnectClientConfig = {
    context?: ModuleContext;
    provider?: AmazonConnectProvider;
};
```

If you do not provide a value for this config, then the client will default to using the **AmazonConnectProvider** set in the global provider scope. You can also manually configure this using **setGlobalProvider**.

You can instantiate the client as follows:

```
import { SessionExpirationWarningClient } from "@amazon-connect/activity";

const sessionExpirationWarningClient = new SessionExpirationWarningClient();
```

**Note**
You must first instantiate the [ AmazonConnectApp](getting-started-initialize-sdk.md) which initializes the default AmazonConnectProvider and returns ` { provider } `. This is the recommended option.

Alternatively, you can provide a constructor argument:

```
import { SessionExpirationWarningClient } from "@amazon-connect/activity";

const sessionExpirationWarningClient = new SessionExpirationWarningClient({
    context: sampleContext,
    provider: sampleProvider
});
```

The following sections describe the API calls for working with the SessionExpirationWarning API.

**Topics**
+ [onExpirationWarning()](3P-apps-activity-offexpirationwarning.md)
+ [offExpirationWarningCleared()](3P-apps-activity-offexpirationwarningcleared.md)
+ [offSessionExtensionError()](3P-apps-activity-offsessionextensionerror.md)
+ [onExpirationWarning()](3P-apps-activity-onexpirationwarning.md)
+ [onExpirationWarningCleared()](3P-apps-activity-onexpirationwarningcleared.md)
+ [onSessionExtensionError()](3P-apps-activity-onsessionextensionerror.md)
+ [sendActivity()](3P-apps-activity-sendactivity.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
