---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/advantages-and-disadvantages-of-the-gitflow-strategy.html
---

# Advantages and disadvantages of the Gitflow strategy
<a name="advantages-and-disadvantages-of-the-gitflow-strategy"></a>

The Gitflow branching strategy is well suited to larger, more distributed teams that have strict release and compliance requirements. Gitflow contributes to a predictable release cycle for the organization, and this is often preferred by larger organizations. Gitflow is also well suited for teams that require guardrails to complete their software development lifecycle properly. This is because there are multiple opportunities for reviews and quality assurance built into the strategy. Gitflow is also well suited for teams that must maintain multiple versions of production releases simultaneously. Some disadvantages of GItflow are that is it more complex than other branching models and requires strict adherence to the pattern to complete successfully. Gitflow does not work well for organizations striving for continuous delivery due to the rigid nature of managing release branches. Gitflow release branches can be long-lived branches that can accumulate technical debt if not properly addressed in a timely manner.

## Advantages
<a name="advantages"></a>

Gitflow-based development offers several advantages that can improve the development process, streamline collaboration, and enhance the overall quality of the software. The following are some of the key benefits:
+ **Predictable release process** – Gitflow follows a regular and predictable release process. It is well suited to teams with regular development and release cadences.
+ **Improved collaboration** – Gitflow encourages the use of `feature` and `release` branches. These two branches help teams work in parallel with minimal dependencies on each other.
+ **Well suited for multiple environments** – Gitflow uses `release` branches, which can be longer-lived branches. These branches enable teams to target individual releases over a longer period of time.
+ **Multiple versions in production** – If your team supports multiple versions of the software in production, Gitflow `release` branches support this requirement.
+ **Built-in code quality reviews** – Gitflow requires and encourages the use of code reviews and approvals before code is promoted to another environment. This process removes friction between developers by requiring this step for all code promotions.
+ **Organization benefits** – Gitflow has advantages at an organization level as well. Gitflow encourages the use of a standard release cycle, which helps the organization understand and anticipate the release schedule. Because the business now understands when new features can be delivered, there is reduced friction about timelines because there are set delivery dates.

## Disadvantages
<a name="disadvantages"></a>

Gitflow-based development does have some disadvantages that can impact the development process and the team dynamics. The following are a few notable drawbacks:
+ **Complexity** – Gitflow is a complex pattern for new teams to learn, and you must adhere to the rules of Gitflow to use this successfully.
+ **Continuous deployment** – Gitflow doesn't fit a model where many deployments are released to production in a rapid fashion. This is because Gitflow requires the use of multiple branches and a strict workflow governing the `release` branch.
+ **Branch management** – Gitflow uses many branches, which can become burdensome to maintain. It can be challenging to track the various branches and merge released code in order to keep the branches properly aligned with each other.
+ **Technical debt** – Because Gitflow releases are typically slower than the other branching models, more features can accumulate for release, which can cause technical debt to accumulate.

Teams should carefully consider these drawbacks when deciding whether Gitflow-based development is the right approach for their project.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
