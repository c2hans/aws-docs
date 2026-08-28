---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET-linux.advanced-otions.html
---

# Configuring additional environment options using AWS toolkit for Visual Studio
<a name="create_deploy_NET-linux.advanced-otions"></a>

Elastic Beanstalk defines a large number of configuration options that you can use to configure your environment's behavior and the resources that it contains. Configuration options are organized into namespaces like `aws:autoscaling:asg`. Each namespace defines options for an environment's Auto Scaling group. The **Advanced** panel lists the configuration option namespaces in alphabetical order that you can update after environment creation.

For a complete list of namespaces and options, including default and supported values for each, see [General options for all environments](command-options-general.md) and [.NET Core on Linux platform options](command-options-specific.md#command-options-dotnet-core-linux).

![Screenshot of advanced configurations options panel in Visual Studio Toolkit for Elastic Beanstalk](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/aeb-vs-linux-advanced-tab.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
