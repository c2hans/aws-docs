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
