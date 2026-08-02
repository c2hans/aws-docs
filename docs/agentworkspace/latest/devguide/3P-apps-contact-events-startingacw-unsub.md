---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-events-startingacw-unsub.html
---

# Unsubscribe a callback function when an Connect Customer agent workspace contact starts ACW
<a name="3P-apps-contact-events-startingacw-unsub"></a>

Unsubscribes the callback function from the contact StartingAcw event in the Connect Customer agent workspace.

 **Signature**

```
offStartingAcw(handler: ContactStartingAcwHandler, contactId?: string)
```

 **Usage**

```
contactClient.offStartingAcw(handler);
```
