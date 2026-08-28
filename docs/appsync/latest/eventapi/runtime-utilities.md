---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/runtime-utilities.html
---

# Runtime utilities
<a name="runtime-utilities"></a>

The runtime library provides utilities to control or modify the runtime properties of your handlers and functions.

Invoking the following function stops the execution of the current handler (AWS AppSync Events API) and returns the specified object as the result.

**`runtime.earlyReturn(obj?: unknown): never`**

When this function is called in an AWS AppSync Events handler, the data source and response function are skipped.

```
import * as ddb from '@aws-appsync/utils/dynamodb';

export const onPublish = {
  request(ctx) {
    if (condition === true) {
      return runtime.earlyReturn(ctx.events)
    }
    // never executed if `condition` is true
    return ddb.batchPut({
      tables: {
        messages: ctx.events.map(({ id, payload }) => ({
          channel: ctx.info.channelNamespace.name,
          id,
          ...payload
        })),
      }
    });
  },
  // never called if `condition` was true
  response: (ctx) => ctx.events
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
