---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-directory-service-for-microsoft-ad-well-architected-analysis/operational-excellence-pillar.html
---

# Operational excellence pillar
<a name="operational-excellence-pillar"></a>

The operational excellence pillar focuses on running and monitoring systems, and continually improving processes and procedures. The following recommendations can help you meet the operational excellence design principles and architectural best practices for AWS Managed Microsoft AD.

**Key focus areas**
+ Automating changes
+ Responding to events
+ Defining standards to manage daily operations

## Perform operations as code
<a name="perform-operations-as-code"></a>
+ Apply infrastructure as a code (IaC) to deploy AWS Managed Microsoft AD. For more information, see the GitHub [quickstart-microsoft-activedirectory](https://github.com/aws-quickstart/quickstart-microsoft-activedirectory) repository.
+ Automate Microsoft Active Directory operations procedures whenever possible. For example, it's a best practice to automate the management of user objects, group objects, and Group Policy Objects (GPOs).
+ Automate the management of domain memberships (**join** and **unjoin**).

## Make frequent, small, reversible changes
<a name="make-frequent-small-reversible-changes"></a>
+ Store IaC such as templates and scripts in a source control service, such as [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html), GitHub, or GitLab.
+ Require IaC deployments to use a continuous integration and continuous delivery (CI/CD) service, such as [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) or [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html). These services compile, test, and deploy code in a test environment, before infrastructure is deployed on AWS and within Microsoft Active Directory.

## Refine operations procedures frequently
<a name="refine-operations-procedures-frequently"></a>
+ Test your infrastructure changes in a test environment before deploying any updates to your production servers.

## Anticipate failure
<a name="anticipate-failure"></a>
+ Load test your setup in a test environment before rolling out changes to production. For more information, see [How to use the Active Directory Performance Testing tool on Windows Server 2012](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/how-to-use-the-active-directory-performance-testing-tool-on-windows-server-2012/256937) on the Microsoft Blog.
+ Automate AWS Managed Microsoft AD scaling based on your organization's utilization metrics. For more information, see [How to automate AWS Managed Microsoft AD scaling based on utilization metrics](https://aws.amazon.com/blogs/security/how-to-automate-aws-managed-microsoft-ad-scaling-based-on-utilization-metrics/) on the AWS Blog.
+ Setup Amazon Simple Notification Service (Amazon SNS) messaging to receive metrics alarms and status changes. For more information, see [Configure directory status notifications](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_enable_notifications.html) in the AWS Directory Service documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
