---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/git-branching-strategies.html
---

# Git branching strategies
<a name="git-branching-strategies"></a>

In order of least to most complex, this guide describes the following Git-based branching strategies in detail:
+ **Trunk** – Trunk-based development is a software development practice in which all developers work on a single branch, typically called the `trunk` or `main` branch. The idea behind this approach is to keep the code base in a continuously releasable state by integrating code changes frequently and relying on automated testing and continuous integration.
+ **GitHub Flow** – GitHub Flow is a lightweight, branch-based workflow that was developed by GitHub. It is based on the idea of short-lived `feature` branches. When a feature is complete and ready to be deployed, the feature is merged into the `main` branch.
+ **Gitflow** – With a Gitflow approach, development is completed in individual feature branches. After approval, you merge `feature` branches into an integration branch that is usually named `develop`. When enough features have accumulated in the `develop` branch, a `release` branch is created to deploy the features to upper environments.

Each branching strategy has advantages and disadvantages. Although they all use the same environments, they don't all use the same branches or manual approval steps. In this section of the guide, review each branching strategy in detail so that you're familiar with its nuances and can evaluate whether it fits your organization's use case.

Topics in this section:
+ [Trunk branching strategy](trunk-branching-strategy.md)
+ [GitHub Flow branching strategy](git-hub-flow-branching-strategy.md)
+ [Gitflow branching strategy](gitflow-branching-strategy.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
