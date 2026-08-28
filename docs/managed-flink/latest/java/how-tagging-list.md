---
source_url: https://docs.aws.amazon.com/managed-flink/latest/java/how-tagging-list.html
---

# List tags for an application
<a name="how-tagging-list"></a>

To list existing tags, you use the [ListTagsForResource](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ListTagsForResource.html) action.

The following example request for the `ListTagsForResource` action lists tags for an application:

```
{
   "ResourceARN": "arn:aws:kinesisanalyticsus-west-2:{{012345678901}}:application/MyApplication"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed Service for Apache Flink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
