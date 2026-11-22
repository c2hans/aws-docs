---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-events-connecting-unsub.html
---

# Unsubscribe a callback function when an Connect Customer agent workspace contact turns to Connecting state

Unsubscribes the callback function from Connecting event in the Connect Customer agent workspace.

 **Signature**

```typescript
offConnecting(handler: ContactConnectingHandler, contactId?: string)
```

 **Usage**

```typescript
contactClient.offConnecting(handler);
```
