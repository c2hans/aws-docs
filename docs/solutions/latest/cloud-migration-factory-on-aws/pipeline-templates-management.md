---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/pipeline-templates-management.html
---

# Pipeline templates management
<a name="pipeline-templates-management"></a>

The pipeline templates provide a way for users to define a list of tasks in a given order to automate migration and modernization activities. You can upload new templates or change existing templates using the pipeline templates management interface. When Cloud Migration Factory on AWS deploys, the solution loads system-managed default pipeline templates automatically.

A template task is the smallest executable unit in a template. There are three types of tasks:
+  **Script package runs on the automation server** - This type of task is a script that runs on the automation server using an AWS Systems Manager agent. The script package is often used to connect to the source environment, such as installing an AWS MGN agent on the source server to initiate data replication.
+  **Lambda function** - This type of task is a Lambda function that runs inside the solution’s AWS account. For example, a Lambda function to connect to the AWS MGN API to initiate instance cutover activities. You can use this type of task to perform actions inside a Lambda function, such as connecting to a remote API, or using other AWS services.
+  **Manual task** - This type of task is managed by the user, not executed by the system. For example, if a user needs to submit a request for change in their environment to change a firewall port or a task to get approval. The user would complete the task outside of the solution and change the status to **complete** to continue the pipeline execution.

## Add a new pipeline template
<a name="add-pipeline-template"></a>

This section provides instructions for adding a new pipeline template.

1. Select **Automation**, then select **Pipeline templates**.

1. Select **Add**.

1. Enter the **Pipeline template description** and **Pipeline template name**.

1. Choose **Save** to create a new template.

## Duplicate an existing template
<a name="duplicate-pipeline-template"></a>

This section provides instructions for duplicating a pipeline template from an existing template and making changes to the tasks based on your requirements. By default, the solution loads system templates, which can’t be deleted.

1. Select **Automation**, then select **Pipeline templates**.

1. Select the template that you want to duplicate from the pipeline template table.

1. Select **Actions**, then select **Duplicate**.

1. Update the **Pipeline Template Description** and **Pipeline Template Name**.

1. Choose **Save** to create a template.

## Delete a pipeline template
<a name="delete-pipeline-template"></a>

This section provides instructions for deleting a user managed template. You can’t delete a system default template.

1. Select **Automation**, then select **Pipeline templates**.

1. Select the template that you want to delete from the pipeline template table.

1. Choose **Delete**.

## Export a pipeline template
<a name="export-pipeline-template"></a>

This section provides instructions for exporting one or more templates to JSON format.

1. Select **Automation**, then select **Pipeline templates**.

1. Select the template that you want to export.

1. Select **Actions**, then select **Export**.

## Import a pipeline template
<a name="import-pipeline-template"></a>

This section provides instructions for importing a template from a JSON format. You can download an existing template, make changes, and import it to the pipeline templates as a new template.

1. Select **Automation**, then select **Pipeline templates**.

1. Select **Actions**, then select **Import**.

1. On the **Import template** page, select **Choose File** to choose the new template in JSON format. The file name for the JSON template appears on the page.

1. Choose **Next**.

1. The **Step-2 Upload data** page appears. Review the template content.

1. Choose **Submit** to import the template.

1. After a few seconds, a **Pipeline templates imported successfully** message appears.

1. Select the newly imported template, then select the **Pipeline Templates tasks** tab.

1. Verify the task list for the template to ensure that all the tasks are imported correctly from the template.

## Add a new pipeline template task
<a name="add-pipeline-template-task"></a>

This section provides instructions for adding a new pipeline template task.

1. Select **Automation**, then **Pipeline templates**.

1. Select one of the templates on the list, then select the **Visual Task Editor** tab.

1. Select **Add** to add a new task.

1. Enter a template task name. Select the script for this task and successors to this task.

1. Choose **Save**.

The following image shows an example of adding a pipeline template task.

 **Add pipeline task screen with Details and Audit menus.**

![add pipeline task](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/add-pipeline-task.png)

## Delete a pipeline template task
<a name="delete-pipeline-template-task"></a>

This section provides instructions for deleting a pipeline template.

1. Select **Automation**, then **Pipeline templates**.

1. Select one of the templates on the list, then select the **Visual Task Editor** tab.

1. From the task list map, select the task that you want to delete.

1. Choose **Delete**.

The following image shows an example of deleting a pipeline template task.

 **Add pipeline task screen with Delete button.**

![delete pipeline template task](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/delete-pipeline-template-task.png)

## Editing a pipeline template
<a name="edit-pipeline-template-task"></a>

This section provides instructions for editing a pipeline template.

1. Select **Automation**, then **Pipeline templates**.

1. Select one of the templates on the list, then select the **Visual Task Editor** tab.

1. From the task list map, select the task that you want to edit.

1. Choose **Edit**.

    **Add pipeline task screen with Delete button.**
![edit pipeline template task](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/edit-pipeline-template-task.png)

1. On the task page, change the details of the task.

1. Choose **Save**.
