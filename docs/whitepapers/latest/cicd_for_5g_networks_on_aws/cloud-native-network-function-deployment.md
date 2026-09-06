---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/cloud-native-network-function-deployment.html
---

# Cloud-native network function deployment
<a name="cloud-native-network-function-deployment"></a>

CNF deployment is about the application deployment. As part of the CNF deployment, the Helm charts for the application are implemented through the CI/CD code pipeline. The callback to run individual application-specific scripts primarily involving pre- and post-checks are incorporated. The Helm charts are implemented in a sequence as per the application’s needs, and check for the status of the Kubernetes PODs before moving to the next step in the deployment. Often, ISVs provide a wrapper script to run the Helm charts and sanity checks. These ISV scripts are invoked from within AWS CodePipeline. As part of this phase, the logging and monitoring agents such as Prometheus and Fluentd are deployed in addition to Amazon CloudWatch, which logs and monitors the cloud infrastructure of the application.

The code pipeline is integrated with the third-party test automation framework. The code pipeline can directly call the test automation framework APIs to run the test on the deployed application, query the test results, and analyze the result. This simplifies the deployment and testing of the application.

![A diagram depicting application deployment and update.](http://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/images/cicd_5g8.png)

*Application deployment and update*

The following is an example of the deployment of the user plane function/session management function (UPF/SMF) CNF via AWS CodePipeline.
+ Automate the complete CI/CD process using CodeCommit, CodeBuild, and CodePipeline.
+ Infra creation and application installation tasks are integrated as part of the pipeline.
+ FluentD and Prometheus agents are installed and created in Amazon CloudWatch dashboards.

![Screenshots showing a deployment example of UPF/SMF CNFs.](http://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/images/cicd_5g9.png)

*Deployment example of UPF/SMF CNFs*
