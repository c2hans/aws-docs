---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/the-response-object.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# Handle service client responses
<a name="the-response-object"></a>

After a service client method has been called, it returns a response object instance of an interface with the name associated with the client method. For example, if you use the {{ AbcCommand}} client method, the response object is of {{AbcResponse}} (interface) type.

## Access data returned in the response
<a name="response-data-property"></a>

The response object contains the data, as properties, returned by the service request.

In [Create service client requests](the-request-object.md), the ` ListTablesCommand` command returned the table names in the `TableNames` property of the response.

## Access error information
<a name="response-error-property"></a>

If a command fails, it throws an exception. The following code snippet shows a way of handling a service exception.

```
try {
  await client.send({{someCommand}});
} catch (e) {
  if (e.name === "{{InvalidSignatureException}}") {
    // Handle InvalidSignatureException
  } else if (e.name === "{{ResourceNotFoundException}}") {
    // Handle ResourceNotFoundException
  } else if (e.name === "{{FooServiceException}}") {
    // Handle all other server-side exceptions from Foo service
  } else {
    // Handle errors from SDK
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for JavaScript. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-javascript` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
