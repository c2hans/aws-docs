---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/appendix.html
---

# Appendix: Example ADR
<a name="appendix"></a>

## Title
<a name="title.5d173230-cd30-5d62-a057-1ad5a711f78b"></a>

This decision defines the software development lifecycle approach for ABC application development.

## Status
<a name="status.e44626de-5cea-5f9d-a502-b6d0b52ed4f8"></a>

Accepted

## Date
<a name="date.4fda946e-12bc-56e5-984b-1ef5820881e6"></a>

2022-03-11

## Context
<a name="context.2580e65e-c06c-5b5b-a282-541e57a5affe"></a>

ABC application is a packaged solution, which will be deployed to the customer's environment by using a deployment package. We need to have a development process that will enable us to have a controllable feature, hotfix, and release pipeline.

## Decision
<a name="decision.01fd23b4-fc6c-54ce-9455-ec067e18b5af"></a>

We use an adapted version of the [GitFlow workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) to develop ABC application.

![GitFlow workflow, adapted for the ABC sample application](http://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/images/guide-img/19b175a3-1b40-432f-9670-fef30553db34/images/6594616b-db16-4b6f-b66d-4c3cf4d75303.png)

For simplicity, we will not be using the hotfix/\* and release/\* branches, because ABC application will be packaged instead of being deployed to a specific environment. For this reason, there is no need for additional complexity that might prevent us from reacting quickly to fix bugs in production releases, or testing releases in a separate environment.

The following is the agreed branching strategy:
+ Each repository must have a protected main branch that will be used to tag releases.
+ Each repository must have a protected develop branch for all ongoing development work.

## Consequences
<a name="consequences.40868996-11ea-50c3-9eed-dbea48864d4d"></a>

Positive:
+ Adapted GitFlow process will enable us to control release versioning of the ABC application.

Negative:
+ GitFlow is more complicated than trunk-based development or [GitHub flow](https://guides.github.com/introduction/flow/) and has more overhead.

## Compliance
<a name="compliance.ab3f2d74-ba3a-52fc-9347-da20969b3bcd"></a>
+ The main and develop branches in each repository must be marked as Protected.
+ Changes to the main and develop branches must be propagated by using merge requests.
+ At least one approval is required for every merge request.

## Notes
<a name="notes.a175ae27-46d8-5ac0-a1a0-5def98651a38"></a>
+ Author: Jane Doe
+ Version: 0.1
+ Changelog:
  + 0.1: Initial proposed version

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
