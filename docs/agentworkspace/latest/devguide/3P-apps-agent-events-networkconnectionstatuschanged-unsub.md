---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-events-networkconnectionstatuschanged-unsub.html
---

# Unsubscribe a callback function when the Connect Customer agent workspace agent's network connection status changes

Unsubscribes the callback function from the network connection status change event in the Connect Customer agent workspace.

 **Signature**

```typescript
offNetworkConnectionStatusChanged(handler: NetworkConnectionStatusChangedHandler)
```

 **Usage**

```typescript
agentClient.offNetworkConnectionStatusChanged(handler);
```
