---
source_url: https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/introduction.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Introduction
<a name="introduction"></a>

 In a traditional approach to application deployment, you typically fix a failed deployment by redeploying an earlier, stable version of the application. Redeployment in traditional data centers is typically done on the same set of resources due to the cost and effort of provisioning additional resources. Although this approach works, it has many shortcomings. Rollback isn’t easy because it’s implemented by redeployment of an earlier version from scratch. This process takes time, making the application potentially unavailable for long periods. Even in situations where the application is only impaired, a rollback is required, which overwrites the faulty version. As a result, you have no opportunity to debug the faulty application in place.

 Applying the principles of agility, scalability, utility consumption, as well as the automation capabilities of Amazon Web Services can shift the paradigm of application deployment. This enables a better deployment technique called *blue/green deployment*.

## Blue/Green Deployment Methodology
<a name="bluegreen-deployment-methodology"></a>

 Blue/green deployments provide releases with near zero-downtime and rollback capabilities. The fundamental idea behind blue/green deployment is to shift traffic between two identical environments that are running different versions of your application. The blue environment represents the current application version serving production traffic. In parallel, the green environment is staged running a different version of your application. After the green environment is ready and tested, production traffic is redirected from blue to green. If any problems are identified, you can roll back by reverting traffic back to the blue environment.

![Basic blue/green example](https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/images/blue-green-example.png)

* Blue/green example *

 Although blue/green deployment isn’t a new concept, you don’t commonly see it used in traditional, on-premises hosted environments due to the cost and effort required to provision additional resources. The advent of cloud computing dramatically changes how easy and cost-effective it is to adopt the blue/green approach for deploying software.

## Benefits of Blue/Green
<a name="benefits-of-bluegreen"></a>

 Traditional deployments with in-place upgrades make it difficult to validate your new application version in a production deployment while also continuing to run the earlier version of the application. Blue/green deployments provide a level of isolation between your blue and green application environments. This helps ensure spinning up a parallel green environment does not affect resources underpinning your blue environment. This isolation reduces your deployment risk.

 After you deploy the green environment, you have the opportunity to validate it. You might do that with test traffic before sending production traffic to the green environment, or by using a very small fraction of production traffic, to better reflect real user traffic. This is called *canary analysis* or *canary testing*. If you discover the green environment is not operating as expected, there is no impact on the blue environment. You can route traffic back to it, minimizing impaired operation or downtime and limiting the blast radius of impact.

 This ability to simply roll traffic back to the operational environment is a key benefit of blue/green deployments. You can roll back to the blue environment at any time during the deployment process. Impaired operation or downtime is minimized because impact is limited to the window of time between green environment issue detection and shift of traffic back to the blue environment. Additionally, impact is limited to the portion of traffic going to the green environment, not all traffic. If the blast radius of deployment errors is reduced, so is the overall deployment risk.

 Blue/green deployments also work well with continuous integration and continuous deployment (CI/CD) workflows, in many cases limiting their complexity. Your deployment automation has to consider fewer dependencies on an existing environment, state, or configuration as your new green environment gets launched onto an entirely new set of resources.

 Blue/green deployments conducted in AWS also provide cost optimization benefits. You’re not tied to the same underlying resources. So, if the performance envelope of the application changes from one version to another, you simply launch the new environment with optimized resources, whether that means fewer resources or just different compute resources. You also don’t have to run an overprovisioned architecture for an extended period of time. During the deployment, you can scale out the green environment as more traffic gets sent to it and scale the blue environment back in as it receives less traffic. Once the deployment succeeds, you decommission the blue environment and stop paying for the resources it was using.

## Define the Environment Boundary
<a name="define-the-environment-boundary"></a>

 When planning for blue/green deployments, you have to think about your environment boundary—where have things changed and what needs to be deployed to make those changes live. The scope of your environment is influenced by a number of factors, as described in the following table.

* Table 1 - Factors that affect environment boundary *

|  Factors  |  Criteria  |
| --- | --- |
|  Application architecture  |  Dependencies, loosely/tightly coupled  |
|  Organization |  Speed and number of iterations  |
|  Risk and complexity  |  Blast radius and impact of failed deployment  |
|  People  |  Expertise of teams  |
|  Process  |  Testing/QA, rollback capability  |
|  Cost  |  Operating budgets, additional resources  |

 For example, organizations operating applications that are based on the microservices architecture pattern could have smaller environment boundaries because of the loose coupling and well-defined interfaces between the individual services. Organizations running legacy, monolithic apps can still leverage blue/green deployments, but the environment scope can be wider and the testing more extensive. Regardless of the environment boundary, you should make use of automation wherever you can to streamline the process, reduce human error, and control your costs.
