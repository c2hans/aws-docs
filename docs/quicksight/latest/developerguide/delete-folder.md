---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-folder.html
---

# DeleteFolder
<a name="delete-folder"></a>

Use the `DeleteFolder` operation to delete an empty folder. To use this operation, you need the ID of the folder whose permissions you want to view. The folder ID is part of the folder URL in Quick Sight. You can also use the `ListFolders` operation to get the ID.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight delete-folder
    --aws-account-id {{AWSACCOUNTID}}
    --folder-id {{FOLDERID}}
```

------

For more information about the `DeleteFolder` operation, see [DeleteFolder](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteFolder.html) in the *Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
