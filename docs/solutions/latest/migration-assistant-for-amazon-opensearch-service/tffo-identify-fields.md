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
