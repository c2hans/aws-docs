---
source_url: https://docs.aws.amazon.com/mediapackage/latest/ug/channels-rotate-creds.html
---

# Rotating credentials on an input URL
<a name="channels-rotate-creds"></a>

Rotate credentials on an input URL to generate a new WebDAV user name and password.

You can use the AWS Elemental MediaPackage console or the MediaPackage API to rotate credentials. For information about rotating credentials through the MediaPackage API, see the [AWS Elemental MediaPackage API Reference](https://docs.aws.amazon.com/mediapackage/latest/apireference/).

**To rotate credentials (console)**

1. Open the MediaPackage console at [https://console.aws.amazon.com/mediapackage/](https://console.aws.amazon.com/mediapackage/).

1. If the **Channels** page doesn't appear, on the MediaPackage home page, choose **Skip and go to console**.

1. On the **Channels** page, choose the name of the channel that holds the input URL that you're rotating the credentials for.

1. On the channel's details page, choose the input URL that you're rotating credentials for, and then choose **Rotate credentials**.

1. To confirm that you want to generate a new user name and password, choose **Rotate**.

   MediaPackage displays the new credentials.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V1. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
