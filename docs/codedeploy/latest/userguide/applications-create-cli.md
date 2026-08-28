---
source_url: https://docs.aws.amazon.com/codedeploy/latest/userguide/applications-create-cli.html
---

# Create an application (CLI)
<a name="applications-create-cli"></a>

To use the AWS CLI to create an application, call the [create-application](https://docs.aws.amazon.com/cli/latest/reference/deploy/create-application.html) command, specifying a name that uniquely represents the application. (In an AWS account, a CodeDeploy application name can be used only once per Region. You can reuse an application name in different Regions.)

After you use the AWS CLI to create an application, the next step is to create a deployment group that specifies the instances to which to deploy revisions. For instructions, see [Create a deployment group with CodeDeploy](deployment-groups-create.md).

After you create the deployment group, the next step is to prepare a revision to deploy to the application and deployment group. For instructions, see [Working with application revisions for CodeDeploy](application-revisions.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
