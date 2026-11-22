---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-events-missed-unsub.html
---

# Unsubscribe a callback function when an Connect Customer agent workspace contact is missed

Unsubscribes the callback function from the contact missed event.

 **Signature**

```typescript
offMissed(handler: ContactMissedHandler, contactId?: string)
```

 **Usage**

```typescript
contactClient.offMissed(handler);
```
