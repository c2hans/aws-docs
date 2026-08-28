---
source_url: https://docs.aws.amazon.com/network-manager/latest/tgwnm/nm-sites.html
---

# Sites and links in AWS Global Networks for Transit Gateways
<a name="nm-sites"></a>

After you've added any devices to your AWS global network, you can associate of your devices with that particular site using a connection, or link. For information on adding devices, see [Devices in AWS Global Networks for Transit Gateways](nm-devices.md).

## Sites
<a name="nm-sites-about"></a>

A site represents the physical location of your network, using location information such as latitude, longitude, and address. You can have multiple sites for each of your network locations. Sites are useful when viewing the global network dashboard, which provides you the geographical location of these sites based on location information you provided. Once you create a site you can view the devices associated with the site and create links between devices and sites. You can also view any VPNs associated with the site as well as monitor CloudWatch metrics for this site.

## Links
<a name="nm-devices-about"></a>

A link represents the connection between a device and a site. Once you've added a device and created a site, you can create an association between the device and a site.

Tasks

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
