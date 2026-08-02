---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/logging-sdk-calls.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# Logging AWS SDK for JavaScript Calls
<a name="logging-sdk-calls"></a>

The AWS SDK for JavaScript is instrumented with a built-in logger so you can log API calls you make with the SDK for JavaScript.

To turn on the logger and print log entries in the console, configure the service client using the optional `logger` parameter. The example below enables client logging while ignoring trace and debug outputs.

```
new S3Client({
  logger: {
    ...console,
    debug(...args) {},
    trace(...args) {},
  },
});
```

## Using middleware to log requests
<a name="middleware-logger"></a>

The AWS SDK for JavaScript uses a middleware stack to control the lifecycle of an operation call. Each middleware in the stack calls the next middleware after making any changes to the request object. This also makes debugging issues in the stack much easier since you can see exactly which middleware have been called leading up to an error. Here is an example of logging requests using middleware:

```
const client = new DynamoDB({ region: "us-west-2" });

client.middlewareStack.add(
  (next, context) => async (args) => {
    console.log("AWS SDK context", context.clientName, context.commandName);
    console.log("AWS SDK request input", args.input);
    const result = await next(args);
    console.log("AWS SDK request output:", result.output);
    return result;
  },
  {
    name: "MyMiddleware",
    step: "build",
    override: true,
  }
);

await client.listTables({});
```

In the example above, a middleware is added to the DynamoDB client’s middleware stack. The first argument is a function that accepts `next`, the next middleware in the stack to call, and `context`, an object that contains some information about the operation being called. It returns a function that accepts `args`, an object that contains the parameters passed to the operation and the request, and it returns the result from calling the next middleware with `args`.
