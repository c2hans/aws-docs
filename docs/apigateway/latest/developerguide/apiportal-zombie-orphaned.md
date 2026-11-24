---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal-zombie-orphaned.html
---

# Zombie and orphaned APIs in API Portal

API Portal adds two labels to managed APIs that need attention. These labels apply only to managed APIs; shadow APIs aren't classified as zombie or orphaned.
+ **Zombie**: the API has received no traffic for 30 days and its backing resource has had no configuration change for 90 days. It's still reachable. Review whether the API should be retired; the label clears if traffic resumes.
+ **Orphaned**: the account that owns the API has left your organization or been closed. The inventory keeps a last-known snapshot, but the API is no longer rediscovered and its findings aren't updated. Remove it from managed APIs and from any products that include it.

These labels apply to managed APIs only. Shadow APIs aren't tracked for traffic or ownership changes.
