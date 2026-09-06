---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-cloudendure/test.html
---

# Testing the migration
<a name="test"></a>

Before you migrate your source machines into the target infrastructure, you should test your CloudEndure Migration configuration. The **Test Mode** workflow launches and runs a target machine in the target infrastructure for the source machine you selected for testing. By testing your migration configuration, you can verify that your source machines are working properly in the target environment. The CloudEndure User Console displays the test results. You can run **Test Mode** after the Initial Sync stage has been completed.

To test your migration, follow these steps:

1. Confirm that the source machine you want to test is in Continuous Data Replication (CDR) mode or that its status is **Ready for testing**.

1. Configure the target machine with Blueprint. Verify that the subnet of the target environment is isolated. This isolation is designed to prevent conflicts with the source environment.

1. Test the target machines:

   1. On the **Machines** page, check the box to the left of each source machine you want to test.

   1. **Choose Launch *x* Target Machine**, and then choose **Test Mode**.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-cloudendure/images/guide-img/bbb5871c-6fdf-4a96-872d-e22410dc477d/images/1492929e-b7a2-4267-887c-c79f9975b9dd.png)

1. When you receive the confirmation prompt, choose **Continue** to launch the target machines. You can monitor the launch process on the **Job Progress** tab.

1. Verify that the test completed successfully.

1. Test the target machines by choosing each machine's name, navigating to the **Target** tab, copying the public IP, and navigating to that IP.

1. Verify service configuration and other settings.

1. Verify that your network works as expected.

1. Validate that you can connect to your target machines by using Secure Shell (SSH) for Linux or Remote Desktop Protocol (RDP) for Windows, and perform acceptance tests for your application.

For more information about the testing process, see [Testing the Migration Solution](https://docs.cloudendure.com/#Configuring_and_Running_Migration/Testing_the_Migration_Solution/Testing_the_Migration_Solution.htm) in the CloudEndure documentation.
