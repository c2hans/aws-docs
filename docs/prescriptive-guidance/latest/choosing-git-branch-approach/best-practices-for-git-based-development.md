---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/best-practices-for-git-based-development.html
---

# Best practices for Git-based development
<a name="best-practices-for-git-based-development"></a>

To successfully adopt Git-based development, it's important to follow a set of best practices that promote collaboration, maintain code quality, and support continuous integration and continuous delivery (CI/CD). In addition to the best practices in this guide, review the [AWS Well-Architected DevOps Guidance](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/devops-guidance.html). The following are some key best practices for Git-based development on AWS:
+ **Keep changes small and frequent** – Encourage developers to commit small, incremental changes or features. This reduces the risk of merge conflicts and makes it easier to identify and fix issues quickly.
+ **Use feature toggles** – To manage the release of incomplete or experimental features, use feature toggles or feature flags. This helps you hide, enable, or disable specific features in production without affecting the main branch's stability.
+ **Maintain a robust test suite** – A comprehensive, well-maintained test suite is crucial for detecting issues early and verifying that the code base remains stable. Invest in test automation and prioritize fixing any failing tests.
+ **Embrace continuous integration** – Use continuous integration tools and practices to automatically build, test, and integrate code changes into the `develop` branch (Gitflow) or `main` branch (Trunk or GitHub Flow). This helps you catch issues early and streamlines the development process.
+ **Perform code reviews** – Encourage peer reviews of code to maintain quality, share knowledge, and catch potential issues before they're integrated into the `main` branch. Use pull requests or other code review tools to facilitate this process.
+ **Monitor and fix broken builds** – When a build breaks or tests fail, prioritize fixing the issue as soon as possible. This keeps the `develop` branch (Gitflow) or `main` branch (Trunk or GitHub Flow) in a releasable state and minimizes the impact on other developers.
+ **Communicate and collaborate** – Promote open communication and collaboration among team members. Make sure that developers are aware of ongoing work and changes being made to the code base.
+ **Refactor continuously** – Regularly refactor the code base to improve its maintainability and reduce technical debt. Encourage developers to leave the code in a better state than they found it.
+ **Use short-lived branches for complex tasks** – For larger or more complex tasks, use short-lived branches (also known as *task branches*) to work on the changes. However, make sure to keep the branch lifespan short, typically less than a day. Merge the changes back into the `develop` branch (Gitflow) or `main` branch (Trunk or GitHub Flow) as soon as possible. Smaller and more frequent merges and reviews are easier for a team to consume and process than one large merge request.
+ **Train and support the team** – Provide training and support to developers who are new to Git-based development or who require guidance in adopting its best practices.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
