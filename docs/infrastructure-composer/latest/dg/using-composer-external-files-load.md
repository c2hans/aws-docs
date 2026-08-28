---
source_url: https://docs.aws.amazon.com/infrastructure-composer/latest/dg/using-composer-external-files-load.html
---

# Load a project with an external file reference in Infrastructure Composer
<a name="using-composer-external-files-load"></a>

Follow the steps listed on this page to load an Infrastructure Composer project with an external file reference.

**From the Infrastructure Composer console**

1. Complete the steps listed in [Import an existing project template in the Infrastructure Composer console](using-composer-project-import-template.md).

1. Confirm Infrastructure Composer prompts you to connect to the root folder of your project

If your browser supports the File System Access API, Infrastructure Composer will prompt you to connect to the root folder of your project. Infrastructure Composer will open your project in **local sync** mode to support your external file. If the referenced external file is not supported, you will receive an error message. For more information about error messages, see [Troubleshooting](ref-troubleshooting.md).

**From the Toolkit for VS Code**

1. Complete the steps listed in [Access Infrastructure Composer from the AWS Toolkit for Visual Studio Code](setting-up-composer-access-ide.md).

1. Open the template you want to view in Infrastructure Composer.

When you access Infrastructure Composer from a template, Infrastructure Composer will automatically detect your external file. If the referenced external file is not supported, you will receive an error message. For more information about error messages, see [Troubleshooting](ref-troubleshooting.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Infrastructure Composer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query infrastructure-composer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
