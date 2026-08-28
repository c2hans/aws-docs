---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/managing-transitive-dependency-conflicts-package-migrations/best-practices.html
---

# Best practices
<a name="best-practices"></a>

Analyze your most-used components first. In a distributed system, in-house shared packages often have many components depending on them. A transitive dependency conflict in one of these shared packages can block progress across every component that uses it.

Run the transitive dependency analysis on your application's most-used, customer-facing components first. Analyzing several complex components surfaces the shared lower-level dependencies that block the most other work. Migrating those shared dependencies first unblocks the largest amount of progress for the least effort.

Treat every pinned version as work you still owe. Pinning unblocks a release, but it leaves the conflict in place. Record a revisit date when you pin. Automate reanalysis in your build pipeline. Add the dependency analysis script as a CI step that runs on pull requests touching package configuration files. Automated checks surface new conflicts before they reach the main branch.

Set version-range policies for shared packages. Define whether shared packages accept minor-version ranges or require exact pins. A written policy reduces ad-hoc decisions during migrations and makes pinning exceptions visible.

Document your dependency governance model. Record who owns each shared package, who approves version bumps, and how cross-team migrations are coordinated. This removes ambiguity when multiple teams share the same dependency tree.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
