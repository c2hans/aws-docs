---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-interceptor-context.html
---

# ContactInterceptorContext in Connect Customer agent workspace
<a name="3P-apps-contact-interceptor-context"></a>

Defines the invocation context that the contact interceptor methods receive.

**Signature**

```
type ContactInterceptorContext = {
  contactId?: string;
}
```

**Properties**

The following table describes the properties.

| **Property** | **Type** | **Description** |
| --- | --- | --- |
| contactId Optional | string | The identifier of the contact that triggered the action. The service omits this value when no specific contact initiated the action. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
