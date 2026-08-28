---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/tag-collection-cli.html
---

# Tagging collections (AWS CLI)
<a name="tag-collection-cli"></a>

To tag a collection using the AWS CLI, send a [TagResource](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_TagResource.html) request:

```
aws opensearchserverless tag-resource
  --resource-arn arn:aws:aoss:{{us-east-1}}:{{123456789012}}:collection/{{my-collection}}
  --tags Key={{service}},Value={{aoss}} Key={{source}},Value={{logs}}
```

View the existing tags for a collection with the [ListTagsForResource](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListTagsForResource.html) command:

```
aws opensearchserverless list-tags-for-resource
  --resource-arn arn:aws:aoss:{{us-east-1}}:{{123456789012}}:collection/{{my-collection}}
```

Remove tags from a collection using the [UntagResource](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UntagResource.html) command:

```
aws opensearchserverless untag-resource
  --resource-arn arn:aws:aoss:{{us-east-1}}:{{123456789012}}:collection/{{my-collection}}
  --tag-keys {{service}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
