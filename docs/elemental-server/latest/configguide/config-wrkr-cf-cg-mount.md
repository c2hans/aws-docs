---
source_url: https://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-cf-cg-mount.html
---

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Add Mount Points to AWS Elemental ServerNodes
<a name="config-wrkr-cf-cg-mount"></a>

To make remote assets, such as scripts, image files, or video source files, available to your AWS Elemental Server nodes, create mount points as described in this section. When you mount a remote folder to a local folder on the node, all of the contents of the remote folder appear as if they are actually in the local mount folder. In this way, you can view the remote folder and verify that the backup files are created. You can also copy or delete a file from the remote folder by copying or deleting it from this mount folder.

The mount folder becomes a mount share. It's mounted to `/data/mnt/{{folder}}`.

**To create a mount**

1. On the AWS Elemental Server web interface, go to the **Settings** page and choose **Mount Points**.

1. On the **Mount Points** page, complete the mount point fields as described in the following table and choose **Save**:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-server/latest/configguide/config-wrkr-cf-cg-mount.html)

The newly mounted folder appears on the node after a few minutes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Server. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-server` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
