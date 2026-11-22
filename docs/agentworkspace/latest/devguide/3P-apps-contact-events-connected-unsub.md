---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-events-connected-unsub.html
---

# Unsubscribe a callback function when an Connect Customer agent workspace contact is connected

Unsubscribes the callback function from Connected event in the Connect Customer agent workspace.

 **Signature**

```typescript
offConnected(handler: ContactConnectedHandler, contactId?: string)
```

 **Usage**

```typescript
contactClient.offConnected(handler);
```
