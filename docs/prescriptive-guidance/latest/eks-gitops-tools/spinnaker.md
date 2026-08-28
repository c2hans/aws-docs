---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-gitops-tools/spinnaker.html
---

# Spinnaker
<a name="spinnaker"></a>

Although Spinnaker isn't exclusively designed as a GitOps tool, you can configure it to implement GitOps principles, especially when you use it for cloud-native and Kubernetes deployments.

## GitOps support
<a name="spinnaker-gitops"></a>
+ **Declarative configuration**: Spinnaker uses declarative pipeline definitions, which are typically stored as JSON or YAML files. These pipeline definitions can be version-controlled in Git repositories, in alignment with GitOps practices.
+ **IaC**: Spinnaker supports the definition of infrastructure and deployment configurations as code. These definitions can be stored in Git repositories, and can serve as the single source of truth.
+ **Multi-cloud deployments**: Spinnaker is designed to work across multiple cloud providers and Kubernetes clusters. It enables consistent GitOps practices across diverse environments.
+ **Pipeline as code**: Spinnaker pipelines can be defined as code and stored in Git repositories. This allows for version control and the review of deployment processes.
+ **Automated deployments**: You can configure Spinnaker to automatically start deployments based on changes in Git repositories. The tool supports continuous deployment practices that are central to GitOps.
+ **Immutable infrastructure**: Spinnaker promotes the use of immutable infrastructure, which is a key concept in GitOps. It encourages the deployment of new instances instead of modifying existing instances.
+ **Rollbacks and versioning**: Spinnaker provides robust rollback capabilities and quick reversion to previous known good states. It supports versioning of deployments, in alignment with GitOps principles of traceability.
+ **Approval workflows**: Spinnaker includes manual judgment stages in pipelines to support controlled promotions between environments. This supports GitOps practices of separation between deployments and releases.
+ **Canary and blue/green deployments**: Spinnaker supports advanced deployment strategies that align with GitOps practices for safe and controlled releases.
+ **Integration with version control systems**: Spinnaker can integrate with various Git providers to start pipelines based on repository events.
+ **Kubernetes integration**: Spinnaker provides native support for Kubernetes and supports GitOps-style management of Kubernetes resources.
+ **Artifact management**: Spinnaker supports artifact management and versioning, which are crucial for maintaining a GitOps workflow.
+ **Observability and monitoring**: Spinnaker offers integration with monitoring tools to support the observability aspect of GitOps.
+ **Audit trail**: Spinnaker provides detailed deployment logs and history, which support the auditability principle of GitOps.
+ **Role-based access control (RBAC)**: This tool implements RBAC for fine-grained control over who can perform which actions, in alignment with GitOps security practices.
+ **Templating and parameterization**: Spinnaker supports templating in pipeline definitions to enable reusable and parameterized deployments.
+ **Environment promotion**: Spinnaker facilitates the promotion of applications between environments (for example, from staging to production) in a controlled manner.
+ **Integration with CI tools**: Spinnaker can integrate with various continuous integration (CI) tools to provide a complete CI/CD pipeline that adheres to GitOps principles.
+ **Custom stages and extensions**: This tool supports custom stages and extensions, so teams can implement GitOps workflows that are tailored to their needs.
+ **Centralized management**: Spinnaker provides a centralized platform for managing deployments across multiple environments and cloud providers.

Although Spinnaker isn't primarily marketed as a GitOps tool, its flexibility and robust feature set make it capable of implementing GitOps workflows, especially in complex, multi-cloud environments. The key difference between Spinnaker and dedicated GitOps tools such as Argo CD or Flux is that Spinnaker offers a more comprehensive continuous delivery platform with advanced deployment strategies and multi-cloud support.

Spinnaker's strength lies in its ability to handle complex deployment scenarios across various cloud providers and its support for advanced deployment strategies. When Spinnaker is configured properly, it can implement GitOps principles effectively. This makes it a powerful tool for organizations who want to adopt GitOps practices in diverse and complex environments.

For more information, see the [Spinnaker documentation](https://spinnaker.io/docs/).

## Architecture
<a name="spinnaker-architecture"></a>

The following diagram illustrates a GitOps-driven CD workflow that uses Spinnaker and Jenkins X. For detailed information, see the [Spinnaker documentation](https://spinnaker.io/docs/concepts/).

![Spinnaker architecture and workflow on AWS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/eks-gitops-tools/images/guide-img/b6f49161-b2c5-42aa-b1d8-b0781836edb7/images/6601ff56-3d46-4dcf-ab6f-0ae4cca17e47.png)

where:
+ **Step 1: Code commit**. Developers commit application code changes to a Git repository. These changes could include updates to the application itself, Dockerfiles, or Kubernetes manifests.
+ **Step 2: Jenkins build and image creation**. Jenkins is automatically triggered by the Git repository through a webhook or polling. Jenkins builds the application, creates a Docker image, and pushes the built image to a configured Docker registry (such as Amazon ECR or Docker Hub).
+ **Step 3: Spinnaker image monitoring and pipeline trigger**. Spinnaker continuously monitors the Docker registry for new images. When a new image version is detected, Spinnaker automatically triggers a pipeline to start the deployment process.
+ **Step 4: Deployment to target namespaces**. Spinnaker deploys the new Docker image to Amazon EKS. Based on pipeline configurations, the image is deployed to target namespaces in the cluster. Spinnaker ensures that the latest application version is deployed while adhering to defined deployment strategies such as blue/green or canary deployments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
