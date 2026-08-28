---
source_url: https://docs.aws.amazon.com/outposts/latest/install-server/authorize-1.html
---

# Connect your laptop to the Outposts server
<a name="authorize-1"></a>

Connect the USB cable to your laptop first and then to the server. The server includes a USB chip that creates a virtual serial port available to you on the laptop. You can use this virtual serial port to connect to the server with serial terminal emulation software. You can only use this virtual serial port to run Outpost Configuration Tool commands.

**To connect the laptop to the server**
Plug the USB cable into your laptop first, then into the server.

**Note**
The USB chip requires drivers to create the virtual serial port. Your operating system should automatically install the required drivers if they are not already present. To download and install the drivers, see [Installation Guides](https://ftdichip.com/document/installation-guides/) from FTDI.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
