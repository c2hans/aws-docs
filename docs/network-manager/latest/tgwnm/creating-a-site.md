---
source_url: https://docs.aws.amazon.com/network-manager/latest/tgwnm/creating-a-site.html
---

# Create a site using AWS Network Manager
<a name="creating-a-site"></a>

Create a site to represent the physical location of your network. Location information is used in the Network Manager transit gateway dashboards.

**To create a site**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Sites**. Choose **Create site**.

1. For **Name** and **Description**, enter a name and description for the site.

1. For **Address**, enter the physical address of the site, for example, `New York, NY 10004`.

1. For **Latitude**, enter the latitude coordinates for the site, for example, `40.7128`.

1. For **Longitude**, enter the longitude coordinates for the site, for example, `-74.0060`.

1. Choose **Create site**.

**Creating and viewing a site using the AWS CLI**
Use the following commands:
+ To create a site: [create-site](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/create-site.html)
+ To view your sites: [get-sites](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/get-sites.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
