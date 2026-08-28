---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/trunk-branching-strategy.html
---

# Trunk branching strategy
<a name="trunk-branching-strategy"></a>

Trunk-based development is a software development practice in which all developers work on a single branch, typically called the `trunk` or `main` branch. The idea behind this approach is to keep the code base in a continuously releasable state by integrating code changes frequently and relying on automated testing and continuous integration.

In trunk-based development, developers commit their changes to the `main` branch multiple times a day, aiming for small, incremental updates. This enables quick feedback loops, reduces the risk of merge conflicts, and fosters collaboration among team members. The practice emphasizes the importance of a well-maintained test suite because it relies on automated testing to catch potential issues early and make sure that the code base remains stable and releasable.

Trunk-based development is often contrasted with *feature-based development* (also known as *feature branching* or *feature-driven development*), where each new feature or bug fix is developed in its own dedicated branch, separate from the main branch. The choice between trunk-based development and feature-based development depends on factors such as team size, project requirements, and the desired balance between collaboration, integration frequency, and release management.

For more information about the Trunk branching strategy, see the following resources:
+ [Implement a Trunk branching strategy for multi-account DevOps environments](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-a-trunk-branching-strategy-for-multi-account-devops-environments.html) (AWS Prescriptive Guidance)
+ [Introduction to Trunk-Based Development](https://trunkbaseddevelopment.com/) (Trunk Based Development website)

Topics in this section:
+ [Visual overview of the Trunk strategy](visual-overview-of-the-trunk-strategy.md)
+ [Branches in a Trunk strategy](branches-in-a-trunk-strategy.md)
+ [Advantages and disadvantages of the Trunk strategy](advantages-and-disadvantages-of-the-trunk-strategy.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
