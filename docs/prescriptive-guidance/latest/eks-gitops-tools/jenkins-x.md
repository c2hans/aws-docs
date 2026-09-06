---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-gitops-tools/jenkins-x.html
---

# Jenkins X
<a name="jenkins-x"></a>

Jenkins X is a cloud-native, open-source CI/CD platform that implements GitOps principles for Kubernetes environments. Although Jenkins X isn't exclusively a GitOps tool such as Argo CD or Flux, it incorporates GitOps practices into its workflows.

## GitOps support
<a name="jenkins-x-gitops"></a>
+ **Git-centric workflow**: Jenkins X uses Git repositories as the primary source of truth for both application code and configuration. All changes to applications and infrastructure are made through Git.
+ **Environment as code (EaC)**: Environments (such as staging and production) are defined as code in Git repositories. This allows for version control and review of environment configurations.
+ **Automated CI/CD pipelines**: Jenkins X automatically sets up CI/CD pipelines for projects. These pipelines are defined as code (pipeline as code) and stored in Git.
+ **Kubernetes-native**: Jenkins X is built specifically for Kubernetes environments. It uses Kubernetes resources and custom resource definitions (CRDs).
+ **Preview environments**: Jenkins X automatically creates temporary environments for pull requests. It enables easy review and testing of changes before merges.
+ **Promotion between environments**: Jenkins X uses a GitOps approach to promote applications between environments (for example, from staging to production). Promotions are handled by using pull requests to ensure proper review and approval processes.
+ **Helm chart management**: Jenkins X uses Helm charts to package and deploy applications. Charts are version-controlled in Git repositories.
+ **Automated versioning**: Jenkins X automatically manages versioning of applications and releases. It uses semantic versioning and generates release notes.
+ **ChatOps integration**: Jenkins X supports ChatOps for common operations. This aligns with the GitOps principles of automation and collaboration.
+ **Extensibility**: This tool provides a plugin system for extending functionality. It allows integration with various cloud-native tools.
+ **Infrastructure as code (IaC)**: Jenkins X supports Terraform, CloudFormation, AWS Cloud Development Kit (AWS CDK), and other IaC tools to define and manage infrastructure. Infrastructure definitions are version-controlled alongside application code.
+ **Automated rollbacks**: Jenkins X supports automated rollbacks if issues are detected after deployment.
+ **Secrets management**: The tool integrates with external secrets management solutions to handle sensitive information securely.
+ **Observability**: Jenkins X provides integration with monitoring and logging tools for observability.
+ **Multi-cloud support**: Jenkins X is designed to work across different cloud providers and on-premises environments.
+ **Team collaboration**: This tool encourages collaboration through Git-based workflows and pull requests.
+ **Continuous feedback**: The tool provides quick feedback on changes through automated testing and preview environments.
+ **DevOps best practices**: Jenkins X implements DevOps best practices by default, including GitOps principles.
+ **Declarative configuration**: The tool uses declarative configurations for defining applications and environments.
+ **Automated upgrades**: Jenkins X provides tools for automating upgrades of the Jenkins X platform itself.

Jenkins X implements these GitOps principles to create a comprehensive CI/CD solution for Kubernetes. It aims to automate and streamline the entire software delivery process, from code commit to production deployment, while adhering to GitOps practices. By doing so, it helps teams achieve faster, more reliable, and more consistent deployments in cloud-native environments.

The key difference between Jenkins X and tools such as Argo CD or Flux is that Jenkins X provides a more comprehensive CI/CD solution, including build automation and pipeline management, while still incorporating GitOps principles for deployment and environment management. This makes it particularly suitable for teams who need an all-in-one solution that covers both CI and CD aspects within a single GitOps framework.

For more information, see the [Jenkins X documentation](https://jenkins-x.io/v3/develop/).

## Architecture
<a name="jenkins-x-architecture"></a>

The following diagram illustrates a GitOps-driven CD workflow that uses Jenkins X. For detailed information, see the [Jenkins X documentation](https://jenkins-x.io/v3/about/overview/).

![Jenkins X architecture and workflow on AWS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/eks-gitops-tools/images/guide-img/b6f49161-b2c5-42aa-b1d8-b0781836edb7/images/0038b3b0-9652-4e04-b03b-bb67d53d3e9b.png)

where:
+ **Step 1: Pull request (PR) merge**. A developer creates a pull request that includes changes to Kubernetes manifests, Helm charts, or application code that's stored in a Git repository. After review and approval, the PR is merged into the main branch and updates the desired state in source control.
+ **Step 2: Repository sync**. Jenkins X automatically triggers a CI/CD pipeline when it detects the change. The pipeline builds, tests, and promotes the application through different environments (for example, staging and production) by using GitOps principles.
+ **Step 3: Deployment to target namespaces**. Jenkins X updates the environment repositories (staging and production) with the new application versions. The cluster automatically reconciles the changes by pulling the latest manifests from Git and deploying the application to the appropriate namespaces.
