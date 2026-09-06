---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-gitops-tools/codefresh.html
---

# Codefresh
<a name="codefresh"></a>

Codefresh is a modern CI/CD platform that supports GitOps principles, particularly for Kubernetes deployments. Codefresh offers a comprehensive set of CI/CD features, and its GitOps capabilities are notable.

## GitOps support
<a name="codefresh-gitops"></a>
+ **Git as the single source of truth**: Codefresh uses Git repositories as the authoritative source for application code, infrastructure definitions, and pipeline configurations. All changes to the system are made through Git, which ensures a complete history and audit trail.
+ **Declarative configuration**: Codefresh supports declarative pipeline definitions by using YAML files that are stored in Git. Kubernetes manifests, Helm charts, CloudFormation templates, and other IaC files can be version-controlled in the same repositories.
+ **GitOps dashboard**: Codefresh provides a dedicated GitOps dashboard for visualizing and managing GitOps workflows. It offers a clear view of the synchronization status between Git and cluster states.
+ **Automated synchronization**: Codefresh continuously monitors Git repositories for changes. It automatically starts pipelines to apply changes to the target environments when it detects differences.
+ **Kubernetes integration**: Codefresh offers deep integration with Kubernetes to support GitOps-style deployments across multiple clusters. It supports various Kubernetes resources and custom resource definitions (CRDs).
+ **Environment management**: You can define and manage multiple environments (such as development, staging, and production) as code. Codefresh supports promotion between environments by using GitOps practices.
+ **Argo CD integration**: Codefresh integrates with Argo CD for enhanced GitOps capabilities. It combines its CI capabilities with the CD strengths of Argo CD to provide a complete GitOps solution.
+ **Helm support**: Codefresh supports Helm charts, and provides easy management of complex applications through GitOps. It also offers Helm chart versioning and promotion.
+ **Progressive delivery**: Codefresh supports advanced deployment strategies such as canary and blue/green deployments. You can implement and manage these strategies through GitOps workflows.
+ **Rollbacks and versioning**: Codefresh enables easy rollbacks to previous versions if issues are detected after deployment. It maintains deployment versioning for traceability.
+ **Approval workflows**: Codefresh supports manual and automated approval processes for deployments. It enables controlled promotions between environments, in compliance with GitOps practices.
+ **IaC**: Codefresh supports integration with IaC tools such as CloudFormation and Terraform. It enables version control of infrastructure definitions alongside application code.
+ **Observability and monitoring**: Codefresh provides built-in monitoring and observability features. It also offers integrations with external monitoring tools for enhanced visibility.
+ **Security scanning**: Codefresh includes security scanning capabilities that can be integrated into GitOps workflows. Security checks are part of the automated deployment process.
+ **Audit trails**: Codefresh maintains comprehensive audit logs for all actions and changes. It supports the traceability and compliance aspects of GitOps.
+ **RBAC and access control**: Codefresh implements role-based access control (RBAC) for fine-grained permissions management. This helps ensure secure GitOps operations across teams and environments.
+ **GitOps automation**: Codefresh offers features to automate various aspects of GitOps workflows, including pull request (PR) creation and merging.
+ **Multi-cloud and hybrid deployments**: Codefresh supports GitOps workflows across multiple cloud providers and on-premises environments.
+ **Templating and parameterization**: Codefresh supports templates in pipeline and deployment configurations. This enables reusable and parameterized GitOps workflows.
+ **Integrated image management**: Codefresh provides built-in container image management capabilities. It integrates image builds and deployments into GitOps workflows.
+ **GitOps for secrets management**: Codefresh offers secure ways to manage secrets within GitOps workflows. It integrates with external secrets management solutions.
+ **Collaboration features**: Codefresh provides features for team collaboration within GitOps processes. These features include commenting, notifications, and shared dashboards.

The Codefresh approach to GitOps is notable for its integration of CI/CD capabilities with GitOps practices. It aims to provide a comprehensive platform that covers the entire software delivery lifecycle while adhering to GitOps principles.

The key differentiator of Codefresh in the GitOps area is its unified platform approach, which combines CI capabilities with CD and GitOps features. This makes it particularly suitable for teams that want an all-in-one solution that can handle complex CI/CD scenarios while implementing GitOps practices.

Codefresh offers a platform for organizations that want to adopt GitOps methodologies within a broader CI/CD context, especially when working with Kubernetes and cloud-native technologies.

For more information, see the [Codefresh documentation](https://codefresh.io/docs/gitops/).
