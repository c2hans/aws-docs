---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-creation-templates-updating.html
---

# Updating a repository creation template
<a name="repository-creation-templates-updating"></a>

You can edit a repository creation template if you need to change its configurations. Once the repository creation template is edited, the new configurations will apply to the existing template.

**Important**
This doesn't have any effect on any previously created repositories.

------
#### [ AWS Management Console ]

**To edit a repository creation template (AWS Management Console)**

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, choose the Region the repository creation template to edit is in.

1. In the navigation pane, choose **Private registry**, then choose **Settings**.

1. From the navigation bar, choose the **Repository creation templates**.

1. On the **Repository creation templates** page, select the repository creation template to edit.

1. From the **Actions** dropdown menu, choose **Edit**.

1. Review and update the configuration settings.

1. Choose update to apply the new creation template configurations.

------
#### [ AWS CLI ]

**To edit a repository creation template (AWS CLI)**
+ Use the [update-repository-creation-template](https://docs.aws.amazon.com/cli/latest/reference/ecr/update-repository-creation-template.html) command to update an existing repository creation template. You must specify the `prefix` value of the template. The following example updates a repository creation template with the `prod` prefix.

  ```
  aws ecr update-repository-creation-template \
       --prefix {{prod}} \
       --image-tag-mutability="IMMUTABLE_WITH_EXCLUSION" \
       --image-tag-mutability-exclusion-filters filterType={{WILDCARD}}, filter={{latest}}
  ```

  The output of the command displays the details of the updated repository creation template.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
