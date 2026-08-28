---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-bkup.html
---

# Configuring for backup
<a name="conductor-live-config-bkup"></a>

This section describes how to modify the backup configuration so that AWS Elemental Conductor Live creates database backups on a remote server. (The default configuration is to back up to a directory on the node.)

You only need to change the configuration on the primary Conductor Live node. The secondary node will copy the configuration information from the primary node.

**To configure for backups**

1. Identify a server and directory on your network for backups. Make a note of the path.

1. Mount the server to the Conductor Live nodes, as described in [Adding mount points to worker nodes](config-wrkr-cf-config-mount.md).

1. On the Conductor Live web interface, go to the **Settings** page and choose **General**.

1. In the **Cluster Tasks** section, change these fields as desired:
   + **Minutes between management database backups**: Change if you want.
   + **Management database backups to keep**: Change if you want.
   + **Path to store management database backups**: Specify the path on the remote server.

1. Choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
