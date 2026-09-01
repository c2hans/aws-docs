---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/deploying-starter-packages.html
---

# Deploying starter packages
<a name="deploying-starter-packages"></a>

The Modern Data Architecture Accelerator provides several starter packages that you can deploy to quickly establish common data architecture patterns. Each starter package includes pre-configured components that work together to create a complete solution for specific use cases.

When deploying starter packages, consider the following:
+  **Environment requirements**: Review the prerequisites for each package to verify your AWS environment meets the necessary requirements
+  **Configuration options**: Each package includes sample configuration files that can be customized to match your specific needs
+  **Deployment methods**: Packages can be deployed using the MDAA CLI, AWS CDK directly, or through the CloudFormation installer
+  **Post-deployment steps**: Most packages require additional configuration after deployment to fully enable all features

**Important**
Before deploying any starter kit, address the `TODO` markers in the kit’s config files. Where a kit includes a `roles.yaml`, its CDK Nag suppression blocks are commented out by default. The location of that file differs by kit — it sits either at the kit root or in a subdirectory such as `governance/`, `shared/`, `common/`, or `config/` — and some kits have more than one copy, so find every copy in the kit directory before you start. Not every kit has one; `mlops_platform`, for example, has none.
Review each suppression, confirm the associated IAM permissions are acceptable for your environment, and uncomment the ones that apply. If you leave them commented, `mdaa synth` and `mdaa deploy` fail CDK Nag compliance checks and the deployment does not proceed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Modern Data Architecture Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
