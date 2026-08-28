---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET.managing.html
---

# Managing your Elastic Beanstalk application environments
<a name="create_deploy_NET.managing"></a>

With the AWS Toolkit for Visual Studio and the AWS Management Console, you can change the provisioning and configuration of the AWS resources used by your application environments. For information on how to manage your application environments using the AWS Management Console, see [Managing Elastic Beanstalk environments](using-features.managing.md). This section discusses the specific service settings you can edit in the AWS Toolkit for Visual Studio as part of your application environment configuration.

## Changing environment configurations settings
<a name="create_deploy_NET.managing.env"></a>

When you deploy your application, Elastic Beanstalk configures a number of AWS cloud computing services. You can control how these individual services are configured using the AWS Toolkit for Visual Studio.

**To edit an application's environment settings**
+ Expand the Elastic Beanstalk node and your application node. Then right-click your Elastic Beanstalk environment in **AWS Explorer**. Select **View Status**.

  You can now configure settings for the following:
  + Server
  + Load balancing
  + Autoscaling
  + Notifications
  + Environment properties

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
