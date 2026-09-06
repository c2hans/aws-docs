---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/continuous_integration_continuous_delivery.html
---

# Continuous Integration and Continuous Delivery
<a name="continuous_integration_continuous_delivery"></a>

## Continuous Integration
<a name="continuous-integration"></a>

*Continuous Integration* (CI) is a software process in which developers regularly push their code into a central repository such as [AWS CodeCommit](https://aws.amazon.com/codecommit/) or [GitHub](https://github.com/). Every code push triggers an automated build, followed by the running of tests. The main goal of CI is to discover code issues at an early stage, improve code quality, and reduce the time it takes to validate and release new software updates.

## Continuous Delivery and Deployment
<a name="continuous-delivery"></a>

*Continuous Delivery* (CD) is a software process in which artifacts are deployed to the test environment, staging environment, and production environment. Continuous delivery can be fully automated, or have approval stages at critical points. This ensures that all required approvals prior to deployment, such as release management approval, are in place. When continuous delivery is correctly implemented, developers always have a deployment-ready build artifact that has passed through a standardized test process.

With *Continuous Deployment*, revisions are deployed to a production environment automatically without explicit approval from a developer, making the entire software release process automated. This allows for a continuous customer feedback loop early in the product lifecycle.

With Continuous Deployment, every change that is committed and passes automated tests is released to production automatically. Continuous Delivery is not meant to release every change that is committed and pass automated tests to production immediately, but to ensure that every change is ready to go to production.
