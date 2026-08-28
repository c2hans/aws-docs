---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/testing-environment.html
---

# Testing environment
<a name="testing-environment"></a>

Quality assurance (QA) personnel use the testing environment to validate features. They approve the changes after they finish testing. When they approve, the branch moves on to the next environment, staging. In Gitflow, this environment and others above it are only available for deployment from `release` branches. A `release` branch is based on a `develop` branch that contains the planned features.

## Access
<a name="access"></a>

Assign permissions according to the principle of least privilege. Developers should have less access to the testing environment than they have to the development environment. QA personnel require sufficient permissions to test the feature.

## Build steps
<a name="build-steps"></a>

The build process in this environment is only applicable for bugfixes when using the Gitflow strategy. Creating a merge request to the `bugfix` branch automatically starts the build.

1. Use [git-secrets](https://github.com/awslabs/git-secrets) (GitHub) to scan for sensitive information

1. Lint the source code

1. Build and compile the source code, if applicable

1. Perform unit testing

1. Perform code coverage analysis

1. Perform static code analysis

1. Build IaC

1. Perform IaC security analysis

1. Extract open source licenses

## Deployment steps
<a name="deployment-steps"></a>

Automatically initiate deployment of the `release` branch (Gitflow) or the `main` branch (Trunk or GitHub Flow) in the testing environment after deployment in the development environment. The following are the deployment steps in the testing environment:

1. Deploy the `release` branch (Gitflow) or `main` branch (Trunk or GitHub Flow) in the testing environment

1. Pause for manual approval by designated personnel

1. Download published artifacts

1. Perform database versioning

1. Perform IaC deployment

1. Perform integration tests

1. Perform performance tests

1. Quality assurance approval

## Expectations before moving to the staging environment
<a name="expectations-before-moving-to-the-staging-environment"></a>
+ The development and QA teams have performed sufficient testing to satisfy your organization's requirements.
+ The development team has resolved any discovered bugs through a `bugfix` branch.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
