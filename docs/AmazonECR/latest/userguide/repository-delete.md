---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-delete.html
---

# Deleting a private repository in Amazon ECR
<a name="repository-delete"></a>

If you're finished using a repository, you can delete it. When you delete a repository in the AWS Management Console, all of the images contained in the repository are also deleted; this cannot be undone.

**Important**
Images in the deleted repositories are also deleted. You cannot undo this operation.

**To delete a repository (AWS Management Console)**

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories).

1. From the navigation bar, choose the Region that contains the repository to delete.

1. In the navigation pane, choose **Repositories**.

1. On the **Repositories** page, choose the **Private** tab and then select the repository to delete and choose **Delete**.

1. In the **Delete {{repository\_name}}** window, verify that the selected repositories should be deleted and choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
