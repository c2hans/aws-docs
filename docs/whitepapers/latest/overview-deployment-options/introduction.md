---
source_url: https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/introduction.html
---

# Introduction
<a name="introduction"></a>

 Designing a deployment solution for your application is a critical part of building a well-architected application on AWS. Based on the nature of your application and the underlying services that it requires, you can use AWS services to create a ﬂexible deployment solution that can be tailored to ﬁt the needs of both your application and your organization.

 The constantly growing catalog of AWS services not only complicates the process of deciding which services will compose your application architecture, but also the process of deciding how you will create, manage, and update your application. When designing a deployment solution on AWS, you should consider how your solution will address the following capabilities:
+  **Provision** - Create the raw infrastructure or managed service infrastructure required for your application.
+  **Configure** - Customize your infrastructure based on environment, runtime, security, availability, performance, network or other application requirements.
+  **Deploy** - Install or update your application components onto infrastructure resources and manage the transition from a previous application version to a new application version.
+  **Scale** - Proactively or reactively adjust the amount of resources available to your application based on a set of user-deﬁned criteria.
+  **Monitor** - Provide visibility into the resources that are launched as part of your application architecture. Track resource usage, deployment success or failure, application health, application logs, conﬁguration drift, and more.

 This whitepaper highlights the deployment services offered by AWS and outlines strategies for designing a successful deployment architecture for any type of application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
