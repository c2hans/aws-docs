---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-ts-operation-status.html
---

# Checking operation status
<a name="msk-data-delivery-ts-operation-status"></a>
+ **Symptom:** You want to confirm the status of a create, update, or delete operation, or find why it failed.
+ **Resolution:** Use the `ClusterOperationArn` returned by `CreateChannel`, `UpdateChannel`, and `DeleteChannel` to look up the operation's state and any error message. Combine this with `DescribeChannel` to see the Channel's current state.
