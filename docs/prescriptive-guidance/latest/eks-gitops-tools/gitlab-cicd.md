---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-gitops-tools/gitlab-cicd.html
---

# GitLab CI/CD
<a name="gitlab-cicd"></a>

GitLab CI/CD is an integrated part of the GitLab platform that provides continuous integration, delivery, and deployment capabilities. Although GitLab CI/CD isn't exclusively a GitOps tool, you can configure it to implement GitOps principles, especially when you use it for Kubernetes deployments.

## GitOps support
<a name="gitlab-cicd-gitops"></a>
+ **Git as the single source of truth**: GitLab CI/CD uses Git repositories to store both application code and infrastructure configurations. All changes to the system are made through Git, which ensures a complete history and audit trail.
+ **Declarative configuration**: GitLab CI/CD pipelines are defined in a `.gitlab-ci.yml` file, which is a declarative configuration stored in the Git repository. Kubernetes manifests, Helm charts, or other infrastructure as code (IaC) files can be stored in the same repository to define the desired state of the infrastructure.
+ **Automated pipelines**: GitLab CI/CD automatically triggers pipelines when changes are pushed to the repository. These pipelines can include stages for building, testing, and deploying applications.
+ **Kubernetes integration**: GitLab CI/CD provides native Kubernetes integration and supports GitOps-style deployments to Kubernetes clusters. It can automatically create and manage Kubernetes resources based on the configuration in Git.
+ **Environment management**: GitLab CI/CD supports the definition of multiple environments (such as staging and production) as code. Deployments to these environments can be automated or might require manual approval, in compliance with GitOps practices.
+ **Review applications**: GitLab can automatically create temporary environments for merge requests, similar to preview environments in other GitOps tools. This supports easy review and testing of changes before merges.
+ **Continuous deployment**: GitLab CI/CD can be configured to automatically deploy changes to Kubernetes clusters when changes are merged to specific branches.
+ **IaC**: GitLab CI/CD supports integration with tools such as Terraform and CloudFormation to manage infrastructure as code. Infrastructure definitions can be version-controlled alongside application code.
+ **Observability and monitoring**: GitLab CI/CD provides built-in monitoring and observability features, including integration with Prometheus and Grafana.
+ **Security scanning**: GitLab CI/CD includes built-in security scanning tools that can be integrated into the CI/CD pipeline to enforce security as part of the GitOps workflow.
+ **Container registry**: GitLab CI/CD includes a built-in container registry for seamless integration of container image management in the GitOps workflow.
+ **Auto DevOps**: The Auto DevOps feature in GitLab CI/CD can automatically configure CI/CD pipelines that follow GitOps principles for Kubernetes deployments.
+ **Approval workflows**: GitLab CI/CD supports approval processes for deployments, which provide controlled promotions between environments.
+ **Secrets management**: GitLab CI/CD provides features to securely manage and use secrets within CI/CD pipelines.
+ **Versioning and releases**: GitLab CI/CD supports automatic versioning and release management as part of the CI/CD process.
+ **Rollbacks**: GitLab CI/CD enables easy rollbacks to previous versions if issues are detected after deployment.
+ **Audit logs**: GitLab CI/CD provides comprehensive audit logs for all actions to support the traceability aspect of GitOps.
+ **Multi-project pipelines**: GitLab CI/CD supports complex GitOps workflows that span multiple projects or repositories.
+ **ChatOps**: GitLab CI/CD supports ChatOps integrations, which provide collaboration and operations through chat interfaces.
+ **Kubernetes cluster management**: GitLab CI/CD provides features for managing Kubernetes clusters directly from the GitLab interface.

Although GitLab CI/CD is not exclusively designed for GitOps, it can be used effectively to implement GitOps practices, especially for teams that already use GitLab as their primary development platform. Its integrated approach, which combines source control, CI/CD, and Kubernetes management, makes it a powerful tool for implementing GitOps workflows.

The key difference between GitLab CI/CD and dedicated GitOps tools such as Argo CD or Flux is that GitLab provides a more comprehensive platform that includes source control management, issue tracking, and other development tools along with its CI/CD capabilities. This makes it particularly suitable for teams that need an all-in-one solution that can implement GitOps practices within a broader development system.

For more information about GitLab CI/CD and its architecture, see the [GitLab CI/CD documentation](https://docs.gitlab.com/ci/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
