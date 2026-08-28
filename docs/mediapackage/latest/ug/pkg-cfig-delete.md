---
source_url: https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-cfig-delete.html
---

# Deleting a packaging configuration
<a name="pkg-cfig-delete"></a>

To remove a playback endpoint from an asset, delete the packaging configuration.

To delete a packaging configuration, you can use the AWS Elemental MediaPackage console, the AWS CLI, or the MediaPackage API. For information about deleting a packaging configuration with the AWS CLI or MediaPackage API, see [Packaging\_configurations id](https://docs.aws.amazon.com/mediapackage-vod/latest/apireference/packaging_configurations-id.html) in the *AWS Elemental MediaPackage VOD API Reference*.

**To delete a packaging configuration (console)**

1. Open the MediaPackage console at [https://console.aws.amazon.com/mediapackage/](https://console.aws.amazon.com/mediapackage/).

1. In the navigation pane, under **Video on demand**, choose **Packaging groups**.

1. On the **Packaging groups** page, choose the group that contains the configuration that you're deleting.

1. On the details page for the packaging group, under **Packaging configurations**, choose either the packaging configuration ID of the configuration that you're deleting and choose **Delete** or choose **Manage configurations**, **Actions**, **Delete**.

1. On the **Delete packaging configurations** page, choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V1. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
