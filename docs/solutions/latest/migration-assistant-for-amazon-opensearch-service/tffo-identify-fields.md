---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/tffo-identify-fields.html
---

# Identifying flattened fields
<a name="tffo-identify-fields"></a>

Before you migrate, you can confirm whether any source index uses the `flattened` type so you know which indexes the transformation will touch. Run the following from the Migration Console pod (`migration-console-0`) to inspect the source mappings:

```
console clusters curl source /_mapping
```

Scan the response for fields declared as `"type": "flattened"`. For example:

```
{
  "products": {
    "mappings": {
      "properties": {
        "attributes": {
          "type": "flattened"
        }
      }
    }
  }
}
```

Any field reported this way is automatically converted to `flat_object` when you run metadata migration against the Amazon OpenSearch Service domain or Amazon OpenSearch Serverless NextGen collection.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
