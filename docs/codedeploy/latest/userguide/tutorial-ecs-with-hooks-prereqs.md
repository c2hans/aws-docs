---
source_url: https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-ecs-with-hooks-prereqs.html
---

# Prerequisites
<a name="tutorial-ecs-with-hooks-prereqs"></a>

To successfully complete this tutorial, you must first:
+  Complete the prerequisites in [Prerequisites](tutorial-ecs-prereqs.md) for [Tutorial: Deploy an application into Amazon ECS](tutorial-ecs-deployment.md).
+  Complete the steps in [Tutorial: Deploy an application into Amazon ECS](tutorial-ecs-deployment.md). Make a note of the following:
  +  The name of your load balancer.
  +  The names of your target groups.
  +  The port used by your load balancer's listener.
  +  The ARN of your load balancer. You use this to create a new listener.
  +  The ARN of one of your target groups. You use this to create a new listener.
  +  The CodeDeploy application and deployment group you create.
  +  The AppSpec file you create that is used by your CodeDeploy deployment. You edit this file in this tutorial.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
