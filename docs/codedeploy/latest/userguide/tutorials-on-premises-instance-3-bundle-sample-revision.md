---
source_url: https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorials-on-premises-instance-3-bundle-sample-revision.html
---

# Step 3: Bundle and upload your application revision to Amazon S3
<a name="tutorials-on-premises-instance-3-bundle-sample-revision"></a>

Before you can deploy your application revision, you'll need to bundle the files, and then upload the file bundle to an Amazon S3 bucket. Follow the instructions in [Create an application with CodeDeploy](applications-create.md) and [Push a revision for CodeDeploy to Amazon S3 (EC2/On-Premises deployments only)](application-revisions-push.md). (Although you can give the application and deployment group any name, we recommend you use `CodeDeploy-OnPrem-App` for the application name and `CodeDeploy-OnPrem-DG` for the deployment group name.) After you have completed those instructions, return to this page.

**Note**
Alternatively, you can upload the file bundle to a GitHub repository and deploy it from there. For more information, see [Integrating CodeDeploy with GitHub](integrations-partners-github.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
