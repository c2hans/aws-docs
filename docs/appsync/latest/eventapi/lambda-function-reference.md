---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/lambda-function-reference.html
---

# AWS AppSync JavaScript function reference for Lambda
<a name="lambda-function-reference"></a>

You can use AWS AppSync integration for AWS Lambda to invoke Lambda functions located in your account. You can shape your request payloads and the response from your Lambda functions before returning them to your clients. You can also specify the type of operation to perform in your request object. This section describes the requests for the supported Lambda operations.

## Request object
<a name="request-object-js"></a>

The Lambda request object handles fields related to your Lambda function:

```
export type LambdaRequest = {
  operation: 'Invoke';
  invocationType?: 'RequestResponse' | 'Event';
  payload: unknown;
};
```

The following example uses an `invoke` operation with its payload data being a field, along with its arguments from the context:

```
export const onPublish = {
  request(ctx) {
    return {
      operation: 'Invoke',
      payload: { field: 'getPost', arguments: ctx.args },
    };
  }
}
```

### Operation
<a name="operation-js"></a>

When doing an `Invoke`, the resolved request matches the input payload of the *Lambda* function. The following example modifies the previous example:

```
export const onPublish = {
  request(ctx) {
    return {
      operation: 'Invoke',
      payload: ctx // send the entire context to the Lambda function
    };
  }
}
```

### Payload
<a name="payload-js"></a>

The `payload` field is a container used to pass any data to the Lambda function. The `payload` field is optional.

### Invocation type
<a name="async-invocation-type-js"></a>

The Lambda data source allows you to define two invocation types: `RequestResponse` and `Event`. The invocation types are synonymous with the invocation types defined in the [Lambda API](https://docs.aws.amazon.com/lambda/latest/api/API_Invoke.html). The `RequestResponse` invocation type lets AWS AppSync call your Lambda function synchronously to wait for a response. The `Event` invocation allows you to invoke your Lambda function asynchronously. For more information on how Lambda handles `Event` invocation type requests, see [Asynchronous invocation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html). The `invocationType` field is optional. If this field is not included in the request, AWS AppSync will default to the `RequestResponse` invocation type.

For any `invocationType` field, the resolved request matches the input payload of the Lambda function. The following example modifies the previous example:

```
export const onPublish = {
  request(ctx) {
     return {
       operation:  'Invoke',
       invocationType:  'Event',
       payload: ctx
    };
  }
}
```

## Response object
<a name="response-object-js"></a>

As with other data sources, your Lambda function sends a response to AWS AppSync that must be processed. The result of the Lambda function is contained in the `context` result property (`context.result`).

If the shape of your Lambda function response matches the expected output, you can forward the response using the following function response handler:

```
export const onPublish = {
  respone(ctx) {
    console.log(`the response: ${ctx.result}`)
    return ctx.events
  }
}
```

There are no required fields or shape restrictions that apply to the response object.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
