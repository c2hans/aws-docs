---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal-troubleshooting.html
---

# Troubleshoot API Portal

The **Enable discovery** page shows "Trusted access is not enabled."
Enable trusted access from the button on that page or from **Organization settings**, wait until it shows **Enabled**, and then enable discovery again. You must be signed in to the management account.

I can't register a delegated administrator.
Trusted access must show **Enabled** first, and you must be signed in to the management account.

An API that I expect isn't in the inventory.
Check the following, in order:
+ The API's source service is selected in your discovery configuration, and the resource isn't excluded by a filter.
+ For API Gateway, the API is a REST API. HTTP APIs and WebSocket APIs aren't discovered.
+ For API Gateway REST APIs discovered from configuration, the method is explicit (for example `GET`, not `ANY`) and the path is literal (not `{proxy+}`). Otherwise the API appears only after it receives traffic.
+ For Application Load Balancer and CloudFront, the endpoint has received sustained traffic. These sources are discovered from traffic only.
+ Enough time has passed. New APIs typically appear within a few hours; allow up to 24 hours after you first enable discovery.
+ In an organization, the owning account is in scope and isn't excluded, and the Region is one where you enabled discovery.

An API that I deleted still shows in the inventory.
Inventory rows for deleted APIs, and for APIs that stop receiving traffic, are removed about 30 days after the last configuration record or traffic. This is expected. Deleting the discovery configuration doesn't remove rows sooner. If the API was a managed API, remove it from your managed APIs so it's no longer evaluated or counted.

Discovery status shows Failed.
The status includes a reason. `ACCESS_DENIED` usually means the service-linked role is missing in the target account or the account isn't in the organization. `THROTTLED` means discovery was rate-limited by a source service; it retries automatically and the status clears on its own, usually within an hour. If it persists for more than a day, contact AWS Support. `INVALID_CONFIGURATION` means an unsupported Region or an invalid filter; correct the configuration and start discovery again.

I can't add an API to a product.
Only managed APIs can be added. Promote the API first. For a rule-based product, the API must match the product's rules.

A published portal doesn't show my latest changes.
Choose **Publish portal** again. The live portal is a snapshot from the last publish.

The security checklist shows Not applicable for several items.
Postures are specific to the source service. Checks that don't describe an Application Load Balancer or CloudFront resource show Not applicable.

Consumers get a sign-in error on a portal that uses Amazon Cognito.
Confirm that the user pool ARN, user pool domain, and app client ID on the portal match your user pool and that the user exists in the pool. After you correct the settings, publish the portal again.

Publishing fails with a domain error.
The custom domain name is already in use by another CloudFront distribution, or the certificate isn't in us-east-1. Choose a different domain name or certificate and publish again.
