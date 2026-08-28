---
source_url: https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-continuous-delivery-integration.html
---

# Continuous delivery and continuous integration
<a name="concepts-continuous-delivery-integration"></a>

CodePipeline is a *continuous delivery* service that automates the building, testing, and deployment of your software into production.

[Continuous delivery](https://aws.amazon.com/devops/continuous-delivery/) is a software development methodology where the release process is automated. Every software change is automatically built, tested, and deployed to production. Before the final push to production, a person, an automated test, or a business rule decides when the final push should occur. Although every successful software change can be immediately released to production with continuous delivery, not all changes need to be released right away.

[Continuous integration](https://aws.amazon.com/devops/continuous-integration/) is a software development practice where members of a team use a version control system and frequently integrate their work to the same location, such as a main branch. Each change is built and verified to detect integration errors as quickly as possible. Continuous integration is focused on automatically building and testing code, as compared to *continuous delivery*, which automates the entire software release process up to production.

For more information, see [Practicing Continuous Integration and Continuous Delivery on AWS: Accelerating Software Delivery with DevOps](https://d0.awsstatic.com/whitepapers/DevOps/practicing-continuous-integration-continuous-delivery-on-AWS.pdf).

You can use the CodePipeline console, the AWS Command Line Interface (AWS CLI), the AWS SDKs, or any combination of these to create and manage your pipelines.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
