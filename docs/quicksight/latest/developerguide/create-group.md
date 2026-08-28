---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/create-group.html
---

# CreateGroup
<a name="create-group"></a>

Use the `CreateGroup` API operation to create a user group in Amazon Quick Sight. Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight create-group
    --namespace {{NAMESPACE}}
    --aws-account-id {{AWSACCOUNTID}}
    --group-name {{GROUPNAME}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight create-group
    --cli-input-json file://{{creategroup}}.json
```

------

For more information about the `CreateGroup` API operation, see [CreateGroup](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateGroup.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
