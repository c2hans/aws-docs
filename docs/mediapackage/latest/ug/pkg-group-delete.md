---
source_url: https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-group-delete.html
---

# Deleting a packaging group
<a name="pkg-group-delete"></a>

To stop AWS Elemental MediaPackage from delivering more content from an asset, delete the packaging group. Before you can delete the packaging group, you must delete the group's packaging configurations and any assets that use the group.
+ To delete a packaging configuration, see [Deleting a packaging configuration](pkg-cfig-delete.md).
+ To delete an asset, see [Deleting an asset](asset-delete.md).

To delete a packaging group, you can use the MediaPackage console, the AWS CLI, or the MediaPackage API. For information about deleting a packaging group with the AWS CLI or MediaPackage API, see [Packaging\_groups id](https://docs.aws.amazon.com/mediapackage-vod/latest/apireference/packaging_groups-id.html) in the *AWS Elemental MediaPackage VOD API Reference*.

**To delete a packaging group (console)**

1. Open the MediaPackage console at [https://console.aws.amazon.com/mediapackage/](https://console.aws.amazon.com/mediapackage/).

1. In the navigation pane, under **Video on demand**, choose **Packaging groups**.

1. On the **Packaging groups** page, choose the packaging group that you want to delete.

1. Choose **Delete**.

1. In the **Packaging group delete** dialog box, choose **Delete** to finish deleting the packaging group.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V1. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
