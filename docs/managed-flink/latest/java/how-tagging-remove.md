---
source_url: https://docs.aws.amazon.com/managed-flink/latest/java/how-tagging-remove.html
---

# Remove tags from an application
<a name="how-tagging-remove"></a>

To remove tags from an application, you use the [UntagResource](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_UntagResource.html) action.

The following example request for the `UntagResource` action removess tags from an application:

```
{
   "ResourceARN": "arn:aws:kinesisanalyticsus-west-2:{{012345678901}}:application/MyApplication",
   "TagKeys": [ "KeyOfFirstTagToRemove", "KeyOfSecondTagToRemove" ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed Service for Apache Flink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
