---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/publish-http.html
---

# Publish events via HTTP
<a name="publish-http"></a>

AWS AppSync Events allows you to publish events via your API’s HTTP endpoint using a POST operation. Publishing is the only supported action over the endpoint.

**Publish steps**

1. Send a POST request to the address: `https://HTTP_DOMAIN/event`.

1. Add the authorization header(s) required to authorize your request.

1. Specify the following in the request body:
   + The channel that you are publishing to.
   + The list of events you are publishing. You can publish up to 5 events in a batch.

Each specified event in your publish request must be a stringified valid JSON value.

**Publish example**

The following is an example of a request.

```
{
  "method": "POST",
  "headers": {
    "content-type": "application/json",
    "x-api-key": "da2-your-api-key"
  },
  "body": {
    "channel": "default/channel",
    "events": [
      "{\"event_1\":\"data_1\"}",
      "{\"event_2\":\"data_2\"}"
    ]
  }
}
```

You can use your Browser’s `fetch API` to publish the events. The following example demonstrates this.

```
await fetch(`https://${HTTP_DOMAIN}/event`, {
  "method": "POST",
  "headers": {
    "content-type": "application/json",
    "x-api-key": "da2-your-api-key"
  },
  "body": {
    "channel": "default/channel",
    "events": [
      "{\"event_1\":\"data_1\"}",
      "{\"event_2\":\"data_2\"}"
    ]
  }
})
```

To learn more about the different authorization types that AWS AppSync Events supports, see [Configuring authorization and authentication to secure Event APIs](configure-event-api-auth.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
