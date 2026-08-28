---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-tag-project-delete.html
---

# Remove a tag from a project
<a name="how-to-tag-project-delete"></a>

You can remove one or more tags associated with a project. Removing a tag does not delete the tag from other AWS resources that are associated with that tag.

**Important**
Removing tags for a project can impact access to that project. Before you remove a tag from a project, make sure to review any IAM policies that might use the key or value for a tag to control access to resources such as build projects. For examples of tag-based access policies, see [Using tags to control access to AWS CodeBuild resources](auth-and-access-control-using-tags.md).

## Remove a tag from a project (console)
<a name="how-to-tag-project-delete-console"></a>

You can use the CodeBuild console to remove the association between a tag and a CodeBuild project.

1. Open the CodeBuild console at [https://console.aws.amazon.com/codebuild/](https://console.aws.amazon.com/codebuild/).

1. In **Build projects**, choose the name of the project where you want to remove tags.

1. In the navigation pane, choose **Settings**. Choose **Build project tags**.

1. Choose **Edit**.

1. Find the tag you want to remove, and then choose **Remove tag**.

1. When you have finished removing tags, choose **Submit**.

## Remove a tag from a project (AWS CLI)
<a name="how-to-tag-project-delete-cli"></a>

 To delete one or more tags from a build project, see [Change a build project's settings (AWS CLI)](change-project.md#change-project-cli). Update the `tags` section in the JSON-formatted data with an updated list of tags that does not contain the ones you want to delete. If you want to delete all tags, update the `tags` section to:

```
"tags: []"
```

**Note**
If you delete a CodeBuild build project, all tag associations are removed from the deleted build project. You do not have to remove tags before you delete a build project.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
