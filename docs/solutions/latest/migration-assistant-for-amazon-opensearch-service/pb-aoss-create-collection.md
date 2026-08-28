---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-aoss-create-collection.html
---

# Step 2: Create the collection
<a name="pb-aoss-create-collection"></a>

With the policies in place, create the vector-search collection:

```
aws opensearchserverless create-collection \
  --name vector-search \
  --type VECTORSEARCH \
  --description "Vector search collection migrated from Amazon OpenSearch Service"
```

A new collection takes several minutes to become active. Poll its status with `batch-get-collection` until `status` reports `ACTIVE`:

```
aws opensearchserverless batch-get-collection --names vector-search \
  --query 'collectionDetails[0].{status:status,endpoint:collectionEndpoint}'
```

Record the `collectionEndpoint` from the response. It has the form `https://<collection-id>.<region>.aoss.amazonaws.com` and is the endpoint you configure as the migration target. Do not continue until the status is `ACTIVE`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
