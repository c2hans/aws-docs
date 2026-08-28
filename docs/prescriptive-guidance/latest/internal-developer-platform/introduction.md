---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/internal-developer-platform/introduction.html
---

# Building an internal developer platform on AWS
<a name="introduction"></a>

*Omar Kahil, Amazon Web Services*

Traditionally, operations teams define and set up environments for developers, which can be a time-consuming and error-prone process. An *internal developer platform* is intended to modernize enterprise software delivery through a self-service portal. It is an internal product that helps developers independently manage environments, deployments, resources, and configurations. Organizations typically establish platform engineering teams to create and manage internal developer platforms.

According to [Gartner](https://www.gartner.com/en/articles/what-is-platform-engineering), by 2026, "80% of large software engineering organizations will establish platform engineering teams as internal providers of reusable services, components, and tools for application delivery." The goal of the platform engineering team is to solve the central problems of cooperation between software developers and operators. These goals include the following:

1. Help developers be self-sufficient

1. Reduce the cognitive load for developers

1. Encapsulate common best practices into reusable building blocks, known as *golden paths*

1. Automate many common tasks, such as provisioning clusters or continuous integration and continuous deployment (CI/CD) pipelines

The goal of building an internal developer platform is to guide your developers with well-defined standards and patterns, from development to production. The platform should not negatively affect developer productivity, and it should automate, secure, and centralize their tools and capabilities.

This guide helps you implement an internal developer platform on AWS. It focuses on the different platform capabilities and describes how to successfully build a platform that meets your business goals.  It also includes some modernization patterns that you can follow.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
