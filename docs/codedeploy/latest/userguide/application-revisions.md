---
source_url: https://docs.aws.amazon.com/codedeploy/latest/userguide/application-revisions.html
---

# Working with application revisions for CodeDeploy
<a name="application-revisions"></a>

In CodeDeploy, a revision contains a version of the source files CodeDeploy will deploy to your instances or scripts CodeDeploy will run on your instances.

You plan the revision, add an AppSpec file to the revision, and then push the revision to Amazon S3 or GitHub. After you push the revision, you can deploy it.

**Topics**
+ [Plan a revision](application-revisions-plan.md)
+ [Add an AppSpec File](application-revisions-appspec-file.md)
+ [Choose a repository type](application-revisions-repository-type.md)
+ [Push a revision](application-revisions-push.md)
+ [View application revision details](application-revisions-view-details.md)
+ [Register an application revision](application-revisions-register.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
