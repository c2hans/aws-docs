---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-folder-permissions.html
---

# DescribeFolderPermissions
<a name="describe-folder-permissions"></a>

Use the `DescribeFolderPermissions` operation to describe the permissions of a folder. To use this operation, you need the ID of the folder whose permissions you want to view. The folder ID is part of the folder URL in Quick Sight. You can also use the `ListFolders` operation to get the ID.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight describe-folder-permissions
    --aws-account-id {{AWSACCOUNTID}}
    --folder-id {{FOLDERID}}
```

------

You can find the folder ID by using a `ListFolders` operation or through the URL in the Quick Sight user interface.

For more information about the `DescribeFolderPermissions` operation, see [DescribeFolderPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeFolderPermissions.html) in the *Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
