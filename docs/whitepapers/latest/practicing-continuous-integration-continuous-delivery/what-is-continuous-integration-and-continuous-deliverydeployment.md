---
source_url: https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/what-is-continuous-integration-and-continuous-deliverydeployment.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# What is continuous integration and continuous delivery/deployment?
<a name="what-is-continuous-integration-and-continuous-deliverydeployment"></a>

 This section discusses the practices of continuous integration and continuous delivery and explains the difference between continuous delivery and continuous deployment.

## Continuous integration
<a name="continuous-integration"></a>

 Continuous integration (CI) is a software development practice where developers regularly merge their code changes into a central repository, after which automated builds and tests are run. CI most often refers to the build or integration stage of the software release process and requires both an automation component (for example a CI or build service) and a cultural component (for example learning to integrate frequently). The key goals of CI are to find and address bugs more quickly, improve software quality, and reduce the time it takes to validate and release new software updates.

 Continuous integration focuses on smaller commits and smaller code changes to integrate. A developer commits code at regular intervals, at minimum once a day. The developer pulls code from the code repository to ensure the code on the local host is merged before pushing to the build server. At this stage the build server runs the various tests and either accepts or rejects the code commit.

 It takes time to automate builds as well as testing of projects into a full continuous integration process. A few common challenges in this process are caused by the increased frequency of commits, as this causes a higher maintenance burden on the single source code repository, and increases hardware requirements to accommodate the testing of every change. Additional challenges include the creation of testing environments that represent production without inclusion of sensitive data, providing visibility of the testing process to the team, and providing easy access to any version of the application.

## Continuous delivery and deployment
<a name="continuous-delivery-and-deployment"></a>

 Continuous delivery (CD) is a software development practice where code changes are automatically built, tested, and prepared for production release. It expands on continuous integration by deploying all code changes to a testing environment, a production environment, or both after the build stage has been completed. Continuous delivery can be fully automated with a workflow process or partially automated with manual steps at critical points. When continuous delivery is properly implemented, developers always have a deployment-ready build artifact that has passed through a standardized test process.

 With continuous deployment, revisions are deployed to a production environment automatically without explicit approval from a developer, making the entire software release process automated. This, in turn, allows for a continuous customer feedback loop early in the product lifecycle.

## Continuous delivery is not continuous deployment
<a name="continuous-delivery-is-not-continuous-deployment"></a>

One misconception about continuous delivery is that it means every change committed is applied to production immediately after passing automated tests. However, the point of continuous delivery is not to apply every change to production immediately, but to ensure that every change is ready to go to production.

 Before deploying a change to production, you can implement a decision process to ensure that the production deployment is authorized and audited. This decision can be made by a person and then run by the tooling.

 Using continuous delivery, the decision to go live becomes a business decision, not a technical one. The technical validation happens on every commit.

 Rolling out a change to production is not a disruptive event. Deployment doesn’t require the technical team to stop working on the next set of changes, and it doesn’t need a project plan, handover documentation, or a maintenance window. Deployment becomes a repeatable process that has been carried out and proven multiple times in testing environments.
