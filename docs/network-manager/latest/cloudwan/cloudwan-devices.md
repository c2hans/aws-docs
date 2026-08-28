---
source_url: https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-devices.html
---

# Devices in AWS Cloud WAN
<a name="cloudwan-devices"></a>

Devices represent a physical or virtual appliance. When you add a device to your core network, you can include optional information such as vendor, model and serial number to help you more easily identify the device.

In addition, you'll indicate whether the device is on-premises or in the AWS Cloud. If the device is on-premises you can specify optional information such as physical address. If the device is in the AWS Cloud, you can specify the zone, subnet ID, latitude and longitude, and physical address. Tags are also used to more help you identify this Network Manager resource.

Once added to your global network, a device can then be associated with a site. Before you can associate the device with a site using a link, you must first create the site. For more information on creating sites and linking the site to a device, see [Sites and links in AWS Cloud WAN](cloudwan-sites-links.md).

**Note**
A single device can't be associated with multiple sites.

**Topics**
+ [Add a device](cloudwan-devices-add.md)
+ [Delete a device](cloudwan-devices-delete.md)
+ [Edit a device](cloudwan-device-edit.md)
+ [View device details](cloudwan-devices-working.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
