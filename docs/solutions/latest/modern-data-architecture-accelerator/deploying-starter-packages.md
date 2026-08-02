---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/deploying-starter-packages.html
---

# Deploying starter packages
<a name="deploying-starter-packages"></a>

The Modern Data Architecture Accelerator provides several starter packages that you can deploy to quickly establish common data architecture patterns. Each starter package includes pre-configured components that work together to create a complete solution for specific use cases.

When deploying starter packages, consider the following:
+  **Environment requirements**: Review the prerequisites for each package to ensure your AWS environment meets the necessary requirements
+  **Configuration options**: Each package includes sample configuration files that can be customized to match your specific needs
+  **Deployment methods**: Packages can be deployed using the MDAA CLI, AWS CDK directly, or through the CloudFormation installer
+  **Post-deployment steps**: Most packages require additional configuration after deployment to fully enable all features

**Important**
Before deploying any starter kit, address the `TODO` markers in each kit’s config files. In particular, the CDK Nag suppression blocks in `roles.yaml` (path varies by kit — for example, `govern/roles.yaml`, `governance/roles.yaml`, `shared/roles.yaml`, or `common/roles.yaml`) are commented out by default. Review each suppression, confirm the associated IAM permissions are acceptable for your environment, and uncomment the ones that apply. If you leave them commented, `mdaa synth`/`deploy` will fail CDK Nag compliance checks and the deployment will not proceed.

The following sections provide detailed information about each available starter package, including architecture components, deployment instructions, and usage guidelines.
