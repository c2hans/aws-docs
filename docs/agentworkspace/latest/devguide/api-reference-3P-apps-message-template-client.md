---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/api-reference-3P-apps-message-template-client.html
---

# Connect Customer agent workspace Message Template API
<a name="api-reference-3P-apps-message-template-client"></a>

The Amazon Connect SDK provides a `MessageTemplateClient` which serves as an interface that you can use to make requests to search and get content from your Amazon Connect Message Template Knowledge Base.

The `MessageTemplateClient` accepts an optional constructor argument, ` ConnectClientConfig` which itself is defined as:

```
export type ConnectClientConfig = {
    context?: ModuleContext;
    provider?: AmazonConnectProvider;
};
```

If you do not provide a value for this config, then the client will default to using the ** AmazonConnectProvider** set in the global provider scope. You can also manually configure this using **setGlobalProvider**.

You can instantiate the agent client as follows:

```
import { MessageTemplateClient } from "@amazon-connect/message-template";

const messageTemplateClient = new MessageTemplateClient({ provider });
```

**Note**
You must first instantiate the [ AmazonConnectApp](getting-started-initialize-sdk.md) which initializes the default AmazonConnectProvider and returns ` { provider } `. This is the recommended option.

Alternatively, providing a constructor argument:

```
import { MessageTemplateClient } from "@amazon-connect/message-template";

const messageTemplateClient = new MessageTemplateClient({
    context: sampleContext,
    provider: sampleProvider
});
```

**Note**
Third-party applications must be configured with \* permission in order to utilize the MessageTemplateClient APIs.

The following sections describe API calls for working with the MessageTemplate API.

**Topics**
+ [getContent()](3P-apps-message-template-requests-getcontent.md)
+ [isEnabled()](3P-apps-message-template-requests-isenabled.md)
+ [searchMessageTemplates()](3P-apps-message-template-requests-searchmessagetemplates.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
