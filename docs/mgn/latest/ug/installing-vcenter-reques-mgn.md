---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/installing-vcenter-reques-mgn.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# VMware limitations
<a name="installing-vcenter-reques-mgn"></a>
+ MGN supports using agentless and agent-based replication for migrations from VMC on AWS.
+ MGN partially supports vMotion, Storage vMotion, and other features based on virtual machine migration (such as DRS and Storage DRS) subject to these limitations:
  + Migrating a virtual machine to a new ESXi host or datastore after one replication run ends, and before the next replication run begins, is supported as long as the vCenter account has sufficient permissions on the destination ESXi host, datastores, and datacenter, and on the virtual machine itself at the new location.
  + Migrating a virtual machine to a new ESXi host, datastore, and/or datacenter while a replication run is active, that is, while a virtual machine upload is in progress, is not supported. Cross vCenter vMotion is not supported for use with MGN.
+ AWS does not provide support for migrating VMware Virtual Volumes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
