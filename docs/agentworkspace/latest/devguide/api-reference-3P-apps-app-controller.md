---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/api-reference-3P-apps-app-controller.html
---

# Connect Customer agent workspace AppController API
<a name="api-reference-3P-apps-app-controller"></a>

The Amazon Connect SDK provides an `AppControllerClient` to control applications in the Connect Customer agent workspace.

The `AppControllerClient` accepts an optional argument, ` ConnectClientConfig` which itself is defined as:

```
export type ConnectClientConfig = {
    context?: ModuleContext;
    provider?: AmazonConnectProvider;
};
```

If you do not provide a value for this config, then the client will default to using the ** AmazonConnectProvider** set in the global provider scope. You can also manually configure this using **setGlobalProvider**.

You can instantiate the AppControllerClient as follows:

```
import { AppControllerClient } from "@amazon-connect/app-controller";

const appControllerClient = new AppControllerClient({ provider });
```

The following sections describe API calls for working with the App Controller API.

**Topics**
+ [closeApp()](api-reference-3P-apps-app-controller-closeapp.md)
+ [focusApp()](api-reference-3P-apps-app-controller-focusapp.md)
+ [getApp()](api-reference-3P-apps-app-controller-getapp.md)
+ [getAppCatalog()](api-reference-3P-apps-app-controller-getappcatalog.md)
+ [getAppConfig()](api-reference-3P-apps-app-controller-getappconfig.md)
+ [getApps()](api-reference-3P-apps-app-controller-getapps.md)
+ [launchApp()](api-reference-3P-apps-app-controller-launchapp.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
