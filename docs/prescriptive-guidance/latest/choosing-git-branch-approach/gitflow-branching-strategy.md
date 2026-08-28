---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/gitflow-branching-strategy.html
---

# Gitflow branching strategy
<a name="gitflow-branching-strategy"></a>

Gitflow is a branching model that involves the use of multiple branches to move code from development to production. Gitflow works well for teams that have scheduled release cycles and a need to define a collection of features as a release. Development is completed in individual feature branches that are merged, with approval, into a develop branch, which is used for integration. The features in this branch are considered ready for production. When all planned features have accumulated in the develop branch, a release branch is created for deployments to upper environments. This separation improves control over which changes are moving to which named environment on a defined schedule. If necessary, you can accelerate this process into a faster deployment model.

For more information about the Gitflow branching strategy, see the following resources:
+ [Implement a Gitflow branching strategy for multi-account DevOps environments](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-a-gitflow-branching-strategy-for-multi-account-devops-environments.html) (AWS Prescriptive Guidance)
+ [The original Gitflow blog ](https://nvie.com/posts/a-successful-git-branching-model/)(Vincent Driessen blog post)
+ [Gitflow workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) (Atlassian)

Topics in this section:
+ [Visual overview of the Gitflow strategy](visual-overview-of-the-gitflow-strategy.md)
+ [Branches in a Gitflow strategy](branches-in-a-gitflow-strategy.md)
+ [Advantages and disadvantages of the Gitflow strategy](advantages-and-disadvantages-of-the-gitflow-strategy.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
