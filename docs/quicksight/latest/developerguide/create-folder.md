---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/create-folder.html
---

# CreateFolder
<a name="create-folder"></a>

The `CreateFolder` operation creates an empty shared folder. To use this operation, you need the ID of the folder whose permissions you want to view. The folder ID is part of the folder URL in Quick Sight. You can also use the `ListFolders` operation to get the ID.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight create-folder
    --aws-account-id {{AWSACCOUNTID}}
    --folder-id {{FOLDERID}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight create-folder
    --cli-input-json file://{{createfolder}}.json
```

------

For more information about the `CreateFolder` operation, see [CreateFolder](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateFolder.html) in the *Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
