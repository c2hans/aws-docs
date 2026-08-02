---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-es68-connectivity.html
---

# Step 7: Verify connectivity
<a name="pb-es68-connectivity"></a>

Confirm the Migration Console can reach and authenticate to both clusters before you submit anything:

```
console clusters connection-check
```

To check each side independently:

```
console clusters connection-check --cluster source
console clusters connection-check --cluster target
```

Because the target uses SigV4, also confirm that pod identity is working from the Migration Console pod:

```
aws sts get-caller-identity
```

If any check fails, stop and fix connectivity or authentication first. Do not submit a workflow yet.
