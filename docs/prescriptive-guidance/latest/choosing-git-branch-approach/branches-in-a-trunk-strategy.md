---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/branches-in-a-trunk-strategy.html
---

# Branches in a Trunk strategy
<a name="branches-in-a-trunk-strategy"></a>

A Trunk branching strategy commonly has the following branches.

![The branches and environments in a Trunk branching strategy.](http://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/images/guide-img/2c642ab1-73c3-487b-9aff-d887904354b7/images/710dd758-9c16-4f6c-8f4e-c44bbbc5a926.png)

## feature branch
<a name="feature-branch"></a>

You develop features or create a hotfix in a `feature` branch. To create a `feature` branch, you branch off of the `main` branch. Developers iterate, commit, and test code in a `feature` branch. When a feature is complete, the developer promotes the feature. There are only two paths forward from a `feature` branch:
+ Merge into the `sandbox` branch
+ Create a merge request into the `main` branch

|  |  |
| --- |--- |
| Naming convention: | `feature/<story number>_<developer initials>_<descriptor>` |
| Naming convention example: | `feature/123456_MS_Implement_Feature_A` |

## sandbox branch
<a name="sandbox-branch"></a>

This branch is a non-standard trunk branch, but it is useful for CI/CD pipeline development. The `sandbox` branch is primarily used for the following purposes:
+ Perform a full deployment to the sandbox environment by using the CI/CD pipelines
+ Develop and test a pipeline before submitting merge requests for full testing in a lower environment, such as development or testing.

`Sandbox` branches are temporary in nature and are intended to be short-lived. They should be deleted after the specific testing is complete.

|  |  |
| --- |--- |
| Naming convention: | `sandbox/<story number>_<developer initials>_<descriptor>` |
| Naming convention example: | `sandbox/123456_MS_Test_Pipeline_Deploy` |

## main branch
<a name="main-branch"></a>

The `main` branch always represents the code that is running in production. Code is branched from `main`, developed, and then merged back to `main`. Deployments from `main` could target any environment. To protect against deletion, enable branch protection for the `main` branch.

|  |  |
| --- |--- |
| Naming convention: | `main` |

## hotfix branch
<a name="hotfix-branch"></a>

There is no dedicated `hotfix` branch in a trunk-based workflow. Hotfixes use `feature` branches.
