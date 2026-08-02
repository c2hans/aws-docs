---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-activity-offexpirationwarning.html
---

# Unsubscribe a callback function from the expiration warning event
<a name="3P-apps-activity-offexpirationwarning"></a>

Unsubscribes a callback function from the expiration warning event that is triggered when the agent is nearing expiration due to inactivity.

 **Signature**

```
offExpirationWarning(handler: ExpirationWarningHandler);
```

 **Usage**

```
sessionExpirationWarningClient.offExpirationWarning(handler);
```
