---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/staging-environment.html
---

# Staging environment
<a name="staging-environment"></a>

The *staging environment* is configured to be the same as the production environment. For example, the data setup should be similar in scope and size to production workloads. Use the staging environment to verify that code and infrastructure operate as expected. This environment is also the preferred choice for business use cases, such as previews or customer demonstrations.

## Access
<a name="access"></a>

Assign permissions according to the principle of least privilege. Developers should have the same access to the staging environment as they do the production environment.

## Build steps
<a name="build-steps"></a>

None. The same artifacts that were used in the testing environment are reused in the staging environment.

## Deployment steps
<a name="deployment-steps"></a>

Automatically initiate deployment of the `release` branch (Gitflow) or the `main` branch (Trunk or GitHub Flow) in the staging environment after approval and deployment in the testing environment. The following are the deployment steps in the staging environment:

1. Deploy the `release` branch (Gitflow) or `main` branch (Trunk or GitHub Flow) in the staging environment

1. Pause for manual approval by designated personnel

1. Download published artifacts

1. Perform database versioning

1. Perform IaC deployment

1. (Optional) Perform integration testing

1. (Optional) Perform load testing

1. Obtain approval from the required development, QA, product, or business approvers

## Expectations before moving to the production environment
<a name="expectations-before-moving-to-the-production-environment"></a>
+ A production-equivalent release has been deployed successfully to the staging environment
+ (Optional) Integration and load testing were successful

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
