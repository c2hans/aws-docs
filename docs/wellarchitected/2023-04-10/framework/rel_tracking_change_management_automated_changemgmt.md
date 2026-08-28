---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/rel_tracking_change_management_automated_changemgmt.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL08-BP05 Deploy changes with automation
<a name="rel_tracking_change_management_automated_changemgmt"></a>

 Deployments and patching are automated to eliminate negative impact.

 Making changes to production systems is one of the largest risk areas for many organizations. We consider deployments a first-class problem to be solved alongside the business problems that the software addresses. Today, this means the use of automation wherever practical in operations, including testing and deploying changes, adding or removing capacity, and migrating data. AWS CodePipeline lets you manage the steps required to release your workload. This includes a deployment state using AWS CodeDeploy to automate deployment of application code to Amazon EC2 instances, on-premises instances, serverless Lambda functions, or Amazon ECS services.

**Recommendation**
 Although conventional wisdom suggests that you keep humans in the loop for the most difficult operational procedures, we suggest that you automate the most difficult procedures for that very reason.

 **Common anti-patterns:**
+  Manually performing changes.
+  Skipping steps in your automation through emergency work flows.
+  Not following your plans.

 **Benefits of establishing this best practice:** Using automation to deploy all changes removes the potential for introduction of human error and provides the ability to test before changing production to ensure that your plans are complete.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Automate your deployment pipeline. Deployment pipelines allow you to invoke automated testing and detection of anomalies, and either halt the pipeline at a certain step before production deployment, or automatically roll back a change.
  +  [The Amazon Builders' Library: Ensuring rollback safety during deployments](https://aws.amazon.com/builders-library/ensuring-rollback-safety-during-deployments)
  +  [The Amazon Builders' Library: Going faster with continuous delivery](https://aws.amazon.com/builders-library/going-faster-with-continuous-delivery/)
    +  Use AWS CodePipeline (or a trusted third-party product) to define and run your pipelines.
      +  Configure the pipeline to start when a change is committed to your code repository.
        +  [What is AWS CodePipeline?](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)
      +  Use Amazon Simple Notification Service (Amazon SNS) and Amazon Simple Email Service (Amazon SES) to send notifications about problems in the pipeline or integrate with a team chat tool, like Amazon Chime.
        +  [What is Amazon Simple Notification Service?](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)
        +  [What is Amazon SES?](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/Welcome.html)
        +  [What is Amazon Chime?](https://docs.aws.amazon.com/chime/latest/ug/what-is-chime.html)
        +  [Automate chat messages with webhooks.](https://docs.aws.amazon.com/chime/latest/ug/webhooks.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [APN Partner: partners that can help you create automated deployment solutions](https://aws.amazon.com/partners/find/results/?keyword=devops)
+  [AWS Marketplace: products that can be used to automate your deployments](https://aws.amazon.com/marketplace/search/results?searchTerms=DevOps)
+  [Automate chat messages with webhooks.](https://docs.aws.amazon.com/chime/latest/ug/webhooks.html)
+  [The Amazon Builders' Library: Ensuring rollback safety during deployments](https://aws.amazon.com/builders-library/ensuring-rollback-safety-during-deployments)
+  [The Amazon Builders' Library: Going faster with continuous delivery](https://aws.amazon.com/builders-library/going-faster-with-continuous-delivery/)
+  [What Is AWS CodePipeline?](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)
+  [What Is CodeDeploy?](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html)
+  [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html)
+  [What is Amazon SES?](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/Welcome.html)
+  [What is Amazon Simple Notification Service?](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)

 **Related videos:**
+  [AWS Summit 2019: CI/CD on AWS](https://youtu.be/tQcF6SqWCoY)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
