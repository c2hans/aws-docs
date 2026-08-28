---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/opensearch-service-migration/deployment-frameworks.html
---

# Deployment frameworks
<a name="deployment-frameworks"></a>

Many modern teams use continuous integration and continuous delivery (CI/CD) practices and pipelines to automate the deployment of their solutions and infrastructure. If your team already uses CI/CD pipelines, you should be able to incorporate Amazon OpenSearch Service in your environment. If you are deploying manually in your current setup, consider building pipelines to automate repeatable work, reduce operational overhead, and reduce human errors.

You can deploy Amazon OpenSearch Service by using a variety of infrastructure as code (IaC) frameworks, including Terraform by HashiCorp, Chef, and Puppet.** **Terraform offers an [OpenSearch module](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/opensearch_domain) that you can use to create Amazon OpenSearch Service domains. In** **many cases, you can use your existing infrastructure deployment pipeline and point the search engine module to the Amazon OpenSearch Service module.

If you are thinking about building pipelines from the ground up, or if you want to use AWS native services, AWS provides several of CI/CD tooling and service options. These include the following:
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html)
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html)
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html)

You can use these services to automate infrastructure build, test, and deployment. Deploying your pipelines by using any of these cloud-native services has many advantages, including the following:
+ Fully automated end-to-end (build, test, deployment) product releases
+ Deployment to multiple environments (dev, test, pre-prod, prod)
+ Integration with other AWS services
+ The ability to modernize your deployment pipelines to automate deployments of Amazon OpenSearch Service across multiple environments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
