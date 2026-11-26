---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/permission-set-architecture.html
---

# Permission-set discovery and synchronization

The solution uses existing IAM Identity Center permission sets to control sandbox account access. Administrators register custom permission sets by tagging them, and the solution caches their metadata in the Principal DynamoDB table. The built-in user permission set is included without a tag; the Admin and Manager permission sets are excluded from lease selection.

The Principal Cache Sync function updates the cache in two ways:
+  **Event-driven updates**: An EventBridge rule in the AWS IAM Identity Center (IDC) account forwards permission-set events to the Hub account’s event bus. The rule matches successful `CreatePermissionSet`, `TagResource`, `UntagResource`, `DeletePermissionSet`, and `UpdatePermissionSet` API events from AWS CloudTrail. The Principal Cache Sync function validates the account and instance, reads the current permission set and tags, and updates or removes its cache entry.
+  **Hourly reconciliation**: After synchronizing users and groups, the same function discovers registered permission sets through the AWS Resource Groups Tagging API and reconciles the cache. This handles missed events and indexing delays.

For operational guidance, see [Permission set issues](troubleshooting.md#permission-set-issues).
