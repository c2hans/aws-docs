---
source_url: https://docs.aws.amazon.com/solutions/latest/deploy-to-done/quickstart.html
---

# Quickstart
<a name="quickstart"></a>

Deploy a sample application to AWS Elastic Beanstalk. The goal is to see the full deployment experience before reading about architecture, positioning, or operational philosophy.

**What you will do:**

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk). If prompted, choose **Switch to new version** to access the latest console experience.

1. Choose **Deploy application**. This process triggers creating the environment and application together.

1. On the **Deployment mode** step, choose **Standard** (a dedicated environment per application, including Windows and .NET Framework workloads) or **Cluster** (multiple applications on shared infrastructure). This choice comes before you configure the application.

1. Name your application. In Standard Mode, select a platform (Node.js, Python, Java, .NET, or another supported runtime). In Cluster Mode, there is no platform to choose; you provide source code, a Dockerfile, or a container image.

1. Use the sample application provided by the console, or upload your own source bundle.

1. Scroll to the bottom of the configuration page. Skip intermediary steps for networking and health monitoring; these can be configured later.

1. Choose **Create**. Elastic Beanstalk creates the application and provisions its first environment. Wait for provisioning to finish.

1. When the health indicator turns green, choose the environment URL. Your application is live.

No VPC design. No load balancer configuration. No IAM policy authoring. The platform provisions networking, compute, scaling, health monitoring, and a public endpoint as part of the creation workflow.

**What just happened underneath:** Elastic Beanstalk created an Auto Scaling group, configured a load balancer, set up health checks, attached security groups, provisioned compute, deployed your application, and started monitoring. You provided the application. AWS built and now operates the environment.

**Important: Application and Environment.** An *application* is the logical container for your work; it groups your code versions and the environments that run them. An *environment* is the collection of running AWS resources that serves one version of your code at a live URL. An application holds one or more environments (for example, one application with separate development, staging, and production environments). You always begin by creating the application; Elastic Beanstalk launches your first environment inside it as part of the same flow, so there is no separate "create an environment" step to do first. In Standard Mode you choose a platform for the environment; in Cluster Mode there is no platform to choose because you provide your application as a container.

## Go Deeper
<a name="quickstart-go-deeper"></a>

**Go Deeper**
[Learn How to Get Started with Elastic Beanstalk (Console Tutorial)](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.html) - Full walkthrough with screenshots
[QuickStart: Deploy a Node.js Application](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/nodejs-quickstart.html) - Node.js deployment walkthrough
[QuickStart: Deploy a Docker Application](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/docker-quickstart.html) - Container-based quickstart
[QuickStart: Deploy .NET Core on Linux](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-linux-quickstart.html) - .NET deployment path
