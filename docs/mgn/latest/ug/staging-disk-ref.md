---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/staging-disk-ref.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Change target storage type
<a name="staging-disk-ref"></a>

You can change the target storage type for all disks on a source server. The available options are Amazon Elastic Block Store (Amazon EBS) and Amazon FSx for NetApp ONTAP. This change applies to all disks on the server.

When using Amazon EBS, you can also customize the Amazon EBS volume type for each individual disk or group of disks. For details, see [Change staging disk type](ebs-storage.md#staging-disk) in the [Amazon EBS configuration](ebs-storage.md).

For information on configuring FSx for ONTAP as the target storage type, see the [FSx for ONTAP configuration](fsx-ontap.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
