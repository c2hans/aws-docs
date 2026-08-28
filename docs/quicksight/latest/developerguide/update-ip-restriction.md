---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/update-ip-restriction.html
---

# UpdateIpRestriction
<a name="update-ip-restriction"></a>

Use the `UpdateIpRestriction` operation to update the content and status of IP rules. To use this operation, provide the entire map of rules. You can use the `DescribeIpRestriction` operation to get the current rule map.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight update-ip-restriction \
    --aws-account-id {{AWSACCOUNTID}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight update-ip-restriction \
    --cli-input-json file://{{updateiprestriction}}.json
```

------

For more information about the `UpdateIpRestriction` operation, see [UpdateIpRestriction](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateIpRestriction) in the *Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
