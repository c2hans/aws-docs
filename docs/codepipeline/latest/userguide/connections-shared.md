---
source_url: https://docs.aws.amazon.com/codepipeline/latest/userguide/connections-shared.html
---

# Use a connection shared with another account
<a name="connections-shared"></a>

You can create and manage a shared connection using AWS RAM. This allows connections to be shared between AWS accounts for access to third-party repositories. This allows a single connection to be used in CodePipeline pipelines across accounts while reducing the need for users to manage and administer separate connections in each account.

To use shared connections in CodePipeline, do the following.
+ Create a connection using the Developer Tools console under **Settings**. See [Create a Connection](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-create.html).
+ Set up the resource share using AWS RAM. See [Share connections with AWS accounts](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-share.html).
+ When you use the CodePipeline console **Create pipeline** wizard or **Edit action** page to choose the connection provider, such as the **Bitbucket** provider option, you can choose the connection that has been shared with the target account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
