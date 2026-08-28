---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/api-reference-3P-apps-contact-ui-client.html
---

# Connect Customer agent workspace Contact UI API
<a name="api-reference-3P-apps-contact-ui-client"></a>

With the Amazon Connect SDK, your app in the Connect Customer agent workspace can intercept contact-related UI actions by using the `ContactInterceptorService` in the `@amazon-connect/contact-ui` package. Use contact interceptors to override or augment built-in contact behaviors. For example, you can present a custom transfer UI instead of the default Quick Connect menu. You can also require agents to submit a disposition code before clearing a contact.

You can instantiate the contact interceptor service as follows:

```
import { ContactInterceptorService } from '@amazon-connect/contact-ui';

const service = new ContactInterceptorService(provider);
```

**Note**
The `provider` is your `AmazonConnectProvider` instance — the same provider you use to initialize other `@amazon-connect/*` packages.

The `ContactInterceptorService` provides action-specific methods that use the `ExtensibilityService` interceptor pipeline. Each method targets one contact UI action and provides the callback context as [ContactInterceptorContext in Connect Customer agent workspace](3P-apps-contact-interceptor-context.md). To learn how an interceptor allows or blocks a default action, see [Interceptor callback type in Connect Customer agent workspace](3P-apps-extensibility-interceptor-type.md).

To scope an interceptor to a single contact, pass its `contactId`. If you omit the `contactId`, the interceptor applies to all contacts.

**Topics**
+ [addOpenQuickConnectInterceptor()](3P-apps-contact-interceptor-add-quick-connect.md)
+ [removeOpenQuickConnectInterceptor()](3P-apps-contact-interceptor-remove-quick-connect.md)
+ [addOpenOutboundDialerInterceptor()](3P-apps-contact-interceptor-add-outbound-dialer.md)
+ [removeOpenOutboundDialerInterceptor()](3P-apps-contact-interceptor-remove-outbound-dialer.md)
+ [addClearContactInterceptor()](3P-apps-contact-interceptor-add-clear-contact.md)
+ [removeClearContactInterceptor()](3P-apps-contact-interceptor-remove-clear-contact.md)
+ [ContactInterceptorContext](3P-apps-contact-interceptor-context.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
