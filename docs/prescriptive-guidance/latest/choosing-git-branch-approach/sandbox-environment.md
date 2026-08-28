---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/sandbox-environment.html
---

# Sandbox environment
<a name="sandbox-environment"></a>

The *sandbox environment* is where developers write code, make mistakes, and perform proof of concept work. You can deploy to a sandbox environment from a local workstation or through a script on a local workstation.

## Access
<a name="access"></a>

Developers should have full access to the sandbox environment.

## Build steps
<a name="build-steps"></a>

Developers manually run the build on their local workstations when they are ready to deploy changes to the sandbox environment.

1. Use [git-secrets](https://github.com/awslabs/git-secrets) (GitHub) to scan for sensitive information

1. Lint the source code

1. Build and compile the source code, if applicable

1. Perform unit testing

1. Perform code coverage analysis

1. Perform static code analysis

1. Build infrastructure as code (IaC)

1. Perform IaC security analysis

1. Extract open source licenses

1. Publish build artifacts

## Deployment steps
<a name="deployment-steps"></a>

If you're using the Gitflow or Trunk models, the deployment steps automatically initiate when a `feature` branch is successfully built in the sandbox environment. If you're using the GitHub Flow model, then you manually perform the following deployment steps. The following are the deployment steps in the sandbox environment:

1. Download published artifacts

1. Perform database versioning

1. Perform IaC deployment

1. Perform integration testing

## Expectations before moving to the development environment
<a name="expectations-before-moving-to-the-development-environment"></a>
+ Successful build of the `feature` branch in the sandbox environment
+ A developer has manually deployed and tested the feature in the sandbox environment

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
