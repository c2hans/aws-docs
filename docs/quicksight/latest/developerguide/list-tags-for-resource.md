---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/list-tags-for-resource.html
---

# ListTagsForResource
<a name="list-tags-for-resource"></a>

Use the `ListTagsForResource` API operation to list tags assigned to a resource.

Following is an example AWS CLI command for this operation. To find a resource’s Amazon Resource Name (ARN), use the `List` operation for the resource. For example, `ListDashboards`.

------
#### [ AWS CLI ]

```
aws quicksight list-tags-for-resource
    --resource-arn {{444455556666}}
```

------

For more information about the `ListTagsForResource` API operation, see [ListTagsForResource](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListTagsForResource.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
