---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/channel-namespaces.html
---

# Understanding channel namespaces
<a name="channel-namespaces"></a>

Channel namespaces (or just namespaces for short) define the channels that are available on your Event API, and the capabilities and behaviors of these channels. Channel namespaces provide a scalable approach to managing large numbers of channels. Instead of configuring each channel individually, developers can apply settings across an entire namespace.

Each namespace has a name. This name represents the starting segment (the prefix) of a channel path. Any channel where the first segment in the path matches the name of a namespace, belongs to that namespace. For example, any channel with a first segment of `default`, such as `/default/messages`, `/default/greetings`, and `/default/inbox/user` belongs to the namespace named `default`. A channel namespace is made up of a maximum of five segments.

In a sports-related Event API example, you could have namespaces such as `basketball`, `soccer`, and `baseball`, with channels within each namespace such as `basketball/games/1`, `soccer/scores`, and `baseball/players`.

You can only publish and subscribe to channels that belong to a defined namespace. However, a channel is ephemeral and is created on-demand when a client needs to publish or subscribe to it.

When you define your Event API, you must configure the default authorization for connecting, publishing and subscribing to an Event API. The publishing and subscribing authorization configuration is automatically applied to all namespaces. You can override this configuration at the namespace. To learn more about authorization, see [Configuring authorization and authentication to secure Event APIs](configure-event-api-auth.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
