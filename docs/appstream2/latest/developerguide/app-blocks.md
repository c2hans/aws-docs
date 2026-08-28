---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/app-blocks.html
---

# App Blocks
<a name="app-blocks"></a>

App blocks represent a virtual hard disk (VHD) that is stored within an Amazon S3 bucket within your account that contains the application files and binaries necessary to launch the applications your users will use. App blocks also include the setup script that informs the operating system how to handle the VHD file.

App blocks support two different types of packaging:
+ Custom - Choose this option to create your application package (VHD) manually. For more information, see [Custom App Blocks](custom-app-blocks.md).
+ WorkSpaces Applications - Choose this recommended option to create your application package using app block builder. For more information, see [WorkSpaces Applications App Blocks](appstream-app-blocks.md).

**Topics**
+ [Custom App Blocks](custom-app-blocks.md)
+ [WorkSpaces Applications App Blocks](appstream-app-blocks.md)
+ [Unsupported Applications](app-blocks-unsupported.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
