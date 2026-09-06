---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/branches-in-a-gitflow-strategy.html
---

# Branches in a Gitflow strategy
<a name="branches-in-a-gitflow-strategy"></a>

A Gitflow branching strategy commonly has the following branches.

![The branches and environments in a Gitflow branching strategy.](http://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/images/guide-img/2c642ab1-73c3-487b-9aff-d887904354b7/images/796ec7d6-dd2c-41d2-ac97-f004cfbd3f55.png)

## feature branch
<a name="feature-branch"></a>

`Feature` branches are short-term branches where you develop features. The `feature` branch is created by branching off of the `develop` branch. Developers iterate, commit, and test code in the `feature` branch. When the feature is complete, the developer promotes the feature. There are only two paths forward from a feature branch:
+ Merge into the `sandbox` branch
+ Create a merge request into the `develop` branch

|  |  |
| --- |--- |
| Naming convention: | `feature/<story number>_<developer initials>_<descriptor>` |
| Naming convention example: | `feature/123456_MS_Implement_Feature_A` |

## sandbox branch
<a name="sandbox-branch"></a>

The `sandbox` branch is a non-standard, short-term branch for Gitflow. However, it is useful for CI/CD pipeline development. The `sandbox` branch is primarily used for the following purposes:
+ Perform a full deployment to the sandbox environment by using the CI/CD pipelines rather than a manual deployment.
+ Develop and test a pipeline before submitting merge requests for full testing in a lower environment, such as development or testing.

`Sandbox` branches are temporary in nature and are not meant to be long-lived. They should be deleted after the specific testing is complete.

|  |  |
| --- |--- |
| Naming convention: | `sandbox/<story number>_<developer initials>_<descriptor>` |
| Naming convention example: | `sandbox/123456_MS_Test_Pipeline_Deploy` |

## develop branch
<a name="develop-branch"></a>

The `develop` branch is a long-lived branch where features are integrated, built, validated, and deployed to the development environment. All `feature` branches are merged into the `develop` branch. Merges into the `develop` branch are completed through a merge request that requires a successful build and two developer approvals. To prevent deletion, enable branch protection on the `develop` branch.

|  |  |
| --- |--- |
| Naming convention: | `develop` |

## release branch
<a name="release-branch"></a>

In Gitflow, `release` branches are short-term branches. These branches are special because you can deploy them to multiple environments, embracing the build-once, deploy-many methodology. `Release` branches can target the testing, staging, or production environments. After a development team has decided to promote features into higher environments, they create a new `release` branch and use increment the version number from the previous release. At gates in each environment, deployments require manual approvals to proceed. `Release` branches should require a merge request to be changed.

After the `release` branch has deployed to production, it should be merged back into the `develop` and `main` branches to make sure that any bugfixes or hotfixes are merged back into future development efforts.

|  |  |
| --- |--- |
| Naming convention: | `release/v{major}.{minor}` |
| Naming convention example: | `release/v1.0` |

## main branch
<a name="main-branch"></a>

The `main` branch is a long-lived branch that always represents the code that is running in production. Code is merged into the `main` branch automatically from a release branch after a successful deployment from the release pipeline. To prevent deletion, enable branch protection on the `main` branch.

|  |  |
| --- |--- |
| Naming convention: | `main` |

## bugfix branch
<a name="bugfix-branch"></a>

The `bugfix` branch is a short-term branch that is used to fix issues in release branches that haven't been released to production. A `bugfix` branch should only be used to promote fixes in `release` branches to the testing, staging, or production environments. A `bugfix` branch is always branched off of a `release` branch.

After the bugfix is tested, it can be promoted to the `release` branch through a merge request. Then you can push the `release` branch forward by following the standard release process.

|  |  |
| --- |--- |
| Naming convention: | `bugfix/<ticket>_<developer initials>_<descriptor>` |
| Naming convention example: | `bugfix/123456_MS_Fix_Problem_A` |

## hotfix branch
<a name="hotfix-branch"></a>

The `hotfix` branch is a short-term branch that is used to fix issues in production. It only be used to promote fixes that must be expedited to reach the production environment. A `hotfix` branch is always branched from `main`.

After the hotfix is tested, you can promote it to production through a merge request into the `release` branch that was created from `main`. For testing, you can then push the `release` branch forward by following the standard release process.

|  |  |
| --- |--- |
| Naming convention: | `hotfix/<ticket>_<developer initials>_<descriptor>` |
| Naming convention example: | `hotfix/123456_MS_Fix_Problem_A` |
