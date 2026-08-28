---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_NET-linux.healthstatus.html
---

# Monitoring application health
<a name="create_deploy_NET-linux.healthstatus"></a>

This topic explains how to monitor the health of your application's website. It's important to know that your production website is available and responding to requests. Elastic Beanstalk provides features to help you monitor your application's responsiveness. It monitors statistics about your application and alerts you when thresholds are exceeded.

For information about the health monitoring provided by Elastic Beanstalk, see [Basic health reporting](using-features.healthstatus.md).

You can access operational information about your application by using either the AWSToolkit for Visual Studio or the AWS Management Console.

The toolkit displays your environment's status and application health in the **Status** field.

**To monitor application health**

1. In the AWS Toolkit for Visual Studio, in **AWS Explorer**, expand the Elastic Beanstalk node, and then expand your application node.

1. Open the context (right-click) menu for your application environment and select **View Status**.

1. On your application environment tab, select **Monitoring**.

   The **Monitoring** panel includes a set of graphs showing resource usage for your particular application environment.
**Note**
By default, the time range is set to the last hour. To modify this setting, in the **Time Range** list, select a different time range.

You can use the AWS Toolkit for Visual Studio or the AWS Management Console to view events associated with your application.

**To view application events**

1. In the AWS Toolkit for Visual Studio, in **AWS Explorer**, expand the Elastic Beanstalk node and your application node.

1. Open the context (right-click) menu for your application environment and select **View Status**.

1. In your application environment tab, select **Events**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
