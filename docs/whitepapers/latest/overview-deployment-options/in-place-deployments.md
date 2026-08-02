---
source_url: https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/in-place-deployments.html
---

# In-place deployments
<a name="in-place-deployments"></a>

 An [in-place deployment](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/in-place-deployments.html) is a deployment strategy that updates the application version without replacing any infrastructure components. In an in-place deployment, the previous version of the application on each compute resource is stopped, the latest application is installed, and the new version of the application is started and validated. This allows application deployments to proceed with minimal disturbance to underlying infrastructure.

 An in-place deployment allows you to deploy your application without creating new infrastructure; however, the availability of your application can be affected during these deployments. This approach also minimizes infrastructure costs and management overhead associated with creating new resources.

 Refer to [Overview of an in-place deployment](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html#welcome-deployment-overview-in-place) for more details on using in-place deployment strategies with CodeDeploy.
