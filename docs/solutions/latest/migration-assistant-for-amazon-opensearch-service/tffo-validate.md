---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/tffo-validate.html
---

# Validating the transformation after migration
<a name="tffo-validate"></a>

After metadata migration completes, confirm that the affected fields landed as `flat_object` on the target and that queries against the nested keys still behave as expected.

First, inspect the mapping for an affected index on the target:

```
console clusters curl target /<INDEX>/_mapping?pretty
```

Confirm that the field that was `flattened` on the source is now reported as `flat_object`:

```
{
  "products": {
    "mappings": {
      "properties": {
        "attributes": {
          "type": "flat_object"
        }
      }
    }
  }
}
```

Next, run a representative query against a nested key inside the converted field to verify retrieval behavior on the target. For a `flat_object` field, reference a nested key with dot notation:

```
console clusters curl target /<INDEX>/_search?pretty -X POST -H 'Content-Type: application/json' -d '{
  "query": {
    "term": {
      "attributes.color": "blue"
    }
  }
}'
```

If you have aggregations, dashboards, or application queries that depend on these fields, exercise those as well, and compare the results against the source before you switch production traffic to the target.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
