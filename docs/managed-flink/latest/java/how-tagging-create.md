---
source_url: https://docs.aws.amazon.com/managed-flink/latest/java/how-tagging-create.html
---

# Add tags when an application is created
<a name="how-tagging-create"></a>

You add tags when creating an application using the `tags` parameter of the [CreateApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CreateApplication.html) action.

The following example request shows the `Tags` node for a `CreateApplication` request:

```
"Tags": [
    {
        "Key": "Key1",
        "Value": "Value1"
    },
    {
        "Key": "Key2",
        "Value": "Value2"
    }
]
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed Service for Apache Flink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
