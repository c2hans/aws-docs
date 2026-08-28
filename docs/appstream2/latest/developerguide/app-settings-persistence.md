---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/app-settings-persistence.html
---

# Enable Application Settings Persistence for Your WorkSpaces Applications Users
<a name="app-settings-persistence"></a>

WorkSpaces Applications supports persistent application settings for Windows-based stacks. This means that your users' application customizations and Windows settings are automatically saved after each streaming session and applied during the next session. Examples of persistent application settings that your users can configure include, but are not limited to, browser favorites, settings, webpage sessions, application connection profiles, plugins, and UI customizations. These settings are saved to an Amazon Simple Storage Service (Amazon S3) bucket in your account, within the AWS Region in which application settings persistence is enabled. They are available in each WorkSpaces Applications streaming session.

**Note**
Enabling application settings persistence is currently not supported for Linux-based stacks.

**Note**
Standard Amazon S3 charges may apply to data that is stored in your S3 bucket. For more information, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/).

**Topics**
+ [How Application Settings Persistence Works](how-it-works-app-settings-persistence.md)
+ [Enabling Application Settings Persistence](enabling-app-settings-persistence.md)
+ [Administer the VHDs for Your Users' Application Settings](administer-app-settings-vhds.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
