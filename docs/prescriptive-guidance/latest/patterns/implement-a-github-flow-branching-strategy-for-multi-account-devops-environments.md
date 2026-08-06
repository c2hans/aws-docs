---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-a-github-flow-branching-strategy-for-multi-account-devops-environments.html
---

# Implement a GitHub Flow branching strategy for multi-account DevOps environments
<a name="implement-a-github-flow-branching-strategy-for-multi-account-devops-environments"></a>

*Mike Stephens and Abhilash Vinod, Amazon Web Services*

## Summary
<a name="implement-a-github-flow-branching-strategy-for-multi-account-devops-environments-summary"></a>

When managing a source code repository, different branching strategies affect the software development and release processes that development teams use. Examples of common branching strategies include Trunk, GitHub Flow, and Gitflow. These strategies use different branches, and the activities performed in each environment are different. Organizations that are implementing DevOps processes would benefit from a visual guide to help them understand the differences between these branching strategies. Using this visual in your organization helps development teams align their work and follow organizational standards. This pattern provides this visual and describes the process of implementing a GitHub Flow branching strategy in your organization.

This pattern is part of a documentation series about choosing and implementing DevOps branching strategies for organizations with multiple AWS accounts. This series is designed to help you apply the correct strategy and best practices from the outset, to streamline your experience in the cloud. GitHub Flow is just one possible branching strategy that your organization can use. This documentation series also covers [Trunk](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-a-trunk-branching-strategy-for-multi-account-devops-environments.html) and [Gitflow](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-a-gitflow-branching-strategy-for-multi-account-devops-environments.html) branching models. If you haven't done so already, we recommend that you review [Choosing a Git branching strategy for multi-account DevOps environments](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/) prior to implementing the guidance in this pattern. Please use due diligence to choose the right branching strategy for your organization.

This guide provides a diagram that shows how an organization might implement the GitHub Flow strategy. It is recommended that you review the [AWS Well-Architected DevOps Guidance](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/devops-guidance.html) to review best practices. This pattern includes recommended tasks, steps, and restrictions for each step in the DevOps process.

## Prerequisites and limitations
<a name="implement-a-github-flow-branching-strategy-for-multi-account-devops-environments-prereqs"></a>

**Prerequisites**
+ Git, [installed](https://git-scm.com/downloads). This is used as a source code repository tool.
+ Draw.io, [installed](https://github.com/jgraph/drawio-desktop/releases). This application is used to view and edit the diagram.

## Architecture
<a name="implement-a-github-flow-branching-strategy-for-multi-account-devops-environments-architecture"></a>

**Target architecture**

The following diagram can be used like a [Punnett square](https://en.wikipedia.org/wiki/Punnett_square) (Wikipedia). You line up the branches on the vertical axis with the AWS environments on the horizontal axis to determine what actions to perform in each scenario. The numbers indicate the sequence of the actions in the workflow. This example takes you from a `feature` branch through deployment in production.

![Punnett square of the GitHub Flow activities in each branch and environment.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/780a5bce-3cd2-4092-8537-b7a77c3d6b8d/images/8a2a774a-cd85-466e-838e-a9a1f3b58a63.png)

For more information about the AWS accounts, environments, and branches in a GitHub Flow approach, see [Choosing a Git branching strategy for multi-account DevOps environments](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach).

**Automation and scale**

Continuous integration and continuous delivery (CI/CD) is the process of automating the software release lifecycle. It automates much or all of the manual processes traditionally required to get new code from an initial commit into production. A CI/CD pipeline encompasses the sandbox, development, testing, staging, and production environments. In each environment, the CI/CD pipeline provisions any infrastructure that is needed to deploy or test the code. By using CI/CD, development teams can make changes to code that are then automatically tested and deployed. CI/CD pipelines also provide governance and guardrails for development teams by enforcing consistency, standards, best practices, and minimal acceptance levels for feature acceptance and deployment. For more information, see [Practicing Continuous Integration and Continuous Delivery on AWS](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/welcome.html).

AWS offers a suite of developer services that are designed to help you build CI/CD pipelines. For example, [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) is a fully managed continuous delivery service that helps you automate your release pipelines for fast and reliable application and infrastructure updates. [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) compiles source code, runs tests, and produces ready-to-deploy software packages. For more information, see [Developer Tools on AWS](https://aws.amazon.com/products/developer-tools/).

## Tools
<a name="implement-a-github-flow-branching-strategy-for-multi-account-devops-environments-tools"></a>

**AWS services and tools**

AWS provides a suite of developer services that you can use to implement this pattern:
+ [AWS CodeArtifact](https://docs.aws.amazon.com/codeartifact/latest/ug/welcome.html) is a highly scalable, managed artifact repository service that helps you store and share software packages for application development.
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) is a fully managed build service that helps you compile source code, run unit tests, and produce artifacts that are ready to deploy.
+ [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) automates deployments to Amazon Elastic Compute Cloud (Amazon EC2) or on-premises instances, AWS Lambda functions, or Amazon Elastic Container Service (Amazon ECS) services.
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) helps you quickly model and configure the different stages of a software release and automate the steps required to release software changes continuously.

**Other tools**
+ [Draw.io Desktop](https://github.com/jgraph/drawio-desktop/releases) is an application for making flowcharts and diagrams. The code repository contains templates in .drawio format for Draw.io.
+ [Figma](https://www.figma.com/design-overview/) is an online design tool designed for collaboration. The code repository contains templates in .fig format for Figma.

**Code repository**

This source file for the diagram in this pattern is available in the GitHub [Git Branching Strategy for GitHub Flow](https://github.com/awslabs/git-branching-strategies-for-multiaccount-devops/tree/main/github-flow) repository. It includes files in PNG, draw.io, and Figma formats. You can modify these diagrams to support your organization's processes.

## Best practices
<a name="implement-a-github-flow-branching-strategy-for-multi-account-devops-environments-best-practices"></a>

Follow the best practices and recommendations in [AWS Well-Architected DevOps Guidance](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/devops-guidance.html) and [Choosing a Git branching strategy for multi-account DevOps environments](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/). These help you effectively implement GitHub Flow-based development, foster collaboration, improve code quality, and streamline the development process.

## Epics
<a name="implement-a-github-flow-branching-strategy-for-multi-account-devops-environments-epics"></a>

### Reviewing the GitHub Flow workflows
<a name="reviewing-the-github-flow-workflows"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Review the standard GitHub Flow process. | 1. In the sandbox environment, the developer creates a `feature` branch from the `main` branch and uses the naming pattern `feature/<ticket>_<initials>_<short description>`.<br />2. The developer adds one or more commits to the `feature` branch, each representing a discrete change or improvement.<br />3. The developer opens a merge request (MR) to merge the changes into the `main` branch. This initiates a review process.<br />4. During the review process, developers discuss the code changes and provide feedback. The goal is to ensure that the changes are of high quality and meet the project's standards.<br />5. After the developer creates the merge request, an automated build process starts and deploys the changes in the `feature` branch to the development environment.<br />6. Automated tests verify the integrity and quality of the changes encapsulated in the merge request. A successful build, successful deployment, and successful testing are required to complete the merge request.<br />7. When the review process is complete, the changes are merged into the `main` branch.<br />8. An approver manually approves the deployment of the release artifacts to the testing environment.<br />9. An approver manually approves the deployment of the release artifacts to the staging environment.<br />10. An approver manually approves the deployment of the release artifacts to the production environment. | DevOps engineer |
| Review the bugfix GitHub Flow process. | 1. The developer creates a `bugfix` branch from the `main` branch and uses the naming pattern `bugfix/<ticket number>_<developer initials>_<descriptor>`.<br />2. The developer fixes the issue, commits the fix, and builds the `bugfix` branch.<br />3. The developer opens a merge request to merge the `bugfix` branch into the `main` branch. This initiates a review process.<br />4. During the review process, developers discuss the code changes and provide feedback.<br />5. Upon review completion and approval, the developer completes the merge request of the `bugfix` branch into the `main` branch.<br />6. An approver manually approves the deployment of the release artifacts to higher environments. | DevOps engineer |
| Review the hotfix GitHub Flow process. | GitHub Flow is designed to enable continuous delivery, where code changes are frequently and reliably deployed to higher environments. The key is that every `feature` branch is deployable at any time.<br />`Hotfix` branches, which are akin to `feature` or `bugfix` branches, can follow the same process as either of these other branches. However, given their urgency, hotfixes typically have a higher priority. Depending on the team's policies and the immediacy of the situation, certain steps in the process could be expedited. For instance, code reviews for hotfixes might be fast-tracked. Therefore, while the hotfix process parallels the feature or bugfix process, the urgency surrounding hotfixes may warrant modifications in the procedural adherence. It's crucial to establish guidelines about managing hotfixes to make sure that they are handled efficiently and securely. | DevOps engineer |

## Troubleshooting
<a name="implement-a-github-flow-branching-strategy-for-multi-account-devops-environments-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Branch conflicts | A common issue that can occur with the GitHub Flow model is where a hotfix needs to occur in production but a corresponding change needs to occur in a `feature`, `bugfix`, or `hotfix` branch where the same resources are being modified. We recommend that you frequently merge changes from `main` into lower branches to avoid significant conflicts when you merge to `main`. |
| Team maturity | GitHub Flow encourages daily deployments to higher environments, embracing true continuous integration and continuous delivery (CI/CD). It is imperative that the team has the engineering maturity to build features and create automation tests for them. The team must perform an exhaustive merge request review before changes are approved. This fosters a robust engineering culture that promotes quality, accountability, and efficiency in the development process. |

## Related resources
<a name="implement-a-github-flow-branching-strategy-for-multi-account-devops-environments-resources"></a>

This guide doesn't include training for Git; however, there are many high-quality resources available on the internet if you need this training. We recommend that you start with the [Git documentation](https://git-scm.com/doc) site.

The following resources can help you with your GitHub Flow branching journey in the AWS Cloud.

**AWS DevOps guidance**
+ [AWS DevOps Guidance](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/devops-guidance.html)
+ [AWS Deployment Pipeline Reference Architecture](https://pipelines.devops.aws.dev/)
+ [What is DevOps?](https://aws.amazon.com/devops/what-is-devops/)
+ [DevOps resources](https://aws.amazon.com/devops/resources/)

**GitHub Flow guidance**
+ [GitHub Flow Quickstart Tutorial](https://docs.github.com/en/get-started/using-github/github-flow) (GitHub)
+ [Why GitHub Flow?](https://githubflow.github.io/)

**Other resources**
+ [Twelve-factor app methodology](https://12factor.net/) (12factor.net)
