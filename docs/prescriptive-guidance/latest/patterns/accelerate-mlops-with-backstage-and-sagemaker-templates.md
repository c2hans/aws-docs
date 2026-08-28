---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/accelerate-mlops-with-backstage-and-sagemaker-templates.html
---

# Accelerate MLOps with Backstage and self-service Amazon SageMaker AI templates
<a name="accelerate-mlops-with-backstage-and-sagemaker-templates"></a>

*Ashish Bhatt, Shashank Hirematt, and Shivanshu Suryakar, Amazon Web Services*

## Summary
<a name="accelerate-mlops-with-backstage-and-sagemaker-templates-summary"></a>

Organizations that use machine learning operations (MLOps) systems face significant challenges in scaling, standardizing, and securing their ML infrastructure. This pattern introduces a transformative approach that combines [Backstage](https://backstage.io/), an open source developer portal, with [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) and hardened infrastructure as code (IaC) modules to improve how your data science teams can develop, deploy, and manage ML workflows.

The IaC modules for this pattern are provided in the GitHub [AWS AIOps modules](https://github.com/awslabs/aiops-modules/tree/main/modules/sagemaker) repository. These modules offer pre-built templates for setting up ML infrastructure and creating consistent ML environments. However, data scientists often struggle to use these templates directly because they require infrastructure expertise. Adding a developer portal such as Backstage creates a user-friendly way for data scientists to deploy standardized ML environments without needing to understand the underlying infrastructure details.

By using Backstage as a self-service platform and integrating preconfigured SageMaker AI templates, you can:
+ Accelerate time to value for your ML initiatives.
+ Help enforce consistent security and governance.
+ Provide data scientists with standardized, compliant environments.
+ Reduce operational overhead and infrastructure complexity.

This pattern provides a solution that addresses the critical challenges of MLOps and also provides a scalable, repeatable framework that enables innovation while maintaining organizational standards.

**Target audience**

This pattern is intended for a broad audience involved in ML, cloud architecture, and platform engineering within an organization. This includes:
+ **ML engineers** who want to standardize and automate ML workflow deployments.
+ **Data scientists** who want self-service access to preconfigured and compliant ML environments.
+ **Platform engineers** who are responsible for building and maintaining internal developer platforms and shared infrastructure.
+ **Cloud architects** who design scalable, secure, and cost-effective cloud solutions for MLOps.
+ **DevOps engineers** who are interested in extending continuous integration and continuous delivery (CI/CD) practices to ML infrastructure provisioning and workflows.
+ **Technical leads and managers** who oversee ML initiatives and want to improve team productivity, governance, and time to market.

For more information about MLOps challenges, SageMaker AI MLOps modules, and how the solution provided by this pattern can address the needs of your ML teams, see the [Additional information](#accelerate-mlops-with-backstage-and-sagemaker-templates-additional) section.

## Prerequisites and limitations
<a name="accelerate-mlops-with-backstage-and-sagemaker-templates-prereqs"></a>

**Prerequisites**
+ AWS Identity and Access Management (IAM) [roles and permissions](https://github.com/aws-samples/sample-aiops-idp-backstage/blob/main/SETUP.md#prerequisites) for provisioning resources into your AWS account
+ An understanding of [Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated.html), [SageMaker Projects](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects-whatis.html), [SageMaker Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-overview.html), and [SageMaker Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html) concepts
+ An understanding of IaC principles and experience with tools such as the [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/)

**Limitations**
+ **Limited template coverage**. Currently, the solution supports only SageMaker AI-related AIOps modules from the broader [AIOps solution](https://github.com/awslabs/aiops-modules). Other modules, such as Ray on Amazon Elastic Kubernetes Service (Amazon EKS), MLflow, Apache Airflow, and fine-tuning for Amazon Bedrock, are not yet available as Backstage templates.
+ **Non-configurable default settings**. Templates use fixed default configurations from the AIOps SageMaker modules with no customization. You cannot modify instance types, storage sizes, networking configurations, or security policies through the Backstage interface, which limits flexibility for specific use cases.
+ **AWS-only support**. The platform is designed exclusively for AWS deployments and doesn't support multicloud scenarios. Organizations that use cloud services outside the AWS Cloud cannot use these templates for their ML infrastructure needs.
+ **Manual credential management**. You must manually provide your AWS credentials for each deployment. This solution doesn’t provide integration with corporate identity providers, AWS IAM Identity Center, or automated credential rotation.
+ **Limited lifecycle management**. The templates lack comprehensive resource lifecycle management features such as automated cleanup policies, cost optimization recommendations, and infrastructure drift detection. You must manually manage and monitor deployed resources after creation.

## Architecture
<a name="accelerate-mlops-with-backstage-and-sagemaker-templates-architecture"></a>

The following diagram shows the solution architecture for a unified developer portal that standardizes and accelerates ML infrastructure deployment with SageMaker AI across environments.

![Architecture for unified developer portal with Backstage, CNOE, GitHub Actions, and Seed-Farmer.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/c16160cf-d637-423e-93a7-485ffbb28646/images/233adab3-83cf-42f3-a1de-72d0b8ade5ae.png)

In this architecture:

1. [AWS application modernization blueprints](https://github.com/aws-samples/appmod-blueprints.git) provision the infrastructure setup with an [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) cluster as a base for the [Cloud Native Operational Excellence (CNOE)](https://cnoe.io/) framework. This comprehensive solution addresses complex cloud-native infrastructure management challenges by providing a scalable internal developer platform (IDP). The blueprints offer a structured approach to setting up a robust, flexible infrastructure that can adapt to your evolving organizational needs.

1. The CNOE open source framework consolidates DevOps tools and solves ecosystem fragmentation through a unified platform engineering approach. By bringing together disparate tools and technologies, it simplifies the complex landscape of cloud-native development, so your teams can focus on innovation instead of toolchain management. The framework provides a standardized methodology for selecting, integrating, and managing development tools.

1. With CNOE, Backstage is deployed as an out-of-the-box solution within the Amazon EKS cluster. Backstage is bundled with robust authentication through [Keycloak](https://www.keycloak.org/) and comprehensive deployment workflows through [Argo CD](https://argo-cd.readthedocs.io/en/stable/). This integrated platform creates a centralized environment for managing development processes and provides a single place for teams to access, deploy, and monitor their infrastructure and applications across multiple environments.

1. A GitHub repository contains preconfigured AIOps software templates that cover the entire SageMaker AI lifecycle. These templates address critical ML infrastructure needs, including SageMaker Studio provisioning, model training, inference pipelines, and model monitoring. These templates help you accelerate your ML initiatives and ensure consistency across different projects and teams.

1. [GitHub Actions](https://github.com/features/actions) implements an automated workflow that dynamically triggers resource provisioning through the [Seed-Farmer](https://github.com/awslabs/seed-farmer) utility. This approach integrates the Backstage catalog with the AIOps modules repository and creates a streamlined infrastructure deployment process. The automation reduces manual intervention, minimizes human error, and ensures rapid, consistent infrastructure creation across different environments.

1. The [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html) helps you define and provision infrastructure as code, and ensures repeatable, secure, and compliant resource deployment across specified AWS accounts. This approach provides maximum governance with minimal manual intervention, so you can create standardized infrastructure templates that can be easily replicated, version-controlled, and audited.

## Tools
<a name="accelerate-mlops-with-backstage-and-sagemaker-templates-tools"></a>

**AWS services**
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html) is a software development framework that helps you define and provision AWS Cloud infrastructure in code.
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) helps you run Kubernetes on AWS without needing to install or maintain your own Kubernetes control plane or nodes.
+ [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/) is a managed ML service that helps you build and train ML models and then deploy them into a production-ready hosted environment.

**Other tools**
+ [Backstage](https://backstage.io/) is an open source framework that helps you build internal developer portals.
+ [GitHub Actions](https://github.com/features/actions) is a CI/CD platform that automates software development workflows, including tasks such as building, testing, and deploying code.

**Code repositories**

This pattern uses code and templates from the following GitHub repositories:
+ [AIOps internal developer platform (IDP) with Backstage](https://github.com/aws-samples/sample-aiops-idp-backstage/) repository
+ SageMaker AI-related modules from the [AWS AIOps modules](https://github.com/awslabs/aiops-modules) repository
+ [Modern engineering on AWS](https://github.com/aws-samples/appmod-blueprints) repository

**Implementation**

This implementation uses a production-grade deployment pattern for Backstage from the [Modern engineering on AWS](https://github.com/aws-samples/appmod-blueprints) repository. This approach significantly simplifies the setup process while incorporating AWS best practices for security and scalability.

The [Epics](#accelerate-mlops-with-backstage-and-sagemaker-templates-epics) section of this pattern outlines the implementation approach. For detailed, step-by-step deployment instructions, see the comprehensive [deployment guide](https://github.com/aws-samples/sample-aiops-idp-backstage/blob/main/SETUP.md) available in the [AIOps internal developer platform (IDP) with Backstage](https://github.com/aws-samples/sample-aiops-idp-backstage/) repository. The implementation includes:
+ Initial Backstage platform deployment
+ Integration of SageMaker software templates with Backstage
+ Consuming and maintaining Backstage templates

The deployment guide also includes guidance for ongoing maintenance, troubleshooting, and platform scaling.

## Best practices
<a name="accelerate-mlops-with-backstage-and-sagemaker-templates-best-practices"></a>

Follow these best practices to help ensure security, governance, and operational excellence in your MLOps infrastructure implementations.

**Template management**
+ Never make breaking changes to live templates.
+ Always test updates thoroughly before production deployment.
+ Maintain clear and well-documented template versions.

**Security**
+ Pin GitHub Actions to specific commit secure hash algorithms (SHAs) to help prevent supply chain attacks.
+ Use least privilege IAM roles with granular permissions.
+ Store sensitive credentials in [GitHub Secrets](https://docs.github.com/en/actions/concepts/security/secrets) and [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html).
+ Never hardcode credentials in templates.

**Governance and tracking**
+ Implement comprehensive resource tagging standards.
+ Enable precise cost tracking and compliance monitoring.
+ Maintain clear audit trails for infrastructure changes.

This guide provides a strong foundation for implementing these best practices by using Backstage, SageMaker AI, and IaC modules.

## Epics
<a name="accelerate-mlops-with-backstage-and-sagemaker-templates-epics"></a>

### Set up your ML environment
<a name="set-up-your-ml-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy Backstage. | This step uses the blueprints in the [Modern engineering on AWS](https://github.com/aws-samples/appmod-blueprints) repository to build a robust, scalable infrastructure that integrates multiple AWS services to create a centralized IDP for ML workflows. Follow the instructions in the [Backstage deployment section](https://github.com/aws-samples/sample-aiops-idp-backstage/blob/main/SETUP.md#backstage-deployment) of the deployment guide to clone the repository, install dependencies, bootstrap the AWS CDK configure environment variables, and deploy the Backstage platform.<br />The infrastructure uses Amazon EKS as a container orchestration platform for deploying IDP components. The Amazon EKS architecture includes secure networking configurations to establish strict network isolation and control access patterns. The platform integrates with authentication mechanisms to help secure user access across services and environments. | Platform engineer |
| Set up your SageMaker AI templates. | This step uses the scripts in the GitHub [AIOps internal developer platform (IDP) with Backstage](https://github.com/aws-samples/sample-aiops-idp-backstage/) repository. Follow the instructions in the [SageMaker template setup](https://github.com/aws-samples/sample-aiops-idp-backstage/blob/main/SETUP.md#sagemaker-template-setup) section of the deployment guide to clone the repository, set up prerequisites, and run the setup script.<br />This process creates a repository that contains the SageMaker AI templates that are required for integration with Backstage. | Platform engineer |
| Integrate the SageMaker AI** **templates with Backstage. | Follow the instructions in the [SageMaker templates integration](https://github.com/aws-samples/sample-aiops-idp-backstage/blob/main/SETUP.md#sagemaker-templates-integration) section of the deployment guide to register your SageMaker AI templates.<br />This step integrates the AIOps modules (SageMaker AI templates from the last step) into your Backstage deployment so you can self-service your ML infrastructure needs. | Platform engineer |
| Use the SageMaker AI templates from Backstage. | Follow the instructions in the [Using SageMaker templates](https://github.com/aws-samples/sample-aiops-idp-backstage/blob/main/SETUP.md#using-sagemaker-templates) section of the deployment guide to access the Backstage portal and create the ML environment in SageMaker Studio.<br />In the Backstage portal, you can select from available SageMaker AI templates, including options for SageMaker Studio environments, SageMaker notebooks, custom SageMaker project templates, and model deployment pipelines. After you provide configuration parameters, the platform creates dedicated repositories automatically and provisions AWS resources through GitHub Actions and Seed-Farmer. You can monitor progress through GitHub Actions logs and the Backstage component catalog. | Data scientist, Data engineer, Developer |

### Manage templates for governance and compliance
<a name="manage-templates-for-governance-and-compliance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Update SageMaker AI templates. | To update a SageMaker AI template in Backstage, follow these steps.1. Modify the template content:Make the necessary changes in the `template.yaml` file or by editing the files in the `skeleton/` directory.Test any new parameters, actions, or file structures locally or in a development environment.<br />2. Test changes:Use the Backstage UI or CLI (`@backstage/create-app`) to scaffold a test component by using the updated template.Validate that all steps run successfully and that the generated code meets your expectations.<br />3. Commit and push changes:Push the changes to the Git repository where the template is stored.<br />If the template is registered in a specific branch (for example, `main`), the updates will be reflected automatically.If you’re using versioning (see next step), make sure that the correct version or tag is updated. | Platform engineer |
| Create and manage multiple versions of a template. | For breaking changes or upgrades, you might want to create multiple versions of a SageMaker AI template.1. Use Git tags or branches for each version; for example:<pre>git checkout -b v2.0.0<br />git push origin v2.0.0</pre><br />2. (Optional but recommended) Register each version separately.<br />In Backstage, you can register different versions of a template as separate entities in the catalog, where each entity points to a specific branch or tag. For example (for a `.yaml` file):<pre>metadata:<br />name: node-service-template-v2<br />description: Node.js service template - Version 2<br />spec:<br />type: template<br />lifecycle: experimental<br />version: '2.0.0'</pre><br />3. Communicate changes clearly by maintaining a `CHANGELOG.md` file in the template repository. In this file, document which features or changes were introduced in each version of the template.<br />4. Deprecate older versions of the template, if necessary:Mark it as deprecated in the template description.Remove the version from the catalog if it’s no longer needed. | Platform engineer |

### Extend your ML environment
<a name="extend-your-ml-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Expand template coverage beyond SageMaker AI. | The current solution implements only SageMaker AI-related AIOps templates. You can extend the ML environment by adding [AIOps modules](https://github.com/awslabs/aiops-modules) and integrating custom software templates for additional AWS services and applications. You can create these by using the template designer interface in Backstage, by implementing custom scaffolder actions, or by maintaining template repositories with standard metadata. The platform supports template versioning, cross-team sharing, and validation workflows for consistency. For more information, see the [Backstage documentation](https://backstage.io/docs/overview/what-is-backstage/).<br />You can also implement template inheritance patterns to create specialized versions of base templates. This extensibility enables you to manage diverse AWS resources and applications beyond SageMaker AI while preserving the simplified developer experience and maintaining your organization’s standards. | Platform engineer |
| Use dynamic parameter injection. | The current templates use default configurations without customization, and run the Seed-Farmer CLI to deploy resources with default variables. You can extend the default configuration by using dynamic parameter injection for module-specific configurations. | Platform engineer |
| Enhance security and compliance. | To enhance security in the creation of AWS resources, you can enable role-based access control (RBAC) integration with single sign-on (SSO), SAML, OpenID Connect (OIDC), and policy as code enforcement. | Platform engineer |
| Add automated resource cleanup. | You can enable features for automated cleanup policies, and also add infrastructure drift detection and remediation. | Platform engineer |

### Clean up resources
<a name="clean-up-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Remove the Backstage infrastructure and SageMaker AI resources. | When you’ve finished using your ML environment, follow the instructions in the [Cleanup and resource management](https://github.com/aws-samples/sample-aiops-idp-backstage/blob/main/SETUP.md#cleanup-and-resource-management) section of the deployment guide to remove the Backstage infrastructure and to delete the SageMaker AI resources in your ML environment. | Platform engineer |

## Troubleshooting
<a name="accelerate-mlops-with-backstage-and-sagemaker-templates-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| AWS CDK bootstrap failures |  Verify AWS credentials and Region configuration. |
| Amazon EKS cluster access issues | Check **kubectl** configuration and IAM permissions. |
| Application Load Balancer connectivity issues | Make sure that security groups allow inbound traffic on port 80/443. |
| GitHub integration issues | Verify GitHub token permissions and organization access. |
| SageMaker AI deployment failures | Check [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/sagemaker.html#limits_sagemaker) and IAM permissions. |

## Related resources
<a name="accelerate-mlops-with-backstage-and-sagemaker-templates-resources"></a>
+ [Platform engineering ](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-caf-platform-perspective/platform-eng.html)(in the guide *AWS Cloud Adoption Framework: Platform perspective*)
+ [Amazon SageMaker AI documentation](https://docs.aws.amazon.com/sagemaker/)
+ [Backstage Software Templates](https://backstage.io/docs/features/software-templates/) (Backstage website)
+ [AIOps modules repository](https://github.com/awslabs/aiops-modules) (collection of reusable IaC modules for ML)
+ [AIOps internal developer platform (IDP) with Backstage](https://github.com/aws-samples/sample-aiops-idp-backstage/) repository
+ [Modern engineering on AWS](https://github.com/aws-samples/appmod-blueprints) repository
+ [Cloud Native Operational Excellence (CNOE) website](https://cnoe.io/)

## Additional information
<a name="accelerate-mlops-with-backstage-and-sagemaker-templates-additional"></a>

**Business challenges**

Organizations that embark on or scale their MLOps initiatives frequently encounter these business and technical challenges:
+ **Inconsistent environments**. The lack of standardized development and deployment environments makes collaboration difficult and increases deployment risks.
+ **Manual provisioning overhead**. Manually setting up an ML infrastructure with SageMaker Studio, Amazon Simple Storage Service (Amazon S3) buckets, IAM roles, and CI/CD pipelines is time-consuming and error-prone, and diverts data scientists from their core task of model development.
+ **Lack of discoverability and reuse**. The lack of a centralized catalog makes it difficult to find existing ML models, datasets, and pipelines. This leads to redundant work and missed opportunities for reuse.
+ **Complex governance and compliance**. Ensuring that ML projects adhere to organizational security policies, data privacy regulations, and compliance standards such as Health Insurance Portability and Accountability Act (HIPAA) and General Data Protection Regulation (GDPR) can be challenging without automated guardrails.
+ **Slow time to value**. The cumulative effect of these challenges results in protracted ML project lifecycles and delays the realization of business value from ML investments.
+ **Security risks**. Inconsistent configurations and manual processes can introduce security vulnerabilities that make it difficult to enforce least privilege and network isolation.

These issues prolong development cycles, increase operational overhead, and introduce security risks. The iterative nature of ML requires repeatable workflows and efficient collaboration.

Gartner predicts that by 2026, 80% of software engineering organizations will have platform teams. (See [Platform Engineering Empowers Developers to be Better, Faster, Happier](https://www.gartner.com/en/experts/top-tech-trends-unpacked-series/platform-engineering-empowers-developers) on the Gartner website.) This prediction highlights how an IDP can accelerate software delivery. As an IDP, Backstage helps restore order to complex infrastructure so that teams can deliver high-quality code rapidly and safely. Integrating Backstage with hardened AIOps modules helps you shift from reactive troubleshooting to proactive prevention.

**MLOps SageMaker modules**

The [AIOps modules](https://github.com/awslabs/aiops-modules) in the GitHub repository used for this pattern provide a valuable foundation for standardizing MLOps on AWS through reusable and hardened IaC. These modules encapsulate best practices for provisioning SageMaker projects, pipelines, and associated networking and storage resources, with the goal to reduce complexity and accelerate the setup of ML environments. You can use these templates for various MLOps use cases to establish consistent and secure deployment patterns that foster a more governed and efficient approach to ML workflows.

Using the AIOps modules directly often requires platform teams to deploy and manage these IaC templates, which can present challenges for data scientists who want self-service access. Discovering and understanding the available templates, configuring the necessary parameters, and triggering their deployment might require navigating AWS service consoles or directly interacting with IaC tools. This can create friction, increase cognitive load for data scientists who prefer to focus on ML tasks, and potentially lead to inconsistent parameterization or deviations from organizational standards if these templates aren’t managed through a centralized and user-friendly interface. Integrating these powerful AIOps modules with an IDP such as Backstage helps address these challenges by providing a streamlined, self-service experience, enhanced discoverability, and stronger governance controls for using these standardized MLOps building blocks.

**Backstage as IDP**

An internal developer platform (IDP) is a self-service layer built by platform teams to simplify and standardize how developers build, deploy, and manage applications. It abstracts infrastructure complexity and provides developers with easy access to tools, environments, and services through a unified interface.

The primary goal of an IDP is to enhance developer experience and productivity by:
+ Enabling self-service for tasks such as service creation and deployment.
+ Promoting consistency and compliance through standard templates.
+ Integrating tools across the development lifecycle (CI/CD, monitoring, and documentation).

Backstage is an open source developer portal that was created by Spotify and is now part of the Cloud Native Computing Foundation (CNCF). It helps organizations build their own IDP by providing a centralized, extensible platform to manage software components, tools, and documentation. With Backstage, developers can:
+ Discover and manage all internal services through a software catalog.
+ Create new projects by using predefined templates through the scaffolder plugin.
+ Access integrated tooling such as CI/CD pipelines, Kubernetes dashboards, and monitoring systems from one location.
+ Maintain consistent, markdown-based documentation through TechDocs.

**FAQ**

**What's the difference between using this Backstage template versus deploying SageMaker Studio manually through the SageMaker console?**

The Backstage template provides several advantages over manual AWS console deployment, including standardized configurations that follow organizational best practices, automated IaC deployment using Seed-Farmer and the AWS CDK, built-in security policies and compliance measures, and integration with your organization's developer workflows through GitHub. The template also creates reproducible deployments with version control, which make it easier to replicate environments across different stages (development, staging, production) and maintain consistency across teams. Additionally, the template includes automated cleanup capabilities and integrates with your organization's identity management system through Backstage. Manual deployment through the console requires deep AWS expertise and doesn’t provide version control or the same level of standardization and governance that the template offers. For these reasons, console deployments are more suitable for one-off experiments than production ML environments.

**What is Seed-Farmer and why does this solution use it?**

Seed-Farmer is an AWS deployment orchestration tool that manages infrastructure modules by using the AWS CDK. This pattern uses Seed-Farmer because it provides standardized, reusable infrastructure components that are specifically designed for AI/ML workloads, handles complex dependencies between AWS services automatically, and ensures consistent deployments across different environments.

**Do I need to install the AWS CLI to use these templates?**

No, you don't have to install the AWS CLI on your computer. The templates run entirely through GitHub Actions in the cloud. You provide your AWS credentials (access key, secret key, and session token) through the Backstage interface, and the deployment happens automatically in the GitHub Actions environment.

**How long does it take to deploy a SageMaker Studio environment?**

A typical SageMaker Studio deployment takes 15-25 minutes to complete. This includes AWS CDK bootstrapping (2-3 minutes), Seed-Farmer toolchain setup (3-5 minutes), and resource creation (10-15 minutes). The exact time depends on your AWS Region and the complexity of your networking setup.

**Can I deploy multiple SageMaker environments in the same AWS account?**

Yes, you can. Each deployment creates resources with unique names based on the component name you provide in the template. However, be aware of AWS service quotas: Each account can have a limited number of SageMaker domains per Region, so [check your quotas](https://docs.aws.amazon.com/general/latest/gr/sagemaker.html#limits_sagemaker) before you create multiple environments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
