---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cicd-litmus/releases.html
---

# Releases
<a name="releases"></a>

One of the things that often makes a hotfix necessary is that, in a legacy workflow, the state of the application that developers are working on might contain several unreleased features that are not yet live in production. The production environment and the development environment only become in sync when a scheduled release occurs, and then they immediately begin to diverge again until the next scheduled release.

Having scheduled releases is possible within a fully CI/CD process. You can delay the release of code to production by using feature flags. However, a fully CI/CD process allows more flexibility by making scheduled releases unnecessary. After all, *continuous* is a key word in CI/CD, and that suggests that changes are released as they become ready. Avoid maintaining a separate release environment that is almost always out of sync with the lower test environments.

If a pipeline is not fully CI/CD, the divergence between upper and lower environments usually occurs at the branch level. Developers work in a development branch and maintain a separate release branch that is updated only when it is time for a scheduled release. As the release branch and the development branch diverge, other complications can arise.

In addition to environments being out of sync, as developers work on the development branch and become accustomed to an application state that is far ahead of what is in production, they must readjust to the state of production every time an issue arises there. The state of the development branch could be many features ahead of production. When developers work in that branch every day, it's difficult to remember what is and isn't released to production. This adds risk that new bugs will be introduced while in the process of fixing other bugs. This result is a seemingly endless cycle of fixes that extend timelines and delay feature releases for weeks, months, or even years.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
