---
source_url: https://docs.aws.amazon.com/elemental-cf2/latest/configguide/config-cond-cf-cg-bkup-view.html
---

This is version 2.18 of the AWS Elemental Conductor File documentation. This is the latest version. For prior versions, see the *Archive* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server).

# View Folder for Database Backups
<a name="config-cond-cf-cg-bkup-view"></a>

1. On the primary Conductor web interface, choose **Configuration** (cog icon) on the main menu.

1. On the **Conductor Configuration** screen, review the management database fields.

   In the following example, the system creates backups every 24 hours and five consecutive backup files are saved. When the system creates the sixth backup, the it deletes the oldest file before saving the most recent backup.
![](http://docs.aws.amazon.com/elemental-cf2/latest/configguide/images/bkup-mgmt-shared-png.png)

Backup files are named in this format: `<yyyy-mm-dd_hh-mm-ss.tar.bz2>`

**Important**
Similar database fields also appear in the **Settings** > **General** screen on the worker nodes. When the workers are part of a cluster, the system ignores the values set on the worker nodes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor File. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cf2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
