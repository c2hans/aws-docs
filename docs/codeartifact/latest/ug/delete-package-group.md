---
source_url: https://docs.aws.amazon.com/codeartifact/latest/ug/delete-package-group.html
---

# Delete a package group
<a name="delete-package-group"></a>

You can delete a package group using the CodeArtifact console or the AWS Command Line Interface (AWS CLI).

Note the following behavior when deleting package groups:
+ The root package group, `/*`, cannot be deleted.
+ The packages and package versions that are associated with that package group are not deleted.
+ When a package group is deleted, the direct child package groups will become children of the package group's direct parent package group. Therefore, if any of the child groups are inheriting any settings from the parent, those settings could change.

## Delete a package group (console)
<a name="delete-package-group-console"></a>

1. Open the AWS CodeArtifact console at [https://console.aws.amazon.com/codesuite/codeartifact/home](https://console.aws.amazon.com/codesuite/codeartifact/home).

1. In the navigation pane, choose **Domains**, and then choose the domain that contains the package group you want to view or edit.

1. Choose **Package groups**.

1. Choose the package group you want to delete and choose **Delete**.

1. Enter delete in the field and choose **Delete**.

## Delete a package group (AWS CLI)
<a name="delete-package-group-cli"></a>

To delete a package group, use the `delete-package-group` command.

```
aws codeartifact delete-package-group \
         --domain {{my_domain}} \
         --domain-owner {{111122223333}} \
         --package-group {{'/nuget/*'}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeArtifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeartifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
