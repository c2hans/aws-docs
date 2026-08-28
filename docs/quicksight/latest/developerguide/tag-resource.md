---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/tag-resource.html
---

# TagResource
<a name="tag-resource"></a>

Use the `TagResource` API operation to assign one or more tags (key-value pairs) to the specified Amazon Quick Sight resource.

Following is an example AWS CLI command for this operation. To find a resource's Amazon Resource Name (ARN), use the `List` operation for the resource, for example `ListDashboards`.

------
#### [ AWS CLI ]

```
aws quicksight tag-resource
    --resource-arn {{777788889999}}
    --tags Key={{NewDashboard}},Value={{True}}
```

------

For more information about the `TagResource` API operation, see [TagResource](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TagResource.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
