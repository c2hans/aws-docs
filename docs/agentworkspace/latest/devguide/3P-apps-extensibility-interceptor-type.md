---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-extensibility-interceptor-type.html
---

# Interceptor callback type in Connect Customer agent workspace
<a name="3P-apps-extensibility-interceptor-type"></a>

Defines the callback signature and return value for an interceptor. An interceptor receives a context object and returns a result that indicates whether the action proceeds.

 **Signature**

```
type Interceptor<T> = (context: T) => Promise<InterceptorResult>

type InterceptorResult = boolean | { continue: boolean }
```

 **Context**

For the currently supported interceptor keys, the context object is:

```
{ contactId?: string }
```

 **Return value**

The following table describes the return values.

| **Return value** | **Shorthand** | **Effect** |
| --- | --- | --- |
| { continue: true } | true | Allow the default action to proceed. |
| { continue: false } | false | Block the default action. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
