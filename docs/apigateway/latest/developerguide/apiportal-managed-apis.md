---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal-managed-apis.html
---

# Managed APIs in API Portal

Promoting an API changes its classification from shadow to managed. Managed APIs are evaluated for security posture and can be added to products and published in documentation portals. Promoting an API doesn't change the underlying resource. A managed API persists until you remove it, regardless of when it last received traffic; an API that stops receiving traffic is flagged as a zombie API but stays managed. For more information, see [Zombie and orphaned APIs in API Portal](apiportal-zombie-orphaned.md).

**To promote APIs**

1. On the **API inventory** page, select the check box for each API that you want to promote.

1. Choose **Add to Managed APIs**.

1. In the **Add APIs as managed** dialog, review the number of APIs and choose **Add as managed**.

The APIs appear on the **Managed APIs** page, and their classification in the inventory changes to Managed. To reverse a promotion, on the **Managed APIs** page, select the API and choose **Remove from Managed APIs**. The API returns to shadow.

**Note**
You can promote only APIs that were discovered in your own scope. In organization scope, promote APIs from the management account or a delegated administrator account. When an API is managed at organization scope, the member account that hosts the API sees it classified as managed in its own inventory, but not which account manages it. Other member accounts don't see it.

To promote an API using the AWS CLI, pass the API's signature from the inventory item:

```
aws apiportal create-managed-api \
  --api-signature '{"resourceArn":"{{resourceArn}}","method":"GET","hostname":"{{api-id}}.execute-api.us-east-1.amazonaws.com","port":443,"path":"/pets"}' \
  --region us-east-1
```
