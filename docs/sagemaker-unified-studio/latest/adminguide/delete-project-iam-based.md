---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/delete-project-iam-based.html
---

# Delete a Project
<a name="delete-project-iam-based"></a>

Before deleting a project, ensure that all important data and resources have been backed up or migrated, as the deletion process removes all project content permanently.

1. From the domain administration page, choose **Projects** in the left navigation pane.

1. Choose the project name you want to delete from the Projects list.

1. On the project details page, choose **Delete**.

1. In the Delete project confirmation dialog:

   1. Review the warning message: "Deleting a project is final and removes all resources and assets created in the project"

   1. In the confirmation field, type **confirm** to acknowledge the deletion

   1. Choose **Delete** to permanently delete the project.

1. The project status changes to "Deleting" and the project is removed from the domain.

**Warning**
Deleting a project is final and removes all resources and assets created in the project. This action cannot be undone by you or by AWS.

The project and all associated resources are permanently removed from your Amazon SageMaker Unified Studio domain.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
