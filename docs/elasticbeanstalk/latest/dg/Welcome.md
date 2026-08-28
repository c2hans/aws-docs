---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html
---

# What is AWS Elastic Beanstalk?
<a name="Welcome"></a>

With Elastic Beanstalk you can deploy web applications into the AWS Cloud on a variety of supported platforms. You build and deploy your applications. Elastic Beanstalk provisions Amazon EC2 instances, configures load balancing, sets up health monitoring, and dynamically scales your environment.

In addition to *web server* environments, Elastic Beanstalk also provides *worker* environments which you can use to process messages from an Amazon SQS queue, useful for asynchronous or long-running tasks. For more information, see [Elastic Beanstalk worker environments](using-features-managing-env-tiers.md).

![Illustrative diagram showing the relationship between an Elastic Beanstalk application and web/worker environments.](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/aeb-overview.png)

## Supported platforms
<a name="welcome-platform-support"></a>

Elastic Beanstalk supports applications developed in Go, Java, .NET, Node.js, PHP, Python, and Ruby. Elastic Beanstalk also supports Docker containers, where you can choose your own programming language and application dependencies. When you deploy your application, Elastic Beanstalk builds the selected supported platform version and provisions one or more AWS resources, such as Amazon EC2 instances, in your AWS account to run your application.

You can interact with Elastic Beanstalk through the Elastic Beanstalk console, the AWS Command Line Interface (AWS CLI), or the EB CLI, a high-level command line tool designed specifically for Elastic Beanstalk.

You can perform most deployment tasks, such as changing the size of your fleet of Amazon EC2 instances or monitoring your application, directly from the Elastic Beanstalk web interface (console).

To learn more about how to deploy a sample web application using Elastic Beanstalk, see [Learn how to get started with Elastic Beanstalk](GettingStarted.md).

## Application deploy workflow
<a name="welcome-workflow"></a>

To use Elastic Beanstalk, you create an application, then upload your application source bundle to Elastic Beanstalk. Next, you provide information about the application, and Elastic Beanstalk automatically launches an environment and creates and configures the AWS resources needed to run your code.

After you create and deploy your application and your environment is launched, you can manage your environment and deploy new application versions. Information about the application—including metrics, events, and environment status—is made available through the Elastic Beanstalk console, APIs, and Command Line Interfaces.

 The following diagram illustrates Elastic Beanstalk workflow:

![Elastic Beanstalk workflow.](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/images/clearbox-flow-00.png)

## Pricing
<a name="Welcome.pricing"></a>

There is no additional charge for Elastic Beanstalk. You pay only for the underlying AWS resources that your application consumes. For details about pricing, see the [Elastic Beanstalk service detail page](https://aws.amazon.com/elasticbeanstalk).

## Next steps
<a name="Welcome.WhereToGo"></a>

We recommend the tutorial, [Getting started tutorial](GettingStarted.md), to start using Elastic Beanstalk. The tutorial steps you through creating, viewing, and updating a sample Elastic Beanstalk application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
