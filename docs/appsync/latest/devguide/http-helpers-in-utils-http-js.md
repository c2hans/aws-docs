---
source_url: https://docs.aws.amazon.com/appsync/latest/devguide/http-helpers-in-utils-http-js.html
---

# HTTP helpers in util.http
<a name="http-helpers-in-utils-http-js"></a>

The `util.http` utility provides helper methods that you can use to manage HTTP request parameters and to add response headers.

## util.http utils list
<a name="http-helpers-in-utils-http-list-js"></a>

 **`util.http.copyHeaders(headers)`**
Copies the headers from the map, excluding the following restricted HTTP headers:
+ transfer-encoding
+ connection
+ host
+ expect
+ keep-alive
+ upgrade
+ proxy-authenticate
+ proxy-authorization
+ te
+ content-length

**`util.http.addResponseHeader(String, Object)`**
Adds a single custom header with the name (`String`) and value (`Object`) of the response. The following limitations apply:
+ In addition to the list of restricted headers for `copyHeaders(headers)`, header names cannot match any of the following:
  + Access-Control-Allow-Credentials
  + Access-Control-Allow-Origin
  + Access-Control-Expose-Headers
  + Access-Control-Max-Age
  + Access-Control-Allow-Methods
  + Access-Control-Allow-Headers
  + Vary
  + Content-Type
+ Header names can't start with the restricted prefixes `x-amzn-` or `x-amz-`.
+ The size of custom response headers can't exceed 4 KB. This includes header names and values.
+ You should define each response header once per GraphQL operation. However, if you define a custom header with the same name multiple times, the most recent definition appears in the response. All headers count towards the header size limit regardless of naming.
+ Headers with an empty or restricted name `(String)` or a null value `(Object)` will be ignored and yield a `ResponseHeaderError` error that is added to the operation's `errors` output.

```
export function request(ctx) {
  util.http.addResponseHeader('itemsCount', 7)
  util.http.addResponseHeader('render', ctx.args.render)
  return {}
}
```

**`util.http.addResponseHeaders(Map)`**
Adds multiple response headers to the response from the specified map of names `(String)` and values `(Object)`. The same limitations listed for the `addResponseHeader(String, Object)` method also apply to this method.

```
export function request(ctx) {
  const headers = {
    headerInt: 12,
    headerString: 'stringValue',
    headerObject: {
      field1: 7,
      field2: 'string'
    }
  }
  util.http.addResponseHeaders(headers)
  return {}
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
