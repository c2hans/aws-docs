---
source_url: https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-differences.html
---

# Compare image import and instance import processes in VM Import/Export
<a name="vmimport-differences"></a>

The following table summarizes the key differences between image import and instance import.

| Characteristic | Image import (Recommended) | Instance import |
| --- | --- | --- |
| CLI support | AWS CLI | Amazon EC2 CLI |
| Supported formats for import | OVA, VHD, VHDX, VMDK, raw | VHD, VMDK, raw |
| Multi-disk support | ✔ |  |
| Windows BYOL support | ✔ |  |

For additional information on these import processes, see [Image import overview](image-import.md) and [Instance import overview](instance-import.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vm-import` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
