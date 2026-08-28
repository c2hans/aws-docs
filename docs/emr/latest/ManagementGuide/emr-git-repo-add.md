---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-git-repo-add.html
---

# Add a Git-based repository to Amazon EMR
<a name="emr-git-repo-add"></a>

Refer to the following sections for information on how to add a Git-based repository to an EMR notebook in the old console, or to an EMR Studio Workspace in the console.

**Note**
EMR Notebooks are available as EMR Studio Workspaces in the console. The **Create Workspace** button in the console lets you create new notebooks. To access or create Workspaces, EMR Notebooks users need additional IAM role permissions. For more information, see [Amazon EMR Notebooks are Amazon EMR Studio Workspaces in the console](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-migration.html) and [Amazon EMR console](https://docs.aws.amazon.com/emr/latest/ManagementGuide/whats-new-in-console.html).

------
#### [ Console ]

Because EMR Notebooks are EMR Studio Workspaces in the new console, you can follow the instructions in [Link Git-based repositories to an EMR Studio Workspace](emr-studio-git-repo.md) to associate up to three Git repositories with your Workspace.

Alternatively, you can use the JupyterLab Git extension. Choose the **Git** icon from the left sidebar of your Jupyterlab notebook to access the extension. For information about the extension, see the [jupyterlab-git](https://github.com/jupyterlab/jupyterlab-git) GitHub repo.

To associate a Git repository with a Workspace, your Studio administrator must take steps to configure the Studio to allow Git repository linking. For more information, see [Establish access and permissions for Git-based repositories](emr-studio-enable-git.md).

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
