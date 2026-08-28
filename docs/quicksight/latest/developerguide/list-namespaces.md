---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/list-namespaces.html
---

# ListNamespaces
<a name="list-namespaces"></a>

Use the `ListNamespaces` API operation to list namespaces for a specified AWS account. Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight list-namespaces
    --aws-account-id {{AWSACCOUNTID}}
    --page-size {{10}}
    --max-items {{100}}
```

------

For more information about the `ListNamespaces` API operation, see [ListNamespaces](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListNamespaces.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
