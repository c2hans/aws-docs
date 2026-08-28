---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-aoss-map-identities.html
---

# Step 4: Map IAM identities on both sides
<a name="pb-aoss-map-identities"></a>

Both the source and the target use SigV4 in this migration, but with different service names. Load the version-matched sample and open the configuration:

```
workflow configure sample --load
workflow configure edit
```

Set the source to the Amazon OpenSearch Service domain (SigV4 service `es`) and the target to the Amazon OpenSearch Serverless NextGen collection (SigV4 service `aoss`):

```
{
  "sourceClusters": {
    "source": {
      "endpoint": "https://<domain-endpoint>",
      "version": "OpenSearch 2.x",
      "authConfig": {
        "sigv4": {
          "region": "<region>",
          "service": "es"
        }
      }
    }
  },
  "targetClusters": {
    "target": {
      "endpoint": "https://<collection-id>.<region>.aoss.amazonaws.com",
      "authConfig": {
        "sigv4": {
          "region": "<region>",
          "service": "aoss"
        }
      }
    }
  }
}
```

**Important**
The migration IAM role must be authorized on **both** sides. On the source domain, if fine-grained access control is enabled, map `<eks-cluster-name>-migrations-role` to a security role (typically `all_access` during migration, then scope it down afterward). On the target collection, the role must already appear as a principal in the data access policy from Step 1, with both collection-level and index-level permissions. See [Troubleshooting](troubleshooting.md) if the workflow later returns HTTP 401 or 403.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
