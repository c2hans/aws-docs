---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-clearedunsubscribing.html
---

# Unsubscribes the callback function from the contact cleared event in Connect Customer agent workspace
<a name="3P-apps-contact-requests-clearedunsubscribing"></a>

 Unsubscribes the callback function from the contact cleared event in Connect Customer agent workspace.

 **Signature**

```
        offCleared(handler: ContactClearedHandler, contactId?: string)
```

 **Usage**

```
 contactClient.offCleared(handler);
```
