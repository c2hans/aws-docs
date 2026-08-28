---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-interceptor-remove-quick-connect.html
---

# Unregister a Quick Connect interceptor in Connect Customer agent workspace
<a name="3P-apps-contact-interceptor-remove-quick-connect"></a>

Unregisters an interceptor that you registered with `addOpenQuickConnectInterceptor`. Pass the same interceptor reference and the same `contactId` that you used at registration.

**Signature**

```
removeOpenQuickConnectInterceptor(
  interceptor: Interceptor<ContactInterceptorContext>,
  contactId?: string
): Promise<void>
```

**Usage**

```
await service.removeOpenQuickConnectInterceptor(myInterceptor);

// If scoped to a contact, pass the same contactId
await service.removeOpenQuickConnectInterceptor(myInterceptor, contactId);
```

**Input**

The following table describes the input parameters.

| **Parameter** | **Type** | **Description** |
| --- | --- | --- |
| interceptor Required | Interceptor<ContactInterceptorContext> | The same function reference that you passed to addOpenQuickConnectInterceptor. |
| contactId Optional | string | The contact ID that the interceptor was scoped to. Pass the same value that you used at registration. If you omit this value, the framework removes the interceptor that applies to all contacts. |

**Output**

`Promise<void>`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
