---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/create-default-app-windows-settings-image-assistant.html
---

# Creating Default Application and Windows Settings with the Image Assistant CLI operations
<a name="create-default-app-windows-settings-image-assistant"></a>

You can create default application and Windows settings so that your users can get started with their applications quickly. When you create these settings, WorkSpaces Applications replaces the Windows default user profile with the profile that you configure. The Windows default user profile is then used to create the initial settings for users in the fleet instance. If you create these settings by using the Image Assistant CLI operations, your application installer, or the automation, should modify the Windows default user profile directly.

To overwrite the Windows default user profile with that of another Windows user, you can also use the Image Assistant `update-default-profile` CLI operation.

For more information about configuring default application and Windows settings, see *Creating Default Application and Windows Settings for Your WorkSpaces Applications Users* in [Default Application and Windows Settings and Application Launch Performance in Amazon WorkSpaces Applications](customizing-appstream-images.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
