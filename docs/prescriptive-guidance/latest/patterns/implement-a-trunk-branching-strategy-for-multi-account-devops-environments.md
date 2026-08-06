---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-a-trunk-branching-strategy-for-multi-account-devops-environments.html
---

# Implement a Trunk branching strategy for multi-account DevOps environments
<a name="implement-a-trunk-branching-strategy-for-multi-account-devops-environments"></a>

*Mike Stephens and Rayjan Wilson, Amazon Web Services*

## Summary
<a name="implement-a-trunk-branching-strategy-for-multi-account-devops-environments-summary"></a>

When managing a source code repository, different branching strategies affect the software development and release processes that development teams use. Examples of common branching strategies include Trunk, GitHub Flow, and Gitflow. These strategies use different branches, and the activities performed in each environment are different. Organizations that are implementing DevOps processes would benefit from a visual guide to help them understand the differences between these branching strategies. Using this visual in your organization helps development teams align their work and follow organizational standards. This pattern provides this visual and describes the process of implementing a Trunk branching strategy in your organization.

This pattern is part of a documentation series about choosing and implementing DevOps branching strategies for organizations with multiple AWS accounts. This series is designed to help you apply the correct strategy and best practices from the outset, to streamline your experience in the cloud. Trunk is just one possible branching strategy that your organization can use. This documentation series also covers [GitHub Flow](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-a-github-flow-branching-strategy-for-multi-account-devops-environments.html) and [Gitflow](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-a-gitflow-branching-strategy-for-multi-account-devops-environments.html) branching models. If you haven't done so already, we recommend that you review [Choosing a Git branching strategy for multi-account DevOps environments](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/) prior to implementing the guidance in this pattern. Please use due diligence to choose the right branching strategy for your organization.

This guide provides a diagram that shows how an organization might implement the Trunk strategy. It is recommended that you review the official [AWS Well-Architected DevOps Guidance](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/devops-guidance.html) to review best practices. This pattern includes recommended tasks, steps, and restrictions for each step in the DevOps process.

## Prerequisites and limitations
<a name="implement-a-trunk-branching-strategy-for-multi-account-devops-environments-prereqs"></a>

**Prerequisites**
+ Git, [installed](https://git-scm.com/downloads). This is used as a  source code repository tool.
+ Draw.io, [installed](https://github.com/jgraph/drawio-desktop/releases). This application is used to view and edit the diagram.

## Architecture
<a name="implement-a-trunk-branching-strategy-for-multi-account-devops-environments-architecture"></a>

**Target architecture**

The following diagram can be used like a [Punnett square](https://en.wikipedia.org/wiki/Punnett_square) (Wikipedia). You line up the branches on the vertical axis with the AWS environments on the horizontal axis to determine what actions to perform in each scenario. The numbers indicate the sequence of the actions in the workflow. This example takes you from a `feature` branch through deployment in production.

![Punnett square of the Trunk activities in each branch and environment](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/5df23e4d-84fe-4ab3-a54f-96b6406abc57/images/ad549ef4-90ad-47c1-bd01-f21d6ce5511a.png)

For more information about the AWS accounts, environments, and branches in a Trunk approach, see [Choosing a Git branching strategy for multi-account DevOps environments](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach).

**Automation and scale**

Continuous integration and continuous delivery (CI/CD) is the process of automating the software release lifecycle. It automates much or all of the manual processes traditionally required to get new code from an initial commit into production. A CI/CD pipeline encompasses the sandbox, development, testing, staging, and production environments. In each environment, the CI/CD pipeline provisions any infrastructure that is needed to deploy or test the code. By using CI/CD, development teams can make changes to code that are then automatically tested and deployed. CI/CD pipelines also provide governance and guardrails for development teams by enforcing consistency, standards, best practices, and minimal acceptance levels for feature acceptance and deployment. For more information, see [Practicing Continuous Integration and Continuous Delivery on AWS](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/welcome.html).

AWS offers a suite of developer services that are designed to help you build CI/CD pipelines. For example, [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) is a fully managed continuous delivery service that helps you automate your release pipelines for fast and reliable application and infrastructure updates. [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) compiles source code, runs tests, and produces ready-to-deploy software packages. For more information, see [Developer Tools on AWS](https://aws.amazon.com/products/developer-tools/).

## Tools
<a name="implement-a-trunk-branching-strategy-for-multi-account-devops-environments-tools"></a>

**AWS services and tools**

AWS provides a suite of developer services that you can use to implement this pattern:
+ [AWS CodeArtifact](https://docs.aws.amazon.com/codeartifact/latest/ug/welcome.html) is a highly scalable, managed artifact repository service that helps you store and share software packages for application development.
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) is a fully managed build service that helps you compile source code, run unit tests, and produce artifacts that are ready to deploy.
+ [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) automates deployments to Amazon Elastic Compute Cloud (Amazon EC2) or on-premises instances, AWS Lambda functions, or Amazon Elastic Container Service (Amazon ECS) services.
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) helps you quickly model and configure the different stages of a software release and automate the steps required to release software changes continuously.

**Other tools**
+ [Draw.io Desktop](https://github.com/jgraph/drawio-desktop/releases) – An application for making flowcharts and diagrams.
+ [Figma](https://www.figma.com/design-overview/) is an online design tool designed for collaboration. The code repository contains templates in .fig format for Figma.

**Code repository**

This source file for the diagram in this pattern is available in the GitHub [Git Branching Strategy for Trunk](https://github.com/awslabs/git-branching-strategies-for-multiaccount-devops/tree/main/trunk) repository. It includes files in PNG, draw.io, and Figma formats. You can modify these diagrams to support your organization's processes.

## Best practices
<a name="implement-a-trunk-branching-strategy-for-multi-account-devops-environments-best-practices"></a>

Follow the best practices and recommendations in [AWS Well-Architected DevOps Guidance](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/devops-guidance.html) and [Choosing a Git branching strategy for multi-account DevOps environments](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/). These help you effectively implement Trunk-based development, foster collaboration, improve code quality, and streamline the development process.

## Epics
<a name="implement-a-trunk-branching-strategy-for-multi-account-devops-environments-epics"></a>

### Reviewing the Trunk workflow
<a name="reviewing-the-trunk-workflow"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Review the standard Trunk process. | 1. In the sandbox environment, the developer creates a `feature` branch from the `main` branch and uses the naming pattern `feature/<ticket>_<initials>_<short description>`.<br />2. The developer develops code and deploys the code to the sandbox environment iteratively in order to complete the ticket.The developer can optionally create a `sandbox` branch to run an automated build or deploy pipeline in the sandbox environment.<br />3. The developer creates a merge request from the `feature` branch into the `main` branch by using a squash merge.<br />4. A continuous integration and continuous delivery (CI/CD) pipeline automatically builds and publishes the artifacts from the `main` branch to the development environment.<br />5. An approver manually approves the deployment of the release artifacts to the development environment.<br />6. An approver manually approves the deployment of the release artifacts to the testing environment.<br />7. An approver manually approves the deployment of the release artifacts to the staging environment.<br />8. An approver manually approves the deployment of the release artifacts to the production environment. | DevOps engineer |

## Troubleshooting
<a name="implement-a-trunk-branching-strategy-for-multi-account-devops-environments-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Branch conflicts | A common issue that can occur with the Trunk model is where a hotfix needs to occur in production but a corresponding change needs to occur in a `feature` branch, where the same resources are being modified. We recommend that you frequently merge changes from `main` into lower branches to avoid significant conflicts on merge to `main`. |

## Related resources
<a name="implement-a-trunk-branching-strategy-for-multi-account-devops-environments-resources"></a>

This guide doesn't include training for Git; however, there are many high-quality resources available on the internet if you need this training. We recommend that you start with the [Git documentation](https://git-scm.com/doc) site.

The following resources can help you with your Trunk branching journey in the AWS Cloud.

**AWS DevOps guidance**
+ [AWS DevOps Guidance](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/devops-guidance.html)
+ [AWS Deployment Pipeline Reference Architecture](https://pipelines.devops.aws.dev/)
+ [What is DevOps?](https://aws.amazon.com/devops/what-is-devops/)
+ [DevOps resources](https://aws.amazon.com/devops/resources/)

**Trunk guidance**
+ [Trunk Based Development](https://trunkbaseddevelopment.com/)

**Other resources**
+ [Twelve-factor app methodology](https://12factor.net/) (12factor.net)
