---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-network-manual-enable-internet-access-image-builder.html
---

# Enable Internet Access for Your Image Builder in Amazon WorkSpaces Applications
<a name="managing-network-manual-enable-internet-access-image-builder"></a>

If you plan to enable internet access for your image builder, you must do so when you create the image builder.

**To enable internet access for an image builder**

1. Complete the steps in [Launch an Image Builder to Install and Configure Streaming Applications](tutorial-image-builder-create.md), up to **Step 3: Configure Network**.

1. Choose the VPC with a NAT gateway.

1. If **Subnet** is empty, select a subnet.

1. Continue with the steps in [Launch an Image Builder to Install and Configure Streaming Applications](tutorial-image-builder-create.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
