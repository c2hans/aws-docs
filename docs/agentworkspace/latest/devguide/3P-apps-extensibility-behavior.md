---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-extensibility-behavior.html
---

# Interceptor behavior in Connect Customer agent workspace
<a name="3P-apps-extensibility-behavior"></a>

The following rules describe how the framework evaluates interceptors at runtime:
+ **Thrown error** – If your interceptor throws an error, the framework catches it and allows the default action to proceed.
+ **Multiple interceptors** – When you register multiple interceptors for the same key, the framework evaluates all of them. If any interceptor returns `{ continue: false }`, the framework blocks the action.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
