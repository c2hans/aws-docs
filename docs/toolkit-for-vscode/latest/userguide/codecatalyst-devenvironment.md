---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/codecatalyst-devenvironment.html
---

# Working with the Toolkit in a Dev Environments
<a name="codecatalyst-devenvironment"></a>

Dev Environments are virtual computing environments for Amazon CodeCatalyst. The following sections describe how to create, launch, and work from Dev Environments using the AWS Toolkit for Visual Studio Code.

For detailed information about Dev Environments, see the [Dev Environments](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment.html) topic in the *Amazon CodeCatalyst* User Guide.

## Configuring your Dev Environment with devfiles
<a name="codecatalyst-devenvironment-devfile"></a>

The `devfile` specification is an open-standard format for YAML that can be used to define configurations for Dev Environments. Every Dev Environment has a devfile. If you create a Dev Environment without a repository or from a repository that doesn't contain a devfile, a default is applied to the source automatically. Devfiles can be updated from CodeCatalyst or your IDE. The processes to update a devfile in a local or remote instance of VS Code are identical, but if you update a devfile locally, you must push the updates to your source repository before the updates take effect.

For detailed information about configuring Dev Environments with devfiles, see the [Configuring your Dev Environment](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment-devfile.html) topic in the *Amazon CodeCatalyst* User Guide.

The following procedure describes how to edit your devfile from a remote instance of the Toolkit while it's running in a Dev Environment.

**Important**
If you edit the `Devfile` from VS Code, be aware of the following:
Changing the name of the devfile or the devfile component name replaces the contents of your root directory. All previous content is lost and unrecoverable.
If you create a Dev Environment without a devfile in the root folder or a Dev Environment that's not associated with a source repository, a devfile with default configuration settings is generated for your Dev Environment when you create it.
For instructions on how to define and configure your `Devfile`, see the [Adding Commands](https://devfile.io/docs/2.1.0/adding-commands) documentation on the [devfile.io](https://devfile.io/) website.

1. From the Toolkit for VS Code, expand the **DEVELOPER TOOLS** explorer.

1. Expand **CodeCatalyst** and choose **Open Devfile** to open `devfile.yaml` in a new editor window, within your current Dev Environment.

1. From the VS Code editor, update your devfile, then save your changes.

1. The next time you launch your Dev Environment, the configuration is updated to match the specifications that are defined in your `Devfile`.

## Authenticating and connecting to AWS from your Dev Environment
<a name="codecatalyst-devenvironment-credentials"></a>

To access all of your AWS resources from your Dev Environment, you must authenticate and connect your remote instance of the Toolkit with your AWS account. The remote instance of the Toolkit automatically authenticates with the credentials inherited from your local instance of the Toolkit when your Dev Environment is launched.

The procedures to update your credentials for a remote instance of the Toolkit are identical to the authentication experience in your local instance of the Toolkit. For detailed instructions on how to update credentials, authenticate, and connect to AWS from the Toolkit, see the [Connecting to AWS](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/connect.html#connect-to-aws) section in the *Getting started* topic of this User Guide.

For additional information about each of the AWS authentication methods compatible with the AWS Toolkit for Visual Studio Code, see the [Authentication and access](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/connect.html#connect-to-aws) topic in this User Guide.

## Working with the Toolkit for VS Code in Dev Environments
<a name="codecatalyst-devenvironment-toolkit"></a>

After you open or create a Dev Environment in VS Code, you can work from the Toolkit for VS Code, similar to how you can from a local instance of VS Code. Dev Environments running VS Code are configured to automatically install the AWS Toolkit and connect with your AWS Builder ID.

### Stopping a Dev Environment
<a name="codecatalyst-devenvironment-stop"></a>

To stop your current Dev Environment:

1. From the Toolkit for VS Code, expand the **DEVELOPER TOOLS** explorer.

1. Expand **CodeCatalyst** and choose **Stop Dev Environment**.

1. When prompted by VS Code, confirm that you want to stop your Dev Environment.

1. Your Dev Environment has successfully stopped when VS Code closes the remote connection and returns to a local development instance.

### Opening Dev Environment settings
<a name="codecatalyst-devenvironment-settings"></a>

To open the settings for your current Dev Environment, complete the following steps:

**Note**
You can't change the amount of storage space assigned to your Dev Environment after it has been created.

1. From the Toolkit for VS Code, expand the **DEVELOPER TOOLS** explorer.

1. Expand **CodeCatalyst** and choose **Open Settings** to open the **Dev Environment Settings** view, for your current Dev Environment.

1. From the **Dev Environment Settings** view, the following sections contain options for your Dev Environment:
   + **Alias**: View and change the **Alias** assigned to your Dev Environment.
   + **Status**: View your current Dev Environment status, the project it's assigned to, and stop your environment.
   + **Devfile**: View the name and location of the `Devfile` for your Dev Environment. Open your `Devfile` by choosing the **Open in Editor** button.
   + **Compute Settings**: Change the size and default **Timeout Length** for your Dev Environment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for Visual Studio Code. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-vscode` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
