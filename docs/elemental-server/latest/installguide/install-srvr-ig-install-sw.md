---
source_url: https://docs.aws.amazon.com/elemental-server/latest/installguide/install-srvr-ig-install-sw.html
---

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Step C: Install the AWS Elemental Software
<a name="install-srvr-ig-install-sw"></a>

These steps must be performed on each node where you are installing AWS Elemental software, either directly at the machine or from your workstation via SSH.

Make sure that you use the .run file that corresponds to the .iso file that you used to set up the operating system on the node. That is, install AWS Elemental Conductor File software on the nodes that you kickstarted with the AWS Elemental Conductor File .iso and worker software on nodes that you kickstarted with the worker .iso.

**To install the software**

1. At the Linux command line, log in with the *elemental* user credentials.

1. Run the installer as follows. Use the actual filename of your .run file, rather than the example below.

   For GPU and CPU versions of the software.

   ```
   [elemental@hostname ~]$ sudo sh ./elemental_production_server_2.18.n.nnnnn.run -l -z -t
   ```

   For CPU-only versions of the software.

   ```
   [elemental@hostname ~]$ sudo sh ./elemental_production_server_cpu_2.18.n.nnnnn.run -l -z -t
   ```

   Where -l is a letter, not a number.

1. You are prompted as described in the table below.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-server/latest/installguide/install-srvr-ig-install-sw.html)

   Then the software is installed. Finally, this message appears:

   ```
   Installation and configuration complete!
   Please open a web browser and point it to https://xxx.xxx.xxx.xxx to get to the web interface.
   Enjoy!
   ```

1. Start a web browser and start the AWS Elemental Server web interface by typing the following:

   ```
   https://<hostname>
   ```

   Make sure the web interface displays.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Server. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-server` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
