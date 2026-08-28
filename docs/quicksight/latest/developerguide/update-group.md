---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/update-group.html
---

# UpdateGroup
<a name="update-group"></a>

Use the `UpdateGroup` API operation to change a group description. You can find a group name by calling the `ListGroups` API operation.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight update-group
    --group-name {{GROUPNAME}}
    --description "{{NEW DESCRIPTION}}"
    --aws-account-id {{AWSACCOUNTID}}
    --namespace {{default}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight update-group
    --cli-input-json file://{{updategroup}}.json
```

------

For more information about the `UpdateGroup` API operation, see [UpdateGroup](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateGroup.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
