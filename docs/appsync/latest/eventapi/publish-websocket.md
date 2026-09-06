---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/publish-websocket.html
---

# Publish events via WebSocket
<a name="publish-websocket"></a>

AWS AppSync Events allows you to publish events via your API’s WebSocket endpoint after you connect to it.

**Publish steps**

1. Connect to your WebSocket endpoint: `wss://WS_DOMAIN/event/realtime`.

1. Send a `publish` message over the established WebSocket connection with the following information:
   + The authorization header(s) required to authorize your message.
   + The following message details:
     + A unique ID for your message.
     + The channel that you are publishing to.
     + The list of events that you are publishing. You can publish a maximum of five events in a batch.

Each specified event in your publish request must be a stringified valid JSON value.

**Publish example**

The following is an example of a request written in JavaScript that uses an API key for authorization.

```
const message = {
  id: '{{uniqueID}}', // Your unique id for this message.
  type: 'publish',
  channel: '/default/channel',
  events: [
    JSON.stringify({ message: "hello world" }),
    JSON.stringify({ number: 42 })
  ],
  authorization: { 'x-api-key': '{{your key}}' },
}
```

You can use your browser’s WebSocket API to connect and publish the events. The following simplified example uses an API key that sends the message. Notice that you don't need to subscribe to any channel before publishing.

```
const HTTP_DOMAIN = '{{your api HTTP domain }}'
const REALTIME_DOMAIN = '{{api real-time domain}}'
const API_KEY = '{{your api key}}'

const authorization = { 'x-api-key': API_KEY, host: HTTP_DOMAIN }

// construct the protocol header for the connection
function getAuthProtocol() {
  const header = btoa(JSON.stringify(authorization))
    .replace(/\+/g, '-') // Convert '+' to '-'
    .replace(/\//g, '_') // Convert '/' to '_'
    .replace(/=+$/, '') // Remove padding `=`
  return `header-${header}`
}

const socket = await new Promise((resolve, reject) => {
  const socket = new WebSocket(`wss://${REALTIME_DOMAIN}/event/realtime`, [
    'aws-appsync-event-ws',
    getAuthProtocol(),
  ])
  socket.onopen = () => resolve(socket)
  socket.onclose = (event) => reject(new Error(event.reason))
  socket.onmessage = (event) => console.log(event)
})

// when the socket is connected, send the message
socket.send(JSON.stringify(message))
```

You receive an acknowledgement message for every publish. For more information, see [Understanding the Event API WebSocket protocol](event-api-websocket-protocol.md).

To learn more about the different authorization types that AWS AppSync Events supports, see [Configuring authorization and authentication to secure Event APIs](configure-event-api-auth.md).
