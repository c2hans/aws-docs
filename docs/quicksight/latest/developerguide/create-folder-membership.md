---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/create-folder-membership.html
---

# CreateFolderMembership
<a name="create-folder-membership"></a>

Use the `CreateFolderMembership` to add an asset, such as a dashboard, analysis, or dataset, to a folder. To use this operation, you need the member ID of the asset that you want to add to a folder. The member ID is either the dashboard, analysis, or dataset ID of the analysis, dashboard, or dataset that you want to add to a folder. The member ID is part of the analysis, dashboard, or dataset URL in Quick Sight. You can also use the `ListAnalyses`, `ListDashboards`, or `ListDataSets` operations to get the ID.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight create-folder-membership
    --aws-account-id {{AWSACCOUNTID}}
    --folder-id {{FOLDERID}}
    --member-id {{444455556666}}
    --member-type {{DASHBOARD}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight create-folder-membership
    --cli-input-json file://{{createfoldermembership}}.json
```

------

For more information about the `CreateFolderMembership` operation, see [CreateFolderMembership](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateFolderMembership.html) in the *Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
