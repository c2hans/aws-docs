---
source_url: https://docs.aws.amazon.com/appsync/latest/devguide/resolver-reference-none-js.html
---

# AWS AppSync JavaScript resolver function reference for `None` data source
<a name="resolver-reference-none-js"></a>

The AWS AppSync resolver function request and response with the data source of type *None* enables you to shape requests for AWS AppSync local operations.

## Request
<a name="request-js"></a>

The request handler can be simple and enables you to pass as much contextual information as possible via the `payload` field.

```
type NONERequest = {
  payload: any;
};
```

Here is an example where the field arguments are passed to the payload:

```
export function request(ctx) {
  return {
    payload: context.args
  };
}
```

The value of the `payload` field will be forwarded to the function response handler and is available in `context.result`.

## Payload
<a name="payload-js"></a>

The `payload` field is a container that can be used to pass any data that is then made available to the function response handler.

 The `payload` field is optional.

## Response
<a name="response-js"></a>

Because there is no data source, the value of the `payload` field will be forwarded to the function response handler and set on the `context.result` property.

If the shape of the `payload` field value exactly matches the shape of the GraphQL type, you can forward the response using the following response handler:

```
export function response(ctx) {
  return ctx.result;
}
```

There are no required fields or shape restrictions that apply to the return response. However, because GraphQL is strongly typed, the resolved response must match the expected GraphQL type.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
