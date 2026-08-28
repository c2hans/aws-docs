---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/base-images-agent.html
---

# Manage WorkSpaces Applications Agent Versions
<a name="base-images-agent"></a>

The WorkSpaces Applications agent is software that runs on your streaming instances and enables users to stream applications. When you create a new image, the **Always use latest agent version** option is selected by default. When this option is selected, new image builders or fleet instances that are launched from your image always use the latest WorkSpaces Applications agent version. You might want to control agent updates to ensure compatibility with your software or to qualify the updated environment before you deploy it for your end users.

The following procedures describe how to manage WorkSpaces Applications agent versions.

**Topics**
+ [Create an Image That Always Uses the Latest Version of the WorkSpaces Applications Agent](create-image-that-always-uses-latest-agent.md)
+ [Create an Image That Uses a Specific Version of the WorkSpaces Applications Agent](create-image-that-uses-specific-agent.md)
+ [Create an Image That Uses a Newer Version of the WorkSpaces Applications Agent](create-image-that-uses-newer-agent.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
