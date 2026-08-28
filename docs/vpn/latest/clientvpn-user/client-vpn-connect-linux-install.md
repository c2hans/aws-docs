---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-user/client-vpn-connect-linux-install.html
---

# Install the provided AWS Client VPN for Linux
<a name="client-vpn-connect-linux-install"></a>

There are multiple methods that can be used to install the AWS provided client for Linux. Use one of the methods provided in the following options. Before you begin, ensure that you've read the [requirements](client-vpn-connect-linux.md#client-vpn-connect-linux-req).

**Option 1: Install via package repository**

1. Add the AWS VPN Client public key to your Ubuntu OS.

   ```
   wget -qO- https://d20adtppz83p9s.cloudfront.net/GTK/latest/debian-repo/awsvpnclient_public_key.asc | sudo tee /etc/apt/trusted.gpg.d/awsvpnclient_public_key.asc
   ```

1. Use the following command to add the repository to your Ubuntu OS (version 22.04 and above):

   ```
   echo "deb [arch=amd64] https://d20adtppz83p9s.cloudfront.net/GTK/latest/debian-repo ubuntu main" | sudo tee /etc/apt/sources.list.d/aws-vpn-client.list
   ```

1. Use the following command to update the repositories on your system.

   ```
   sudo apt-get update
   ```

1. Use the following command to install the AWS provided client for Linux.

   ```
   sudo apt-get install awsvpnclient
   ```

**Option 2: Install using the .deb package file**

1. Download the .deb file from [AWS Client VPN download ](https://d20adtppz83p9s.cloudfront.net/GTK/latest/awsvpnclient_amd64.deb) or by using the following command.

   ```
   curl https://d20adtppz83p9s.cloudfront.net/GTK/latest/awsvpnclient_amd64.deb -o awsvpnclient_amd64.deb
   ```

1. Install the AWS provided client for Linux using the `dpkg` utility.

   ```
   sudo dpkg -i awsvpnclient_amd64.deb
   ```

**Option 3 -- Install the .deb package using Ubuntu Software Center**

1. Download the .deb package file from [AWS Client VPN download ](https://d20adtppz83p9s.cloudfront.net/GTK/latest/awsvpnclient_amd64.deb).

1.  After downloading the .deb package file, use the Ubuntu Software Center to install the package. Follow the steps for installing from a standalone .deb package using Ubuntu Software Center, as described on the [Ubuntu Wiki](https://wiki.ubuntu.com/SoftwareCenter#from_a_standalone_.deb_package).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
