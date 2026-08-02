---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/developer-guide.html
---

# Developer guide
<a name="developer-guide"></a>

This section provides the source code for the solution and additional customizations.

## Source code
<a name="source-code"></a>

Visit our [GitHub repository](https://github.com/aws-solutions/distributed-load-testing-on-aws) to download the templates and scripts for this solution, and to share your customizations with others.

## Maintenance
<a name="maintenance"></a>

This solution uses Docker images with fixed versions that correspond to each solution release. By default, automatic updates are disabled, giving you complete control over when and which version updates are applied to your deployment. The AWS Solutions team uses Amazon ECR Enhanced Scanning to detect Common Vulnerabilities and Exposures (CVEs) in the base image and installed packages. When possible, the team publishes patched images with the same version tag to resolve CVEs without breaking compatibility with the released solution version.

When images are patched on the same minor version, the stable tag is automatically updated, and an additional image tag is created in the format `<solution-version>_<date-of-fix>`. If a major or minor version is released, you must perform a full stack update to get the latest image version, as the stable tag is incremented to match the solution version.

If you opt in to automatic updates during deployment, changes to the image, including CVE patches and minor bug fixes, are automatically applied up to the latest matching minor release.

## Versions
<a name="versions"></a>

By default, this solution deploys with automatic updates disabled. This means the container image version is locked to the specific version matching your deployed solution version, providing you with full control over version updates.

If you choose to enable automatic updates by selecting **Yes** during CloudFormation deployment, the solution will automatically receive security patches and minor, non-breaking bug fixes up to the latest matching minor version. For example, if you deploy version 4.0.0 with automatic updates enabled, you will receive updates up to 4.0.x, but not 4.1.0 or higher.

To manually control the container image version, you can edit the task definition to specify a particular image version using the tagged version format. This allows you to pin to a specific image version regardless of the automatic updates setting.
