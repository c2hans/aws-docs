---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/event-api-concepts.html
---

# AWS AppSync Events concepts
<a name="event-api-concepts"></a>

Before you get started, review the following topics to help you understand the fundamental concepts of AWS AppSync Events.

## API
<a name="API"></a>

An Event API provides real-time capabilities by enabling you to publish events over HTTP and WebSocket, and subscribe to events over WebSockets. An Event API has one or more channel namespaces that define the capabilities and behavior of channels that events can be addressed to. To learn more about configuring an API, see [Configuring authorization and authentication to secure Event APIs](configure-event-api-auth.md) and [Configuring custom domain names for Event APIs](event-api-custom-domains.md).

## Event
<a name="event"></a>

An event is a JSON-formatted unit of data that can be published to channels on your API and received by clients that are interested in that channel. Events can contain any arbitrary data you want to transmit in real-time, such as user actions, data updates, system notifications, or sensor readings. Events are designed to be lightweight and efficient, with a maximum size of 240 KB per event.

## Channel
<a name="channel"></a>

Channels are the routing mechanism for directing events from publishers to subscribers. You can think of a channel as a "topic" or "subject" that represents a stream of related events. Clients subscribe to channels in order to receive events published to those channels in real-time. Channels are ephemeral and can be created on-demand.

## Channel namespace
<a name="namespace"></a>

A channel namespace (or just namespace for short) provides a way to define the capabilities and behaviors of the channels associated with it. Each namespace has a name. This name represents the starting segment (the prefix) of a channel path. Any channel where the first segment in the path matches the name of a namespace, belongs to that namespace. For example, any channel with a first segment of `default`, such as `/default/messages`, `/default/greetings`, and `/default/inbox/user` belongs to the namespace named `default`. To learn more about namespaces, see [Understanding channel namespaces](channel-namespaces.md).

## Event handler
<a name="handlers"></a>

An event handler is a function defined in a namespace. An event handler is a custom function to process published events before they are broadcast to subscribers. A event handler can also be used to process subscription requests when clients try to subscribe to a channel. Handlers are written in JavaScript and run on the AppSync\_JS runtime. Handlers can be associated with data sources to access external data or run custom business logic.

## Data sources
<a name="data-sources"></a>

Data sources are the resources that AWS AppSync Events can interact with to process, store, or retrieve event data. AWS AppSync Events supports data sources that provide the following capabilities:
+ **Storage solutions (DynamoDB, Amazon RDS)** – Store event data and state.
+ **Compute resources (Lambda)** – Process and transform events.
+ **AI/ML services (Amazon Bedrock)** – Add intelligence to event processing.
+ **Search and analytics (OpenSearch)** – Index and analyze event patterns.
+ **Event routing (EventBridge)** – Connect with broader event architectures.
+ **External integration (HTTP endpoints)** – Interact with external services.

Data sources can be associated with channel namespaces as integrations, and used by handlers to access external data. AWS AppSync Events can combine multiple data sources within a single API, enabling you to build sophisticated event processing workflows. Each event can interact with one or more data sources based on your application's needs.

## Publishing
<a name="publishing"></a>

Publishing is the act of sending a batch of events to your Event API. Published events can be broadcasted to subscribed clients. Publish is done over HTTP or WebSocket.

## Subscribing
<a name="subscribing"></a>

Subscribing is the act of listening for events on a specific channel or subset of channels over an Event API WebSocket. Clients that subscribe can receive broadcast events in real-time. Clients can establish multiple subscriptions over a single WebSocket.
