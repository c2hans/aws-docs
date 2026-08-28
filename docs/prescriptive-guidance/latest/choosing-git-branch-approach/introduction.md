---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/introduction.html
---

# Choosing a Git branching strategy for multi-account DevOps environments
<a name="introduction"></a>

*Mike Stephens, Abhilash Vinod, and Rayjan Wilson, Amazon Web Services*

Moving to a cloud-based approach and delivering software solutions on AWS can be transformative. It might require changes to your software development lifecycle process. Typically, multiple AWS accounts are used during the development process in the AWS Cloud. Choosing a compatible Git branching strategy to pair with your DevOps processes is essential to success. Choosing the right Git branching strategy for your organization helps you concisely communicate DevOps standards and best practices across development teams. Git branching can be simple in a single environment, but it can become confusing when applied across multiple environments, such as sandbox, development, testing, staging, and production environments. Having multiple environments increases the complexity of the DevOps implementation.

This guide provides visual diagrams of Git branching strategies that show how an organization can implement a multi-account DevOps process. Visual guides help teams understand how to merge their Git branching strategies with their DevOps practices. Using a standard branching model, like Gitflow, GitHub Flow, or Trunk, for managing the source code repository helps development teams align their work. These teams can also use standard Git training resources on the internet to understand and implement those models and strategies.

For DevOps best practices on AWS, review the [DevOps Guidance](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/devops-guidance.html) in AWS Well-Architected. As you review this guide, use due diligence to select the right branching strategy for your organization. Some strategies might fit your use case better than others.

## Objectives
<a name="objectives"></a>

This guide is part of a documentation series about choosing and implementing DevOps branching strategies for organizations with multiple AWS accounts. This series is designed to help you apply the strategy that best meets your requirements, goals, and best practices from the outset, to streamline your experience in the AWS Cloud. This guide does not contain DevOps executable scripts because they vary based on the continuous integration and continuous delivery (CI/CD) engine and technology frameworks that your organization uses.

This guide explains the differences between three common Git branching strategies: GitHub Flow, Gitflow, and Trunk. The recommendations in this guide help teams identify a branching strategy that aligns with their organizational goals. After reviewing this guide, you should be able to choose a branching strategy for your organization. After choosing a strategy, you can use one of the following patterns to help you implement that strategy with your development teams:
+ [Implement a Trunk branching strategy for multi-account DevOps environments](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-a-trunk-branching-strategy-for-multi-account-devops-environments.html)
+ [Implement a GitHub Flow branching strategy for multi-account DevOps environments](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-a-github-flow-branching-strategy-for-multi-account-devops-environments.html)
+ [Implement a Gitflow branching strategy for multi-account DevOps environments](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-a-gitflow-branching-strategy-for-multi-account-devops-environments.html)

It's important to note that what works for one organization, team, or project might not be suitable for others. The choice between Git branching strategies depends on various factors, such as team size, project requirements, and the desired balance between collaboration, integration frequency, and release management.

## Using CI/CD practices
<a name="using-ci-cd-practices"></a>

AWS recommends that you implement continuous integration and continuous delivery (CI/CD), which is the process of automating the software release lifecycle. It automates much or all of the manual DevOps processes that are traditionally required to get new code from development into production. A CI/CD pipeline encompasses the sandbox, development, testing, staging, and production environments. In each environment, the CI/CD pipeline provisions any infrastructure that is needed to deploy or test the code. By using CI/CD, development teams can make changes to code that are then automatically tested and deployed. CI/CD pipelines also provide governance and guardrails for development teams. They enforce consistency, standards, best practices, and minimum acceptance levels for feature acceptance and deployment. For more information, see [Practicing Continuous Integration and Continuous Delivery on AWS](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/welcome.html).

All of the branching strategies discussed in this guide are well suited to CI/CD practices. The complexity of the CI/CD pipeline increases with the complexity of the branching strategy. For example, Gitflow is the most complex branching strategy discussed in this guide. CI/CD pipelines for this strategy require more steps (such as for compliance reasons), and they must support multiple, simultaneous production releases. Using CI/CD also becomes more important as the complexity of the branching strategy increases. This is because CI/CD establishes guardrails and mechanisms for development teams that prevents developers from intentionally or unintentionally circumnavigating the defined process.

AWS offers a suite of developer services that are designed to help you build CI/CD pipelines. For example, [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) is a fully managed continuous delivery service that helps you automate your release pipelines for fast and reliable application and infrastructure updates. [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) compiles source code, runs tests, and produces ready-to-deploy software packages. For more information, see [Developer Tools on AWS](https://aws.amazon.com/products/developer-tools/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
