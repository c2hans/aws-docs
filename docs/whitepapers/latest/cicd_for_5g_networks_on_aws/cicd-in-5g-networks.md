---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/cicd-in-5g-networks.html
---

# CI/CD in 5G networks
<a name="cicd-in-5g-networks"></a>

The design construct of the infrastructure is stored in the form of code using declarative language. This enables the CSP to have a repeatable reproduction of the infrastructure with the same expected behavior as needed. The code is maintained in the code repository, and a pipeline is set up to orchestrate updates to the deployed stacks (for example, AWS CDK and CloudFormation). AWS can help build Infrastructure as Code (IaC) for agile onboarding of Independent Software Vendor (ISV) functions.

![A diagram depicting code pipeline flow.](http://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/images/cicd_5g6.png)

*Code pipeline flow*

Changes in cloud-native network function configurations through Helm charts are considered to be triggers for an automatic CI/CD pipeline execution for network functions.

AWS CodeCommit can be used to maintain configuration files, and Amazon ECR can be used to preserve container images.

As shown in the *Code pipeline flow* figure, when the ISV pushes new code changes into the code repository (Helm chart, config files, or a properties file), the code pipeline is triggered. The code pipeline pulls the image from ECR and use the Helm chart to deploy the application. The new application testing can be integrated with the third-party test automation framework. Based on the result, CSPs can approve for production deployment.

The CodePipeline source stage looks for changes in configuration files. The valid providers for source stage are CodeCommit, Amazon S3, GitHub, or CloudFormation. Alternative source systems can be integrated by using Lambda functions to implement Webhooks, which enables event-driven integration between Gitlab and AWS CodePipeline. See the following links for a detailed implementation guide.
+ [Webhooks with GitLab](https://docs.gitlab.com/ee/user/project/integrations/webhooks.html)
+ [Container registry integrations](https://docs.gitlab.com/ee/administration/packages/container_registry.html)

CI/CD pipeline design should account for critical deployment steps such as initial deployment, testing, and promotion to production after test results are aligned with expectations and verified against the baseline. Every stage of the pipeline process provides data artifacts, which enable comparison and data-driven decisions.

![A diagram depicting application CI/CD pipeline steps: Change, Deploy, Test, Promote, Monitor.](http://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/images/cicd_5g7.png)

*Application CI/CD pipeline steps*

Every stage can be considered a separate task, allowing the incorporation of validation and deployment workflows adequate to support network service and cloud-native network functions. Run tasks can incorporate additional third-party tools such as traffic generators and simulators, enabling end-to-end network service validation.

AWS provides a sophisticated [AWS Step Function](https://aws.amazon.com/step-functions/) (cloud-native state machine) service that natively integrates with other AWS Services, and also has the ability to integrate with external systems such as Jira or a test automation framework.
