---
source_url: https://docs.aws.amazon.com/transform/latest/userguide/dotnet-creating-repo-connector.html
---

# Creating a source code repository connector
<a name="dotnet-creating-repo-connector"></a>

After [Creating the AWS Transform .NET job plan](dotnet-creating-job-plan.md), on the **Tasks** tab, the left pane of the AWS Transform window lists the phases of the transformation job. The first phase is *Get resources to be transformed*. In this phase, you can *Invite collaborators* and *Connect a source code repository*. The right pane of the AWS Transform window is where you specify the details.

Each transformation job is required to have only one source code repository connector. The AWS Transform agent uses this connector to download your .NET codebase from GitHub, GitLab, or Bitbucket by using [AWS CodeConnections](https://docs.aws.amazon.com/dtconsole/latest/userguide/welcome-connections.html). You must set up AWS CodeConnections in the same Region as your AWS Transform job. Alternatively, you can [Connect to source code in Amazon S3](https://docs.aws.amazon.com/transform/latest/userguide/dotnet-connect-source-code-s3.html) instead of a source code repository.

**Note**
If you have an existing source code repository connector, AWS Transform will notify you. Select **Use existing connector** to use this connector. If you do not wish to use the existing connector, see [Deleting an existing connector](#deleting-existing-connector) before [Adding a new connector](#adding-new-connector). You can only have one source repository connector per job.

## Adding a new connector
<a name="adding-new-connector"></a>

To create a new source code repository connector:

1. Enter the AWS account number that you would like to use for the AWS CodeConnections connector.

1. If you have not set up AWS CodeConnections for the same AWS account, [Set up AWS CodeConnections](https://docs.aws.amazon.com/dtconsole/latest/userguide/setting-up-connections.html).

1. Use the [AWS Developer Tools Console](https://console.aws.amazon.com/codesuite/settings/connections) to create a connection to your [Bitbucket](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-create-bitbucket.html), [GitHub](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-create-github.html), [GitHub Enterprise Server](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-create-gheserver.html), [GitLab](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-create-gitlab.html), or [AzureDevOps](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-create-azure.html) repository.

1. Copy the Amazon Resource Name (ARN) of the connection you created.

1. Return to AWS Transform, and paste the ARN of the connection you created.

1. Enter a name for the connector.
**Note**
Do not enter personal information as part of the connector name.

1. Select **Initiate connector creation.**

1. AWS Transform makes the request to create a connector for AWS account you entered, in the same Region as the current transformation job, and notifies you that an approval request is ready to be approved by your AWS administrator in the AWS Management Console. Select **Copy the verification link**.

1. If you are the AWS administrator, sign into the AWS account and go to the verification link to approve the connection request. If you are not the AWS administrator, provide the verification link to your AWS administrator.

1. After the AWS administrator approves the connector request, select **Finalize connector** to complete the connector creation process. Should you wish to use a different connector, select **Restart**, to restart the connector creation process.

The Collaboration tab also includes details about your connector, which include:
+ Status -- Approved or Pending approval
+ AWS account ID
+ AWS Region
+ Connection ARN

## Deleting an existing connector
<a name="deleting-existing-connector"></a>

**Note**
If you have an existing source code repository connector, AWS Transform will notify you. Select either **Use existing connector** or **Delete and create a new connector**.

If you choose to delete an existing source code repository connect, AWS Transform will warn you before actually deleting the connector.

1. You can delete an existing connector a couple of ways:

   1. If AWS Transform prompts you to, you can select **Delete and create a new connector**.

   1. You can also select **restart** in the prompt, **To modify this connector, you must restart**.

1. AWS Transform warns you that restarting will delete the connector. To delete the connector, select **Restart** again.

1. AWS Transform warns you again that deleting the connector will remove the connection to your third party repository, such as Bitbucket, GitHub, and GitLab. Also, any AWS Transform jobs that are using this connector will fail if the connector is deleted. To confirm deletion, type *delete* and select **Delete**.

1. To add a new source code repository connector, see [Adding a new connector](#adding-new-connector).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transform` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
