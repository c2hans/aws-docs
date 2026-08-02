---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/development-environment.html
---

# Development environment
<a name="development-environment"></a>

The *development environment* is where developers integrate their code together to ensure it all works as one cohesive application. In Gitflow, the development environment contains the latest features included by merge request and are ready for release. In GitHub Flow and Trunk strategies, the development environment is considered to be a testing environment, and the code base might be unstable and unsuitable for deployment to production.

## Access
<a name="access"></a>

Assign permissions according to the principle of least privilege. *Least privilege* is the security best practice of granting the minimum permissions required to perform a task. Developers should have less access to the development environment than they have to the sandbox environment.

## Build steps
<a name="build-steps"></a>

Creating a merge request to the `develop` branch (Gitflow) or the `main` branch (Trunk or GitHub Flow) automatically starts the build.

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

If you're using the Gitflow model, the deployment steps automatically initiate when a `develop` branch is successfully built in the development environment. If you're using the GitHub Flow model or Trunk model, then the deployment steps automatically initiate when a merge request is created against the `main` branch. The following are the deployment steps in the development environment:

1. Download the published artifacts from the build steps

1. Perform database versioning

1. Perform IaC deployment

1. Perform integration tests

## Expectations before moving to the testing environment
<a name="expectations-before-moving-to-the-testing-environment"></a>
+ Successful build and deployment of the `develop` branch (Gitflow) or the `main` branch (Trunk or GitHub Flow) in the development environment
+ Unit testing passes at 100%
+ Successful IaC build
+ Deployment artifacts were successfully created
+ A developer has performed a manual verification to confirm that the feature is functioning as expected
