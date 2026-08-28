---
source_url: https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport.html
---

# Export an EC2 instance as a VM using VM Import/Export
<a name="vmexport"></a>

Exporting as a VM is useful when you want to deploy a copy of an Amazon EC2 instance in your virtualization environment. You can export most EC2 instances to Citrix Xen, Microsoft Hyper-V, or VMware vSphere.

When you export an instance, you are charged the standard Amazon S3 rates for the bucket where the exported VM is stored. In addition, there might be a small charge for the temporary use of an Amazon EBS snapshot. For more information about Amazon S3 pricing, see [Amazon Simple Storage Service Pricing](https://aws.amazon.com/s3/pricing/).

**Topics**
+ [Prerequisites for exporting an instance from Amazon EC2](vmexport-prerequisites.md)
+ [Considerations for instance export](vmexport-limits.md)
+ [Start an instance export task](export-instance.md)
+ [Monitor an instance export task](vmexport-monitor.md)
+ [Cancel an instance export task](vmexport-cancel.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vm-import` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
