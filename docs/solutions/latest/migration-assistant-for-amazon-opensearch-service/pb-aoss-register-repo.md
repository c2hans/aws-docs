---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-aoss-register-repo.html
---

# Step 5: Register the snapshot repository on the source
<a name="pb-aoss-register-repo"></a>

RFS reads from a snapshot that lives in an Amazon S3 repository registered on the source domain. Register the repository directly through the source domain’s API from the Migration Console pod. The following uses the Amazon S3 plugin repository type and points at the migration bucket:

```
console clusters curl source /_snapshot/migration-repo -XPUT \
  -H 'Content-Type: application/json' \
  -d '{
    "type": "s3",
    "settings": {
      "bucket": "migrations-default-<ACCOUNT_ID>-<STAGE>-<REGION>",
      "region": "<REGION>",
      "base_path": "vector-search-snapshot"
    }
  }'
```

Verify the repository is reachable before creating a snapshot:

```
console clusters curl source /_snapshot/migration-repo/_verify -XPOST
```

A successful `_verify` returns the list of source nodes that can write to the repository. If it fails, confirm the source domain has an IAM role with `s3:PutObject` and `s3:GetObject` on the bucket and that the bucket is in the migration Region.
