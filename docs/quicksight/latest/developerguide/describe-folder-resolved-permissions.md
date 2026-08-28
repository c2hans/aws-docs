---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-folder-resolved-permissions.html
---

# DescribeFolderResolvedPermissions
<a name="describe-folder-resolved-permissions"></a>

Use the `DescribeFolderResolvedPermissions` operation to describe the resolved permissions of a folder. Permissions consist of both folder direct permissions and the inherited permissions from the ancestor folders. To use this operation, you need the ID of the folder whose permissions you want to view. The folder ID is part of the folder URL in Quick Sight. You can also use the `ListFolders` operation to get the ID.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight describe-folder-resolved-permissions
    --aws-account-id {{AWSACCOUNTID}}
    --folder-id {{FOLDERID}}
```

------

For more information about the `DescribeFolderResolvedPermissions` operation, see [DescribeFolderResolvedPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeFolderResolvedPermissions.html) in the *Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
