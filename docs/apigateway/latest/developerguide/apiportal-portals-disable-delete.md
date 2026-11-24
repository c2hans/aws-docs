---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal-portals-disable-delete.html
---

# Disable or delete a documentation portal

Disabling a portal takes it off the web while keeping its configuration, so you can republish it later. A portal must be disabled before you can delete it. Deleting a portal can't be undone; its products and pages aren't deleted and can be added to another portal. A portal is billed until it's deleted, including while disabled.

**To disable a portal**
+ On the portal detail page, choose **Actions**, then **Disable portal**, and confirm. The status shows **Disable in progress**, then **Disabled**.

**To delete a portal**

1. Disable the portal first.

1. Choose **Actions**, then **Delete portal**, and confirm.

```
aws apiportal update-portal-publish-status --portal-id {{portal-id}} --status DISABLED --region us-east-1
aws apiportal delete-portal --portal-id {{portal-id}} --region us-east-1
```
