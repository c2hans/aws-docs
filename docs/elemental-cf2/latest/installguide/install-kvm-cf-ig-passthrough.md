---
source_url: https://docs.aws.amazon.com/elemental-cf2/latest/installguide/install-kvm-cf-ig-passthrough.html
---

This is version 2.18 of the AWS Elemental Conductor File documentation. This is the latest version. For prior versions, see the *Archive* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server).

# Step C: Enable CPU Passthrough
<a name="install-kvm-cf-ig-passthrough"></a>

Enable CPU passthrough so that the KVM can tell what CPU you're using. The AWS Elemental software installer could fail, or jobs remain in a pending state, if passthrough isn't enabled.

**To enable CPU passthrough**

1. At the Linux command line on the KVM host, use the following command to update the virtual machine configuration file.

   ```
   sudo virsh edit {{hostname}}
   ```

   where `hostname` is the name that you gave the virtual machine when you deployed it.

1.  Go to the line that defines `cpu mode` and change it to **host-passthrough**.

1. Save and exit the editor.

1. Enable passthrough on all KVMs that you deployed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor File. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cf2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
