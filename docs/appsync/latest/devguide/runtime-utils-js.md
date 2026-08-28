---
source_url: https://docs.aws.amazon.com/appsync/latest/devguide/runtime-utils-js.html
---

# Runtime utilities
<a name="runtime-utils-js"></a>

The `runtime` library provides utilities to control or modify the runtime properties of your resolvers and functions.

## Runtime utils list
<a name="runtime-utils-list-js"></a>

 **`runtime.earlyReturn(obj?: unknown, returnOptions?: {skipTo: 'END' | 'NEXT'}): never`**
Invoking this function will halt the execution of the current handler, AWS AppSync function or resolver (Unit or Pipeline Resolver) depending on the current context. The specified object is returned as the result.
+ When called in an AWS AppSync function request handler, the data source and response handler are skipped, and the next function request handler (or the pipeline resolver response handler if this was the last AWS AppSync function) is called.
+ When called in an AWS AppSync pipeline resolver request handler, the pipeline execution is skipped, and the pipeline resolver response handler is called immediately.
+ When `returnOptions` is given with `skipTo` set to "END", the pipeline execution is skipped, and the pipeline resolver response handler is called immediately.
+ When `returnOptions` is given with `skipTo` set to "NEXT", the function execution is skipped, and the next pipeline handler is called.
**Example**

```
import { runtime } from '@aws-appsync/utils'

export function request(ctx) {
  runtime.earlyReturn({ hello: 'world' })
  // code below is not executed
  return ctx.args
}

// never called because request returned early
export function response(ctx) {
  return ctx.result
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
