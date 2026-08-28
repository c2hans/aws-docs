---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-wscat.html
---

# Use `wscat` to connect to a WebSocket API and send messages to it
<a name="apigateway-how-to-call-websocket-api-wscat"></a>

The `[wscat](https://www.npmjs.com/package/wscat)` utility is a convenient tool for testing a WebSocket API that you have created and deployed in API Gateway. You can install and use `wscat` as follows:

1. Download `wscat` from [https://www.npmjs.com/package/wscat](https://www.npmjs.com/package/wscat).

1. Install `wscat` by running the following command:

   ```
   npm install -g wscat
   ```

1. To connect to your API, run the `wscat` command as shown in the following example. Note that this example assumes that the `Authorization` setting is `NONE`.

   ```
   wscat -c wss://{{aabbccddee}}.execute-api.{{us-east-1}}.amazonaws.com/test/
   ```

   You need to replace `{{aabbccddee}}` with the actual API ID, which is displayed in the API Gateway console or returned by the AWS CLI [`create-api`](https://docs.aws.amazon.com/cli/latest/reference/apigatewayv2/create-api.html) command.

   In addition, if your API is in a Region other than `us-east-1`, you need to substitute the correct Region.

1. To test your API, enter a message such as the following while connected:

   ```
   {"{{{jsonpath-expression}}}":"{{{route-key}}}"}
   ```

   where {{{jsonpath-expression}}} is a JSONPath expression and {{{route-key}}} is a route key for the API. For example:

   ```
   {"action":"action1"}
   {"message":"test response body"}
   ```

   For more information about JSONPath, see [JSONPath](https://goessner.net/articles/JsonPath/) or [JSONPath for Java](https://github.com/json-path/JsonPath).

1. To disconnect from your API, enter `ctrl-C`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
