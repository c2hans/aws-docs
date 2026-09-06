---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/event-handlers-overview.html
---

# Event handlers overview
<a name="event-handlers-overview"></a>

An event handler is a function defined in a namespace that is invoked by specific triggers in the system. Currently you can define onPublish and onSubscribe event handlers: handlers that respond to events being published to a channel in the namespace, and handlers that respond to subscription items on a channel in the namespace. An onPublish handler is called before events are broadcast to subscribed clients, giving you a chance to transform the events first. An onSubscribe handler is called as a client tries to subscribe, giving you the chance to accept or reject the subscription attempt.

Event handlers are optional and are not required for your channel namespaces to be effective.
