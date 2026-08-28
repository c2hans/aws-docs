---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/devops-pipeline-accelerator/introduction.html
---

# Standardizing IaC pipelines by using the AWS DevOps Pipeline Accelerator
<a name="introduction"></a>

*Ruchika Modi, Ashish Bhatt, Eknaprasath P, and Mayuri Patil, Amazon Web Services*

It's common for organizations to use various technology stacks, such as:
+ **Infrastructure as code (IaC)** – HashiCorp Terraform, AWS CloudFormation, and AWS Cloud Development Kit (AWS CDK)
+ **Application development** – npm, Gradle, Apache Maven, and TypeScript
+ **Application deployment** – Amazon Simple Storage Service (Amazon S3), Amazon Elastic Container Service (Amazon ECS), Amazon Elastic Kubernetes Service (Amazon EKS), and AWS Lambda

With these diverse technology stacks, each team creates their own pipeline to build and deploy applications or infrastructure. This approach lacks standardization,** **increases time to production,** **and introduces code redundancy. Each product follows its own processes for application or infrastructure delivery to various environments. It also adds complexity for compliance teams, making it more difficult for them** **to enforce controls and quality gates.

## What is DPA?
<a name="what-is-dpa"></a>

[DevOps Pipeline Accelerator](https://github.com/aws-samples/aws-devops-pipeline-accelerator) (DPA) is a solution composed of templates that help you construct a complete continuous integration and continuous delivery (CI/CD) pipeline for application or infrastructure deployment. This solution builds centralized templates as accelerators. Product teams can use these accelerators to help onboard their applications into CI/CD, which allows teams to focus on developing their business functionality.

The accelerators are configurable. You configure the build tools, deployment platform, quality gates rules, and more. Using an IaC tool, you construct the entire pipeline based on these configurations. These pipeline accelerators currently support the following common continuous integration and continuous delivery (CI/CD) services and tools:
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)
+ [GitLab CI/CD](https://docs.gitlab.com/ee/ci/index.html)
+ [GitHub Actions](https://docs.github.com/en/actions)
+ [Jenkins](https://www.jenkins.io/doc/book/)

This solution builds upon the best practices defined in the [AWS Deployment Pipeline Reference Architecture (DPRA)](https://pipelines.devops.aws.dev/).

## Benefits of using the DPA
<a name="benefits"></a>

The following are the high-level benefits that DPA provides:
+ **Standardization and consistency** – Standardized application pipelines improve consistency for CI/CD and application deployment.
+ **Reusability** – DPA is reusable and scalable. Applications consume accelerators in order to orchestrate pipelines.
+ **Velocity** – Application teams focus more on development rather than pipeline construction, which improves the overall development velocity.
+ **Security** – Built-in quality gates help secure the application during deployment by following DevSecOps best practices.
+ **Scalability** – DPA templates are configurable and highly scalable. They easily integrate with any type of application that is deployed through a supported CI/CD service or tool.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
