---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cicd-litmus/understanding-cicd.html
---

# Understanding CI/CD
<a name="understanding-cicd"></a>

Continuous integration and continuous delivery (CI/CD) is the process of automating the software release lifecycle. In some cases, the *D* in CI/CD can also mean *deployment*. The difference between *continuous delivery* and* continuous deployment* occurs when you release a change to the production environment. With continuous delivery, a manual approval is required before promoting changes to production. Continuous deployment features an uninterrupted flow through the entirety of the pipeline, and no explicit approvals are required. Because this strategy discusses general CI/CD concepts, the recommendations and information provided are applicable to both the continuous delivery and continuous deployment approaches.

CI/CD automates much or all of the manual processes traditionally required to get new code from a commit into production. A CI/CD pipeline encompasses the source, build, test, staging, and production stages. In each stage, the CI/CD pipelines provisions any infrastructure that is needed to deploy or test the code. By using a CI/CD pipeline, development teams can make changes to code that are then automatically tested and pushed to deployment.

Let's review the basic CI/CD process before discussing some of the ways that you can, knowingly or unknowingly, deviate from being fully CI/CD. The following diagram shows the CI/CD stages and activities in each stage.

![The five stages of a CI/CD process and the activities and environments of each.](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cicd-litmus/images/guide-img/de5d2132-0072-4b65-b7ac-e1e4c4852e08/images/de1d32ab-bd01-444e-9e65-7148b0aabdb2.png)

## About continuous integration
<a name="about-continuous-integration"></a>

Continuous integration occurs in a code repository, such as a Git repository in GitHub. You treat a single, main branch as the source of truth for the code base, and you create short-lived branches for feature development. You integrate a feature branch into the main branch when you're ready to deploy the feature to upper environments. Feature branches are never deployed directly to upper environments. For more information, see [Trunk-based workflow](fully-cicd-process-differences.md#trunk-based-approach) in this guide.

### Continuous integration process
<a name="continuous-integration-process.0b453d26-ac82-54c7-9d18-ea6b132b9e72"></a>

1. The developer creates a new branch from the main branch.

1. The developer makes changes and builds and tests locally.

1. When the changes are ready, the developer creates a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) (GitHub documentation) with the main branch as the destination.

1. The code is reviewed.

1. When the code is approved, it is merged into the main branch.

## About continuous delivery
<a name="about-continuous-delivery"></a>

Continuous delivery occurs in isolated environments, such as development environments and production environments. The actions that occur in each environment can vary. Often, one of the first stages is used to make updates to the pipeline itself before proceeding. The end result of the deployment is that each environment is updated with the latest changes. The number of development environments for building and testing also varies, but we recommend you use at least two. In the pipeline, each environment is updated in order of its significance, ending with the most important environment, the production environment.

### Continuous delivery process
<a name="continuous-delivery-process.cf7a3f2d-0bd5-5665-8164-58f138ebf3ce"></a>

The continuous delivery portion of the pipeline initiates by pulling the code from the main branch of the source repository and passing it to the build stage. The infrastructure as code (IaC) document for the repository outlines the tasks that are performed in each stage. Although using an IaC document is not mandatory, an IaC service or tool, such as [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) or [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/latest/guide/home.html), is strongly recommended. The most common steps include:

1. Unit tests

1. Code build

1. Resource provisioning

1. Integration tests

If any errors occur or any tests fail at any stage in the pipeline, the current stage rolls back to its previous state, and the pipeline is terminated. Subsequent changes must start in the code repository and go through the fully CI/CD process.
