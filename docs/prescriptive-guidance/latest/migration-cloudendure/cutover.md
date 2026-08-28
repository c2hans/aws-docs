---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-cloudendure/cutover.html
---

# Cutting over to AWS
<a name="cutover"></a>

When you've completed your test and you're ready to cut over to the target environment on AWS, follow these steps:

1. Confirm that the **Data Replication Progress** for the source machine is **Continuous Data Replication** mode, and that the **Live Migration Lifecycle** column displays the  status  **Tested**.

1. Verify the Blueprint configuration.

1. Schedule and perform the cutover:

   1. On the **Machines** page, check the box to the left of each source machine you want to migrate.

   1. **Choose Launch *x* Target Machine**, and then choose **Cutover Mode**.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-cloudendure/images/guide-img/bbb5871c-6fdf-4a96-872d-e22410dc477d/images/05afae8a-99cb-4fda-a3f8-abcf4582aced.png)

   1. When you receive the confirmation prompt, choose **Continue** to launch the target machines. You can monitor the launch process on the **Job Progress** tab.

   1. Verify that the cutover completed successfully.
![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-cloudendure/images/guide-img/bbb5871c-6fdf-4a96-872d-e22410dc477d/images/89a88c88-39f4-4079-b5f1-da46a927586f.png)

   1. Verify service configuration and other settings.

   1. Verify that your network works as expected.

   1. Validate that you can connect to your target machines by using SSH for Linux or RDP for Windows, and perform acceptance tests for your application.

   1. Shut down your source machines.

1. After cutover is validated, uninstall the CloudEndure Agent by removing machines from the CloudEndure User Console.

   1. On the **Machines** page, check the box to the left of each source machine you want to remove.

   1. From the **Machine Actions** menu, choose **Remove x Machines from This Console**. It takes up to 60 minutes for CloudEndure Migration to clean up the replication instances and volumes in the staging area.

   1. When all Agents have been uninstalled, delete the virtual private cloud (VPC) for the staging area. This deletes all the AWS resources that you created for replication.

For more information about the cutover process, see [Performing a Migration Cutover](https://docs.cloudendure.com/#Configuring_and_Running_Migration/Performing_a_Migration_Cutover/Performing_a_Migration_Cutover.htm) in the CloudEndure documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
