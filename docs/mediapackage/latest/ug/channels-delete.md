---
source_url: https://docs.aws.amazon.com/mediapackage/latest/ug/channels-delete.html
---

# Deleting a channel
<a name="channels-delete"></a>

Delete a channel to stop AWS Elemental MediaPackage from receiving further content. You must delete the channel's endpoints (as described in [Deleting an endpoint](endpoints-delete.md)) before you can delete the channel.

You can use the MediaPackage console, the AWS CLI, or the MediaPackage API to delete a channel. For information about deleting a channel through the AWS CLI or MediaPackage API, see the [AWS Elemental MediaPackage API Reference](https://docs.aws.amazon.com/mediapackage/latest/apireference/).

**To delete a channel (console)**

1. Open the MediaPackage console at [https://console.aws.amazon.com/mediapackage/](https://console.aws.amazon.com/mediapackage/).

1. If the **Channels** page doesn't appear, on the MediaPackage home page, choose **Skip and go to console**.

1. On the **Channels** page, choose the name of the channel that you want to delete.

1. Choose **Delete**.

   If there's an Amazon CloudFront distribution associated with the channel, select the CloudFront link in the confirmation dialog box to go to the CloudFront console to delete the distribution. MediaPackage will not delete the distribution when the channel is deleted. For help deleting in CloudFront, see [Deleting a distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowToDeleteDistribution.html) in the *Amazon CloudFront Developer Guide*.

1. In the confirmation dialog box in MediaPackage, choose **Delete** to proceed with the channel deletion.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V1. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
