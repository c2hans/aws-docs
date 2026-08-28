---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/understanding-the-dev-ops-environments.html
---

# Understanding the DevOps environments
<a name="understanding-the-dev-ops-environments"></a>

To understand the branching strategies, you must understand the purpose and activities that occur in each environment. Establishing several environments helps you separate the development activities into stages, monitor those activities, and prevent the unintentional release of unapproved features. You can have one or more AWS accounts in each environment.

Most organizations have several environments outlined for use. However, the number of environments can vary by organization and according to software development policies. This documentation series assumes that you have the following five, common environments that span your development pipeline, although they might be called by different names:
+ **Sandbox** – An environment where developers write code, make mistakes, and perform proof of concept work.
+ **Development** – An environment where developers integrate their code to confirm that it all works as a single, cohesive application.
+ **Testing** – An environment where QA teams or acceptance testing takes place. Teams often do performance or integration testing in this environment.
+ **Staging** – A preproduction environment where you validate that the code and infrastructure perform as expected under production-equivalent circumstances. This environment is configured to be as similar as possible to the production environment.
+ **Production** – An environment that handles traffic from your end users and customers.

This section describes each environment in detail. It also describes the build steps, deployment steps, and exit criteria for each environment so that you can proceed to the next. The following image shows these environments in sequence.

![Common DevOps environments in sequential order](http://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/images/guide-img/2c642ab1-73c3-487b-9aff-d887904354b7/images/d1ccb5b9-30b4-4bcf-b9dd-efa3f0be0f19.png)

Topics in this section:
+ [Sandbox environment](sandbox-environment.md)
+ [Development environment](development-environment.md)
+ [Testing environment](testing-environment.md)
+ [Staging environment](staging-environment.md)
+ [Production environment](production-environment.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
