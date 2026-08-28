---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/untag-resource.html
---

# UntagResource
<a name="untag-resource"></a>

Use the `UntagResource` API operation to remove a tag from a resource. Before you do so, you can call the `ListTagsForResource` API operation to list the tags assigned to a resource.

Following is an example AWS CLI command for this operation. To find a resource’s Amazon Resource Name (ARN), use the `List` operation for the resource, for example `ListDashboards`.

------
#### [ AWS CLI ]

```
aws quicksight untag-resource
    --resource-arn {{777788889999}}
    --tag-keys {{NewDashboard}},{{ExampleDashboard}}
```

------

For more information about the `UntagResource` API operation, see [UntagResource](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UntagResource.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
