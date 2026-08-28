---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/creating-default-app-Windows-settings.html
---

# Creating Default Application and Windows Settings for Your WorkSpaces Applications Users
<a name="creating-default-app-Windows-settings"></a>

Application customizations and Windows settings that are saved to the Windows user profile folder or the user registry hive can be set as defaults. When you save the default settings by using the **Template User** in Image Assistant, WorkSpaces Applications replaces the Windows default user profile with the profile that you configure. The Windows default user profile is then used to create the initial settings for users in the fleet instance. If the application or Windows settings that you configure don't work in the fleet, confirm that they are saved in the Windows user profile. For more information, see Step 3: Create Default Application and Windows Settings in [Tutorial: Create a Custom WorkSpaces Applications Image by Using the WorkSpaces Applications Console](tutorial-image-builder.md).

Default settings that you can create and configure include:
+ Application preferences, including a browser home page, toolbar customizations, and security settings.
+ Application data settings, including browser bookmarks and connection profiles.
+ Windows experience settings, including displaying file name extensions and hidden folders.

Additionally, you can modify or disable Internet Explorer security settings, such as Enhanced Security Configuration (ESC). For more information, see [Disable Internet Explorer Enhanced Security Configuration in Amazon WorkSpaces Applications](customize-fleets-disable-ie-esc.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
