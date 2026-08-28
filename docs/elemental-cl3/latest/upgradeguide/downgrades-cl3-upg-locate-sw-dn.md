---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/downgrades-cl3-upg-locate-sw-dn.html
---

# Step B: Copy the AWS Elemental installers
<a name="downgrades-cl3-upg-locate-sw-dn"></a>

Locate and copy the AWS Elemental installers for worker and Conductor nodes.

1. Find the version of the software that you're downgrading to.

   Follow these steps:

   1. From a Linux prompt, log in to the hardware until with the *elemental* user credentials.

   1. Look for the desired installer as shown here.

      ```
      [elemental@hostname ~] ls
      ```

      Look for the file named similar to this `...elemental_production_conductor_live247_3.23.5.12345.run...`

1. If you find the software, skip to [Step C: Stop the running channels](downgrades-cl3-upg-stop-chan.md)

   If the software isn't on the appliance, go to the next step.

1. From your regular workstation, open a web browser, go to [AWS Elemental Support Center Activations](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/activations) and download the and download the software for the version that you're going to.

1. Make a note of where downloads are stored on your workstation. For example:

   ```
   h:/corporate/downloads/.
   ```

1. Make a note of the name of the download file. For example: `elemental_production_conductor_live247_3.23.5.12345.run`

1.  Copy the download file from your workstation to `/home/elemental/` on one of the nodes. For example:
   + Use SFTP protocol and an FTP client application on your workstation computer. Connect to the IP address for the product , using the *elemental* user credentials, and transfer the file.
   + Use SCP protocol and an SCP client application on your workstation computer. Copy the file with the *elemental* user credentials and transfer the file.

1. Repeat the download to any other nodes that are changing versions. If you're changing versions on several nodes, copy the download file to every appliance at once. Doing so reduces downtime on each node as you start installing the new software.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
