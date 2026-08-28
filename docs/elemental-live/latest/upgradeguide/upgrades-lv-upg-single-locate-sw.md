---
source_url: https://docs.aws.amazon.com/elemental-live/latest/upgradeguide/upgrades-lv-upg-single-locate-sw.html
---

# Step C: Copy the AWS Elemental Live installer
<a name="upgrades-lv-upg-single-locate-sw"></a>

1. From your regular workstation, open a web browser, go to [AWS Elemental Support Center Activations](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations) and download the software for the version that you're going to.

1. Make a note of where downloads are stored on your workstation. For example:

   ```
   h:/corporate/downloads/.
   ```

1. Make a note of the name of the download file. For example: `elemental_production_live_2.25.4.12345.run`

1.  Copy the download file from your workstation to `/home/elemental/` on one of the nodes. For example:
   + Use SFTP protocol and an FTP client application on your workstation computer. Connect to the IP address for Elemental Live on port 22 with the *elemental* user credentials and transfer the file.
   + Use SCP protocol and an SCP client application on your workstation computer. Copy the file with the *elemental* user credentials and transfer the file.

1. Repeat the download to any other nodes that are changing versions. If you're changing versions on several nodes, copy the download file to every hardware unit at once. Doing so reduces downtime on each node as you start installing the new software.

For detailed downloading steps, see [Downloading AWS Elemental Live software](detailed-dl-lv-upg.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
