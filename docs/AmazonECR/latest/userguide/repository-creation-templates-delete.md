---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-creation-templates-delete.html
---

# Deleting a repository creation template in Amazon ECR
<a name="repository-creation-templates-delete"></a>

You can delete a repository creation template if you are finished using it. Once a repository creation template is deleted, any newly created repositories under the associated prefix during a pull through cache or replication action will inherit the default settings, unless another matching template is found, see [How repository creation templates work](repository-creation-templates.md#repository-creation-templates-works).

**Important**
This doesn't have any effect on any previously created repositories.

------
#### [ AWS Management Console ]

**To delete a repository creation template (AWS Management Console)**

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, choose the Region the repository creation template to delete is in.

1. In the navigation pane, choose **Private registry**, **Repository creation templates**.

1. On the **Repository creation templates** page, select the repository creation template to delete.

1. From the **Actions** dropdown menu, choose **Delete**.

------
#### [ AWS CLI ]

**To delete a repository creation template (AWS CLI)**
+ Use the [delete-repository-creation-template.html](https://docs.aws.amazon.com/cli/latest/reference/ecr/delete-repository-creation-template.html) command to delete an existing repository creation template. You must specify the `prefix` value of the template. The following example deletes a repository creation template with the `prod` prefix.

  ```
  aws ecr delete-repository-creation-template \
       --prefix {{prod}}
  ```

  The output of the command displays the details of the deleted repository creation template.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
