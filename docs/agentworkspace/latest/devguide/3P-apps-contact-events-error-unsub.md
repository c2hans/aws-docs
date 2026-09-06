---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-events-error-unsub.html
---

# Unsubscribe a callback function when an Connect Customer agent workspace contact turns to Error state
<a name="3P-apps-contact-events-error-unsub"></a>

Unsubscribes the callback function from Error event in the Connect Customer agent workspace.

 **Signature**

```
offError(handler: ContactErrorHandler)
```

 **Usage**

```
contactClient.offError(handler);
```
