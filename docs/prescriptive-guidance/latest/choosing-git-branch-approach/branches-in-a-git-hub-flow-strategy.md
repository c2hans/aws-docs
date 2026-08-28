---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/branches-in-a-git-hub-flow-strategy.html
---

# Branches in a GitHub Flow strategy
<a name="branches-in-a-git-hub-flow-strategy"></a>

A GitHub Flow branching strategy commonly has the following branches.

![The branches and environments in a GitHub Flow branching strategy.](http://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/images/guide-img/2c642ab1-73c3-487b-9aff-d887904354b7/images/5a124d59-766a-4f2e-81dc-092ac8e8f20c.png)

## feature branch
<a name="feature-branch"></a>

You develop features in `feature` branches. To create a `feature` branch, you branch off of the `main` branch. Developers iterate, commit, and test the code in the `feature` branch. When a feature is complete, the developer promotes the feature by creating a merge request to `main`.

|  |  |
| --- |--- |
| Naming convention: | `feature/<story number>_<developer initials>_<descriptor>` |
| Naming convention example: | `feature/123456_MS_Implement_Feature_A` |

## bugfix branch
<a name="bugfix-branch"></a>

The `bugfix` branch is used to fix issues. These branches are branched off of the `main` branch. After the bugfix is tested in sandbox or any of the lower environments, it can be promoted to higher environments by merging it to `main` through a merge request. This is a suggested naming convention for organization and tracking, this process could also be managed using a feature branch.

|  |  |
| --- |--- |
| Naming convention: | `bugfix/<ticket number>_<developer initials>_<descriptor>` |
| Naming convention example: | `bugfix/123456_MS_Fix_Problem_A` |

## hotfix branch
<a name="hotfix-branch"></a>

The `hotfix` branch is used to resolve high impact critical issues with minimal delay between the development staff and the code deployed in production. These branches are branched off of the `main` branch. After the hotfix is tested in sandbox or any of the lower environments, it can be promoted to higher environments by merging it to `main` through a merge request. This is a suggested naming convention for organization and tracking, this process could also be managed using a feature branch.

|  |  |
| --- |--- |
| Naming convention: | `hotfix/<ticket number>_<developer initials>_<descriptor>` |
| Naming convention example: | `hotfix/123456_MS_Fix_Problem_A` |

## main branch
<a name="main-branch"></a>

The `main` branch always represents the code that is running in production. Code is merged into the `main` branch from `feature` branches by using merge requests. To protect against deletion and to prevent developers from pushing code directly to `main`, enable branch protection for the `main` branch.

|  |  |
| --- |--- |
| Naming convention: | `main` |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
