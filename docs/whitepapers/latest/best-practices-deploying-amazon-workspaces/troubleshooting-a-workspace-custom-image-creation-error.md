---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/troubleshooting-a-workspace-custom-image-creation-error.html
---

# Troubleshooting A WorkSpace custom image creation error
<a name="troubleshooting-a-workspace-custom-image-creation-error"></a>

 If a Windows or Amazon Linux WorkSpace has been launched and customized, a custom image can be created from that WorkSpace. A custom image contains the operating system, application software, and settings for the WorkSpace.

 Review the [requirements to create a Windows custom image](https://docs.aws.amazon.com/workspaces/latest/adminguide/create-custom-bundle.html#windows_custom_image_requirements) or the [requirements to create an Amazon Linux custom image](https://docs.aws.amazon.com/workspaces/latest/adminguide/create-custom-bundle.html#linux_custom_image_requirements). Image creation requires that all prerequisites are met before image creation can start.

 To confirm that the Windows WorkSpace meets the requirements for image creation, we recommend running the Image Checker. The Image Checker performs a series of tests on the WorkSpace when an image is created, and provides guidance on how to resolve any issues it finds. For detailed information, refer to [installing and configuring the image checker](https://docs.aws.amazon.com/workspaces/latest/adminguide/create-custom-bundle.html#run_image_checker).

 After the WorkSpace passes all tests, a “Validation Successful” message appears. You can now create a custom bundle. Otherwise, resolve any issues that cause test failures and warnings, and repeat the process of running the Image Checker until the WorkSpace passes all tests. All failures and warnings must be resolved before an image can be created.

 For more information, follow the [tips for resolving issues detected by the Image Checker](https://docs.aws.amazon.com/workspaces/latest/adminguide/create-custom-bundle.html#run_image_checker).
