---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-clearedunsubscribing.html
---

# Unsubscribes the callback function from the contact cleared event in Connect Customer agent workspace

 Unsubscribes the callback function from the contact cleared event in Connect Customer agent workspace.

 **Signature**

```typescript
        offCleared(handler: ContactClearedHandler, contactId?: string)
```

 **Usage**

```typescript
 contactClient.offCleared(handler);
```
