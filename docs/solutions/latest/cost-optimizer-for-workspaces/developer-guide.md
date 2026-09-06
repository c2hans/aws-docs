---
source_url: https://docs.aws.amazon.com/solutions/latest/cost-optimizer-for-workspaces/developer-guide.html
---

# Developer guide
<a name="developer-guide"></a>

This section provides the source code for the solution.

## Source code
<a name="source-code"></a>

You can visit our [GitHub repository](https://github.com/aws-solutions/cost-optimizer-for-amazon-workspaces) to download the templates and scripts for this solution, and to share your customizations with others.

## Container image
<a name="container-image"></a>

This section provides information about the container image used by the solution.

### Maintenance
<a name="maintenance"></a>

This solution uses Docker images with ﬁxed versions that match each solution release if automatic updates is not selected. The AWS Solutions team uses ECR Enhanced Scanning to detect Common Vulnerabilities and Exposures (CVEs) in the base image and installed packages. When possible, the team will publish patched images with the same version tag to resolve CVEs, without breaking compatibility with the released solution version. When images are patched, if they are on the same minor version, the stable tag will be automatically updated, and an additional image tag will be created in the format `<solution-version>_<date-of-fix>` . If a major or minor version is released, a full stack update will be required to get the latest image version as the stable tag will be incremented so that its version matches the version of the solution. If opting-in to automatic updates the changes to the image, including the CVEs and minor bug fixes, will automatically be applied to the image up to the latest matching minor release.

### Versions
<a name="versions"></a>

Customers on the latest solution version will receive security patches and minor, non-breaking, bug fixes automatically if they opt-in to automatic image updates. The image will automatically pull the latest image up to the latest matching minor version. In order to lock the container to a speciﬁc version, the task deﬁnition can be edited to specify the container to use a speciﬁc image version by using the tagged version of the image. Automatic updates can also be turned off by selecting **No** to automatic updates in CloudFormation when launching the stack. This will launch the image version matching the solution version.
