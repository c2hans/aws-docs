---
source_url: https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-smooth-packager.html
---

# Packager settings fields
<a name="endpoints-smooth-packager"></a>

The Packager settings fields hold general information about the endpoint.

1. For **Packaging type**, choose **Microsoft Smooth**.

1. (Optional) For **Segment duration**, enter the duration (in seconds) of each segment. Enter a value equal to, or a multiple of, the input segment duration. If the value that you enter is different from the input segment duration, AWS Elemental MediaPackage rounds segments to the nearest multiple of the input segment duration.

1. (Optional) For **Manifest window duration**, enter the total duration (in seconds) of the manifest.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V1. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
